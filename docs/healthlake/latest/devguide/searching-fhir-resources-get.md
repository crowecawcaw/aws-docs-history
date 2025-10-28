# Searching FHIR resources with GET

You can use `GET` requests to search a HealthLake data store. When using
`GET`, HealthLake supports providing search parameters as part of the URL, but not
as part of a request body. For more information, see [FHIR R4 search parameters for HealthLake](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md").

###### Important

For searches that involve personally identifiable information (PII) or protected health information (PHI), security best practices call for
using `POST` requests, as PII and PHI is added as part of the request body
and is encrypted in transit. For more information, see [Searching FHIR resources with POST](searching-fhir-resources-post.md "searching-fhir-resources-post.md").

The following procedure is followed by examples that use `GET` to search a
HealthLake data store.

###### To search a HealthLake data store with `GET`

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Determine the type of FHIR resource to search for and collect the associated
   `id` value. For more information, see [Resource types](reference-fhir-resource-types.md "reference-fhir-resource-types.md").
3. Construct a URL for the request using the collected values for HealthLake
   `region` and `datastoreId`. Also include the FHIR
   `Resource` type and supported [search parameters](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md"). To view the
   entire URL path in the following example, scroll over the
   **Copy** button.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`Resource{?[parameters]{&_format=[mime-type]}}`
```

4. Send the `GET` request with either [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
   or SMART on FHIR authorization. The following `curl` example returns the
   total number of `Patient` resources in a HealthLake data store. To view the
   entire example, scroll over the **Copy** button.

SigV4
SigV4 authorization

```
curl --request GET \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_total=accurate' \
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

###### Note

The HealthLake Console supports only SigV4 authorization. SMART on FHIR
authorization is supported through AWS CLI and AWS SDKs.

1. Sign in to the [Run query](https://console.aws.amazon.com/healthlake/home#/crud "https://console.aws.amazon.com/healthlake/home#/crud") page on the HealthLake
   Console.

2. Under the **Query settings** section, make the
   following selections.
   - **Data Store ID** — choose a data
     store ID to generate a query string.
   - **Query type** — choose `Search
with GET`.
   - **Resource type** — choose the FHIR
     [resource
     type](reference-fhir-resource-types.md "reference-fhir-resource-types.md") to search on.
   - **Search parameters** — Select a [search
     parameter](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md") or combination of search parameters to
     focus your query on specific records.

3. Choose **Run query**.

## Examples: search with

GET

The following tabs provide examples for searching on specific FHIR resource types
with `GET`. The examples show how to specify search parameters in the request
URLs.

###### Note

The HealthLake Console supports only SigV4 authorization. SMART on FHIR authorization
is supported through AWS CLI and AWS SDKs.

HealthLake supports a subset of FHIR R4 search parameters. For more information, see
[Search parameters](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md").

Patient (age)
Although age is not a defined resource type in FHIR, it is captured as
an element in the [`Patient`](https://hl7.org/fhir/R4/patient.html "https://hl7.org/fhir/R4/patient.html") resource type. Use the following
example to make a `GET`-based search request on [`Patient`](https://hl7.org/fhir/R4/patient.html "https://hl7.org/fhir/R4/patient.html")
resource types using the [birthDate](https://hl7.org/fhir/R4/patient-definitions.html#Patient.birthDate "https://hl7.org/fhir/R4/patient-definitions.html#Patient.birthDate") element and the `eq`
[search comparator](reference-fhir-search-parameters.md#search-comparators "reference-fhir-search-parameters.md#search-comparators") to search for
individuals born in the year 1997.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?birthdate=eq1997
```

Condition
Use the following example to make a `GET` request on the [`Condition`](https://hl7.org/fhir/R4/condition.html "https://hl7.org/fhir/R4/condition.html")
resource type. The search finds conditions in your HealthLake data store that
contain the SNOMED medical code `72892002`, which translates to
`Normal pregnancy`.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Condition?code=72892002
```

DocumentationReference
The following example shows how to create a `GET` request on
the [`DocumentReference`](https://hl7.org/fhir/R4/documentreference.html "https://hl7.org/fhir/R4/documentreference.html") resource type for
`Patient`(s) with a streptococcal diagnosis and who have also
been prescribed amoxicillin.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/DocumentReference?_lastUpdated=le2021-12-19&infer-icd10cm-entity-text-concept-score;=streptococcal|0.6&infer-rxnorm-entity-text-concept-score=Amoxicillin|0.8
```

Location
Use the following example to make a `GET` request on the [`Location`](https://hl7.org/fhir/R4/location.html "https://hl7.org/fhir/R4/location.html")
resource type. The following search finds locations in your HealthLake data store
that contain the city name Boston as part of the address.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Location?address=boston
```

Observation
Use the following example to make a `GET`-based search request
on the [`Observation`](https://hl7.org/fhir/R4/observation.html "https://hl7.org/fhir/R4/observation.html") resource type. This search uses
the `value-concept`
[search parameter](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md") to
look for medical code `266919005`, which translates to
`Never smoker`.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Observation?value-concept=266919005
```
