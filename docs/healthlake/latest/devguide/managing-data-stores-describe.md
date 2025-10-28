# Getting HealthLake data store properties

Use `DescribeFHIRDatastore` to get properties for an AWS HealthLake data store. The
following menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS
SDKs. For more information, see [`DescribeFHIRDatastore`](../APIReference/API_DescribeFHIRDatastore.md "../APIReference/API_DescribeFHIRDatastore.md") in the _AWS HealthLake API
Reference_.

###### To get properties for a HealthLake data store

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**To describe a FHIR data store**

The following `describe-fhir-datastore` example demonstrates how to find the properties of a data store in AWS HealthLake.

```
`aws healthlake describe-fhir-datastore \
 --datastore-id `"1f2f459836ac6c513ce899f9e4f66a59"``

```

Output:

```
{
    "DatastoreProperties": {
        "PreloadDataConfig": {
            "PreloadDataType": "SYNTHEA"
        },
        "SseConfiguration": {
            "KmsEncryptionConfig": {
                "CmkType": "CUSTOMER_MANAGED_KMS_KEY",
                "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            }
        },
        "DatastoreName": "Demo",
        "DatastoreArn": "arn:aws:healthlake:us-east-1:<AWS Account ID>:datastore/<Data store ID>",
        "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/<Data store ID>/r4/",
        "DatastoreStatus": "ACTIVE",
        "DatastoreTypeVersion": "R4",
        "CreatedAt": 1603761064.881,
        "DatastoreId": "<Data store ID>",
        "IdentityProviderConfiguration": {
            "AuthorizationStrategy": "AWS_AUTH",
            "FineGrainedAuthorizationEnabled": false
        }
    }
}
```

- For API details, see
  [DescribeFHIRDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-datastore.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-datastore.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)


    def describe_fhir_datastore(self, datastore_id: str) -> dict[str, any]:
        """
        Describes a HealthLake data store.
        :param datastore_id: The data store ID.
        :return: The data store description.
        """
        try:
            response = self.health_lake_client.describe_fhir_datastore(
                DatastoreId=datastore_id
            )
            return response["DatastoreProperties"]
        except ClientError as err:
            logger.exception(
                "Couldn't describe data store with ID %s. Here's why %s",
                datastore_id,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [DescribeFHIRDatastore](../../../goto/boto3/healthlake-2017-07-01/DescribeFHIRDatastore.md "../../../goto/boto3/healthlake-2017-07-01/DescribeFHIRDatastore.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

1. Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores "https://console.aws.amazon.com/healthlake/home#/list-datastores") page on the HealthLake Console.
2. Choose a data store.

The **Data Store details** page opens and all HealthLake data store
properties are available.
