import click
from .web import cache_sweetgreen_wordpress_content
from .data import clean_raw_files



SG_LOGO = """
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
"""


@click.command()
@click.option("--cache-wp", "cache_wp",  default=False, is_flag=True)
@click.option("--clean-wp", "clean_wp",  default=False, is_flag=True)
def main(cache_wp, clean_wp):
    print(SG_LOGO)
    if cache_wp:
        cache_sweetgreen_wordpress_content()

    if clean_wp:
        clean_raw_files()

    return


if __name__ == "__main__":
    main()

