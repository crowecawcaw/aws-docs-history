# Updating a FHIR resource

The FHIR `update` interaction creates a new current version for an existing
resource or creates an initial version if no resource already exists for the given
`id`. For additional information, see [`update`](https://hl7.org/fhir/R4/http.html#update "https://hl7.org/fhir/R4/http.html#update") in the **FHIR R4 RESTful API documentation**.

###### To update a FHIR resource

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Determine the type of FHIR `Resource` to update and collect the associated
   `id` value. For more information, see [Resource types](reference-fhir-resource-types.md "reference-fhir-resource-types.md").
3. Construct a URL for the request using the collected values for HealthLake `region`
   and `datastoreId`. Also include the FHIR `Resource` type and its
   associated `id`. To view the entire URL path in the following example, scroll
   over the **Copy** button.

```
PUT https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`Resource`/`id`
```

4. Construct a `JSON` body for the request, specifying the FHIR data updates
   to be made. For the purpose of this procedure, save the file as
   `update-patient.json`.

```
{
    "id": "2de04858-ba65-44c1-8af1-f2fe69a977d9",
    "resourceType": "Patient",
    "active": true,
    "name": [
        {
            "use": "official",
            "family": "Doe",
            "given": [
                "Jane"
            ]
        },
        {
            "use": "usual",
            "given": [
                "Jane"
            ]
        }
    ],
    "gender": "female",
    "birthDate": "1985-12-31"
}

```

5. Send the request. The FHIR `update` interaction uses a `PUT`
   request with either [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") or
   SMART on FHIR authorization. The following `curl` example updates a
   `Patient` resource in HealthLake. To view the entire example, scroll over the
   **Copy** button.

SigV4
SigV4 authorization

```
curl --request PUT \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json' \
  --data @update-patient.json

```

Your request will return a `200` HTTP status code if an existing
resource is _updated_ or a `201` HTTP status code if a
new resource is created.

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
   - **Query type** — choose `Update
(PUT)`.
   - **Resource type** — choose the FHIR [resource type](reference-fhir-resource-types.md "reference-fhir-resource-types.md") to update or
     create.
   - **Request body** — construct a JSON body for the
     request, specifying the FHIR data to update the resource with.

3. Choose **Run query**.

## Updating FHIR resources based

on conditions

Conditional update allows you to update an existing resource based on some identification
search criteria, rather than by logical FHIR `id`. When the server processes the
update, it performs a search using its standard search capabilities for the resource type,
with the goal of resolving a single logical `id` for the request.

The action the server takes depends on how many matches it finds:

- **No matches, no `id` provided in the request
  body**: The server creates the FHIR resource.
- **No matches, `id` provided and resource doesn't
  already exist with the `id`**: The server treats the interaction as
  an Update as Create interaction.
- **No matches, `id` provided and already
  exist**: The server rejects the update with a `409 Conflict`
  error.
- **One Match, no resource `id` provided OR (resource
  `id` provided and it matches the found resource)**: The server
  performs the update against the matching resource as above where, if the resource was
  updated, the server SHALL return a `200 OK`.
- **One Match, resource `id` provided but does not match
  resource found**: The server returns a `409 Conflict` error
  indicating the client id specification was a problem preferably with an
  `OperationOutcome`
- **Multiple matches**: The server returns a `412
Precondition Failed` error indicating the client's criteria were not selective
  enough preferably with an OperationOutcome

The following example updates a `Patient` resource whose name is peter,
birthdate is 1st Jan 2000, and phone number is 1234567890.

```
PUT https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?name=peter&birthdate=2000-01-01&phone=1234567890
```

## Configuring validation level for resource updates

When updating a FHIR resource, you can optionally specify an `x-amzn-healthlake-fhir-validation-level`
HTTP header to configure a validation level for the resource. AWS HealthLake currently supports the following validation levels:

- `strict`: Resources are validated according to the profile element of
  the resource, or the R4 specification if no profile is present. This is the default validation
  level for AWS HealthLake.
- `structure-only`: Resources are validated against R4, ignoring any
  referenced profiles.
- `minimal`: Resources are validated minimally, ignoring certain R4
  rules. Resources that fail structure checks required for search/analytics will be updated to
  include a warning for audit.

Resources updated with the minimal validation level may be ingested into a Datastore despite
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

Note that data ingested that is malformed according the R4 specification may not be
searchable as expected if these errors are present.
