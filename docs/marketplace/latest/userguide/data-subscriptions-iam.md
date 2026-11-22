

# Controlling access to data subscriptions

You use AWS Identity and Access Management (IAM) to control who in your account can create, view, tag, and cancel data subscriptions. A subscription belongs to your account, and you can see and manage only the subscriptions that your account owns.

The `AWSMarketplaceSellerFullAccess` managed policy grants all of the following actions. To grant only data subscription access, use a policy with the actions that you need. The following table lists the actions. For more information about the managed policy, see [AWS managed policy: AWSMarketplaceSellerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsmarketplacesellerfullaccess).


**Data subscription actions**  

| Action | Grants permission to | 
| --- | --- | 
| aws-marketplace:CreateDataSubscription | Create a subscription, including its tags. | 
| aws-marketplace:GetDataSubscription | View the details and delivery status of a subscription. | 
| aws-marketplace:ListDataSubscriptions | List the subscriptions that the account owns. | 
| aws-marketplace:DeleteDataSubscription | Cancel a subscription. | 
| aws-marketplace:TagResource | Add or change tags on a subscription. | 
| aws-marketplace:UntagResource | Remove tags from a subscription. | 
| aws-marketplace:ListTagsForResource | View the tags on a subscription. | 

Each subscription has an ARN of the following form, where `family` is `Agreement_V1` for Marketplace Agreements and Renewals or `Usage_V1` for Marketplace Usage, and the identifier starts with `ds-`. You can use the ARN in the `Resource` element of a policy to limit it to specific subscriptions.

```
arn:aws:aws-marketplace::{{account-id}}:AWSMarketplace/ReportingData/{{family}}/DataSubscription/ds-{{identifier}}
```
+ {{account-id}} – Your AWS account ID.
+ {{family}} – The dataset family (`Agreement_V1` or `Usage_V1`).
+ {{identifier}} – The unique subscription identifier (starts with `ds-`).

## Example: Manage all data subscriptions
<a name="data-subscriptions-iam-example-manage"></a>

Attach the following policy to grant an IAM identity in your account permission to create, view, tag, and cancel every data subscription that your account owns. This policy uses `"Resource": "*"` because actions like `CreateDataSubscription` and `ListDataSubscriptions` are account-level actions that can't be scoped to individual subscription ARNs.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ManageDataSubscriptionsAccountLevel",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:CreateDataSubscription",
                "aws-marketplace:GetDataSubscription",
                "aws-marketplace:ListDataSubscriptions",
                "aws-marketplace:DeleteDataSubscription",
                "aws-marketplace:TagResource",
                "aws-marketplace:UntagResource",
                "aws-marketplace:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

## Example: View data subscriptions
<a name="data-subscriptions-iam-example-view"></a>

Attach the following policy to grant an IAM identity in your account permission to view your subscriptions and their delivery status, without permission to create or cancel them. This policy uses `"Resource": "*"` because `ListDataSubscriptions` is an account-level action that can't be scoped to individual subscription ARNs.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewDataSubscriptionsAccountLevel",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:GetDataSubscription",
                "aws-marketplace:ListDataSubscriptions",
                "aws-marketplace:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about creating IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.