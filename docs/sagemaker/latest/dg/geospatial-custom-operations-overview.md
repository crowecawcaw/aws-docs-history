

# Overview: Run processing jobs using `ProcessingJob` and a SageMaker geospatial container
<a name="geospatial-custom-operations-overview"></a>

**Note**  
Amazon SageMaker geospatial capabilities is no longer open to new customers. Offboard any previously saved jobs to Amazon S3 by using the [ExportEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportEarthObservationJob.html) and [ExportVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportVectorEnrichmentJob.html) API operations.

SageMaker geospatial provides a purpose-built processing container, `081189585635.dkr.ecr.us-west-2.amazonaws.com/sagemaker-geospatial-v1-0:latest`. You can use this container when running a job with Amazon SageMaker Processing. When you create an instance of the [`ProcessingJob`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html) class that is available through the *Amazon SageMaker Python SDK for Processing*, specify this `image_uri`.

**Note**  
If you receive a ResourceLimitExceeded error when attempting to start a processing job, you need to request a quota increase. To get started on a Service Quotas quota increase request, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide* 

**Prerequisites for using `ProcessingJob`**

1. You have created a Python script that specifies your geospatial ML workload.

1. You have granted the SageMaker AI execution role access to any Amazon S3 buckets that are needed.

1. Prepare your data for import into the container. Amazon SageMaker Processing jobs support either setting the `s3_data_type` equal to `"ManifestFile"` or to `"S3Prefix"`.

The following procedure show you how to create an instance of `ProcessingJob` and submit a Amazon SageMaker Processing job using the SageMaker geospatial container.

**To create a `ProcessingJob` instance and submit a Amazon SageMaker Processing job using a SageMaker geospatial container**

1. Instantiate an instance of the `ProcessingJob` class using the SageMaker geospatial image:

   ```
   from sagemaker.core.processing import Processor, ProcessingInput, ProcessingOutput
   from sagemaker.core.helper.session_helper import Session, get_execution_role
   	
   sm_session = Session()
   execution_role_arn = get_execution_role()
   
   # purpose-built geospatial container
   image_uri = '081189585635.dkr.ecr.us-west-2.amazonaws.com/sagemaker-geospatial-v1-0:latest'
   
   script_processor = Processor(
   	command=['python3'],
   	image_uri=image_uri,
   	role={{execution_role_arn}},
   	instance_count=4,
   	instance_type='ml.m5.4xlarge',
   	sagemaker_session={{sm_session}}
   )
   ```

   Replace {{execution\_role\_arn}} with the ARN of the SageMaker AI execution role that has access to the input data stored in Amazon S3 and any other AWS services that you want to call in your processing job. You can update the `instance_count` and the `instance_type` to match the requirements of your processing job.

1. To start a processing job, use the `.run()` method:

   ```
   # Can be replaced with any S3 compliant string for the name of the folder.
   s3_folder = {{geospatial-data-analysis}}
   
   # Use .default_bucket() to get the name of the S3 bucket associated with your current SageMaker session
   s3_bucket = sm_session.default_bucket()
   					
   s3_manifest_uri = f's3://{s3_bucket}/{s3_folder}/manifest.json'
   s3_prefix_uri =  f's3://{s3_bucket}/{s3_folder}/image-prefix
   
   script_processor.run(
   	code='{{preprocessing.py}}',
   	inputs=[
   		ProcessingInput(
   			source={{s3_manifest_uri}} | {{s3_prefix_uri}} ,
   			destination='/opt/ml/processing/input_data/',
   			s3_data_type= {{"ManifestFile" }}| {{"S3Prefix"}},
   			s3_data_distribution_type= {{"ShardedByS3Key"}} | {{"FullyReplicated"}}
   		)
   	],
   	outputs=[
           ProcessingOutput(
               source='/opt/ml/processing/output_data/',
               destination=s3_output_prefix_url
           )
       ]
   )
   ```
   + Replace {{preprocessing.py}} with the name of your own Python data processing script.
   + A processing job supports two methods for formatting your input data. You can either create a manifest file that points to all of the input data for your processing job, or you can use a common prefix on each individual data input. If you created a manifest file set `s3_manifest_uri` equal to `"ManifestFile"`. If you used a file prefix set `s3_manifest_uri` equal to `"S3Prefix"`. You specify the path to your data using `source`.
   + You can distribute your processing job data two ways:
     + Distribute your data to all processing instances by setting `s3_data_distribution_type` equal to `FullyReplicated`.
     + Distribute your data in shards based on the Amazon S3 key by setting `s3_data_distribution_type` equal to `ShardedByS3Key`. When you use `ShardedByS3Key` one shard of data is sent to each processing instance.

    You can use a script to process SageMaker geospatial data. That script can be found in [Step 3: Writing a script that can calculate the NDVI](geospatial-custom-operations-procedure.md#geospatial-custom-operations-script-mode). To learn more about the `.run()` API operation, see [`run`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html) in the *Amazon SageMaker Python SDK for Processing*.

To monitor the progress of your processing job, the `ProcessingJobs` class supports a [`describe`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html) method. This method returns a response from the `DescribeProcessingJob` API call. To learn more, see [`DescribeProcessingJob` in the *Amazon SageMaker AI API Reference*](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProcessingJob.html).

The next topic show you how to create an instance of the `ProcessingJob` class using the SageMaker geospatial container, and then how to use it to calculate the Normalized Difference Vegetation Index (NDVI) with Sentinel-2 images.

