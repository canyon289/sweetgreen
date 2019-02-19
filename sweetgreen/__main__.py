import click
from .web import (
    cache_sweetgreen_wordpress_content,
    cache_restaurants,
    cache_restaurant_menus,
)
from .data import compile_ingredients_json, flatten_restaurants_json



SG_LOGO = """
 #     #                                                          
 #  #  # ###### #       ####   ####  #    # ######   #####  ####  
 #  #  # #      #      #    # #    # ##  ## #          #   #    # 
 #  #  # #####  #      #      #    # # ## # #####      #   #    # 
 #  #  # #      #      #      #    # #    # #          #   #    # 
 #  #  # #      #      #    # #    # #    # #          #   #    # 
  ## ##  ###### ######  ####   ####  #    # ######     #    ####  
 
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddddy/-.```.:+shdddddddy+:.` `.-/shdy:/ydddddddddddddddd
ddddddddddddddddd/  -/+o+/-`-hdddddy:  `:++o+:` `/` `odddddddddddddddd
ddddddddddddddddh` -dddddddhhdddddy` `ohdddddddo.   sddddddddddddddddd
ddddddddddddddddd+` .:+syhdddddddd.  sddddddddddy` `hddddddddddddddddd
ddddddddddddddddddho:-`   ./sddddh` `hddddddddddd. `hddddddddddddddddd
dddddddddddddddddddddddhso:` -hddd:  +ddddddddddo  `hddddddddddddddddd
dddddddddddddddddyydddddddd+  sdddh-  -shddddhs:   `hddddddddddddddddd
ddddddddddddddddo  -+shddho. `hddddho-  `.--.` `/. `hddddddddddddddddd
dddddddddddddddddy+-`      `/hddddddddhs+////oyhh` -dddddddddddddddddd
ddddddddddddddddddddhysoosyhddddddddyshdddddddds. `ydddddddddddddddddd
ddddddddddddddddddddddddddddddddddds` `-:/++/:.  :yddddddddddddddddddd
ddddddddddddddddddddddddddddddddddddhs+:-.``.-:oyddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
 
 ######                                                           
 #     #   ##   #####   ####  ###### #####                        
 #     #  #  #  #    # #      #      #    #                       
 ######  #    # #    #  ####  #####  #    #                       
 #       ###### #####       # #      #####                        
 #       #    # #   #  #    # #      #   #                        
 #       #    # #    #  ####  ###### #    #                       
"""


@click.command()
@click.option("--cache-wp", "cache_wp", default=False, is_flag=True)
@click.option("--cache-rest", "cache_rest", default=False, is_flag=True)
@click.option("--cache-menus", "cache_menus", default=0)
@click.option("--flatten-rest", "flatten_rest", default=False, is_flag=True)
@click.option(
    "--compile-ingredients", "compile_ingredients", default=False, is_flag=True
)
def main(cache_wp, flatten_rest, cache_rest, cache_menus, compile_ingredients):
    print(SG_LOGO)

    if cache_wp:
        cache_sweetgreen_wordpress_content()

    if cache_rest:
        cache_restaurants()

    if cache_menus is not 0:
        cache_restaurant_menus(cache_menus)

    if compile_ingredients:
        compile_ingredients_json()

    if flatten_rest:
        flatten_restaurants_json()
    return


if __name__ == "__main__":
    main()
