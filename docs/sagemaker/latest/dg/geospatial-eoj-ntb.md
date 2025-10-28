# Create an Earth Observation Job Using a Amazon SageMaker Studio Classic Notebook with a SageMaker geospatial Image

**To use a SageMaker Studio Classic notebook with a SageMaker geospatial image:**

1. From the **Launcher**, choose **Change environment**
   under **Notebooks and compute resources**.
2. Next, the **Change environment** dialog opens.
3. Select the **Image** dropdown
   and choose **Geospatial 1.0**. The **Instance type** should be **ml.geospatial.interactive**.
   Do not change the default values for other settings.
4. Choose **Select**.
5. Choose **Create notebook**.
   You can initiate an EOJ using a Amazon SageMaker Studio Classic notebook with a SageMaker geospatial image using the code provided below.

```
import boto3
import sagemaker
import sagemaker_geospatial_map

session = boto3.Session()
execution_role = sagemaker.get_execution_role()
sg_client = session.client(service_name="sagemaker-geospatial")
```

The following is an example showing how to create an EOJ in the in the US West (Oregon) Region.

```
#Query and Access Data
search_rdc_args = {
    "Arn": "arn:aws:sagemaker-geospatial:us-west-2:378778860802:raster-data-collection/public/nmqj48dcu3g7ayw8",  # sentinel-2 L2A COG
    "RasterDataCollectionQuery": {
        "AreaOfInterest": {
            "AreaOfInterestGeometry": {
                "PolygonGeometry": {
                    "Coordinates": [
                        [
                            [-114.529, 36.142],
                            [-114.373, 36.142],
                            [-114.373, 36.411],
                            [-114.529, 36.411],
                            [-114.529, 36.142],
                        ]
                    ]
                }
            }
        },
        "TimeRangeFilter": {
            "StartTime": "2021-01-01T00:00:00Z",
            "EndTime": "2022-07-10T23:59:59Z",
        },
        "PropertyFilters": {
            "Properties": [{"Property": {"EoCloudCover": {"LowerBound": 0, "UpperBound": 1}}}],
            "LogicalOperator": "AND",
        },
        "BandFilter": ["visual"],
    },
}

tci_urls = []
data_manifests = []
while search_rdc_args.get("NextToken", True):
    search_result = sg_client.search_raster_data_collection(**search_rdc_args)
    if search_result.get("NextToken"):
        data_manifests.append(search_result)
    for item in search_result["Items"]:
        tci_url = item["Assets"]["visual"]["Href"]
        print(tci_url)
        tci_urls.append(tci_url)

    search_rdc_args["NextToken"] = search_result.get("NextToken")

# Perform land cover segmentation on images returned from the sentinel dataset.
eoj_input_config = {
    "RasterDataCollectionQuery": {
        "RasterDataCollectionArn": "arn:aws:sagemaker-geospatial:us-west-2:378778860802:raster-data-collection/public/nmqj48dcu3g7ayw8",
        "AreaOfInterest": {
            "AreaOfInterestGeometry": {
                "PolygonGeometry": {
                    "Coordinates": [
                        [
                            [-114.529, 36.142],
                            [-114.373, 36.142],
                            [-114.373, 36.411],
                            [-114.529, 36.411],
                            [-114.529, 36.142],
                        ]
                    ]
                }
            }
        },
        "TimeRangeFilter": {
            "StartTime": "2021-01-01T00:00:00Z",
            "EndTime": "2022-07-10T23:59:59Z",
        },
        "PropertyFilters": {
            "Properties": [{"Property": {"EoCloudCover": {"LowerBound": 0, "UpperBound": 1}}}],
            "LogicalOperator": "AND",
        },
    }
}
eoj_config = {"LandCoverSegmentationConfig": {}}

response = sg_client.start_earth_observation_job(
    Name="lake-mead-landcover",
    InputConfig=eoj_input_config,
    JobConfig=eoj_config,
    ExecutionRoleArn=execution_role,
)
```

