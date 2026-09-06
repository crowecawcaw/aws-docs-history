

# Creating a SMART on FHIR enabled HealthLake data store
<a name="reference-smart-on-fhir-create-data-store"></a>

To use the SMART on FHIR framework with HealthLake, create a HealthLake data store with the `IdentityProviderConfiguration` parameter specified in your `CreateFHIRDatastore` request. In the `IdentityProviderConfiguration` parameter you specify the following information:
+ Set the [AuthorizationStrategy](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) equal to `SMART_ON_FHIR_V1`.
+ Set the [IdpLambdaArn](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) equal to the ARN of the AWS Lambda you created to manage token decoding with your authorization server.
+ Define the [Metadata](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) elements specified in the authorization server as a JSON block. These metadata elements are returned in the Discovery Document.
+ *Optional*: Enable [FineGrainedAuthorizationEnabled](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html). Specify `True` to use the Fine grained authorization provided by HealthLake

**Note**  
After you create the data store, you can change its identity provider configuration—including the `AuthorizationStrategy`, `IdpLambdaArn`, `Metadata`, and `FineGrainedAuthorizationEnabled` values—by using `UpdateFHIRDatastore`. Updating the identity provider configuration replaces it in full, so include every field you want to keep; any field you omit is cleared. Identity provider updates take effect immediately and do not move the data store to the `UPDATING` status. For more information, see [Updating a HealthLake data store](managing-data-stores-update.md).

You can make a SMART on FHIR enabled data store using the AWS Command Line Interface (AWS CLI) or via one of the AWS supported SDKs. Creating a SMART on FHIR enabled HealthLake data store is not supported using the HealthLake console.

## Using the AWS CLI to create a SMART on FHIR enabled HealthLake data store
<a name="create-smart-ds-request"></a>

You can use the following code example to create SMART on FHIR enabled HealthLake data store using the AWS CLI. When creating a SMART on FHIR enabled HealthLake data store you must specify the [`identity-provider-configuration`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) parameter.

In the `identity-provider-configuration` parameter you can *optionally* enable fine-grained authorization by setting `FineGrainedAuthorizationEnabled` equal to `True`. To learn more about Fine grained authorization, see [Using fine-grained authorization with a SMART on FHIR enabled HealthLake data store](reference-smart-on-fhir-fine-grained-authorization.md). The example below contains a special character `\` to indicate line breaks or as an escape character. This is for clarity.

```
aws healthlake create-fhir-datastore \
  --region us-east-1 \
  --datastore-name "your-data-store-name" \
  --datastore-type-version R4 \
  --preload-data-config PreloadDataType="SYNTHEA" \
  --sse-configuration '{ "KmsEncryptionConfig": { \
    "CmkType": "customer-managed-kms-key1",
    "KmsKeyId": "arn:aws:kms:us-east-1:your-account-id:key/your-key-id" } }' \
  --identity-provider-configuration  \
      '{"AuthorizationStrategy": "SMART_ON_FHIR_V1", \
      "FineGrainedAuthorizationEnabled": boolean-false-by-default, \
      "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name", \
      "Metadata": "{\"issuer\":\"https://ehr.example.com\",\"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credentials\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openid\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\"]}"}'
```

When successful you get the following JSON response:

```
{
  "DatastoreArn": "arn:aws:healthlake:your-region:111122223333:datastore/fhir/your-datastore-id",
  "DatastoreEndpoint": "https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/",
  "DatastoreId": "your-data-store-id",
  "DatastoreStatus": "data-store-creation-status"
}
```