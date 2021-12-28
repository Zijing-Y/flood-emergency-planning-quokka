from shapely.geometry import Point, Polygon
import rasterio
import geopandas as gpd
from rasterio import mask
import json
import numpy as np

# Task_1


def get_location():
    test_range = Polygon([(430000, 80000), (430000, 95000), (465000, 95000), (465000, 80000)])
    try:
        easting = float(input('Please enter your east coordinate (4300000-465000):'))
        northing = float(input('Please enter your north coordinate (80000-95000):'))
        location = Point(easting, northing)
        # Check if user is in the area
        if test_range.contains(location):
            print('User location:', location)
            return location
        else:
            print('Out of range,please check your input is within range.')
            exit()
    except ValueError:
        print('Invalid data type')

# Task 2


def highest_point(location):
    # reference: https://automating-gis-processes.github.io/site/notebooks/Raster/clipping-raster.html
    # create 5km buffer around user location
    buffer = location.buffer(5000)
    # read elevation raster file
    elevation_raster = rasterio.open('Material/elevation/SZ.asc')
    # create a Dataframe from buffer
    geo = gpd.GeoDataFrame({'geometry': buffer}, index=[0], crs=elevation_raster.crs.data)
    # get the coordinates of the geometry
    coord = [json.loads(geo.to_json())['features'][0]['geometry']]
    # clip the raster with buffer
    out_image, out_transform = rasterio.mask.mask(elevation_raster, coord, crop=True)
    out_meta = elevation_raster.meta.copy()
    # update the metadata with new attributes
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # write the clipped raster
    with rasterio.open('mask.tif', "w", **out_meta) as dest:
        dest.write(out_image)
    # read the new clipped raster
    ele_rst = rasterio.open('mask.tif')
    altitude = ele_rst.read(1)
    # get highest elevation
    highest_value = np.max(altitude)
    # get the pixel of the highest point
    highest_p = np.where(altitude == highest_value)
    highest_row = highest_p[0][0]
    highest_col = highest_p[1][0]
    # return coordinates in CRS
    highest_east, highest_north = rasterio.transform.xy(out_transform,
                                                        highest_row,
                                                        highest_col,
                                                        offset='center')
    hp = Point(highest_east, highest_north)
    print('The highest point within a 5km radius is', hp, 'and the altitude is', highest_value, 'm')
    return highest_east, highest_north


location = get_location()
high_point = highest_point(location)
