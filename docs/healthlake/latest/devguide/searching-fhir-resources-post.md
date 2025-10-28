# Searching FHIR resources with POST

You can use the FHIR [`search`](https://hl7.org/fhir/R4/search.html "https://hl7.org/fhir/R4/search.html") interaction with `POST` requests to search a
HealthLake data store. When using `POST`, HealthLake supports search parameters in either
the URL or in a request body, but you cannot use both in a single request.

###### Important

For searches that involve personally identifiable information (PII) or protected health information (PHI), security best practices call for
using `POST` requests, as PII and PHI is added as part of the request body
and is encrypted in transit.

The following procedure is followed by examples using FHIR R4 `search`
interaction with `POST` to search a HealthLake data store. The examples show how to
specify search parameters in the JSON request body.

###### To search a HealthLake data store with `POST`

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Determine the type of FHIR resource to search for and collect the associated
   `id` value. For more information, see [Resource types](reference-fhir-resource-types.md "reference-fhir-resource-types.md").
3. Construct a URL for the request using the collected values for HealthLake
   `region` and `datastoreId`. Also include the FHIR
   `Resource` type and `_search` interaction. To view the
   entire URL path in the following example, scroll over the
   **Copy** button.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`Resource`/_search
```

4. Construct a JSON body for the request, specifying the FHIR data to search for.
   For the purpose of this procedure, you will search `Observation`
   resources to discover patients who have never smoked. To specify the medical code
   status `Never smoker`, set `value-concept=266919005` in the
   JSON request body. Save the file as
   `search-observation.json`.

```
value-concept=266919005
```

5. Send the request. The FHIR `search` interaction uses the
   `GET` request with either [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
   or SMART on FHIR authorization.

###### Note

When making a `POST` request with search parameters in the request
body, use `Content-Type: application/x-www-form-urlencoded` as part
of the header.

The following `curl` example makes a POST-based search request on the
`Observation` resource type. The request uses the [`value-concept`](https://hl7.org/fhir/R4/observation.html#search "https://hl7.org/fhir/R4/observation.html#search") search parameter to look for medical code
`266919005` which indicates value `Never smoker`. To view
the entire example, scroll over the **Copy** button.

SigV4
SigV4 authorization

```
curl --request POST \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Observation/_search' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header "Content-Type: application/x-www-form-urlencoded"
  --header "Accept: application/json"
  --data @search-observation.json

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

## Examples: search with

POST

The following tabs provide examples for searching on specific FHIR resource types
with `POST`. The examples show how to specify a request in the URLs.

###### Note

The HealthLake Console supports only SigV4 authorization. SMART on FHIR authorization
is supported through AWS CLI and AWS SDKs.

HealthLake supports a subset of FHIR R4 search parameters. For more information, see
[Search parameters](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md").

Patient (age)
Although age is not a defined resource type in FHIR, it is captured as
an element in the [`Patient`](https://hl7.org/fhir/R4/patient.html "https://hl7.org/fhir/R4/patient.html") resource type. Use the following
example to make a `POST`-based search request on the
`Patient` resource type. The following search example uses
the `eq`
[search comparator](reference-fhir-search-parameters.md#search-comparators "reference-fhir-search-parameters.md#search-comparators") to search for
individuals born in 1997.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/_search
```

To specify the year 1997 in the search, add the following element to the
request body.

```
birthdate=eq1997
```

Condition
Using the following to make a `POST` request on the
`Condition` resource type. This search finds locations in
your HealthLake data store that contain the medical code `72892002`.

You have to specify a request URL and a request body. Here is an example
request URL.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Condition/_search
```

To specify the medical code you want to search, you add the following JSON element
to the request body.

```
code=72892002
```

DocumentReference
To see the results of HealthLake's integrated natural language processing (NLP)
when making a `POST` request on the
`DocumentReference` resource type, format a request as
follows.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/DocumentReference/_search
```

To specify the `DocumentReference` search parameters to
reference, see [Search parameter types](reference-fhir-search-parameters.md#search-parameter-types "reference-fhir-search-parameters.md#search-parameter-types"). The following query
string uses multiple search parameters to search on Amazon Comprehend Medical API operations
used to generate the integrated NLP results.

```
_lastUpdated=le2021-12-19&infer-icd10cm-entity-text-concept-score;=streptococcal|0.6&infer-rxnorm-entity-text-concept-score=Amoxicillin|0.8
```

Location
Use the following example to make a `POST` request on the
`Location` resource type. The search finds locations in your
HealthLake data store that contain the city name Boston as part of the
address.

You must specify a request URL and a request body. Here is an example
request URL.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Location/_search
```

To specify `Boston` in the search, add the following element to
the request body:

```
address=Boston
```

Observation
Use the following example to make a `POST`-based search request
on the `Observation` resource type. The search uses the
`value-concept` search parameter to look for medical code,
`266919005` that indicates `Never smoker`.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Observation/_search
```

To specify the status, `Never smoker` , set
`value-concept=266919005` in the body of the JSON.

```
value-concept=266919005
```
