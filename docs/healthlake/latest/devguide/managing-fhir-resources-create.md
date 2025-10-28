# Creating a FHIR resource

The FHIR `create` interaction creates a new FHIR resource in a HealthLake data
store. For additional information, see [`create`](https://hl7.org/fhir/R4/http.html#create "https://hl7.org/fhir/R4/http.html#create") in the **FHIR R4 RESTful API documentation**.

###### To create a FHIR resource

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Determine the type of FHIR `Resource` to create. For more information, see
   [Resource types](reference-fhir-resource-types.md "reference-fhir-resource-types.md").
3. Construct a URL for the request using the collected values for HealthLake `region`
   and `datastoreId`. Also include the FHIR `Resource` type to create.
   To view the entire URL path in the following example, scroll over the
   **Copy** button.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`Resource`
```

4. Construct a JSON body for the request, specifying the FHIR data for the new resource.
   For the purpose of this procedure, we are using a FHIR `Patient` resource, so
   save the file as `create-patient.json`.

```
{
    "resourceType": "Patient",
    "identifier": [
        {
            "system": "urn:oid:1.2.36.146.595.217.0.1",
            "value": "12345"
        }
    ],
    "name": [
        {
            "family": "Silva",
            "given": [
                "Ana",
                "Carolina"
            ]
        }
    ],
    "gender": "female",
    "birthDate": "1992-02-10"
}

```

5. Send the request. The FHIR `create` interaction uses a `POST`
   request with either [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") or
   SMART on FHIR authorization. The following examples create a FHIR `Patient`
   resource in HealthLake using either curl or the HealthLake Console. To view an entire example, scroll
   over the **Copy** button.

SigV4
SigV4 authorization

```
curl --request POST \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastore-id`/r4/Patient' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json' \
  --data @create-patient.json

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

###### Note

The HealthLake Console supports only [AWS SigV4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
authorization.

1. Sign in to the [Run query](https://console.aws.amazon.com/healthlake/home#/crud "https://console.aws.amazon.com/healthlake/home#/crud") page on the HealthLake Console.

2. Under the **Query settings** section, make the following
   selections.
   - **Data Store ID** — choose a data store ID to generate
     a query string.
   - **Query type** — choose `Create`.
   - **Resource type** — choose the FHIR [resource type](reference-fhir-resource-types.md "reference-fhir-resource-types.md") to create.
   - **Request body** — construct a JSON body for the
     request, specifying the FHIR data for the new resource.

3. Choose **Run query**.

###### Configuring validation level for resource creation

When creating a FHIR resource, you can optionally specify an `x-amzn-healthlake-fhir-validation-level`
HTTP header to configure a validation level for the resource. AWS HealthLake currently supports the following validation levels:

- `strict`: Resources are validated according to the profile element of
  the resource, or the R4 specification if no profile is present. This is the default validation
  level for AWS HealthLake.
- `structure-only`: Resources are validated against R4, ignoring any
  referenced profiles.
- `minimal`: Resources are validated minimally, ignoring certain R4
  rules. Resources that fail structure checks required for search/analytics will be updated to
  include a warning for audit.
  Resources created with the minimal validation level may be ingested into a Datastore despite
  failing validation required for search indexing. In this case, resources will be updated to include
  a Healthlake specific extension to document said failures:

```
{
    "url": "http://healthlake.amazonaws.com/fhir/StructureDefinition/validation-issue",
    "valueString": "{\"resourceType\":\"OperationOutcome\",\"issue\":[{\"severity\":\"error\",\"code\":\"processing\",\"details\":{\"text\":\"FHIR resource in payload failed FHIR validation rules.\"},\"diagnostics\":\"FHIR resource in payload failed FHIR validation rules.\"}]}"
}
```

Additionally, the following HTTP response header will be included with a value of "true":

```
x-amzn-healthlake-validation-issues : true
```

###### Note

The data ingested that is malformed according the R4 specification may not be
searchable as expected if these errors are present.
