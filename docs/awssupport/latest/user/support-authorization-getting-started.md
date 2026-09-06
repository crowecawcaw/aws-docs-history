

# Getting started with AWS Support authorization
<a name="support-authorization-getting-started"></a>

This tutorial walks you through setting up AWS Support authorization and creating your first support permit. You complete the following steps:

This tutorial takes approximately 10 minutes to complete.

1. Create an AWS KMS signing key

1. Set up IAM permissions

1. Create your first support permit

1. Review support permit requests from AWS Support

## Prerequisites
<a name="support-authorization-getting-started-prereqs"></a>

Before you begin, verify that you have the following:
+ An active AWS account
+ Permissions to create AWS KMS keys in your account
+ Permissions to create IAM policies and attach them to users or roles

## Step 1: Create an AWS KMS signing key
<a name="support-authorization-getting-started-step1"></a>

AWS Support authorization requires a AWS KMS key with key spec `ECC_NIST_P384` and key usage `SIGN_VERIFY`. The key must be in the same Region as your support permit.

**Note**  
If you already have a AWS KMS key with key spec `ECC_NIST_P384` and key usage `SIGN_VERIFY` in the same Region, you can skip this step and use that key.

To create the key, run the following AWS CLI command:

```
aws kms create-key \
    --key-usage SIGN_VERIFY \
    --key-spec ECC_NIST_P384 \
    --description "SupportAuthZ signing key" \
    --tags TagKey=supportauthz:managed,TagValue=true \
    --region us-east-1
```

Note the key ARN from the output. You use this value when you create support permits.

Include the required AWS Support authorization policy statements in the `create-key` call. For the required statements, see [Configuring AWS KMS keys for AWS Support authorization](support-authorization-kms.md).

**Example output**  

```
{
    "KeyMetadata": {
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Arn": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeySpec": "ECC_NIST_P384",
        "KeyUsage": "SIGN_VERIFY"
    }
}
```

## Step 2: Set up IAM permissions
<a name="support-authorization-getting-started-step2"></a>

Attach an IAM policy that grants permissions for AWS Support authorization API operations. The following example policy grants access to all AWS Support authorization actions.

The `supportauthz:RegisterKey` action lets you associate AWS KMS keys with support permits. This permission-only action must be present in your IAM policy for AWS Support authorization to function.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "supportauthz:CreateSupportPermit",
                "supportauthz:RegisterKey",
                "supportauthz:DeleteSupportPermit",
                "supportauthz:GetSupportPermit",
                "supportauthz:ListSupportPermits",
                "supportauthz:ListSupportPermitRequests",
                "supportauthz:RejectSupportPermitRequest",
                "supportauthz:GetAction",
                "supportauthz:ListActions"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "supportauthz.us-east-1.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant"
            ],
            "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "supportauthz.us-east-1.amazonaws.com",
                    "kms:RetiringServicePrincipal": "us-east-1.supportauthz.amazonaws.com",
                    "kms:GranteeServicePrincipal": "us-east-1.supportauthz.amazonaws.com"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": [
                        "DescribeKey",
                        "GetPublicKey",
                        "Sign"
                    ]
                }
            }
        }
    ]
}
```

To attach this policy to an IAM user or role, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *AWS Identity and Access Management User Guide*.

## Step 3: Create your first support permit
<a name="support-authorization-getting-started-step3"></a>

Create a support permit that authorizes AWS Support to access information about your services for specific resources.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Granted access** section, choose **Preconfigure access**.

1. For **Access type**, choose one of the following:
   + **All supported resources in this Region** – Applies broad access to your entire account in the selected Region.
   + **Choose resource ARN** – Limits access to a specific resource that you identify by ARN.

1. (Optional) For **Details**, enter a **Name** and **Description** for the support permit.

1. For **Access duration**, choose one of the following:
   + **No expiration** – Access remains active until you revoke it.
   + **Custom duration** – Set a specific time window during which the support permit is valid.

1. For **Actions**, choose the actions that AWS Support is permitted to perform:
   + Select the **All actions** check box to permit all available actions on the covered resources. This removes the 10-action limit.
   + To choose specific actions, clear the **All actions** check box. Select a service from the **Services** list, and then select up to 10 individual actions from the actions table.

1. For **Signing key**, choose an AWS KMS key from the dropdown list. To create a new key, choose **Create KMS signing key**.

1. Choose **Submit**.

------
#### [ AWS CLI ]

Run the following command to create a time-bounded support permit for a specific resource:

```
aws supportauthz create-support-permit \
    --name "MyFirstPermit" \
    --signing-key-info '{"kmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}' \
    --permit '{
        "actions": {"allActions": {}},
        "resources": {"resources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster"]},
        "conditions": [
            {"allowAfter": "2026-06-01T00:00:00Z"},
            {"allowBefore": "2026-07-01T00:00:00Z"}
        ]
    }'
```

This support permit authorizes AWS Support to perform all available actions on the specified Amazon Aurora cluster during June 2026.

------

## Step 4: Review support permit requests from AWS Support
<a name="support-authorization-getting-started-step4"></a>

When AWS Support needs access to information about your services and no matching support permit exists, AWS Support submits a support permit request. You can view pending requests and approve or reject them.

------
#### [ Console ]

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. In the navigation pane, choose **Support authorization**.

1. In the **Pending access requests** section, review the list of requests. Each request shows the associated support case, service, Support Permit Request ARN, status, and request access date.

1. (Optional) To filter requests, use the **Status** and **Service** dropdown filters, or search by resource in the search field.

1. To approve or reject a request, choose **Manage support access**.

------
#### [ AWS CLI ]

To list pending requests, run the following command:

```
aws supportauthz list-support-permit-requests
```

**Example output**  

```
{
    "supportPermitRequests": [
        {
            "arn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/req-1234abcd",
            "status": "PENDING",
            "supportCaseDisplayId": "case-12345678",
            "requestedActions": ["rds:ReadClusterData"],
            "requestedResources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster"],
            "createdAt": "2026-06-01T12:00:00Z"
        }
    ]
}
```

To approve this request, create a support permit that covers the requested scope:

```
aws supportauthz create-support-permit \
    --name "ApproveCase12345678" \
    --signing-key-info '{"kmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}' \
    --support-case-display-id "case-12345678" \
    --permit '{
        "actions": {"actions": ["rds:ReadClusterData"]},
        "resources": {"resources": ["arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster"]},
        "conditions": [
            {"allowBefore": "2026-06-15T00:00:00Z"}
        ]
    }'
```

To reject a request, run the following command. This notifies AWS Support that you don't want to accept the request. Rejecting a request doesn't prevent you from creating a support permit for the same actions and resources later.

```
aws supportauthz reject-support-permit-request \
    --request-arn "arn:aws:supportauthz:us-east-1:111122223333:supportpermitrequest/request-id"
```

------

Review each request and decide whether to approve or reject it:
+ **To approve**: Create a support permit that covers the requested scope. Include the `supportCaseDisplayId` parameter to automatically deactivate the support permit when the case closes.
+ **To reject**: Call `RejectSupportPermitRequest` to notify AWS Support that you don't want to accept the request. Rejecting a request doesn't prevent you from creating a support permit for the same actions and resources later.

## Next steps
<a name="support-authorization-getting-started-next-steps"></a>

After you complete this tutorial, see the following topics:
+ To learn more about scoping support permits, see [Managing support permits](support-authorization-permits.md).
+ To monitor support actions on your resources, see [Monitoring AWS Support authorization with AWS CloudTrail](support-authorization-monitoring.md).