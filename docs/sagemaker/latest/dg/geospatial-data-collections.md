# Data collections

Amazon SageMaker geospatial supports the following raster data collections. Of the following data collections,
you can use the

USGS Landsat and the Sentinel-2 Cloud-Optimized GeoTIFF
data collections when starting an Earth
Observation Job (EOJ). To learn more about the EOJs, see [Earth Observation Jobs](geospatial-eoj.md "geospatial-eoj.md").

- [Copernicus Digital Elevation Model (DEM) – GLO-30](https://registry.opendata.aws/copernicus-dem/ "https://registry.opendata.aws/copernicus-dem/")
- [Copernicus Digital Elevation Model (DEM) – GLO-90](https://registry.opendata.aws/copernicus-dem/ "https://registry.opendata.aws/copernicus-dem/")
- [Sentinel-2 Cloud-Optimized GeoTIFFs](https://registry.opendata.aws/sentinel-2-l2a-cogs/ "https://registry.opendata.aws/sentinel-2-l2a-cogs/")
- [Sentinel-1](https://registry.opendata.aws/sentinel-1/ "https://registry.opendata.aws/sentinel-1/")
- [National Agriculture Imagery Program (NAIP) on AWS](https://registry.opendata.aws/naip/ "https://registry.opendata.aws/naip/")
- [USGS Landsat 8](https://registry.opendata.aws/usgs-landsat/ "https://registry.opendata.aws/usgs-landsat/")
  To find the list of available raster data collections in your AWS Regions, use
  `ListRasterDataCollections`. In the [`ListRasterDataCollections` response](../APIReference/API_geospatial_ListRasterDataCollections.md#API_geospatial_ListRasterDataCollections_ResponseSyntax "../APIReference/API_geospatial_ListRasterDataCollections.md#API_geospatial_ListRasterDataCollections_ResponseSyntax"), you get a [`RasterDataCollectionMetadata`](../APIReference/API_geospatial_ListRasterDataCollections.md#API_geospatial_ListRasterDataCollections_ResponseSyntax "../APIReference/API_geospatial_ListRasterDataCollections.md#API_geospatial_ListRasterDataCollections_ResponseSyntax") object that contains details
  about the available raster data collections.

###### Example – Calling the `ListRasterDataCollections` API using the AWS SDK for Python (Boto3)

When you use the SDK for Python (Boto3) and SageMaker geospatial, you must create a geospatial client,
`geospatial_client`. Use the following Python snippet to
make a call to the `list_raster_data_collections` API:

```
import boto3
import sagemaker
import sagemaker_geospatial_map
import json

## SageMaker Geospatial Capabilities is currently only avaialable in US-WEST-2
session = boto3.Session(region_name='us-west-2')
execution_role = sagemaker.get_execution_role()

## Creates a SageMaker Geospatial client instance
geospatial_client = session.client(service_name="sagemaker-geospatial")

# Creates a resusable Paginator for the list_raster_data_collections API operation
paginator = geospatial_client.get_paginator("list_raster_data_collections")

# Create a PageIterator from the Paginator
page_iterator = paginator.paginate()

# Use the iterator to iterate throught the results of list_raster_data_collections
results = []
for page in page_iterator:
	results.append(page['RasterDataCollectionSummaries'])

print (results)
```

In the JSON response, you will receive the following, which has been truncated for
clarity:

```
{
    "Arn": "arn:aws:sagemaker-geospatial:us-west-2:555555555555:raster-data-collection/public/dxxbpqwvu9041ny8",
    "Description": "Copernicus DEM is a Digital Surface Model which represents the surface of the Earth including buildings, infrastructure, and vegetation. GLO-30 is instance of Copernicus DEM that provides limited worldwide coverage at 30 meters.",
    "DescriptionPageUrl": "https://registry.opendata.aws/copernicus-dem/",
    "Name": "Copernicus DEM GLO-30",
    "Tags": {},
    "Type": "PUBLIC"
}
```

## Image band information from the USGS Landsat and Sentinel-2 data collections

Image band information from the USGS Landsat 8 and Sentinel-2 data collections are provided in the following table.

USGS Landsat

| Band name  | Wave length range (nm)    | Units                  | Valid range | Fill value      | Spatial resolution     |
| ---------- | ------------------------- | ---------------------- | ----------- | --------------- | ---------------------- | ---------- |
| coastal    | 435 - 451                 | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| blue       | 452 - 512                 | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| green      | 533 - 590                 | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| red        | 636 - 673                 | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| nir        | 851 - 879                 | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| swir16     | 1566 - 1651               | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| swir22     | 2107 - 2294               | Unitless               | 1 - 65455   | 0 (No Data)     | 30m                    |
| qa_aerosol | NA                        | Bit Index              | 0 - 255     | 1               | 30m                    |
| qa_pixel   | NA                        | Bit Index              | 1 - 65455   | 1 (bit 0)       | 30m                    |
| qa_radsat  | NA                        | Bit Index              | 1 - 65455   | NA              | 30m                    |
| t          | 10600 - 11190             | Scaled Kelvin          | 1 - 65455   | 0 (No Data)     | 30m (scaled from 100m) |
| atran      | NA                        | Unitless               | 0 - 10000   | -9999 (No Data) | 30m                    |
| cdist      | NA                        | Kilometers             | 0 - 24000   | -9999 (No Data) | 30m                    |
| drad       | NA                        | W/(m^2 sr µm)/DN       | 0 - 28000   | -9999 (No Data) | 30m                    |
| urad       | NA                        | W/(m^2 sr µm)/DN       | 0 - 28000   | -9999 (No Data) | 30m                    |
| trad       | NA                        | W/(m^2 sr µm)/DN       | 0 - 28000   | -9999 (No Data) | 30m                    |
| emis       | NA                        | Emissivity coefficient | 1 - 10000   | -9999 (No Data) | 30m                    |
| emsd       | NA                        | Emissivity coefficient | 1 - 10000   | -9999 (No Data) | 30m                    | Sentinel-2 |
| Band name  | Wave length range (nm)    | Scale                  | Valid range | Fill value      | Spatial resolution     |
| ---        | ---                       | ---                    | ---         | ---             | ---                    |
| coastal    | 443                       | 0.0001                 | NA          | 0 (No Data)     | 60m                    |
| blue       | 490                       | 0.0001                 | NA          | 0 (No Data)     | 10m                    |
| green      | 560                       | 0.0001                 | NA          | 0 (No Data)     | 10m                    |
| red        | 665                       | 0.0001                 | NA          | 0 (No Data)     | 10m                    |
| rededge1   | 705                       | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| rededge2   | 740                       | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| rededge3   | 783                       | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| nir        | 842                       | 0.0001                 | NA          | 0 (No Data)     | 10m                    |
| nir08      | 865                       | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| nir08      | 865                       | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| nir09      | 940                       | 0.0001                 | NA          | 0 (No Data)     | 60m                    |
| swir16     | 1610                      | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| swir22     | 2190                      | 0.0001                 | NA          | 0 (No Data)     | 20m                    |
| aot        | Aerosol optical thickness | 0.001                  | NA          | 0 (No Data)     | 10m                    |
| wvp        | Scene-average water vapor | 0.001                  | NA          | 0 (No Data)     | 10m                    |
| scl        | Scene classification data | NA                     | 1 - 11      | 0 (No Data)     | 20m                    |
