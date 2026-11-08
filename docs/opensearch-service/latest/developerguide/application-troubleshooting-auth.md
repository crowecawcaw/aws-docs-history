

# Resolving sign-in and permission errors in OpenSearch UI
<a name="application-troubleshooting-auth"></a>

The following errors occur when a user cannot sign in to an OpenSearch UI application or cannot reach part of the interface after signing in.

## Resolving 403 Forbidden errors
<a name="application-troubleshooting-auth-403"></a>

A response of `{"status":403,"error":{"reason":"403 Forbidden","type":"Forbidden"}}` indicates that the IAM role is missing the `opensearch:ApplicationAccessAll` permission. Attach it to the role:

```
aws iam put-role-policy \
    --role-name {{role-name}} \
    --policy-name OpenSearchAppAccess \
    --policy-document '{
      "Version":"2012-10-17",
      "Statement":[{
        "Effect":"Allow",
        "Action":"opensearch:ApplicationAccessAll",
        "Resource":"arn:aws:opensearch:{{region}}:{{account-id}}:application/*"
      }]
    }'
```

## Resolving 403 errors for the es:GetApplication permission
<a name="application-troubleshooting-auth-getapplication"></a>

This error appears in the AWS Management Console when a user opens the application from the console and the `es:GetApplication` permission is missing. It is required only for the console flow. Add the following JSON statement to the IAM policy:

```
{
    "Effect": "Allow",
    "Action": "es:GetApplication",
    "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/{{application-id}}"
}
```

## Resolving 400 Bad Request errors on the login endpoint
<a name="application-troubleshooting-auth-login"></a>

A response of `HTTP 400` with the header `x-aoss-response-hint: X01:gw-helper-deny` indicates that a client other than a browser called the `/_login/` endpoint. That endpoint works only in a browser. For programmatic access, sign a request to `/` with Signature Version 4 headers. For instructions on signing requests programmatically, see [Verify access programmatically](application-auth-iam.md#application-auth-iam-verify-programmatic).

## Resolving 401 Unauthorized errors on dashboard pages
<a name="application-troubleshooting-auth-401"></a>

If requests to dashboard pages return `401`, the dashboard administrator is not configured on the application. Configure it with the following command:

```
aws opensearch update-application \
    --id {{application-id}} \
    --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"*"}]' \
    --region {{region}}
```

## Resolving Signature Version 4 signature errors
<a name="application-troubleshooting-auth-sigv4"></a>

A signature mismatch or an invalid signature error indicates that you signed the request with the wrong service name. Sign requests to OpenSearch UI with `opensearch`, not `es` or `aoss`.

## Resolving single sign-on errors
<a name="application-troubleshooting-auth-sso"></a>

For errors that occur with AWS IAM Identity Center, including sign-in that redirects and then returns an error, users who sign in but have no access, and failures that report that the authorization code cannot be validated, see [Troubleshooting AWS IAM Identity Center authentication](application-auth-idc.md#application-auth-idc-troubleshooting).