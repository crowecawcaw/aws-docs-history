# Troubleshoot authentication issues

This section describes possible solutions for the following authentication issues.

###### Topics

- [Authentication failures—SSH/SFTP](#publickey-auth "#publickey-auth")
- [Managed AD mismatched realms
  issue](#managed-ad-realms-mismatched "#managed-ad-realms-mismatched")
- [Active Directory group limits exceeded](#managed-ad-group-limits "#managed-ad-group-limits")
- [Miscellaneous authentication issues](#misc-auth-issues "#misc-auth-issues")
- [Troubleshoot Amazon API Gateway issues](#transfer-apigateway "#transfer-apigateway")
- [Troubleshoot testing your identity
  provider](#blank-test-identity-provider "#blank-test-identity-provider")
- [Duplicate Amazon S3 buckets in web app](#webapp-duplicate-buckets "#webapp-duplicate-buckets")

## Authentication failures—SSH/SFTP

Description

When you try to connect to your server using Secure Shell (SSH) File Transfer Protocol
(SFTP), you receive a message similar to the following:

```
Received disconnect from 3.130.115.105 port 22:2: Too many authentication failures
  Authentication failed.
```

###### Note

If you are using an API Gateway and receive this error, see [Too many authentication failures](#auth-failures-sftp "#auth-failures-sftp").

Cause

You have not added an RSA key pair for your user, so you must authenticate using a
password instead.

Solution

When you run the `sftp` command, specify the `-o
 PubkeyAuthentication=no` option. This option forces the system to request your
password. For example:

```
sftp -o PubkeyAuthentication=no `sftp-user`@`server-id`.server.transfer.`region-id`.amazonaws.com
```

## Managed AD mismatched realms

issue

Description

A user's realm and their group realm must match. They must both be in the default
realm, or they must both be in the trusted realm.

Cause

If a user and their group do not match, the user cannot be authenticated by Transfer Family. If
you test the identity provider for the user, you receive the error **`No
 associated access found for user's groups`**.

Solution

Reference a group in the user's realm that matches the group realm (either default or
trusted).

## Active Directory group limits exceeded

Description

When attempting to add more Active Directory groups to your AWS Transfer Family server, you
receive an error indicating you've reached the maximum number of groups allowed.

Cause

AWS Transfer Family has a default limit of 100 Active Directory groups per server.

Solution

These are two possible solutions:

- Consolidate your Active Directory groups to reduce the total number
  needed.
- If your use case requires more than 100 groups, consider using a custom
  identity provider solution as described in [Simplify Active Directory authentication with a custom identity provider
  for AWS Transfer Family](https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/ "https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/").

## Miscellaneous authentication issues

Description

You receive an authentication error and none of the other troubleshooting works

Cause

You might have specified a target for a logical directory that contains a leading or
trailing slash (/).

Solution

Update your logical directory target, to make sure it begins with a slash, and does
not contain a trailing slash. For example, `/amzn-s3-demo-bucket/images` is
acceptable, but `amzn-s3-demo-bucket/images` and `/amzn-s3-demo-bucket/images/`
are not.

## Troubleshoot Amazon API Gateway issues

This section describes possible solutions for the following API Gateway issues.

###### Topics

- [Too many authentication failures](#auth-failures-sftp "#auth-failures-sftp")
- [Connection closed](#connection-closed "#connection-closed")

### Too many authentication failures

Description

When you try to connect to your server using Secure Shell (SSH) File Transfer
Protocol (SFTP), you get the following error:

```
Received disconnect from 3.15.127.197 port 22:2: Too many authentication failures
Authentication failed.
Couldn't read packet: Connection reset by peer
```

Cause

You might have entered an incorrect password for your user. Try again to enter the
correct password.

If the password is correct, the issue might be caused by a role Amazon Resource
Name (ARN) that is not valid. To confirm that this is the issue, test the identity
provider for your server. If you see a response similar to the following, the role
ARN is a placeholder only, as indicated by the role ID value of all zeros:

```
{
    "Response": "{\"Role\": \"arn:aws:iam::000000000000:role/MyUserS3AccessRole\",\"HomeDirectory\": \"/\"}",
    "StatusCode": 200,
    "Message": "",
    "Url": "https://`api-gateway-ID`.execute-api.us-east-1.amazonaws.com/prod/servers/`transfer-server-ID`/users/myuser/config"
}
```

Solution

Replace the placeholder role ARN with an actual role that has permission to access
the server.

###### To update the role

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the left navigation pane, choose **Stacks**.
3. In the **Stacks** list, choose your stack, and then
   choose the **Parameters** tab.
4. Choose **Update**. On the **Update
   stack** page, choose **Use current template**,
   and then choose **Next**.
5. Replace **UserRoleArn** with a role ARN that has
   sufficient permissions for accessing your Transfer Family server.

###### Note

To grant the necessary permissions, you can add the
`AmazonAPIGatewayAdministrator` and the
`AmazonS3FullAccess` managed policies to your role. 6. Choose **Next**, and then choose
**Next** again. On the **Review
`stack`** page, select **I
acknowledge that AWS CloudFormation might create IAM resources**, and
then choose **Update stack**.

### Connection closed

Description

When you try to connect to your server using Secure Shell (SSH) File Transfer
Protocol (SFTP), you get the following error:

```
Connection closed
```

Cause

One possible cause for this issue is that your Amazon CloudWatch logging role does not have
a trust relationship with Transfer Family.

Solution

Make sure that the logging role for the server has a trust relationship with Transfer Family. For more information,
see [To establish a trust relationship](requirements-roles.md#establish-trust-transfer "requirements-roles.md#establish-trust-transfer").

## Troubleshoot testing your identity

provider

Description

If you test your identity provider using the console or the
`TestIdentityProvider` API operation, the `Response` field is
empty. For example:

```
{
    "Response": "{}",
    "StatusCode": 200,
    "Message": ""
}
```

Cause

The most likely cause is that the authentication failed because of an incorrect user
name or password.

Solution

Make sure that you are using the correct credentials for your user, and make updates
to the username or password, if necessary.

## Duplicate Amazon S3 buckets in web app

Description

The same Amazon S3 bucket appears multiple times in the Transfer Family web app interface.

Cause

This occurs when a user belongs to multiple Active Directory groups that have grants
to the same Amazon S3 bucket. The web app lists all top-level grants associated with the
user's UID or GID, including duplicate grants to the same bucket location.

Solution

To prevent duplicate listings, consolidate grants so each user has only one grant per
Amazon S3 location. Review your Amazon S3 Access Grants configuration and remove redundant grants
for the same bucket across different Active Directory groups.
