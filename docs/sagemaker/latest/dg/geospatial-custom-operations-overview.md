# Overview:

Run processing jobs using `ScriptProcessor` and a SageMaker geospatial
container

SageMaker geospatial provides a purpose-built processing container,
`081189585635.dkr.ecr.us-west-2.amazonaws.com/sagemaker-geospatial-v1-0:latest`.
You can use this container when running a job with Amazon SageMaker Processing. When you create an instance of
the [`ScriptProcessor`](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ScriptProcessor "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ScriptProcessor") class that is available through the
_Amazon SageMaker Python SDK for Processing_, specify this
`image_uri`.

###### Note

If you receive a **`ResourceLimitExceeded`** error when
attempting to start a processing job, you need to request a quota increase. To get
started on a Service Quotas quota increase request, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_

###### Prerequisites for using `ScriptProcessor`

1. You have created a Python script that specifies your geospatial
   ML workload.
2. You have granted the SageMaker AI execution role access to any Amazon S3 buckets that are
   needed.
3. Prepare your data for import into the container.
   Amazon SageMaker Processing
   jobs support either setting the
   `s3_data_type` equal to `"ManifestFile"` or to
   `"S3Prefix"`.
   The following procedure show you how to create an instance of
   `ScriptProcessor` and submit a Amazon SageMaker Processing job using the SageMaker geospatial
   container.

###### To create a `ScriptProcessor` instance and submit a Amazon SageMaker Processing job using a

SageMaker geospatial container

1. Instantiate an instance of the `ScriptProcessor` class using the
   SageMaker geospatial image:

```
from sagemaker.processing import ScriptProcessor, ProcessingInput, ProcessingOutput

sm_session = sagemaker.session.Session()
execution_role_arn = sagemaker.get_execution_role()

# purpose-built geospatial container
image_uri = `'081189585635.dkr.ecr.us-west-2.amazonaws.com/sagemaker-geospatial-v1-0:latest'`

script_processor = ScriptProcessor(
	command=['python3'],
	image_uri=image_uri,
	role=`execution_role_arn`,
	instance_count=4,
	instance_type='ml.m5.4xlarge',
	sagemaker_session=`sm_session`
)
```

Replace `execution_role_arn` with the ARN of the SageMaker AI
execution role that has access to the input data stored in Amazon S3 and any
other
AWS services that you want to
call in your processing job. You can update the `instance_count` and
the `instance_type` to match the requirements of your processing
job. 2. To start a processing job,
use
the `.run()` method:

```
# Can be replaced with any S3 compliant string for the name of the folder.
s3_folder = `geospatial-data-analysis`

# Use .default_bucket() to get the name of the S3 bucket associated with your current SageMaker session
s3_bucket = sm_session.default_bucket()

s3_manifest_uri = f's3://{s3_bucket}/{s3_folder}/manifest.json'
s3_prefix_uri =  f's3://{s3_bucket}/{s3_folder}/`image-prefix`

script_processor.run(
	code='`preprocessing.py`',
	inputs=[
		ProcessingInput(
			source=`s3_manifest_uri` | `s3_prefix_uri` ,
			destination='/opt/ml/processing/input_data/',
			s3_data_type= `"ManifestFile"` | `"S3Prefix"`,
			s3_data_distribution_type= `"ShardedByS3Key"` | `"FullyReplicated"`
		)
	],
	outputs=[
        ProcessingOutput(
            source='/opt/ml/processing/output_data/',
            destination=`s3_output_prefix_url`
        )
    ]
)
```

    * Replace `preprocessing.py` with the name of
     your own Python data processing script.
    * A processing job supports two
     methods
     for formatting your input data. You can either create
     a manifest file that points to all of the input data for your processing
     job, or you can use a common prefix on each individual data
     input.
     If you created a manifest file set `s3_manifest_uri` equal to
     `"ManifestFile"`. If you used a file prefix set
     `s3_manifest_uri` equal to `"S3Prefix"`.
     You specify the path to your data using
     `source`.
    * You can distribute your processing job data two ways:




    	+ Distribute your data to all processing instances by setting
    	 `s3_data_distribution_type` equal to
    	 `FullyReplicated`.
    	+ Distribute your data in shards based on the Amazon S3 key by
    	 setting `s3_data_distribution_type` equal to
    	 `ShardedByS3Key`. When you use
    	 `ShardedByS3Key` one shard of data is sent to
    	 each processing instance.

You can use a script to process SageMaker geospatial data. That script can be found in [Step 3: Writing a script
that can calculate the NDVI](geospatial-custom-operations-procedure.md#geospatial-custom-operations-script-mode "geospatial-custom-operations-procedure.md#geospatial-custom-operations-script-mode"). To learn more about the
`.run()` API operation, see [`run`](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ScriptProcessor.run "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ScriptProcessor.run") in the _Amazon SageMaker Python SDK for
Processing_.
To monitor the progress of your processing job, the `ProcessingJobs` class
supports a [`describe`](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ProcessingJob.describe "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ProcessingJob.describe") method.
This
method returns a response from the `DescribeProcessingJob`
API call. To learn more, see [`DescribeProcessingJob` in the
_Amazon SageMaker AI API Reference_](../APIReference/API_DescribeProcessingJob.md "../APIReference/API_DescribeProcessingJob.md").

The next topic show you how to create an instance of the `ScriptProcessor`
class using the SageMaker geospatial container, and then how to use it to calculate the Normalized
Difference Vegetation Index (NDVI) with Sentinel-2 images.
