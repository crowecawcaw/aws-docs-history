On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Python SDK examples

## Creating a schema from multiple .csv files

###### Note

If you use the console to ingest your data, Lookout for Equipment can detect your schema for you, according to the way you organize your files.

If you've uploaded multiple .csv files, with each sensor having its own .csv file, you
would use the following schema to create a dataset from those files.

In the following schema, `Components` refers to a collection of identifiers
for the .csv files of your sensors. The `ComponentName` is the portion of a
prefix of an Amazon S3 object key that identifies a .csv file.

For example, `"ComponentName": "Sensor2"` could acccess
`s3://`amzn-s3-demo-bucket`/`AssetName`/`Sensor2`/`Sensor2`.csv`.

You define a `Columns` object for each `ComponentName` that you
define in the schema. The Name fields in the `Columns` object must match the
columns in your .csv files.

Within each `Columns` object, the `Name` fields that reference
the columns containing the timestamp data must have the Type field specified as
`DATETIME`. The Name fields that reference your sensor data must have a
Type of `DOUBLE`.

You can use the following example code with the AWS SDK for Python (Boto3) to create
a dataset.

```

import boto3
import json
import pprint
from botocore.config import Config


config = Config(
    region_name = `Region`, #Choose a valid Amazon Web Services Region
    signature_version = 'v4'
)

lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)

dataset_schema = {
    "Components": [
        {
            "ComponentName": "Sensor1",
            "Columns": [
                {
                    "Name": "Timestamp",
                    "Type": "DATETIME"
                },
                {
                    "Name": "Sensor1",
                    "Type": "DOUBLE"
                }
            ]
        },
        {
            "ComponentName": "Sensor2",
            "Columns": [
                {
                    "Name": "Timestamp",
                    "Type": "DATETIME"
                },
                {
                    "Name": "Sensor2",
                    "Type": "DOUBLE"
                }
            ]
        },
        {
            "ComponentName": "Sensor3",
            "Columns": [
                {
                    "Name": "Timestamp",
                    "Type": "DATETIME"
                },
                {
                    "Name": "Sensor3",
                    "Type": "DOUBLE"
                }
            ]
        },
        {
            "ComponentName": "Sensor4",
            "Columns": [
                {
                    "Name": "Timestamp",
                    "Type": "DATETIME"
                },
                {
                    "Name": "Sensor4",
                    "Type": "DOUBLE"
                }
            ]
        }
    ]
}


```

## Creating a schema from a single .csv file

###### Note

If you use the console to ingest your data, Lookout for Equipment can detect your schema for you, according to the way you organize your files.

If you've uploaded one .csv file containing all of the sensor data for the asset, you
would use the schema in the code below to create a dataset from that file.

The
`ComponentName` is the portion of the prefix of the Amazon S3 object key that identifies the
.csv file containing the sensor data for your asset. When you specify the value of
`ComponentName` as A`ssetName`, you access
`s3://`amzn-s3-demo-bucket`/`FacilityName`/`AssetName`/`AssetName`.csv`. You enter the columns of your
dataset in the Columns object. The name of each column in your .csv file must match the Name
in the schema. For the column containing the time stamp data, you must specify the value of
`Type` as `DATETIME` in the schema. For the columns containing data from sensors, you must
specify the value of `Type` as `DOUBLE`.

You can use the following example code with the AWS SDK for Python (Boto3) to create
a dataset.

```

import boto3
import json
import pprint
from botocore.config import Config


config = Config(
    region_name = `'Region'`, # Choose a valid AWS Region
    signature_version = 'v4'
)

lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)

dataset_schema = {
  "Components": [
    {
      "ComponentName": "AssetName",
      "Columns": [
        {
          "Name": "Timestamp",
          "Type": "DATETIME"
        },
        {
          "Name": "Sensor1",
          "Type": "DOUBLE"
        },
        {
          "Name": "Sensor2",
          "Type": "DOUBLE"
        },
        {
          "Name": "Sensor3",
          "Type": "DOUBLE"
        },
        {
          "Name": "Sensor4",
          "Type": "DOUBLE"
        },
      ]
    }
  ]
}

dataset_name = `"dataset-name"`
data_schema = {
    'InlineDataSchema': json.dumps(dataset_schema),
}

create_dataset_response = lookoutequipment.create_dataset(DatasetName=dataset_name, DatasetSchema=data_schema)

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(create_dataset_response)


```

