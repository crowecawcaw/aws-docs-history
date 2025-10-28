# Creating a HealthLake data store

Use `CreateFHIRDatastore` to create an AWS HealthLake data store conformant to the FHIR R4
specification. HealthLake data stores are used for importing, managing, searching, and exporting
FHIR data. You can choose to import (preload) Synthea open source FHIR R4 health data into
your data store when you create it. For more information, see [Preloaded data
types](reference-healthlake-preloaded-data-types.md "reference-healthlake-preloaded-data-types.md").

###### Important

HealthLake supports two types of FHIR data store authorization strategies, AWS SigV4 or
SMART on FHIR. You must choose one of the authorization strategies prior to creating a HealthLake
FHIR data store. For more information, see [Data store authorization
strategy](getting-started-concepts.md#concept-data-store-authorization-strategy "getting-started-concepts.md#concept-data-store-authorization-strategy").

When you create a HealthLake data store, a FHIR data repository is made available via a RESTful
API [endpoint](reference-healthlake-endpoints-quotas.md#reference-healthlake-endpoints "reference-healthlake-endpoints-quotas.md#reference-healthlake-endpoints"). After you've created your
HealthLake data store, you can request its [Capability Statement](reference-fhir-capability-statement.md "reference-fhir-capability-statement.md") to find all associated FHIR-related capabilities (behaviors).

The following menus provide examples for the AWS CLI and AWS SDKs and a procedure for the
AWS Management Console. For more information, see [`CreateFHIRDatastore`](../APIReference/API_CreateFHIRDatastore.md "../APIReference/API_CreateFHIRDatastore.md") in the _AWS HealthLake API Reference_.

###### To create a HealthLake data store

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**Example 1: Create a SigV4-enabled HealthLake data store**

The following `create-fhir-datastore` example demonstrates how to create a new data store in AWS HealthLake.

```
`aws healthlake create-fhir-datastore \
 --datastore-type-version `R4` \
 --datastore-name `"FhirTestDatastore"``

```

Output:

```
{
    "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/",
    "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)",
    "DatastoreStatus": "CREATING",
    "DatastoreId": "(Data store ID)"
}
```

**Example 2: Create a SMART on FHIR-enabled HealthLake data store**

The following `create-fhir-datastore` example demonstrates how to create a new SMART on FHIR-enabled data store in AWS HealthLake.

```
`aws healthlake create-fhir-datastore \
 --datastore-name `"your-data-store-name"` \
 --datastore-type-version `R4` \
 --preload-data-config PreloadDataType="SYNTHEA" \
 --sse-configuration '`{ "KmsEncryptionConfig": { "CmkType": "CUSTOMER_MANAGED_KMS_KEY", "KmsKeyId": "arn:aws:kms:us-east-1:your-account-id:key/your-key-id" } }`' \
 --identity-provider-configuration `file://identity_provider_configuration.json``

```

Contents of `identity_provider_configuration.json`:

```
{
    "AuthorizationStrategy": "SMART_ON_FHIR_V1",
    "FineGrainedAuthorizationEnabled": true,
    "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
    "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\"]}"
}
```

Output:

```
{
    "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/",
    "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)",
    "DatastoreStatus": "CREATING",
    "DatastoreId": "(Data store ID)"
}
```

- For API details, see
  [CreateFHIRDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/create-fhir-datastore.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/create-fhir-datastore.html")
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


    def create_fhir_datastore(
        self,
        datastore_name: str,
        sse_configuration: dict[str, any] = None,
        identity_provider_configuration: dict[str, any] = None,
    ) -> dict[str, str]:
        """
        Creates a new HealthLake data store.
        When creating a SMART on FHIR data store, the following parameters are required:
        - sse_configuration: The server-side encryption configuration for a SMART on FHIR-enabled data store.
        - identity_provider_configuration: The identity provider configuration for a SMART on FHIR-enabled data store.

        :param datastore_name: The name of the data store.
        :param sse_configuration: The server-side encryption configuration for a SMART on FHIR-enabled data store.
        :param identity_provider_configuration: The identity provider configuration for a SMART on FHIR-enabled data store.
        :return: A dictionary containing the data store information.
        """
        try:
            parameters = {"DatastoreName": datastore_name, "DatastoreTypeVersion": "R4"}
            if (
                sse_configuration is not None
                and identity_provider_configuration is not None
            ):
                # Creating a SMART on FHIR-enabled data store
                parameters["SseConfiguration"] = sse_configuration
                parameters[
                    "IdentityProviderConfiguration"
                ] = identity_provider_configuration

            response = self.health_lake_client.create_fhir_datastore(**parameters)
            return response
        except ClientError as err:
            logger.exception(
                "Couldn't create data store %s. Here's why %s",
                datastore_name,
                err.response["Error"]["Message"],
            )
            raise



```

The following code shows an example of parameters for a SMART on FHIR-enabled HealthLake data store.

```
            sse_configuration = {
                "KmsEncryptionConfig": {"CmkType": "AWS_OWNED_KMS_KEY"}
            }
            # TODO: Update the metadata to match your environment.
            metadata = {
                "issuer": "https://ehr.example.com",
                "jwks_uri": "https://ehr.example.com/.well-known/jwks.json",
                "authorization_endpoint": "https://ehr.example.com/auth/authorize",
                "token_endpoint": "https://ehr.token.com/auth/token",
                "token_endpoint_auth_methods_supported": [
                    "client_secret_basic",
                    "foo",
                ],
                "grant_types_supported": ["client_credential", "foo"],
                "registration_endpoint": "https://ehr.example.com/auth/register",
                "scopes_supported": ["openId", "profile", "launch"],
                "response_types_supported": ["code"],
                "management_endpoint": "https://ehr.example.com/user/manage",
                "introspection_endpoint": "https://ehr.example.com/user/introspect",
                "revocation_endpoint": "https://ehr.example.com/user/revoke",
                "code_challenge_methods_supported": ["S256"],
                "capabilities": [
                    "launch-ehr",
                    "sso-openid-connect",
                    "client-public",
                ],
            }
            # TODO: Update the IdpLambdaArn.
            identity_provider_configuration = {
                "AuthorizationStrategy": "SMART_ON_FHIR_V1",
                "FineGrainedAuthorizationEnabled": True,
                "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
                "Metadata": json.dumps(metadata),
            }
            data_store = self.create_fhir_datastore(
                datastore_name, sse_configuration, identity_provider_configuration
            )


```

- For API details, see
  [CreateFHIRDatastore](../../../goto/boto3/healthlake-2017-07-01/CreateFHIRDatastore.md "../../../goto/boto3/healthlake-2017-07-01/CreateFHIRDatastore.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

###### Note

The following procedure creates a HealthLake data store with [AWS SigV4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") authorization. The
HealthLake Console does not support the creation of a SMART on FHIR data store.

###### To create a HealthLake data store with AWS SigV4 authorization

1. Sign in to the [Create data store](https://console.aws.amazon.com/healthlake/home#/create-datastore "https://console.aws.amazon.com/healthlake/home#/create-datastore") page on the HealthLake Console.
2. Choose **Create Data Store**.
3. In the **Data Store settings** section, for **Data Store
   name**, specify a name.
4. (Optional) In the **Data Store settings** section, for
   **Preload sample data**, select the check box to preload Synthea
   data. Synthea data is an open-source sample dataset. For more information, see [Synthea preloaded data types for
   HealthLake](reference-healthlake-preloaded-data-types.md "reference-healthlake-preloaded-data-types.md").
5. In the **Data Store encryption** section, choose either
   **Use AWS owned key (default)** or **Choose a different AWS
   KMS key (advanced)**.
6. In the **Tags - _optional_** section, you can
   add tags to your data store. To learn more about tagging your data store, see [Tagging HealthLake data stores](managing-data-stores-tagging.md "managing-data-stores-tagging.md").
7. Choose **Create Data Store**.

The status of your data store is available on the **Data stores**
page.
