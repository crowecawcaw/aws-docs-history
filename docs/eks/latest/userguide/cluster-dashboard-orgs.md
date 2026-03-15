**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure EKS Dashboard integration with AWS Organizations

This section provides step-by-step instructions for configuring the EKS Dashboard’s integration with AWS Organizations. You’ll learn how to enable and disable trusted access between services, as well as how to register and deregister delegated administrator accounts. Each configuration task can be performed using either the AWS console or the AWS CLI.

## Enable trusted access

Trusted access authorizes the EKS Dashboard to securely access cluster information across all accounts in your organization.

### Using the AWS console

1. Log in to the management account of your AWS Organization.
2. Navigate to the EKS console in the us-east-1 region.
3. In the left sidebar, select Dashboard Settings.
4. Click **Enable trusted access**.

###### Note

When you enable trusted access through the EKS console, the system automatically creates the `AWSServiceRoleForAmazonEKSDashboard` service-linked role. This automatic creation does not occur if you enable trusted access using the AWS CLI or AWS Organizations console.

### Using the AWS CLI

1. Log in to the management account of your AWS Organization.
2. Run the following commands:

```
aws iam create-service-linked-role --aws-service-name dashboard.eks.amazonaws.com
aws organizations enable-aws-service-access --service-principal eks.amazonaws.com
```

## Disable trusted access

Disabling trusted access revokes the EKS Dashboard’s permission to access cluster information across your organization’s accounts.

### Using the AWS console

1. Log in to the management account of your AWS Organization.
2. Navigate to the EKS Console in the us-east-1 region.
3. In the left sidebar, select Dashboard Settings.
4. Click **Disable trusted access**.

### Using the AWS CLI

1. Log in to the management account of your AWS Organization.
2. Run the following command:

```
aws organizations disable-aws-service-access --service-principal eks.amazonaws.com
```

## Enable a delegated administrator account

A delegated administrator is a member account that’s granted permission to access the EKS Dashboard.

### Using the AWS console

1. Log in to the management account of your AWS Organization.
2. Navigate to the EKS console in the us-east-1 region.
3. In the left sidebar, select Dashboard Settings.
4. Click **Register delegated administrator**.
5. Enter the Account ID of the AWS Account you want to choose as delegated administrator.
6. Confirm the registration.

### Using the AWS CLI

1. Log in to the management account of your AWS Organization.
2. Run the following command, replacing `123456789012` with your account ID:

```
aws organizations register-delegated-administrator --account-id 123456789012 --service-principal eks.amazonaws.com
```

## Disable a delegated administrator account

Disabling a delegated administrator removes the account’s permission to access the EKS Dashboard.

### Using the AWS console

1. Log in to the management account of your AWS Organization.
2. Navigate to the EKS console in the us-east-1 region.
3. In the left sidebar, select Dashboard Settings.
4. Locate the delegated administrator in the list.
5. Click **Deregister** next to the account you want to remove as delegated administrator.

### Using the AWS CLI

1. Log in to the management account of your AWS Organization.
2. Run the following command, replacing `123456789012` with the account ID of the delegated administrator:

```
aws organizations deregister-delegated-administrator --account-id 123456789012 --service-principal eks.amazonaws.com
```

## Minimum IAM policies required

This section outlines the minimum IAM policies required to enable trusted access and delegate an administrator for the EKS Dashboard integration with AWS Organizations.

### Policy for enabling trusted access

To enable trusted access between EKS Dashboard and AWS Organizations, you need the following permissions:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "organizations:EnableAWSServiceAccess",
                "organizations:DescribeOrganization",
                "organizations:ListAWSServiceAccessForOrganization"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/dashboard.eks.amazonaws.com/AWSServiceRoleForAmazonEKSDashboard"
        }
    ]
}
```

### Policy for delegating an administrator

To register or deregister a delegated administrator for the EKS Dashboard, you need the following permissions:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "organizations:RegisterDelegatedAdministrator",
                "organizations:DeregisterDelegatedAdministrator",
                "organizations:ListDelegatedAdministrators"
            ],
            "Resource": "*"
        }
    ]
}
```

### Policy to view EKS Dashboard

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AmazonEKSDashboardReadOnly",
            "Effect": "Allow",
            "Action": [
                "eks:ListDashboardData",
                "eks:ListDashboardResources",
                "eks:DescribeClusterVersions"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AmazonOrganizationsReadOnly",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListAWSServiceAccessForOrganization",
                "organizations:ListRoots",
                "organizations:ListAccountsForParent",
                "organizations:ListOrganizationalUnitsForParent"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AmazonOrganizationsDelegatedAdmin",
            "Effect": "Allow",
            "Action": [
                "organizations:ListDelegatedAdministrators"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "organizations:ServicePrincipal": "eks.amazonaws.com"
                }
            }
        }
    ]
}
```

###### Note

These policies must be attached to the IAM principal (user or role) in the management account of your AWS Organization. Member accounts cannot enable trusted access or delegate administrators.
