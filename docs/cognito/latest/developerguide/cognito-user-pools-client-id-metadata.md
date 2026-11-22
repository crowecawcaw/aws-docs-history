

# Client ID metadata documents (CIMD)

Client ID metadata document (CIMD) is an OAuth extension for authorizing external clients without per-client registration. An external client identifies itself to your user pool with an `https` URL as its `client_id`. The client hosts a JSON metadata document at that URL. Amazon Cognito fetches the document during the `/oauth2/authorize` request. Amazon Cognito then uses the document as the client's registration for that request.

With CIMD, you authorize many external clients without creating an app client for each one. You also avoid per-client Dynamic Client Registration and the storage and lifecycle cleanup that dynamic clients require.

Amazon Cognito supports external CIMD clients with user pools. Amazon Cognito doesn't host metadata documents for its own app clients.

**Important**  
CIMD clients are public clients. The metadata document's `token_endpoint_auth_method` value must support `none`. Amazon Cognito doesn't support confidential CIMD clients, `private_key_jwt`, or symmetric, shared-secret client authentication for CIMD.  
CIMD doesn't support the `client_credentials` grant.

## How CIMD policies work
<a name="cognito-user-pools-client-id-metadata-how-policies-work"></a>

CIMD doesn't replace app clients. A CIMD policy maps a set of metadata URL patterns to exactly one existing user pool app client. Amazon Cognito allows a grant type for a CIMD client only when both the associated app client and the client's metadata document include it.

To use CIMD, you create one app client as the basis for authorization. You then create a CIMD policy that maps metadata URL patterns to that app client. Each external client hosts its own metadata document at a URL that matches a pattern. Amazon Cognito authorizes those clients without a separate app client for each one.

Amazon Cognito includes the `client_id_metadata_document_supported` indicator in a user pool's `.well-known` OpenID Connect discovery document only when the user pool has at least one CIMD policy.

**Important**  
You can create up to 10 CIMD policies in a user pool.

## Metadata URL patterns and wildcards
<a name="cognito-user-pools-client-id-metadata-url-patterns"></a>

A CIMD policy matches client metadata URLs against one or more patterns. Each pattern must use the `https` scheme. Custom schemes aren't allowed.

You can use a single `*` wildcard in a pattern, for example `https://*.example.com/cimd/metadata.json`. A pattern can contain only one wildcard. Amazon Cognito doesn't support the `**` sequence or other regular expression or glob syntax. Host matching is case-insensitive, but path matching is case-sensitive.

When more than one pattern matches a URL, Amazon Cognito applies the most specific match. For example, `https://foo.example.com/tenant/*/metadata.json` is more specific than `https://*.foo.example.com/client-3/metadata.json`.

Amazon Cognito rejects any `/oauth2/authorize` request whose `client_id` URL doesn't match a pattern in a policy.

**Note**  
Amazon Cognito rejects a pattern that is only a wildcard, such as `https://*`. A pattern must specify at least part of the host or the path. We still recommend narrow patterns for more granular control over the clients that you authorize, because a broad pattern can match more clients than you intend.

## Validation and caching
<a name="cognito-user-pools-client-id-metadata-validation-caching"></a>

When a pattern contains no wildcards, Amazon Cognito attempts to retrieve and validate the metadata document asynchronously after you call `CreateCIMDPolicy` or `UpdateCIMDPolicy`. Amazon Cognito doesn't fail the request if it can't reach the document at that time.

When a pattern contains a wildcard, Amazon Cognito retrieves and validates the document at runtime, during the `/oauth2/authorize` request. If Amazon Cognito can't reach the document at that time, it returns an error without a redirect. To troubleshoot a runtime fetch error, review your AWS CloudTrail event history.

Amazon Cognito limits each metadata document to 5 KiB. Amazon Cognito allows 1 second for each fetch request and retries the request up to 3 times.

The `CacheDuration` value of a policy sets how long Amazon Cognito caches a metadata document, in seconds. The minimum is 86,400 seconds (1 day). The maximum is 31,556,952 seconds (1 year).

Amazon Cognito sets cache expiry from the `cache-control` headers on the fetched document. Amazon Cognito applies the policy's `CacheDuration` value instead when the document has no `cache-control` header, or when the header value is below the minimum or above the maximum.

**Important**  
A change to `CacheDuration` doesn't update existing cache entries. Amazon Cognito applies the new value only to new or refreshed entries.  
To act on a cached URL before it's automatically refreshed, call `UpdateClientMetadataURLState`. The `REFRESH` action re-fetches the document now. The `INVALIDATE` action removes the URL from the cache and policy without waiting for expiry.

## Grant types, scopes, and redirect URIs
<a name="cognito-user-pools-client-id-metadata-grants-scopes-redirects"></a>