## Adding a dataset to your project

###### Note

You can also add a dataset to your project [using the console](ingest-dataset.md "ingest-dataset.md").

Use the following AWS SDK for Python (Boto3) example code to tell Lookout for Equipment to ingest your dataset.

```

import boto3
import time
from botocore.config import Config


config = Config(
region_name = `'Region'` #Choose a valid Amazon Web Services Region
	signature_version = 'v4'
	)

	lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)


	INGESTION_DATA_SOURCE_BUCKET = 'amzn-s3-demo-bucket'
	# If you're ingesting multiple .csv files of your sensor data, use the following Amazon S3 path: s3://amzn-s3-demo-bucket/AssetName/. If you're ingesting a single .csv file of your asset data, use the following Amazon S3 path: s3://amzn-s3-demo-bucket/FacilityName/.
	INGESTION_DATA_SOURCE_PREFIX = 'my_data/sensor_readings/'
	# The ROLE_ARN and DATASET_NAME values that are used in this script have been defined in the previous SDK for Python example code for creating a dataset.

	data_ingestion_role_arn = ROLE_ARN
	dataset_name = DATASET_NAME
	ingestion_input_config = dict()
	ingestion_input_config['S3InputConfiguration'] = dict(
	[
	('Bucket', INGESTION_DATA_SOURCE_BUCKET),
	('Prefix', INGESTION_DATA_SOURCE_PREFIX)
	]
	)

	# Start data ingestion
	start_data_ingestion_job_response = lookoutequipment.start_data_ingestion_job(
	DatasetName=dataset_name,
	RoleArn=data_ingestion_role_arn,
	IngestionInputConfiguration=ingestion_input_config)

	data_ingestion_job_id = start_data_ingestion_job_response['JobId']
	data_ingestion_status = start_data_ingestion_job_response['Status']

	print(f'=====Data Ingestion job is started. Job ID: {data_ingestion_job_id}=====\n')

	# Wait until completes
	print("=====Polling Data Ingestion Status=====\n")
	print("Data Ingestion Status: " + data_ingestion_status)
	while data_ingestion_status == 'IN_PROGRESS':
	time.sleep(30)
	describe_data_ingestion_job_response = lookoutequipment.describe_data_ingestion_job(JobId=data_ingestion_job_id)
	data_ingestion_status = describe_data_ingestion_job_response['Status']
	print("Data Ingestion Status: " + data_ingestion_status)
	print("\n=====End of Polling Data Ingestion Status=====")


```

## Viewing a model

###### Note

You can also view and evaluate a model [in the console](view-model.md "view-model.md").

Use the following example AWS SDK for Python (Boto3) code to list the models that you've trained,
to query a model's metadata, and to delete a model that you no longer want to use. If
you've used label data when you created a dataset, you can also use this code to see how
well the model performed. To run this code successfully, you must use the SDK for Python code
in [Training your model](create-model.md "create-model.md") before you run the code
shown here.

