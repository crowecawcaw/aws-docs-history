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

When performing conditional delete based on `id` with additional parameters (`createdAt`, `_tag`, or `_lastUpdated`):

- **204 No Content**: Resource was already deleted
- **404 Not Found**: Resource doesn't exist
- **409 Conflict**: ID matches but other parameters don't match

###### Non-ID-Based Conditional Delete

When `id` is not provided or when using parameters other than `createdAt`, `_tag`, or `_lastUpdated`:

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

### Deleting multiple FHIR resources in one request with `_count`

By default, a conditional delete requires your search criteria to match exactly one resource. To
delete multiple matching resources in a single request, include the `_count` query
parameter. When `_count` is present, HealthLake processes the request as a batch operation. It
searches for matching resources, deletes them, and returns HTTP `200` with a FHIR
`Bundle` of type `batch-response` that contains a per-resource status.

- The _search parameters_ determine _which_ resources
  match. `_count` sets the upper limit on how many matching resources to delete in a
  single request.
- `_count` cannot exceed your data store's maximum page size (default
  100). If you specify a value above this limit, HealthLake returns `400 Bad Request`.
  If more resources match than the `_count` value allows, use pagination to delete the
  remaining matches. For more information, see [Search parameters](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md").
- Total delete throughput is bounded by your data store's write capacity. For your account's
  current limits, see [Endpoints and
  quotas](reference-healthlake-endpoints-quotas.md "reference-healthlake-endpoints-quotas.md").

###### Example request

The following request deletes matching `Coverage` resources tagged
`inactive`:

```
DELETE https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Coverage?_tag=inactive&_count=50
```

#### Batch response format

A request that includes `_count` returns HTTP `200` with a
`batch-response` `Bundle`. Each entry reports the outcome for one matched
resource:

- **204 No Content**: the resource was deleted.
- **412 Precondition Failed**: another operation modified the resource
  between the search and the delete (version conflict), so HealthLake doesn't delete it. Sending the
  conditional delete again runs a new search and removes the resource only if it still matches
  your criteria. Because search results are eventually consistent, a recently modified resource
  might not appear immediately.
- **403 Forbidden**: SMART on FHIR authorization denied deleting this
  resource.

As with any FHIR search, the order in which resources are matched and deleted follows the
order of the underlying search results. The search doesn't guarantee this order unless you include
the `_sort` parameter in your search criteria. If you need a deterministic order across
paginated batch deletes, specify `_sort`. For more information, see [Search parameters](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md").

Within the response `Bundle`, entry order is likewise not guaranteed. Match each
entry to its resource using the `location` field in the entry's
`response`, rather than relying on entry position.

###### Important

Batch conditional delete is not atomic. Some resources in a request can be deleted while
others return errors in the same `Bundle`. Always check the per-entry status codes in
the response `Bundle` rather than assuming the whole request succeeded or failed.

###### Important

When the search matches no resources, a request with `_count` returns HTTP
`200` with an empty `batch-response` `Bundle` (no entries). This
differs from a conditional delete _without_ `_count`, which returns
`404 Not Found` when nothing matches.

###### Partial success (version conflict)

A resource can be modified between the search and the delete. Successfully deleted resources
return `204`; conflicting resources return `412` in the same
`Bundle`.

```
{
  "resourceType": "Bundle",
  "type": "batch-response",
  "entry": [
    {
      "response": {
        "status": "204",
        "location": "Coverage/b807f9ff-2872-45df-9325-0b2efe42e554"
      }
    },
    {
      "response": {
        "status": "412",
        "location": "Coverage/5287b322-d7e5-4688-bd55-022067db4d0f",
        "outcome": {
          "resourceType": "OperationOutcome",
          "issue": [
            {
              "severity": "error",
              "code": "exception",
              "diagnostics": "Resource was modified by another operation. Retry the request."
            }
          ]
        }
      }
    }
  ]
}

```

#### Deleting more matches with pagination

A single request deletes at most one page of matches. If more matching resources remain, the
response `Bundle` includes a `link` with a `next` relation and a
URL. Send an HTTP `DELETE` request to that URL to delete the next page, and repeat until
the response no longer contains a `next` link. The `next` link must be
followed with `DELETE` (the same method as the original request), not
`GET`.

```
{
  "resourceType": "Bundle",
  "type": "batch-response",
  "link": [
    {
      "relation": "next",
      "url": "https://healthlake.us-east-1.amazonaws.com/...<page_token>"
    }
  ],
  "entry": [
    {
      "response": {
        "status": "204",
        "location": "Patient/4aeffdc9-6ac5-46ff-be10-bf8bd74dfecc"
      }
    }
  ]
}

```

#### SMART on FHIR authorization behavior

- **Insufficient delete permission**: if the caller can search but lacks
  delete permission, the request still returns `200` and the affected resources appear
  as `403` entries in the `Bundle` (nothing is deleted for those
  resources).
- **Insufficient read/search permission**: if the caller cannot run the
  underlying search, the entire request fails at the root level with an
  `OperationOutcome` (no `Bundle` is returned), regardless of delete
  permission.
- **IAM authorization**: IAM evaluates permissions at the request level, not
  per resource. The calling principal must be authorized for both the delete and the search
  actions (for example, `healthlake:DeleteResource` and the applicable search action,
  because the operation runs a search to find matches). An unauthorized principal is denied the
  entire request.

For more information about configuring SMART on FHIR authorization, see [SMART on FHIR](reference-smart-on-fhir.md "reference-smart-on-fhir.md").

#### How service quotas apply

Batch conditional delete does not have its own service quota. Each request draws on the same
existing HealthLake quotas as the search and delete interactions it performs, so a single request
consumes multiple quota units:

- **One search**: to resolve the matching resources, each request performs a
  search and consumes search (read) capacity, just like a standard FHIR search.
- **One delete per matched resource**: each resource that is deleted consumes
  delete (write) capacity, the same as an individual delete. A request that deletes
  _N_ resources consumes one search plus _N_
  deletes.
- **Resources per request**: each request deletes at most one page of
  matches (default page size 100). To delete more matches, use pagination.

Throughput is governed by your data store's write capacity. To manage throughput within your
account's quota limits, either issue more requests with a smaller `_count` value, or use
a narrower search with a larger `_count` value. For your account's current search and
write capacity limits, see [Endpoints and
quotas](reference-healthlake-endpoints-quotas.md "reference-healthlake-endpoints-quotas.md").

#### Considerations

- `_count` must be a positive integer. A non-integer or out-of-range value returns
  `400 Bad Request` with a validation `OperationOutcome`. When
  `_count=1`, the response is still a `batch-response` `Bundle`,
  not the single-resource response returned by a conditional delete without
  `_count`.
- The `If-Match` header is not supported together with `_count`. A
  request that includes both returns `400 Bad Request`.
- Batch conditional delete is not supported inside `Bundle` requests.
- Only successfully deleted resources are metered. Resources returned with a `412`
  or `403` status are not metered.
