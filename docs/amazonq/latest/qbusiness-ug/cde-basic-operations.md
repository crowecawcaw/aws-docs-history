# Using basic operations for Amazon Q Business document enrichment

With document enrichment, you can use basic operations to manipulate document
attributes. For example, you can remove document attribute values, modify attribute
values using conditions, or create document attributes.

###### Note

Amazon Q Business can't create a target document attribute field if it
isn't already created as an index field.

###### Topics

- [Basic operations using the Amazon Q Business API](#cde-basic-operations-api "#cde-basic-operations-api")
- [Basic operations using the
  Amazon Q Business console](#cde-basic-operations-console "#cde-basic-operations-console")
- [Use cases for basic
  operations](#cde-basic-operations-examples "#cde-basic-operations-examples")
- [Code examples of basic
  operations](#cde-basic-operations-code-samples "#cde-basic-operations-code-samples")

## Basic operations using the Amazon Q Business API

To apply basic logic, you specify your document attribute configuration using
the [DocumentAttributeTarget](../api-reference/API_DocumentAttributeTarget.md "../api-reference/API_DocumentAttributeTarget.md") object
when you use either the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation. Use
the following parameters to create your configuration:

- `key` – The target field that you want to
  manipulate. For example, the key `Department` is a field or
  attribute that holds all the department names associated with the
  documents.
- `value` – The target value for your target
  attribute.
- `attributeValueOperator` – To delete an existing
  target value, set to `DELETE`. The default value for this
  parameter is `UPDATE`.

If a specific condition is met, you can also specify a value to use in the
target field. Set the condition using the [DocumentAttributeCondition](../api-reference/API_DocumentAttributeCondition.md "../api-reference/API_DocumentAttributeCondition.md")
object. For example, if the `_source_uri` field contains
`financial` in its URI value, you can choose to pre-fill the
target field `department` with the target value `finance`
for the document.

For more information, see the following topics in the _Amazon Q Business API Reference_:

- [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md")
- [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md")
- [DocumentAttributeTarget](../api-reference/API_DocumentAttributeTarget.md "../api-reference/API_DocumentAttributeTarget.md")
- [DocumentAttributeCondition](../api-reference/API_DocumentAttributeCondition.md "../api-reference/API_DocumentAttributeCondition.md")

## Basic operations using the

Amazon Q Business console

###### To apply basic logic using the console

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In **Applications**, select the name of your
   application environment from the list of applications.
3. From the left navigation menu, choose
   **Enhancements**, and then choose **Document enrichments**.
4. In **Document enrichments**, choose **Add
   document enrichment**.
5. In **Configure basic operations**, for **Document enrichment source**, choose a data source
   connected to your application environment.
6. To apply basic manipulations to your document fields and content, go
   to **Configure basic operations** .
7. Choose **Next** to save your configuration.

## Use cases for basic

operations

This section provides two examples of basic operations.

**Example 1: Removing customer identification numbers
associated with the documents**

The following is an example of using a basic operation to remove all customer
identification numbers in the document field called
`customer_id`.

The following table shows the data before basic manipulation is
applied.

| **\_document_id** | **\_document_body** | **customer_id** |
| ----------------- | ------------------- | --------------- |
| 1                 | Example text        | CID1234         |
| 2                 | Example text        | CID1235         |
| 3                 | Example text        | CID1236         |

The following table shows the data after basic manipulation is applied.

| **\_document_id** | **\_document_body** | **customer_id** |
| ----------------- | ------------------- | --------------- |
| 1                 | Example text        |                 |
| 2                 | Example text        |                 |
| 3                 | Example text        |                 |

**Example 2: Creating and pre-filling the
Department field with department names associated with
the documents using a condition**

The following is an example of using basic logic to create a field called
`Department` and pre-filling the field with the department names
based on information from the `_source_uri` field. This example uses
the condition that, if the `_source_uri` field contains
`financial` in its URI value, then the target field
`department` is pre-filled with the target value
`finance` for the document.

The following table shows the data before basic manipulation is
applied.

| **\_document_id** | **document_body** | **\_source_uri** |
| ----------------- | ----------------- | ---------------- |
| 1                 | Example text      | financial/1      |
| 2                 | Example text      | financial/2      |
| 3                 | Example text      | financial/3      |

The following table shows the data after basic manipulation is applied.

| **\_document_id** | **\_document_body** | **\_source_uri** | **department** |
| ----------------- | ------------------- | ---------------- | -------------- |
| 1                 | Example text        | financial/1      | Finance        |
| 2                 | Example text        | financial/2      | Finance        |
| 3                 | Example text        | financial/3      | Finance        |

## Code examples of basic

operations

The following instructions give examples of configuring basic data
manipulation to remove customer identification numbers associated with the
documents.

Console
**To configure basic data manipulation to
remove customer identification numbers**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. From the left navigation pane, select **Document
   enrichments** and then select **Add
   document enrichment**.
3. On the **Configure basic operations**
   page, choose from the data source that you want to alter
   document fields and content in.
4. Select the document field name
   **Customer_ID** from the dropdown menu,
   and then select the target action
   **Delete**.
5. Select **Add basic operation**.

AWS CLI
**To configure basic data manipulation to
remove customer identification numbers**

```
aws qbusiness create-data-source \
 --name `data-source-name` \
 --application-id `application-id` \
 --index-id `index-id` \
 --role-arn `arn:aws:iam::account-id:role/role-name` \
 --type S3 \
 --configuration '{"S3Configuration":{"BucketName":"`S3-bucket-name`"}}' \
 --document-enrichment-configuration '{"InlineDocumentEnrichmentConfiguration":[{"Target":{"key":"Customer_ID", "attributeValueOperator": "DELETE"}}]}'
```

Python
**To configure basic data manipulation to
remove customer identification numbers**

```
import boto3
from botocore.exceptions import ClientError
import pprint
import time

qbusiness = boto3.client("qbusiness")

print("Create a data source with customizations")

# Provide the name of the data source
name = "data-source-name"
# Provide the application environment ID for the data source
application_id = "`application-id`"
# Provide the index ID for the data source
index_id = "index-id"
# Provide the IAM role ARN required for data sources
role_arn = "arn:aws:iam::${account-id}:role/${role-name}"
# Provide the data source connection information
data_source_type = "S3"
S3_bucket_name = "S3-bucket-name"
# Configure the data source with Document Enrichment
configuration = {"S3Configuration":
        {
            "BucketName": S3_bucket_name
        }
    }
document_enrichment_configuration = {"InlineDocumentEnrichmentConfiguration":[
        {
            "Target":{"key":"Customer_ID",
                       "attributeValueOperator": "DELETE"}
        }]
    }

try:
    data_source_response = qbusiness.create_data_source(
        Name = name,
        ApplicationId = application_id,
        IndexId = index_id,
        RoleArn = role_arn,
        Type = data_source_type
        Configuration = configuration
        DocumentEnrichmentConfiguration = document_enrichment_configuration
    )

    pprint.pprint(data_source_response)

    data_source_id = data_source_response["Id"]

    print("Wait for Amazon Q to create the data source with your customizations.")

    while True:
        # Get the details of the data source, such as the status
        data_source_description = qbusiness.get_data_source(
            DataSourceId = data_source_id,
            ApplicationId = application_id,
            IndexId = index_id
        )
        status = data_source_description["Status"]
        print(" Creating data source. Status: "+status)
        time.sleep(60)
        if status != "CREATING":
            break

    print("Synchronize the data source.")

    sync_response = qbusiness.start_data_source_sync_job(
        DataSourceId = data_source_id,
        ApplicationId = application_id,
        IndexId = index_id
    )

    pprint.pprint(sync_response)

    print("Wait for the data source to sync with the index.")

    while True:

        jobs = qbusiness.list_data_source_sync_jobs(
            DataSourceId = data_source_id,
            ApplicationId = application_id,
            IndexId = index_id
        )

        # For this example, there should be one job
        status = jobs["History"][0]["Status"]

        print(" Syncing data source. Status: "+status)
        time.sleep(60)
        if status != "SYNCING":
            break

except  ClientError as e:
        print("%s" % e)

print("Program ends.")
```

Java
**To configure basic data manipulation to
remove customer identification numbers**

```
package com.amazonaws.qbusiness;

import java.util.concurrent.TimeUnit;
import software.amazon.awssdk.services.qbusiness.QBusinessClient;
import software.amazon.awssdk.services.qbusiness.model.AttributeValueOperator;
import software.amazon.awssdk.services.qbusiness.model.CreateDataSourceRequest;
import software.amazon.awssdk.services.qbusiness.model.CreateDataSourceResponse;
import software.amazon.awssdk.services.qbusiness.model.CreateIndexRequest;
import software.amazon.awssdk.services.qbusiness.model.CreateIndexResponse;
import software.amazon.awssdk.services.qbusiness.model.DataSourceConfiguration;
import software.amazon.awssdk.services.qbusiness.model.DataSourceStatus;
import software.amazon.awssdk.services.qbusiness.model.DataSourceSyncJob;
import software.amazon.awssdk.services.qbusiness.model.DataSourceSyncJobStatus;
import software.amazon.awssdk.services.qbusiness.model.DataSourceType;
import software.amazon.awssdk.services.qbusiness.model.GetDataSourceRequest;
import software.amazon.awssdk.services.qbusiness.model.GetDataSourceResponse;
import software.amazon.awssdk.services.qbusiness.model.IndexStatus;
import software.amazon.awssdk.services.qbusiness.model.ListDataSourceSyncJobsRequest;
import software.amazon.awssdk.services.qbusiness.model.ListDataSourceSyncJobsResponse;
import software.amazon.awssdk.services.qbusiness.model.DataSourceConfiguration;
import software.amazon.awssdk.services.qbusiness.model.StartDataSourceSyncJobRequest;
import software.amazon.awssdk.services.qbusiness.model.StartDataSourceSyncJobResponse;

public class CreateDataSourceWithCustomizationsExample {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Create a data source with customizations");

        String dataSourceName = "data-source-name";
        String applicationId = "`application-id`";
        String indexId = "index-id";
        String dataSourceRoleArn = "arn:aws:iam::account-id:role/role-name";
        String s3BucketName = "S3-bucket-name"

        QBusinessClient qbusiness = QBusinessClient.builder().build();

        CreateDataSourceRequest createDataSourceRequest = CreateDataSourceRequest
            .builder()
            .name(dataSourceName)
            .applicationId(applicationId)
            .indexId(indexId)
            .description(experienceDescription)
            .roleArn(experienceRoleArn)
            .type(DataSourceType.S3)
            .configuration(
                DataSourceConfiguration
                    .builder()
                    .s3Configuration(
                        S3DataSourceConfiguration
                            .builder()
                            .bucketName(s3BucketName)
                            .build().Q Business carries
                    ).build()
            )
            .documentEnrichmentConfiguration(
                DocumentEnrichmentConfiguration
                    .builder()
                    .inlineDocumentEnrichmentConfiguration(Arrays.asList(
                        InlineDocumentEnrichmentConfiguration
                            .builder()
                            .target(
                                DocumentAttributeTarget
                                    .builder()
                                    .key("Customer_ID")
                                    .attributeValueOperator(AttributeValueOperator.DELETE)
                                    .build())
                            .build()
                    )).build();

        CreateDataSourceResponse createDataSourceResponse = qbusiness.createDataSource(createDataSourceRequest);
        System.out.println(String.format("Response of creating data source: %s", createDataSourceResponse));

        String dataSourceId = createDataSourceResponse.id();
        System.out.println(String.format("Waiting for Amazon Q to create the data source %s", dataSourceId));
        GetDataSourceRequest getDataSourceRequest = GetDataSourceRequest
            .builder()
            .applicationId(applicationId).Q Business carries
            .indexId(indexId)
            .datasourceId(dataSourceId)
            .build();

        while (true) {
            GetDataSourceResponse getDataSourceResponse = qbusiness.getDataSource(getDataSourceRequest);

            DataSourceStatus status = getDataSourceResponse.status();
            System.out.println(String.format("Creating data source. Status: %s", status));
            TimeUnit.SECONDS.sleep(60);
            if (status != DataSourceStatus.CREATING) {
                break;
            }
        }

        System.out.println(String.format("Synchronize the data source %s", dataSourceId));
        StartDataSourceSyncJobRequest startDataSourceSyncJobRequest = StartDataSourceSyncJobRequest
            .builder()
            .applicationId(applicationId)
            .indexId(indexId)
            .datasourceId(dataSourceId)
            .build();
        StartDataSourceSyncJobResponse startDataSourceSyncJobResponse = qbusiness.startDataSourceSyncJob(startDataSourceSyncJobRequest);
        System.out.println(String.format("Waiting for the data source to sync with the application environment %s index %s for execution ID %s", applicationId, indexId, startDataSourceSyncJobResponse.executionId()));

        // For this example, there should be one job
        ListDataSourceSyncJobsRequest listDataSourceSyncJobsRequest = ListDataSourceSyncJobsRequest
            .builder()
            .applicationId(applicationId)
            .indexId(indexId)
            .datasourceId(dataSourceId)
            .build();

        while (true) {
            ListDataSourceSyncJobsResponse listDataSourceSyncJobsResponse = qbusiness.listDataSourceSyncJobs(listDataSourceSyncJobsRequest);
            DataSourceSyncJob job = listDataSourceSyncJobsResponse.history().get(0);
            System.out.println(String.format("Syncing data source. Status: %s", job.status()));

            TimeUnit.SECONDS.sleep(60);
            if (job.status() != DataSourceSyncJobStatus.SYNCING) {
                break;
            }

        }

        System.out.println("Data source creation with customizations is complete");
    }
}
```