```

import boto3
import json
import pprint
import time
from datetime import datetime
from botocore.config import Config
​
config = Config(region_name = `'Region'`)
​
lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)
​
# List models
MODEL_NAME_PREFIX = None
DATASET_NAME_FOR_LIST_MODELS = None
​
list_models_request = {}
​
if MODEL_NAME_PREFIX is not None:
    list_models_request["ModelNameBeginsWith"] = MODEL_NAME_PREFIX
​
if DATASET_NAME_FOR_LIST_MODELS is not None:
    list_models_request["DatasetNameBeginsWith"] = DATASET_NAME_PREFIX
​

pp = pprint.PrettyPrinter(depth=5)
print("=====Model Summaries=====\n")
has_more_records = True
while has_more_records:
    list_models_response = lookoutequipment.list_models(**list_models_request)
    if "NextToken" in list_models_response:
        list_models_request["NextToken"] = list_models_response["NextToken"]
    else:
        has_more_records = False
    model_summaries = list_models_response["ModelSummaries"]
    for model_summary in model_summaries:
        pp.pprint(model_summary)
print("\n=====End of Model Summaries=====")
​
# Query the metadata for a model
MODEL_NAME_TO_QUERY = MODEL_NAME
​
describe_model_response = lookoutequipment.describe_model(ModelName=MODEL_NAME_TO_QUERY)
​
print(f'Model Status: {describe_model_response["Status"]}')
if "FailedReason" in describe_model_response:
    print(f'Model FailedReason: {describe_model_response["FailedReason"]}')
​
print("\n\n=====DescribeModel Response=====\n")
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(describe_model_response)
print("\n=====End of DescribeModel Response=====")
​
# Get evaluation metrics for a model
MODEL_NAME_TO_DOWNLOAD_EVALUATION_METRICS = MODEL_NAME
​
describe_model_response = lookoutequipment.describe_model(ModelName=MODEL_NAME_TO_DOWNLOAD_EVALUATION_METRICS)
​
if 'ModelMetrics' in describe_model_response:
    model_metrics = json.loads(describe_model_response['ModelMetrics'])
    print("===== Model Metrics =====\n")
    pp = pprint.PrettyPrinter(depth=5)
    pp.pprint(model_metrics)
    print("\n=====End of Model Metrics=====\n")
else:
    print('Model metrics is only available if evaluation data is provided during training.')
​
# Delete a model
MODEL_NAME_TO_DELETE = MODEL_NAME

model_name_to_delete = MODEL_NAME_TO_DELETE
​
delete_model_response = lookoutequipment.delete_model(
    ModelName=model_name_to_delete
)
​
print("=====DeleteModel Response=====\n")
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(delete_model_response)
print("\n=====End of DeleteModel Response=====\n")

```

## Managing your datasets

###### Note

You can also manage your datasets [in the console](understanding-ingestion-validation.md "understanding-ingestion-validation.md").

Use the following AWS SDK for Python (Boto3) example code to manage your datasets. It will show you
how to list all your datasets, get information about a dataset, and delete a dataset.
You must have the modules installed from code examples that showed you how to create a
dataset to successfully use the following code.

