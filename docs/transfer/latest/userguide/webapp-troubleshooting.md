# Troubleshooting your web apps

###### Note

These troubleshooting tips are meant for the web app administrator rather than the
end user. For end users, if you encounter any problems, contact your web app
administrator. All instances of _you_ in the following paragraphs
refer to the web app admin.

## Troubleshoot network errors

Description

Your end user sees a network banner **Network Error** upon
loading the web app endpoint.

Cause

The most common issues are as follows:

- The admin did not assign the user that is attempting to log on to the new
  application.
- The admin did not add the necessary actions to your IAM roles.
- You see a list of S3 Access Grants assigned to your user, but CORS is not
  configured correctly for your Amazon S3 bucket or buckets.

Solution

- In IAM Identity Center, make sure to assign the user to the correct application. Or, if
  you have a group assigned, make sure that the user attempting to log in
  belongs to the correct group. This is described in [Assign or add users or groups to a Transfer Family
  web app](webapp-add-users.md "webapp-add-users.md").
- Check whether your roles contain the necessary actions in the
  **Custom trust policy** for both
  `sts:AssumeRole` and `sts:SetContext` actions.
  This is described in [Configure IAM roles for Transfer Family web apps](webapp-roles.md "webapp-roles.md").
- Check the CORS policy for all of the buckets used by your web app. This is
  described in [Set up Cross-origin resource
  sharing (CORS) for your Amazon S3 bucket](access-grant-cors.md#cors-configure "access-grant-cors.md#cors-configure").

## Troubleshoot configured bucket not

appearing

Description

Everything appears to be configured correctly, but the Amazon S3 bucket doesn't appear
in the web app.

Cause

One possible cause is that the Amazon S3 bucket is not in the same account as the web
app.

Solution

Ensure that the Amazon S3 bucket is in the same account as the web app. Cross-account
buckets are not currently supported.

## Troubleshoot custom URL errors

Description

When your end user signs into the web app, they receive the error message
**Authorization failed: missing authorization code.**

Cause

If you used CloudFront directly, rather than the supplied CloudFormation template, you have
likely misconfigured the origin request policy to not forward query strings.

Solution

Update your origin request policy to forward query strings and cookies to the
origin.

Description

When your end user attempts to access a Transfer Family web app, they receive a 404
response.

Cause

If you used CloudFront directly, rather than the supplied CloudFormation template, you have
likely misconfigured the cache policy to include the `Host` header in the
cache key or misconfigured the origin request policy to forward the
`Host` header.

Solution

- Make sure that your cache policy does not include the `Host`
  header in the cache key
- Make sure that your origin request policy does not forward the
  `Host` header.

## Troubleshoot miscellaneous errors

Description

Your end user cannot log in, or cannot view any buckets or files, or you receive
another error.

Cause

One possible cause is that the IAM Identity Center instance ARN doesn't match the value for your
grants ARN or your web app IAM Identity Center instance ARN.

Solution

Check the following items to see if they match.

- In IAM Identity Center, navigate to **Settings** and view the
  **Instance ARN**.

```
arn:aws:sso:::instance/ssoins-`instance-identifier`
```

- In Amazon S3, navigate to **Access Grants** and view your
  **IAM Identity Center instance ARN**.

```
arn:aws:sso::`account-id`:application/ssoins-`instance-identifier`/apl-1234567890abcdef0
```

- In Transfer Family, navigate to your web app details page and view its Instance
  ARN.

```
arn:aws:sso:::instance/ssoins-`instance-identifier`
```

The `instance-identifier` value must be the same in all
three of these places.

## Duplicate S3 buckets appearing in web app

Description

Users see the same S3 bucket listed multiple times in the Transfer Family web app interface.

Cause

This occurs when a user is part of multiple Active Directory groups that have duplicate grants to the same S3 bucket. The web app lists all top-level grants associated with the user (UID or GID) regardless of whether the user has multiple grants assigned to the same bucket location.

Solution

To resolve this issue, administrators should de-duplicate the grants so that each user has only one grant to each S3 location. Review your S3 Access Grants configuration and consolidate duplicate grants for the same bucket across different Active Directory groups.
