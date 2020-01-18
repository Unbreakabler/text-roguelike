from typing import List, Dict
import tcod as libtcod

from entity import Entity
from map_objects.game_map import GameMap

def render_all(
        con: libtcod.console.Console, entities: List[Entity], game_map: GameMap, fov_map: libtcod.map.Map, 
        fov_recompute: bool, screen_width: int, screen_height: int, colors: Dict[str, libtcod.Color]) -> None:
    # Draw game map
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors['light_wall'], libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors['light_ground'], libtcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors['dark_wall'], libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors['dark_ground'], libtcod.BKGND_SET)

    # Draw all entities
    for entity in entities:
        draw_entity(con, entity, fov_map)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con: libtcod.console.Console, entities: List[Entity]) -> None:
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con: libtcod.console.Console, entity: Entity, fov_map: libtcod.map.Map) -> None:
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con: libtcod.console.Console, entity: Entity) -> None:
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)