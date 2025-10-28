# Amazon SageMaker geospatial capabilities

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. If prior to November 30, 2023 you created a Amazon SageMaker AI domain, Studio Classic remains the default experience. domains created after November 30, 2023 default to the new Studio experience.

Amazon SageMaker geospatial features and resources are _only_ available in Studio Classic. To learn more about setting up a domain and getting started with Studio, see [Getting started with Amazon SageMaker geospatial](geospatial-getting-started.md "geospatial-getting-started.md") .

Amazon SageMaker geospatial capabilities makes it easier for data scientists and machine learning (ML) engineers to build, train, and deploy ML models faster using geospatial data. You have access to open-source and third-party data, processing, and visualization tools to make it more efficient to prepare geospatial data for ML. You can increase your productivity by using purpose-built algorithms and pre-trained ML models to speed up model building and training, and use built-in visualization tools to explore prediction outputs on an interactive map and then collaborate across teams on insights and results.

###### Note

Currently, SageMaker geospatial capabilities are only supported in the US West (Oregon) Region.

If you don't see the SageMaker geospatial UI available in your current Studio Classic instance check to make sure you are currently in the US West (Oregon) Region.

###### Why use SageMaker geospatial capabilities?

You can use SageMaker geospatial capabilities to make predictions on geospatial data faster than do-it-yourself solutions. SageMaker geospatial capabilities make it easier to access geospatial data from your existing customer data lakes, open-source datasets, and other SageMaker geospatial data providers. SageMaker geospatial capabilities minimize the need for building custom infrastructure and data preprocessing functions by offering purpose-built algorithms for efficient data preparation, model training, and inference. You can also create and share custom visualizations and data with your company from Amazon SageMaker Studio Classic. SageMaker geospatial capabilities offer pre-trained models for common uses in agriculture, real estate, insurance, and financial services.

## How can I use SageMaker geospatial capabilities?

You can use SageMaker geospatial capabilities in two ways.

- Through the SageMaker geospatial UI, as a part of Amazon SageMaker Studio Classic UI.
- Through a Studio Classic notebook instance that uses the **Geospatial 1.0** image.

###### SageMaker AI has the following geospatial capabilities

- Use a purpose built SageMaker geospatial image that supports both CPU and GPU-based notebook instances, and also includes commonly used open-source libraries found in geospatial machine
  learning workflows.
- Use the Amazon SageMaker Processing and the SageMaker geospatial container to run large-scale workloads with your own datasets, including soil, weather, climate, LiDAR, and commercial aerial and satellite
  imagery.
- Run an [Earth Observation job](geospatial-eoj.md "geospatial-eoj.md") for raster data processing.
- Run a [Vector Enrichment job](geospatial-vej.md "geospatial-vej.md") to convert latitude and longitude into human readable addresses, and match noisy GPS traces to specific roads.
- Use built-in [visualization tools right in Studio Classic to interactively view geospatial data or model predictions on a map.](geospatial-visualize.md "geospatial-visualize.md")

You can also use data from a collection of geospatial data providers. Currently, the data collections available include:

- [USGS Landsat](https://www.usgs.gov/centers/eros/data-citation?qt-science_support_page_related_con=0#qt-science_support_page_related_con "https://www.usgs.gov/centers/eros/data-citation?qt-science_support_page_related_con=0#qt-science_support_page_related_con")
- [Sentinel-1](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice "https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice")
- [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2 "https://sentinel.esa.int/web/sentinel/missions/sentinel-2")
- [Copernicus DEM](https://registry.opendata.aws/copernicus-dem/ "https://registry.opendata.aws/copernicus-dem/")
- [National Agriculture Imagery Program](https://registry.opendata.aws/naip/ "https://registry.opendata.aws/naip/")

## Are you a first-time user of SageMaker geospatial?

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. New domains created after November 30, 2023 default to the
Studio experience. Access to SageMaker geospatial is limited to Studio Classic, to learn more see [Accessing SageMaker geospatial](access-studio-classic-geospatial.md "access-studio-classic-geospatial.md").

If you're a first-time user of AWS or Amazon SageMaker AI, we recommend that you do the following:

1. **Create an AWS account.**

To learn about setting up an AWS account and getting started with SageMaker AI, see [Complete Amazon SageMaker AI prerequisites](gs-set-up.md "gs-set-up.md"). 2. **Create a user role and execution role that work with SageMaker geospatial**.

As a managed service, Amazon SageMaker geospatial capabilities performs operations on your behalf on the AWS hardware that SageMaker AI manages. A SageMaker AI execution role an perform only the operations that users grant. To work with SageMaker geospatial capabilities, you must set up a user role and an execution role. For more information, see [SageMaker geospatial capabilities roles](sagemaker-geospatial-roles.md "sagemaker-geospatial-roles.md"). 3. **Update your trust policy to include SageMaker geospatial**.

SageMaker geospatial defines an additional service principal. To learn how to create or update your SageMaker AI execution role's trust policy, see [Adding

the SageMaker geospatial service principal to an existing SageMaker AI execution
role](sagemaker-geospatial-roles-pass-role.md "sagemaker-geospatial-roles-pass-role.md"). 4. **Set up an Amazon SageMaker AI domain to access Amazon SageMaker Studio Classic.**

To use SageMaker geospatial, a domain is required. For domains created before November 30, 2023 the default experience is Studio Classic. domains created after November 30, 2023 default to the Studio experience. To learn more about accessing Studio Classic from Studio, see [Accessing SageMaker geospatial](access-studio-classic-geospatial.md "access-studio-classic-geospatial.md"). 5. **Remember, shut down resources.**

When you have finished using SageMaker geospatial capabilities, shut down the instance it runs on to avoid incurring additional charges. For more information, see [Shut Down Resources from
Amazon SageMaker Studio Classic](notebooks-run-and-manage-shut-down.md "notebooks-run-and-manage-shut-down.md").

###### Topics

- [Getting started with Amazon SageMaker geospatial](geospatial-getting-started.md "geospatial-getting-started.md")
- [Using a
  processing
  jobs for custom geospatial workloads](geospatial-custom-operations.md "geospatial-custom-operations.md")
- [Earth Observation Jobs](geospatial-eoj.md "geospatial-eoj.md")
- [Vector Enrichment Jobs](geospatial-vej.md "geospatial-vej.md")
- [Visualization Using SageMaker geospatial capabilities](geospatial-visualize.md "geospatial-visualize.md")
- [Amazon SageMaker geospatial Map SDK](geospatial-notebook-sdk.md "geospatial-notebook-sdk.md")
- [SageMaker geospatial capabilities FAQ](geospatial-faq.md "geospatial-faq.md")
- [SageMaker geospatial Security and Permissions](geospatial-security-general.md "geospatial-security-general.md")
- [Types of compute instances](geospatial-instances.md "geospatial-instances.md")
- [Data collections](geospatial-data-collections.md "geospatial-data-collections.md")
