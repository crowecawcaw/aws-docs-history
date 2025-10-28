# Types of compute instances

SageMaker geospatial capabilities offer three types of compute instances.

- **SageMaker Studio Classic geospatial notebook instances** – SageMaker geospatial supports both CPU and GPU-based notebook instances in Studio Classic. Notebook instances are used to build, train, and deploy ML models. For a list of available notebook instance types that work with the geospatial image, see [Supported notebook instance types](#supported-geospatial-instances "#supported-geospatial-instances").
- **SageMaker geospatial jobs instances** – Run processing jobs to
  transform satellite image data.
- **SageMaker geospatial model inference types** – Make predictions by
  using pre-trained ML models on satellite imagery.
  The instance type is determined by the operations that you run.

The following table shows the available SageMaker geospatial specific operations and
instance types that you can use.

| Operations                    | Instance             |
| ----------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Temporal Statistics           | ml.geospatial.jobs   |
| Zonal Statistics              | ml.geospatial.jobs   |
| Resampling                    | ml.geospatial.jobs   |
| Geomosaic                     | ml.geospatial.jobs   |
| Band Stacking                 | ml.geospatial.jobs   |
| Band Math                     | ml.geospatial.jobs   |
| Cloud Removal with Landsat8   | ml.geospatial.jobs   |
| Cloud Removal with Sentinel-2 | ml.geospatial.models |
| Cloud Masking                 | ml.geospatial.models |
| Land Cover Segmentation       | ml.geospatial.models | ## SageMaker geospatial supported notebook instance types SageMaker geospatial supports both CPU and GPU-based notebook instances in Studio Classic. If when starting a GPU enabled notebook instance you receive a **`ResourceLimitExceeded`** error, you need to request a quota increase. To get started on a Service Quotas quota increase request, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. Supported Studio Classic notebook instance types |
| Name                          | Instance type        |
| ---                           | ---                  |
| ml.geospatial.interactive     | CPU                  |
| ml.g5.xlarge                  | GPU                  |
| ml.g5.2xlarge                 | GPU                  |
| ml.g5.4xlarge                 | GPU                  |
| ml.g5.8xlarge                 | GPU                  |
| ml.g5.16xlarge                | GPU                  |
| ml.g5.12xlarge                | GPU                  |
| ml.g5.24xlarge                | GPU                  |
| ml.g5.48xlarge                | GPU                  | You are charged different rates for each type of compute instance that you use. For more information about pricing, see [Geospatial ML with Amazon SageMaker AI](https://aws.amazon.com/sagemaker/geospatial "https://aws.amazon.com/sagemaker/geospatial"). ## SageMaker geospatial libraries The SageMaker geospatial specific **Instance type**, `ml.geospatial.interactive` contains the following Python libraries. Geospatial libraries available on the geospatial instance type                                                                                                                               |
| Library name                  | Version available    |
| ---                           | ---                  |
| numpy                         | 1.23.4               |
| scipy                         | 1.11.2               |
| pandas                        | 1.4.4                |
| gdal                          | 3.2.2                |
| fiona                         | 1.8.22               |
| geopandas                     | 0.11.1               |
| shapley                       | 1.8.4                |
| seaborn                       | 0.11.2               |
| notebook                      | 1.8.22               |
| scikit-image                  | 0.11.2               |
| rasterio                      | 6.4.12               |
| scikit-learn                  | 0.19.2               |
| ipyleaflet                    | 1.0.1                |
| rtree                         | 0.17.2               |
| opencv                        | 4.6.0.66             |
| supy                          | 2022.4.7             |
| SNAP toolbox                  | 9.0                  |
| cdsapi                        | 0.6.1                |
| arosics                       | 1.8.1                |
| rasterstats                   | 0.18.0               |
| rioxarray                     | 0.14.1               |
| pyroSAR                       | 0.20.0               |
| eo-learn                      | 1.4.1                |
| deepforest                    | 1.2.7                |
| scrapy                        | 2.8.0                |
| netCDF4                       | 1.6.3                |
| xarray[complete]              | 0.20.1               |
| Orfeotoolbox                  | OTB-8.1.1            |
| pytorch                       | 2.0.1                |
| pytorch-cuda                  | 11.8                 |
| torchvision                   | 0.15.2               |
| torchaudio                    | 2.0.2                |
| pytorch-lightning             | 2.0.6                |
| tensorflow                    | 2.13.0               |
