# AWS managed policy:

AmazonWorkSpacesSecureBrowserReadOnly

You can attach the `AmazonWorkSpacesSecureBrowserReadOnly` policy to your
IAM identities.

This policy grants read-only permissions that allow access to WorkSpaces Secure Browser and its
dependencies through the AWS Management Console, SDK, and CLI. This policy does not
include the permissions necessary to interact with portals using
`IAM_Identity_Center` as the authentication type. To get these permissions,
combine this policy with `AWSSSOReadOnly`.

**Permissions details**

This policy includes the following permissions.

- `workspaces-web` – Provides read-only access to WorkSpaces Secure Browser
  and its dependencies through the AWS Management Console, SDK, and CLI.
- `ec2` – Allows principals to describe VPCs, subnets, and
  security groups. This is used in the AWS Management Console in WorkSpaces Secure Browser to
  show you your VPCs, subnets, and security groups that are available foruse with the
  service.
- `Kinesis` - Allows principals to list Kinesis data streams. This is
  used in the AWS Management Console in WorkSpaces Secure Browser to show you Kinesis data
  streams that are available for use with the service.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "workspaces-web:GetBrowserSettings",
                "workspaces-web:GetIdentityProvider",
                "workspaces-web:GetNetworkSettings",
                "workspaces-web:GetPortal",
                "workspaces-web:GetPortalServiceProviderMetadata",
                "workspaces-web:GetTrustStore",
                "workspaces-web:GetTrustStoreCertificate",
                "workspaces-web:GetUserSettings",
                "workspaces-web:GetUserAccessLoggingSettings",
                "workspaces-web:ListBrowserSettings",
                "workspaces-web:ListIdentityProviders",
                "workspaces-web:ListNetworkSettings",
                "workspaces-web:ListPortals",
                "workspaces-web:ListTagsForResource",
                "workspaces-web:ListTrustStoreCertificates",
                "workspaces-web:ListTrustStores",
                "workspaces-web:ListUserSettings",
                "workspaces-web:ListUserAccessLoggingSettings"
            ],
            "Resource": "arn:aws:workspaces-web:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "kinesis:ListStreams"
            ],
            "Resource": "*"
        }
    ]
}
```