To run the following code, you must first run the example code in either [Creating a schema from a single .csv file](#sdk-schema-single-file "#sdk-schema-single-file") or [Creating a schema from multiple .csv files](#sdk-schema-multiple-files "#sdk-schema-multiple-files") .

```

import boto3
import json
import pprint
from botocore.config import Config


config = Config(
    region_name = `'Region'` # Choose a valid Amazon Web Services Region
)

lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)

# Specify a value for the prefixes that your dataset uses to list the
DATASET_NAME_PREFIX = `"dataset-name"`
kargs = {"MaxResults": 50}
if DATASET_NAME_PREFIX is not None:
    kargs["DatasetNameBeginsWith"] = DATASET_NAME_PREFIX
has_more_records = True

pp = pprint.PrettyPrinter(depth=4)
print("=====Dataset Summaries=====\n")
while has_more_records:
    list_datasets_response = lookoutequipment.list_datasets(**kargs)
    if "NextToken" in list_datasets_response:
        kargs["NextToken"] = list_datasets_response["NextToken"]
    else:
        has_more_records = False
    # print datasets
    dataset_summaries = list_datasets_response["DatasetSummaries"]
    for dataset_summary in dataset_summaries:
        pp.pprint(dataset_summary)
print("\n=====End of Dataset Summaries=====")

# The following code queries a dataset
dataset_name_to_query = "example-dataset-1" # Change this to dataset name that you want to query

describe_dataset_response = lookoutequipment.describe_dataset(
    DatasetName=dataset_name_to_query
)

print("=====Dataset Query Response=====\n")
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(describe_dataset_response)
print("\n=====End of Response=====\n")

print("=====Schema of Dataset =====\n")
pp.pprint(json.loads(describe_dataset_response["Schema"]))
print("\n=====End of Schema of Dataset=====\n")

# The following code deletes a dataset
dataset_name_to_delete = "example-dataset-1"  # Change this to dataset name that you want to delete

delete_dataset_response = lookoutequipment.delete_dataset(
    DatasetName=dataset_name_to_delete
)

print("=====Dataset Delete Response=====\n")
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(delete_dataset_response)
print("\n=====End of Response=====\n")


```

## Labeling your data

The following example code uses the AWS SDK for Python (Boto3) to provide labels for your model.

```


import boto3
import json
import pprint
import time
from datetime import datetime
from botocore.config import Config


config = Config(region_name = 'Region')

lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)

LABEL_GROUP_NAME = "[Replace it with your label group name]"
create_label_group_request = {
    "LabelGroupName": LABEL_GROUP_NAME,
    "FaultCodes": ["[Your Fault Code1]", "[Your Fault Code2]"]
}

# CREATE A LABEL GROUP
create_label_group_response = lookoutequipment_client.create_label_group(**create_label_group_request)
pp = pprint.PrettyPrinter(depth=4)
print("=====Create Label Group Response=====\n")
pp.pprint(create_label_group_response)
print("\n=====End of Response=====")

# CREATE A LABEL
# You can create more labels as anomalies are identified before and after creating a model.
create_label_request = {
    "LabelGroupName": LABEL_GROUP_NAME,
    "Rating": "ANOMALY", # ANOMALY, NORMAL or NEUTRAL
    "StartTime": datetime(2022, 1, 1, 0, 0, 0),
    "EndTime": datetime(2022, 1, 1, 1, 0, 0),
    "FaultCode": "[Your Fault Code1]", # Must be defined in label group fault codes. Optional.
    "Equipment": "[replace with your equipment identifier]", # Optional
    "Notes": "[replace with your notes]", # Optional
}

create_label_response = lookoutequipment_client.create_label(**create_label_request)
print("=====Create Label Response=====\n")
pp.pprint(create_label_response)
print("\n=====End of Response=====")


```

## Managing your labels

You can use code like the following example code to manage your labels.

```


import boto3
import json
import pprint
import time
from datetime import datetime
from botocore.config import Config


config = Config(region_name = 'Region')
lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)

LABEL_GROUP_NAME = "[Replace it with your label group name]"

# LIST LABEL GROUPS
list_label_groups_request = {}
list_label_groups_response = lookoutequipment_client.list_label_groups(**list_label_groups_request)
pp = pprint.PrettyPrinter(depth=4)
print("=====List Label Groups Response=====\n")
pp.pprint(list_label_groups_response)
print("\n=====End of Response=====")


# DESCRIBE A LABEL GROUP
describe_label_group_request = {"LabelGroupName": LABEL_GROUP_NAME}
describe_label_group_response = lookoutequipment_client.describe_label_group(**describe_label_group_request)
print("=====Describe Label Group Response=====\n")
pp.pprint(describe_label_group_response)
print("\n=====End of Response=====")


# UPDATE A LABEL GROUP
update_label_group_request = {"LabelGroupName": LABEL_GROUP_NAME, "FaultCodes": ["[Your Fault Code1]", "[Your Fault Code3]"]}
update_label_group_response = lookoutequipment_client.update_label_group(**update_label_group_request)
print("=====Update Label Group Response=====\n")
pp.pprint(update_label_group_response)
print("\n=====End of Response=====")


# LIST LABELS
list_labels = {
    "LabelGroupName": LABEL_GROUP_NAME,
}

list_labels_response = lookoutequipment_client.list_labels(**list_labels)
print("=====Create Label Response=====\n")
pp.pprint(list_labels_response)
print("\n=====End of Response=====")


# DESCRIBE A LABEL
describe_label_request = {
    "LabelGroupName": LABEL_GROUP_NAME,
    "LabelId": "[Replace with Label Id]",
}
describe_label_response = lookoutequipment_client.describe_label(**describe_label_request)
print("=====Describe Label Response=====\n")
pp.pprint(describe_label_response)
print("\n=====End of Response=====")


# DELETE A LABEL
delete_label_request = {
    "LabelGroupName": LABEL_GROUP_NAME,
    "LabelId": "[Replace with Label Id]",
}

delete_label_response = lookoutequipment_client.delete_label(**delete_label_request)
print("=====Delete Label Response=====\n")
pp.pprint(delete_label_response)
print("\n=====End of Response=====")


# DELETE A LABEL GROUP
delete_label_group_request = {
    "LabelGroupName": LABEL_GROUP_NAME
}

delete_label_group_response = lookoutequipment_client.delete_label_group(**delete_label_group_request)
print("=====Delete Label Group Response=====\n")
pp.pprint(delete_label_group_response)
print("\n=====End of Response=====")




```

## Training a model

###### Note

You can also train a model [with the console](create-model.md "create-model.md").

The following example code uses the AWS SDK for Python (Boto3) to train a model.

```


import boto3
import json
import pprint
import time
from datetime import datetime
from botocore.config import Config


config = Config(region_name = 'Region')

lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)

MODEL_NAME = 'model-name'
# You can choose a sampling rate for your data. The valid values are "PT1S", "PT5S", "PT10S", "PT15S", "PT30S", "PT1M", "PT5M", "PT10M", "PT15M", "PT30M", "PT1H". S - second, M - minute, H - hour
TARGET_SAMPLING_RATE = 'sampling-rate'
# If you have label data in label group (See Labeling APIs example)
LABEL_GROUP_NAME = 'your-label-group'
# If you have label data in S3, specify the following variables
LABEL_DATA_SOURCE_BUCKET =  'amzn-s3-demo-source-bucket'
LABEL_DATA_SOURCE_PREFIX = 'label-data-source-prefix/' # This must end with "/" if you provide a prefix

# The following are example training and evaluation start times. datetime(2018, 8, 13, 0, 0, 0) generates 2018-08-13 00:00:00

TRAINING_DATA_START_TIME = datetime(2016, 11, 1, 0, 0, 0)
TRAINING_DATA_END_TIME = datetime(2017, 12, 31, 0, 0, 0)

EVALUATION_DATA_START_TIME = datetime(2018, 1, 1, 0, 0, 0)
EVALUATION_DATA_END_TIME = datetime(2018, 8, 13, 0, 0, 0)

# To configure off-time detection, use the format
# OFF_CONDITION = '{component}\\{sensor} < {target}'
# In the following example, Asset X will be considered to be in the off state if the latest value
# received by Sensor 1 is less than 10.
OFF_CONDITION = 'AssetX\\Sensor1 < 10.0'

########################################################
# construct request for create_model
########################################################

model_name = MODEL_NAME
DATA_SCHEMA_FOR_MODEL = None # You can use a schema similar to dataset here. The sensors used here should be subset of what is present in dataset

create_model_request = {
    'ModelName': model_name,
    'DatasetName': DATASET_NAME,
}

if DATA_SCHEMA_FOR_MODEL is not None:
    data_schema_for_model = {
        'InlineDataSchema': DATA_SCHEMA_FOR_MODEL,
    }
    create_model_request['DatasetSchema'] = data_schema_for_model

if TARGET_SAMPLING_RATE is not None:
    data_preprocessing_config = {
    'TargetSamplingRate': TARGET_SAMPLING_RATE
    }
    create_model_request['DataPreProcessingConfiguration'] = data_preprocessing_config

if LABEL_GROUP_NAME is not None:
    labels_input_config = dict()
    labels_input_config['LabelGroupName'] = LABEL_GROUP_NAME
    create_model_request['LabelsInputConfiguration'] = labels_input_config
elif LABEL_DATA_SOURCE_BUCKET is not None:
    labels_input_config = dict()
    labels_input_config['S3InputConfiguration'] = dict(
        [
            ('Bucket', LABEL_DATA_SOURCE_BUCKET),
            ('Prefix', LABEL_DATA_SOURCE_PREFIX)
        ]
    )
    create_model_request['LabelsInputConfiguration'] = labels_input_config
    # We need to set role_arn to access label data
    create_model_request['RoleArn'] = ROLE_ARN

if TRAINING_DATA_START_TIME is not None or TRAINING_DATA_END_TIME is not None:
    create_model_request['TrainingDataStartTime'] = TRAINING_DATA_START_TIME
    create_model_request['TrainingDataEndTime'] = TRAINING_DATA_END_TIME

if EVALUATION_DATA_START_TIME is not None or EVALUATION_DATA_END_TIME is not None:
    create_model_request['EvaluationDataStartTime'] = EVALUATION_DATA_START_TIME
    create_model_request['EvaluationDataEndTime'] = EVALUATION_DATA_END_TIME

if OFF_CONDITION is not None:
    create_model_request['OffCondition'] = OFF_CONDITION


########################################################
# Create_model
########################################################
create_model_response = lookoutequipment.create_model(**create_model_request)

########################################################
# Wait until complete
########################################################
model_status = create_model_response['Status']
print("=====Polling Model Status=====\n")
print("Model Status: " + model_status)
while model_status == 'IN_PROGRESS':
time.sleep(30)
describe_model_response = lookoutequipment.describe_model(ModelName=model_name)
model_status = describe_model_response['Status']
print("Model Status: " + model_status)
print("\n=====End of Polling Model Status=====")



```

## Schedule inference

###### Note

You can also schedule inference [with the console](inference.md "inference.md").

The following example code uses the AWS SDK for Python (Boto3) to schedule an inference for your
asset.

```

import boto3
import json
import pprint
import time
from datetime import datetime
from botocore.config import Config
​
config = Config(region_name = `'Region'`)
​
lookoutequipment = boto3.client(service_name="lookoutequipment", config=config)
​
# Specify a name for the inference scheduler
INFERENCE_SCHEDULER_NAME = 'inference-scheduler-name'
MODEL_NAME_FOR_CREATING_INFERENCE_SCHEDULER = 'model-name'
# You must specify values for the following variables to successfully schedule an inference.
# DATA_UPLOAD_FREQUENCY – The frequency that the data from the asset uploads to the Amazon S3 data containing the inference data. The valid values are PT5M, PT10M, PT30M, and PT1H
# INFERENCE_DATA_SOURCE_BUCKET – The S3 bucket that stores the inference data coming from your asset.
# INFERENCE_DATA_SOURCE_PREFIX – The S3 prefix that helps you access the inference data coming from your asset.
# INFERENCE_DATA_OUTPUT_BUCKET – The S3 bucket that stores the results of the inference.
# INFERENCE_DATA_OUTPUT_PREFIX – The S3 prefix that helps you access the results of the inference.
# ROLE_ARN_FOR_INFERENCE – The IAM role that gives Amazon Lookout for Equipment read permissions for Amazon S3.
​
# You can specify values for the following optional variables.
# DATA_DELAY_OFFSET_IN_MINUTES – The number of minutes to account for a delay in uploading the data to Amazon S3 from your data pipeline.
# INPUT_TIMEZONE_OFFSET – The default timezone for running inference is in UTC. You can offset the default timezone in increments of 30 minutes. This offset only applies to the file name. If you choose to use the offset, you must have the timestamps for the sensor in UTC as well. The valid values include +00:00, +00:30, -01:00, ... +11:30, +12:00, -00:00, -00:30, -01:00, ... -11:30, -12:00.
# TIMESTAMP_FORMAT – You can specify how the model outputs the timestamp in the results of the inference. The valid values are EPOCH, yyyy-MM-dd-HH-mm-ss or yyyyMMddHHmmss.
# COMPONENT_TIMESTAMP_DELIMITER – Specifies the character used to separate entries in the input data. Default delimiter is - (hyphen). The valid values are -, _ or  .
​
DATA_DELAY_OFFSET_IN_MINUTES = None
​
INPUT_TIMEZONE_OFFSET = None
​
COMPONENT_TIMESTAMP_DELIMITER = None
​
TIMESTAMP_FORMAT = None
​
# Create an inference scheduler.
scheduler_name = INFERENCE_SCHEDULER_NAME
model_name = MODEL_NAME_FOR_CREATING_INFERENCE_SCHEDULER
INFERENCE_DATA_SOURCE_BUCKET = 'amzn-s3-demo-source-bucket'
​
INFERENCE_DATA_SOURCE_PREFIX = 'data-source-prefix'
​
INFERENCE_DATA_OUTPUT_BUCKET = 'amzn-s3-demo-destination-bucket'
​
INFERENCE_DATA_OUTPUT_PREFIX = 'data-output-prefix'
​
ROLE_ARN_FOR_INFERENCE = ROLE_ARN
​
DATA_UPLOAD_FREQUENCY = 'data-upload-frequency'
​
create_inference_scheduler_request = {
    'ModelName': model_name,
    'InferenceSchedulerName': scheduler_name,
    'DataUploadFrequency': DATA_UPLOAD_FREQUENCY,
    'RoleArn': ROLE_ARN_FOR_INFERENCE,
}
​
if DATA_DELAY_OFFSET_IN_MINUTES is not None:
    create_inference_scheduler_request['DataDelayOffsetInMinutes'] = DATA_DELAY_OFFSET_IN_MINUTES
​
# Set up data input configuration.
inference_input_config = dict()
inference_input_config['S3InputConfiguration'] = dict(
    [
        ('Bucket', INFERENCE_DATA_SOURCE_BUCKET),
        ('Prefix', INFERENCE_DATA_SOURCE_PREFIX)
    ]
)
if INPUT_TIMEZONE_OFFSET is not None:
    inference_input_config['InputTimeZoneOffset'] = INPUT_TIMEZONE_OFFSET
if COMPONENT_TIMESTAMP_DELIMITER is not None or TIMESTAMP_FORMAT is not None:
    inference_input_name_configuration = dict()
    if COMPONENT_TIMESTAMP_DELIMITER is not None:
        inference_input_name_configuration['ComponentTimestampDelimiter'] = COMPONENT_TIMESTAMP_DELIMITER
    if TIMESTAMP_FORMAT is not None:
        inference_input_name_configuration['TimestampFormat'] = TIMESTAMP_FORMAT
    inference_input_config['InferenceInputNameConfiguration'] = inference_input_name_configuration
create_inference_scheduler_request['DataInputConfiguration'] = inference_input_config
​
#  Set up output configuration.
inference_output_configuration = dict()
inference_output_configuration['S3OutputConfiguration'] = dict(
    [
        ('Bucket', INFERENCE_DATA_OUTPUT_BUCKET),
        ('Prefix', INFERENCE_DATA_OUTPUT_PREFIX)
    ]
)
create_inference_scheduler_request['DataOutputConfiguration'] = inference_output_configuration
​
########################################################
# Invoke create_inference_scheduler
########################################################
​
create_scheduler_response = lookoutequipment.create_inference_scheduler(**create_inference_scheduler_request)
​
print("\n\n=====CreateInferenceScheduler Response=====\n")
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(create_scheduler_response)
print("\n=====End of CreateInferenceScheduler Response=====")
​
########################################################
# Wait until RUNNING
########################################################
scheduler_status = create_scheduler_response['Status']
print("=====Polling Inference Scheduler Status=====\n")
print("Model Status: " + scheduler_status)
while scheduler_status == 'PENDING':
    time.sleep(5)
    describe_scheduler_response = lookoutequipment.describe_inference_scheduler(InferenceSchedulerName=INFERENCE_SCHEDULER_NAME)
    scheduler_status = describe_scheduler_response['Status']
    print("Scheduler Status: " + scheduler_status)
print("\n=====End of Polling Inference Scheduler Status=====")

```
