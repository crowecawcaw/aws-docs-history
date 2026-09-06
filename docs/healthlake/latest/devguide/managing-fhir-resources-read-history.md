

# Reading FHIR resource history
<a name="managing-fhir-resources-read-history"></a>

The FHIR `history` interaction retrieves the history of a particular FHIR resource in a HealthLake data store. Using this interaction, you can determine how the contents of a FHIR resource have changed over time. It is also useful in coordination with audit logs to see the state of a resource before and after modification. The FHIR interactions `create`, `update`, and `delete` result in a historical version of the resource to be saved. For additional information, see [`history`](https://hl7.org/fhir/R4/http.html#history) in the **FHIR R4 RESTful API documentation**.

**Note**  
You can opt out of `history` for specific FHIR resource types. To opt out, create a case using [AWS Support Center Console](https://console.aws.amazon.com/support/home#/). To create your case, log in to your AWS account and choose **Create case**.

**To read FHIR resource history**  


1. Collect HealthLake `region` and `datastoreId` values. For more information, see [Getting data store properties](managing-data-stores-describe.md).

1. Determine the type of FHIR `Resource` to read and collect the associated `id` value. For more information, see [Resource types](reference-fhir-resource-types.md). 

1. Construct a URL for the request using the collected values for HealthLake `region` and `datastoreId`. Also include the FHIR `Resource` type, its associated `id`, and optional search parameters. To view the entire URL path in the following example, scroll over the **Copy** button.

   ```
   GET https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/{{Resource}}/{{id}}/_history{?[parameters]}
   ```  
**HealthLake supported search parameters for FHIR `history` interaction**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/healthlake/latest/devguide/managing-fhir-resources-read-history.html)

1. Send the request. The FHIR `history` interaction uses a `GET` request with either [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) or SMART on FHIR authorization. The following `curl` example uses the `_count` search parameter to return 100 historical search results per page for a FHIR `Patient` resource in HealthLake. To view the entire example, scroll over the **Copy** button.

------
#### [ SigV4 ]

   SigV4 authorization

   ```
   curl --request GET \
     'https://healthlake.{{region}}.amazonaws.com/datastore/{{datastore-id}}/r4/Patient/{{id}}/_history?_count=100' \
     --aws-sigv4 'aws:amz:region:healthlake' \
     --user "{{$AWS_ACCESS_KEY_ID}}:{{$AWS_SECRET_ACCESS_KEY}}" \
     --header "x-amz-security-token:{{$AWS_SESSION_TOKEN}}" \
     --header 'Accept: application/json'
   ```

------
#### [ SMART on FHIR ]

   SMART on FHIR authorization example for the [`IdentityProviderConfiguration`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) data type.

   ```
   {
       "AuthorizationStrategy": "SMART_ON_FHIR",
       "FineGrainedAuthorizationEnabled": true,
       "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
       "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\",\"permission-v2\"]}"
   }
   ```

   The caller can assign permissions in the authorization lambda. For more information, see [OAuth 2.0 scopes](reference-smart-on-fhir-oauth-scopes.md).

------

   The return content of a `history` interaction is contained in a FHIR resource `Bundle`, with type set to `history`. It contains the specified version history, sorted with oldest versions last, and includes deleted resources. For more information, see [`Resource Bundle`](https://hl7.org/fhir/R4/bundle.html) in the **FHIR R4 documentation**.

## Reading version-specific FHIR resource history
<a name="managing-fhir-data-get-version-specific-resource"></a>

The FHIR `vread` interaction performs a version-specific read of a resource in a HealthLake data store. Using this interaction, you can view the contents of a FHIR resource as it was at a particular time in the past.

**Note**  
If you use FHIR `history` interaction *without* `vread`, HealthLake always returns the latest version of the resource's metadata.

HealthLake declares it support for versioning in [`CapabilityStatement.rest.resource.versioning`](https://hl7.org/fhir/R4/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.versioning) for each supported resource. All HealthLake data stores include `Resource.meta.versionId` (`vid`) on all resources.

When FHIR `history` interaction is enabled (by default for data stores created after 10/25/2024 or by request for older data stores), the `Bundle` response includes the `vid` as part of the [`location`](https://hl7.org/fhir/R4/bundle-definitions.html#Bundle.entry.response.location) element. In the following example, the `vid` displays as the number `1`. To view the full example, see [Example Bundle/bundle-response (JSON)](https://build.fhir.org/bundle-response.json.html).

```
"response" : {
    "status" : "201 Created",
    "location" : "Patient/12423/_history/1",
    ...}
```

**To read version-specific FHIR resource history**  


1. Collect HealthLake `region` and `datastoreId` values. For more information, see [Getting data store properties](managing-data-stores-describe.md).

1. Determine the FHIR `Resource` type to read and collect associated `id` and `vid` values. For more information, see [Resource types](reference-fhir-resource-types.md).

1. Construct a URL for the request using the values collected for HealthLake and FHIR. To view the entire URL path in the following example, scroll over the **Copy** button.

   ```
   GET https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/{{Resource}}/{{id}}/_history/{{vid}}
   ```

1. Send the request. The FHIR `history` interaction uses a `GET` request with either [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) or SMART on FHIR authorization. The following `vread` interaction returns a single instance with the content specified for the FHIR `Patient` resource for the version of the resource metadata specified by the `vid`. To view the entire URL path in the following example, scroll over the **Copy** button.

------
#### [ SigV4 ]

   SigV4 authorization

   ```
   curl --request GET \
     'https://healthlake.{{region}}.amazonaws.com/datastore/{{datastore-id}}/r4/Patient/{{id}}/_history/{{vid}}' \
     --aws-sigv4 'aws:amz:region:healthlake' \
     --user "{{$AWS_ACCESS_KEY_ID}}:{{$AWS_SECRET_ACCESS_KEY}}" \
     --header "x-amz-security-token:{{$AWS_SESSION_TOKEN}}" \
     --header 'Accept: application/json'
   ```

------
#### [ SMART on FHIR ]

   SMART on FHIR authorization example for the [`IdentityProviderConfiguration`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html) data type.

   ```
   {
       "AuthorizationStrategy": "SMART_ON_FHIR",
       "FineGrainedAuthorizationEnabled": true,
       "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
       "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\",\"permission-v2\"]}"
   }
   ```

   The caller can assign permissions in the authorization lambda. For more information, see [OAuth 2.0 scopes](reference-smart-on-fhir-oauth-scopes.md).

------