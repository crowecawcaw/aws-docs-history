

# Controlling access to data subscriptions

You use AWS Identity and Access Management (IAM) to control who in your account can create, view, tag, and cancel data subscriptions. A subscription belongs to your AWS account, and you can see and manage only the subscriptions that your account owns.

The [AWSPartnerCentralFullAccess](https://docs.aws.amazon.com/partner-central/latest/getting-started/managed-policies.html) managed policy grants all of the following actions. To grant only data subscription access, use a policy with the actions that you need. The following table lists the actions.


| Action | Grants permission to | 
| --- | --- | 
| partnercentral:CreateDataSubscription | Create a subscription, including its tags. | 
| partnercentral:GetDataSubscription | View the details and delivery status of a subscription. | 
| partnercentral:ListDataSubscriptions | List the subscriptions that the account owns. | 
| partnercentral:DeleteDataSubscription | Cancel a subscription. | 
| partnercentral:TagResource | Add or change tags on a subscription. | 
| partnercentral:UntagResource | Remove tags from a subscription. | 
| partnercentral:ListTagsForResource | View the tags on a subscription. | 

Each subscription has an ARN of the following form. The `{{domain}}` segment is assigned by AWS Partner Central and groups related datasets. Currently, it is `Opportunity_V1` for ACE Opportunity Pipeline, `Engagement_V1` for ACE Leads and Partner Marketing Campaigns, and `Channel_V1` for Partner Discount Business Report and Partner Account Relationships. New datasets can use other values. The identifier starts with `ds-`. To write a policy that covers all of your subscriptions, use a wildcard for the domain and the identifier. To limit a policy to specific subscriptions, use their full ARNs in the `Resource` element.

```
arn:aws:partnercentral::{{111122223333}}:catalog/AWS/ReportingData/{{domain}}/DataSubscription/{{ds-identifier}}
```

## Example – Manage all data subscriptions
<a name="data-subscriptions-policy-full"></a>

Attach the following policy to grant an IAM identity in your account permission to create, view, tag, and cancel every data subscription that your account owns.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:CreateDataSubscription",
                "partnercentral:GetDataSubscription",
                "partnercentral:ListDataSubscriptions",
                "partnercentral:DeleteDataSubscription",
                "partnercentral:TagResource",
                "partnercentral:UntagResource",
                "partnercentral:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

## Example – View data subscriptions
<a name="data-subscriptions-policy-readonly"></a>

Attach the following policy to grant an IAM identity in your account permission to view your subscriptions and their delivery status, without permission to create or cancel them.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetDataSubscription",
                "partnercentral:ListDataSubscriptions",
                "partnercentral:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about creating IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *AWS Identity and Access Management User Guide*.