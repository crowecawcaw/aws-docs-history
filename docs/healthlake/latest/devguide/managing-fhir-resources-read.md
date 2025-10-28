# Reading a FHIR resource

The FHIR `read` interaction reads the current state of a resource in a HealthLake
data store. For additional information, see [`read`](https://hl7.org/fhir/R4/http.html#read "https://hl7.org/fhir/R4/http.html#read") in the **FHIR R4 RESTful API documentation**.

###### To read a FHIR resource

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Determine the type of FHIR `Resource` to read and collect the associated
   `id` value. For more information, see [Resource types](reference-fhir-resource-types.md "reference-fhir-resource-types.md").
3. Construct a URL for the request using the collected values for HealthLake `region`
   and `datastoreId`. Also include the FHIR `Resource` type and its
   associated `id`. To view the entire URL path in the following example, scroll
   over the **Copy** button.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`Resource`/`id`
```

4. Send the request. The FHIR `read` interaction uses a `GET`
   request with either [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") or
   SMART on FHIR authorization. The following `curl` example reads the current state
   of a FHIR `Patient` resource in HealthLake. To view the entire example, scroll over
   the **Copy** button.

SigV4
SigV4 authorization

```
curl --request GET \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json'

```

SMART on FHIR
SMART on FHIR authorization example for the [`IdentityProviderConfiguration`](../APIReference/API_IdentityProviderConfiguration.md "../APIReference/API_IdentityProviderConfiguration.md") data type.

```
{
    "AuthorizationStrategy": "SMART_ON_FHIR",
    "FineGrainedAuthorizationEnabled": true,
    "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
    "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\",\"permission-v2\"]}"
}

```

The caller can assign permissions in the authorization lambda. For more
information, see [OAuth 2.0
scopes](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md").

AWS Console

1. Sign in to the [Run query](https://console.aws.amazon.com/healthlake/home#/crud "https://console.aws.amazon.com/healthlake/home#/crud") page on the HealthLake Console.

2. Under the **Query settings** section, make the following
   selections.
   - **Data Store ID** — choose a data store ID to generate
     a query string.
   - **Query type** — choose `Read`.
   - **Resource type** — choose the FHIR [resource type](reference-fhir-resource-types.md "reference-fhir-resource-types.md") to read.
   - **Resource ID** — enter the FHIR resource ID.

3. Choose **Run query**.
