# Deleting a FHIR resource

The FHIR `delete` interaction removes an existing FHIR resource from a HealthLake
data store. For additional information, see [`delete`](https://hl7.org/fhir/R4/http.html#delete "https://hl7.org/fhir/R4/http.html#delete") in the **FHIR R4 RESTful API documentation**.

###### To delete a FHIR resource

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Determine the type of FHIR `Resource` to delete and collect the associated
   `id` value. For more information, see [Resource types](reference-fhir-resource-types.md "reference-fhir-resource-types.md").
3. Construct a URL for the request using the collected values for HealthLake `region`
   and `datastoreId`. Also include the FHIR `Resource` type and its
   associated `id`. To view the entire URL path in the following example, scroll
   over the **Copy** button.

```
DELETE https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`Resource`/`id`
```

4. Send the request. The FHIR `delete` interaction uses a `DELETE`
   request with either [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") or
   SMART on FHIR authorization. The following `curl` example removes an existing
   FHIR `Patient` resource from a HealthLake data store. To view the entire example,
   scroll over the **Copy** button.

SigV4
SigV4 authorization

```
curl --request DELETE \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json'

```

The server returns a `204` HTTP status code confirming the resource has
been removed from the HealthLake data store. If a delete request fails, you will receive a
`400` series HTTP status code indicating why the request failed.

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
   - **Query type** — choose `Delete`.
   - **Resource type** — choose the FHIR [resource type](reference-fhir-resource-types.md "reference-fhir-resource-types.md") to delete.
   - **Resource ID** — enter the FHIR resource ID.

3. Choose **Run query**.

## Deleting FHIR resources based on conditions

Conditional delete is particularly useful when you don't know the specific FHIR resource ID but have other identifying information about the resource you want to delete.

Conditional delete allows you to delete an existing resource based on search criteria rather than by logical FHIR ID. When the server processes the delete request, it performs a search using standard search capabilities for the resource type to resolve a single logical ID for the request.

### How conditional delete works

###### The server's action depends on how many matches it finds:

1. **No matches**: The server attempts an ordinary delete and responds appropriately (404 Not Found for non-existent resource, 204 No Content for already deleted resource)
2. **One match**: The server performs an ordinary delete on the matching resource
3. **Multiple matches**: Returns a 412 Precondition Failed error indicating the client's criteria were not selective enough

### Response scenarios

AWS HealthLake handles conditional delete operations with the following response patterns:

###### Successful Operations

- When your search criteria successfully identify a single active resource, the system returns **204 No Content** after completing the deletion, just like standard delete operations.

###### ID-Based Conditional Delete

When performing conditional delete based on `id` with additional parameters (`createdAt`, `tag`, or `_lastUpdated`):

- **204 No Content**: Resource was already deleted
- **404 Not Found**: Resource doesn't exist
- **409 Conflict**: ID matches but other parameters don't match

###### Non-ID-Based Conditional Delete

When `id` is not provided or when using parameters other than `createdAt`, `tag`, or `_lastUpdated`:

- **404 Not Found**: No matches found

###### Conflict Situations

Several scenarios result in 412 Precondition Failed responses:

- Multiple resources match your search criteria (criteria not specific enough)
- Version conflicts when using ETag headers with `If-Match`
- Resource updates occurring between search and delete operations

###### Example of a Successful Conditional Delete

The following example deletes a Patient resource based on specific criteria:

```
DELETE https://healthlake.region.amazonaws.com/datastore/datastoreId/r4/Patient?name=peter&birthdate=2000-01-01&phone=1234567890
```

This request deletes a Patient resource where:

- Name is "peter"
- Birth date is January 1, 2000
- Phone number is 1234567890

###### Best Practices

1. Use specific search criteria to avoid multiple matches and prevent 412 errors.
2. Consider ETag headers for version control when needed to handle concurrent modifications.
3. Handle error responses appropriately:
   - For 404: Refine your search criteria
   - For 412: Make criteria more specific or resolve version conflicts

4. Prepare for timing conflicts in high-concurrency environments where resources may be modified between search and delete operations.