After your EOJ is created, the `Arn` is returned to you. You use the `Arn` to identify a job and perform further operations.
To get the status of a job, you can run
`sg_client.get_earth_observation_job(Arn = response['Arn'])`.

The following example shows how to query the status of an EOJ until it is completed.

```
eoj_arn = response["Arn"]
job_details = sg_client.get_earth_observation_job(Arn=eoj_arn)
{k: v for k, v in job_details.items() if k in ["Arn", "Status", "DurationInSeconds"]}
# List all jobs in the account
sg_client.list_earth_observation_jobs()["EarthObservationJobSummaries"]
```

After the EOJ is completed, you can visualize the EOJ outputs directly in the notebook.
The following example shows you how an interactive map can be rendered.

```
map = sagemaker_geospatial_map.create_map({
'is_raster': True
})
map.set_sagemaker_geospatial_client(sg_client)
# render the map
map.render()
```

The following example shows how the map can be centered
on an area of interest and the input and output of the EOJ can be rendered as separate layers within the map.

```
# visualize the area of interest
config = {"label": "Lake Mead AOI"}
aoi_layer = map.visualize_eoj_aoi(Arn=eoj_arn, config=config)

# Visualize input.
time_range_filter = {
    "start_date": "2022-07-01T00:00:00Z",
    "end_date": "2022-07-10T23:59:59Z",
}
config = {"label": "Input"}

input_layer = map.visualize_eoj_input(
    Arn=eoj_arn, config=config, time_range_filter=time_range_filter
)
# Visualize output, EOJ needs to be in completed status.
time_range_filter = {
    "start_date": "2022-07-01T00:00:00Z",
    "end_date": "2022-07-10T23:59:59Z",
}
config = {"preset": "singleBand", "band_name": "mask"}
output_layer = map.visualize_eoj_output(
    Arn=eoj_arn, config=config, time_range_filter=time_range_filter
)
```

You can use the `export_earth_observation_job` function to export the EOJ results to your Amazon S3 bucket.
The export function makes it convenient to share results across teams. SageMaker AI also simplifies dataset management.
We can simply share the EOJ results using the job ARN, instead of crawling thousands of files in the S3 bucket.
Each EOJ becomes an asset in the data catalog, as results can be grouped by the job ARN.
The following example shows how you can export the results of an EOJ.

```
sagemaker_session = sagemaker.Session()
s3_bucket_name = sagemaker_session.default_bucket()  # Replace with your own bucket if needed
s3_bucket = session.resource("s3").Bucket(s3_bucket_name)
prefix = "eoj_lakemead"  # Replace with the S3 prefix desired
export_bucket_and_key = f"s3://{s3_bucket_name}/{prefix}/"

eoj_output_config = {"S3Data": {"S3Uri": export_bucket_and_key}}
export_response = sg_client.export_earth_observation_job(
    Arn=eoj_arn,
    ExecutionRoleArn=execution_role,
    OutputConfig=eoj_output_config,
    ExportSourceImages=False,
)
```

You can monitor the status of your export job using the following snippet.

```
# Monitor the export job status
export_job_details = sg_client.get_earth_observation_job(Arn=export_response["Arn"])
{k: v for k, v in export_job_details.items() if k in ["Arn", "Status", "DurationInSeconds"]}

```

You are not charged the storage fees after you delete the EOJ.

For an example that showcases how to run an EOJ, see this
[blog post](https://aws.amazon.com/blogs/machine-learning/monitoring-lake-mead-drought-using-the-new-amazon-sagemaker-geospatial-capabilities/ "https://aws.amazon.com/blogs/machine-learning/monitoring-lake-mead-drought-using-the-new-amazon-sagemaker-geospatial-capabilities/").

For more example notebooks on SageMaker geospatial capabilities,
see this [GitHub repository](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-geospatial "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-geospatial").