At runtime, Amazon Cognito determines grant types, scopes, and redirect URIs for a CIMD request as follows:
+ Amazon Cognito allows a grant type only when the associated app client, the CIMD metadata document, and the `/oauth2/authorize` request all include it. Amazon Cognito supports the `authorization code` and `implicit` grants for CIMD.
+ Amazon Cognito grants the scopes that are both configured on the associated app client and requested in the `/oauth2/authorize` request. The metadata document doesn't need to declare scopes. If the request doesn't include the `scope` parameter, Amazon Cognito grants all scopes that are configured on the app client.
+ Amazon Cognito takes redirect URIs from the CIMD metadata document, not from the associated app client.

Amazon Cognito allows redirect URIs that point to `localhost` or loopback addresses (the IPv4 and IPv6 equivalents) when the metadata document provides them, and permits loopback hosts to use arbitrary ports at runtime to support locally running clients. This arbitrary-port behavior is the same rule that Amazon Cognito applies to all app clients. For more information, see [app client callback URLs](user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-about). The restriction on `localhost` applies to the `client_id` URL and the policy's URL patterns, not to redirect URIs.

Scopes can be any valid resource server scope that you define, or the standard OpenID Connect scopes: `openid`, `profile`, `email`, `address`, and `phone`.

## Setting up a CIMD policy (console)
<a name="cognito-user-pools-client-id-metadata-setup-console"></a>

You can create and manage CIMD policies in the Amazon Cognito console. The following procedure describes the general steps.

**To set up a CIMD policy (console)**

1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). If prompted, enter your AWS credentials.

1. Choose **User Pools**.

1. Choose a user pool from the list.

1. In the navigation pane, choose **MCP Auth**.

1. Choose the app client that you want a CIMD policy to authorize against.

1. Create a CIMD policy. Enter a policy name, and add one or more metadata URL patterns.

1. (Optional) Set a cache duration between 86,400 seconds (1 day) and 31,556,952 seconds (1 year).

1. Save the policy.

## Managing CIMD policies (AWS CLI and AWS API)
<a name="cognito-user-pools-client-id-metadata-manage-cli-api"></a>

You can create, update, describe, list, and delete CIMD policies with the AWS CLI and the Amazon Cognito user pools API. You can also list the client metadata URLs for a policy and refresh or invalidate an individual URL.

Create a CIMD policy with the `create-cimd-policy` command. The `--cache-duration` parameter is optional. Specify the user pool, the associated app client, a policy name, and one or more URL patterns:

```
aws cognito-idp create-cimd-policy \
    --user-pool-id {{MyUserPoolID}} \
    --client-id {{MyAppClientID}} \
    --policy-name {{MyCIMDPolicy}} \
    --url-patterns {{https://*.example.com/cimd/metadata.json}} \
    --cache-duration {{86400}}
```

Get the configuration of a CIMD policy with the `describe-cimd-policy` command:

```
aws cognito-idp describe-cimd-policy \
    --user-pool-id {{MyUserPoolID}} \
    --cimd-policy-id {{MyCIMDPolicyID}}
```

Update a CIMD policy with the `update-cimd-policy` command. The policy name and cache duration are optional. You must specify the associated app client and the URL patterns:

```
aws cognito-idp update-cimd-policy \
    --user-pool-id {{MyUserPoolID}} \
    --cimd-policy-id {{MyCIMDPolicyID}} \
    --client-id {{MyAppClientID}} \
    --url-patterns {{https://*.example.com/cimd/metadata.json}}
```

Delete a CIMD policy with the `delete-cimd-policy` command:

```
aws cognito-idp delete-cimd-policy \
    --user-pool-id {{MyUserPoolID}} \
    --cimd-policy-id {{MyCIMDPolicyID}}
```

The `list-cimd-policies` command is paginated. List the CIMD policies in a user pool:

```
aws cognito-idp list-cimd-policies \
    --user-pool-id {{MyUserPoolID}} \
    --max-results {{10}}
```

The `list-client-metadata-urls` command is paginated. List the client metadata URLs for a policy:

```
aws cognito-idp list-client-metadata-urls \
    --user-pool-id {{MyUserPoolID}} \
    --cimd-policy-id {{MyCIMDPolicyID}} \
    --max-results {{10}}
```

Refresh or invalidate a single client metadata URL with the `update-client-metadata-url-state` command. Set `--action` to `REFRESH` to re-fetch the document now, or to `INVALIDATE` to remove the URL from the cache:

```
aws cognito-idp update-client-metadata-url-state \
    --user-pool-id {{MyUserPoolID}} \
    --cimd-policy-id {{MyCIMDPolicyID}} \
    --url {{https://client1.example.com/cimd/metadata.json}} \
    --action {{REFRESH}}
```