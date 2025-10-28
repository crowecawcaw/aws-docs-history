# Introduction to Feature Store example

notebook

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

The example code on this page refers to the [Introduction to Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html") example notebook. We recommend that you run this notebook
in Studio Classic, notebook instances, or JupyterLab because the code in this guide is conceptual
and not fully functional if copied.

Use the following to clone the [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples") GitHub repository, containing the example
notebook:

- **For Studio Classic**

Launch Studio Classic. You can open Studio Classic if Studio or Studio Classic is enabled
as your default experience. For instructions on how to open Studio Classic, see [Launch Amazon SageMaker Studio Classic Using the Amazon SageMaker AI Console](studio-launch.md#studio-launch-console "studio-launch.md#studio-launch-console").

Clone the [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples") GitHub repository to Studio Classic by
following the steps in [Clone a Git Repository in Amazon SageMaker Studio Classic](studio-tasks-git.md "studio-tasks-git.md").

- **For Amazon SageMaker notebook instances**

Launch SageMaker notebook instance by following the instructions in [Access Notebook Instances](howitworks-access-ws.md "howitworks-access-ws.md").
Now that you have the SageMaker AI example notebooks, navigate to the
`amazon-sagemaker-examples/sagemaker-featurestore` directory and open the
[Introduction to Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html") example notebook.

## Step 1: Set up your SageMaker AI session

To start using Feature Store, create a SageMaker AI session. Then, set up the Amazon Simple Storage Service (Amazon S3) bucket
that you want to use for your features. The Amazon S3 bucket is your offline store. The
following code uses the SageMaker AI default bucket and adds a custom prefix to it.

###### Note

The role that you use to run the notebook must have the following managed policies
attached to it: `AmazonS3FullAccess` and
`AmazonSageMakerFeatureStoreAccess`. For information about adding
policies to your IAM role, see [Adding policies to your IAM role](feature-store-adding-policies.md "feature-store-adding-policies.md").

```
# SageMaker Python SDK version 2.x is required
import sagemaker
import sys
```

```
import boto3
import pandas as pd
import numpy as np
import io
from sagemaker.session import Session
from sagemaker import get_execution_role

prefix = 'sagemaker-featurestore-introduction'
role = get_execution_role()

sagemaker_session = sagemaker.Session()
region = sagemaker_session.boto_region_name
s3_bucket_name = sagemaker_session.default_bucket()
```

## Step 2: Inspect your data

In this notebook example, we ingest synthetic data from the [GitHub repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore/data "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore/data") that hosts the full notebook.

```
customer_data = pd.read_csv("data/feature_store_introduction_customer.csv")
orders_data = pd.read_csv("data/feature_store_introduction_orders.csv")

print(customer_data.head())
print(orders_data.head())
```

The following diagram illustrates the steps that data goes through before Feature Store ingests it.
In this notebook, we illustrate the use case where you have data from multiple sources and
want to store them independently in a Feature Store. Our example considers data from a data warehouse
(customer data), and data from a real-time streaming service (order data).

![Feature group creation and data ingestion in Feature Store for this example notebook.](images/feature-store/feature-store-intro-diagram.png)

## Step 3: Create

feature groups

We first start by creating feature group names for customer_data and orders_data.
Following this, we create two feature groups, one for `customer_data` and
another for `orders_data`:

```
import time
from time import strftime, gmtime
customers_feature_group_name = 'customers-feature-group-' + strftime('%d-%H-%M-%S', gmtime())
orders_feature_group_name = 'orders-feature-group-' + strftime('%d-%H-%M-%S', gmtime())
```

Instantiate a `FeatureGroup` object for `customers_data` and
`orders_data`:

```
from sagemaker.feature_store.feature_group import FeatureGroup

customers_feature_group = FeatureGroup(
    name=customers_feature_group_name, sagemaker_session=sagemaker_session
)
orders_feature_group = FeatureGroup(
    name=orders_feature_group_name, sagemaker_session=sagemaker_session
)
```

```
import time
current_time_sec = int(round(time.time()))
record_identifier_feature_name = "customer_id"
```

Append `EventTime` feature to your data frame. This parameter is required,
and timestamps each data point:

```
customer_data["EventTime"] = pd.Series([current_time_sec]*len(customer_data), dtype="float64")
orders_data["EventTime"] = pd.Series([current_time_sec]*len(orders_data), dtype="float64")
```

Load feature definitions to your feature group:

```
customers_feature_group.load_feature_definitions(data_frame=customer_data)
orders_feature_group.load_feature_definitions(data_frame=orders_data)
```

The following calls `create` to create two feature groups,
`customers_feature_group` and `orders_feature_group`,
respectively:

```
customers_feature_group.create(
    s3_uri=f"s3://{s3_bucket_name}/{prefix}",
    record_identifier_name=record_identifier_feature_name,
    event_time_feature_name="EventTime",
    role_arn=role,
    enable_online_store=True
)

orders_feature_group.create(
    s3_uri=f"s3://{s3_bucket_name}/{prefix}",
    record_identifier_name=record_identifier_feature_name,
    event_time_feature_name="EventTime",
    role_arn=role,
    enable_online_store=True
)
```

To confirm that your feature group was created, we display it by using
`DescribeFeatureGroup` and `ListFeatureGroups` APIs:

```
customers_feature_group.describe()
```

```
orders_feature_group.describe()
```

```
sagemaker_session.boto_session.client('sagemaker', region_name=region).list_feature_groups() # We use the boto client to list FeatureGroups
```

## Step 4: Ingest data

into a feature group

After feature groups are created, we can put data into them. If you're using the SageMaker AI
AWS SDK for Python (Boto3), use the `ingest` API call. If you're using SDK for Python (Boto3), then use
the `PutRecord` API. It will take less than 1 minute to ingest data both of
these options. This example uses the SageMaker AI SDK for Python (Boto3), so it uses the `ingest`
API call:

```
def check_feature_group_status(feature_group):
    status = feature_group.describe().get("FeatureGroupStatus")
    while status == "Creating":
        print("Waiting for Feature Group to be Created")
        time.sleep(5)
        status = feature_group.describe().get("FeatureGroupStatus")
    print(f"FeatureGroup {feature_group.name} successfully created.")

check_feature_group_status(customers_feature_group)
check_feature_group_status(orders_feature_group)
```

```
customers_feature_group.ingest(
    data_frame=customer_data, max_workers=3, wait=True
)
```

```
orders_feature_group.ingest(
    data_frame=orders_data, max_workers=3, wait=True
)
```

Using an arbitrary customer record id, 573291 we use `get_record` to check that
the data has been ingested into the feature group.

```
customer_id = 573291
sample_record = sagemaker_session.boto_session.client('sagemaker-featurestore-runtime', region_name=region).get_record(FeatureGroupName=customers_feature_group_name, RecordIdentifierValueAsString=str(customer_id))
```

```
print(sample_record)
```

The following demonstrates how to use the `batch_get_record` to get a batch of
records.

```
all_records = sagemaker_session.boto_session.client(
    "sagemaker-featurestore-runtime", region_name=region
).batch_get_record(
    Identifiers=[
        {
            "FeatureGroupName": customers_feature_group_name,
            "RecordIdentifiersValueAsString": ["573291", "109382", "828400", "124013"],
        },
        {
            "FeatureGroupName": orders_feature_group_name,
            "RecordIdentifiersValueAsString": ["573291", "109382", "828400", "124013"],
        },
    ]
)
```

```
print(all_records)
```

## Step 5: Clean up

Here we remove the Feature Groups that we created.

```
customers_feature_group.delete()
orders_feature_group.delete()
```

## Step 6: Next steps

In this example notebook, you learned how to get started with Feature Store, create feature
groups, and ingest data into them.

For an advanced example on how to use Feature Store for a fraud detection use case, see [Fraud Detection with Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/sagemaker_featurestore_fraud_detection_python_sdk.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/sagemaker_featurestore_fraud_detection_python_sdk.html").

## Step 7: Code examples for

programmers

In this notebook we used a variety of different API calls. Most of them are accessible
through the SageMaker Python SDK, however some only exist within Boto3. You can invoke the
SageMaker Python SDK API calls directly on your Feature Store objects, whereas to invoke API calls
that exist within Boto3, you must first access a Boto3 client through your Boto3 and
SageMaker AI sessions: for example, `sagemaker_session.boto_session.client()`.

The following is a list of API calls for this notebook. These calls exist within the
SDK for Python and exist in Boto3, for your reference:

**SDK for Python (Boto3) API Calls**

```
describe()
ingest()
delete()
create()
load_feature_definitions()
```

**Boto3 API Calls**

```
list_feature_groups()
get_record()
```
