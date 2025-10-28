# Fetching the SMART on FHIR

Discovery Document

SMART defines a Discovery Document that allows clients to learn the authorization endpoint
URLs and features a HealthLake data store supports. This information helps clients direct
authorization requests to the right endpoint and construct authorization requests the HealthLake
data store supports.

For a client application to make a successful FHIR REST request to HealthLake, it must gather
the authorization requirements defined by the HealthLake data store. A bearer token
(authorization) is _not_ required for this request to succeed..

###### To request the Discovery Document for a HealthLake data store

1. Collect HealthLake `region` and `datastoreId` values. For more
   information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Construct a URL for the request using the collected values for HealthLake
   `region` and `datastoreId`. Append
   `/.well-known/smart-configuration` to the endpoint of the URL. To
   view the entire URL path in the following example, scroll over the
   **Copy** button.

```
https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/.well-known/smart-configuration
```

3. Send the request using `GET` with [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
   signing protocol. To view the entire example, scroll over the
   **Copy** button.

curl

```
curl --request GET \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/.well-known/smart-configuration \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json'

```

The Discovery Document for the HealthLake data store returns as a JSON blob, where you
can find the `authorization_endpoint` and the
`token_endpoint`, along with the specifications and defined capabilities
for the data store.

```
{
    "authorization_endpoint": `"https://oidc.example.com/authorize"`,
    "token_endpoint": `"https://oidc.example.com/oauth/token"`,
    "capabilities": [
        "launch-ehr",
        "client-public"
    ]
}
```

Both the `authorization_endpoint` and the `token_endpoint`
are required to launch a client application.

    * **Authorization endpoint** — The URL
     needed to authorize a client application or user.
    * **Token endpoint** — The endpoint of
     the authorization server the client application uses to communicate
     with.
