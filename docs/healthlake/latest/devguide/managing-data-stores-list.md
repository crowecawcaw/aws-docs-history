# Listing HealthLake data stores

Use `ListFHIRDatastores` to list all HealthLake data stores in a user's account,
regardless of data store status. The following menus provide a procedure for the AWS Management Console
and code examples for the AWS CLI and AWS SDKs. For more information, see [`ListFHIRDatastores`](../APIReference/API_ListFHIRDatastores.md "../APIReference/API_ListFHIRDatastores.md") in the _AWS HealthLake API
Reference_.

###### To list all HealthLake data stores

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**To list FHIR data stores**

The following `list-fhir-datastores` example shows to how to use the command and how users can filter results based on data store status in AWS HealthLake.

```
`aws healthlake list-fhir-datastores \
 --filter `DatastoreStatus=ACTIVE``

```

Output:

```
{
    "DatastorePropertiesList": [
    {
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
    ]
}
```

- For API details, see
  [ListFHIRDatastores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-datastores.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-datastores.html")
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


    def list_fhir_datastores(self) -> list[dict[str, any]]:
        """
        Lists all HealthLake data stores.
        :return: A list of data store descriptions.
        """
        try:
            next_token = None
            datastores = []

            # Loop through paginated results.
            while True:
                parameters = {}
                if next_token is not None:
                    parameters["NextToken"] = next_token
                response = self.health_lake_client.list_fhir_datastores(**parameters)
                datastores.extend(response["DatastorePropertiesList"])
                if "NextToken" in response:
                    next_token = response["NextToken"]
                else:
                    break

            return datastores
        except ClientError as err:
            logger.exception(
                "Couldn't list data stores. Here's why %s", err.response["Error"]["Message"]
            )
            raise


```

- For API details, see
  [ListFHIRDatastores](../../../goto/boto3/healthlake-2017-07-01/ListFHIRDatastores.md "../../../goto/boto3/healthlake-2017-07-01/ListFHIRDatastores.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

- Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores "https://console.aws.amazon.com/healthlake/home#/list-datastores") page on the HealthLake Console.

All HealthLake data stores are listed under the **Data stores** section.
