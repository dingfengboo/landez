import logging
from landez import MBTilesBuilder

logging.basicConfig(level=logging.DEBUG)
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
mb = MBTilesBuilder(tiles_url="https://api.mapbox.com/v4/mapbox.terrain-rgb/{z}/{x}/{y}.pngraw?access_token=pk.eyJ1IjoidHNjaGF1YiIsImEiOiJjaW5zYW5lNHkxMTNmdWttM3JyOHZtMmNtIn0.CDIBD8H-G2Gf-cPkIuWtRg",
                    cache=True,
                    filepath="kunming-rgb.mbtiles",
                    header=headers)
mb.add_coverage(bbox=(102.1, 24, 102.2, 24.1), zoomlevels=[10,11,12,13,14,15])
mb.run()