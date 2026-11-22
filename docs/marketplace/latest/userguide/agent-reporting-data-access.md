

# Granting agents access to seller reporting data

If you work with an agent who manages your seller reporting in AWS Marketplace (AWS Marketplace), you can grant them programmatic access to your reporting data so they can retrieve it without needing your credentials. To do this, you use an AWS Identity and Access Management (IAM) policy that grants the `aws-marketplace:GetSellerReportingData` action.

## Agent access policies
<a name="agent-access-policy"></a>

You can grant agent access to your seller reporting data by using one of the following IAM policy options:
+ **Specific datasets (recommended)** – Grants access only to the dataset ARNs you specify. Use this option to follow the principle of least privilege.
+ **All current and future datasets** – Grants access to all reporting data using a wildcard resource. Use this option only if the agent requires access to all datasets.

**To grant an agent access to seller reporting data**

1. Decide whether you want to grant access to specific datasets (recommended) or all current and future datasets.

1. Create an IAM policy using the appropriate JSON example from the following sections. In the policy examples, replace {{account-id}} with your AWS account ID.

1. Attach the policy to the agent's IAM identity (user, group, or role).

1. (Optional) To remove access to a dataset later, delete the dataset entry from the `Resource` section of the policy.

### Example: Access to specific datasets
<a name="agent-access-specific-datasets"></a>

The following policy grants access only to specific datasets. This is the recommended approach because it follows the principle of least privilege—granting agents access only to the data they need.

```json
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:GetSellerReportingData"
            ],
            "Resource": [
                "arn:aws:aws-marketplace::{{account-id}}:AWSMarketplace/ReportingData/Usage_V1/Dataset/Usage_V1",
                "arn:aws:aws-marketplace::{{account-id}}:AWSMarketplace/ReportingData/Agreement_V1/Dataset/AgreementsAndRenewals_V1",
                "arn:aws:aws-marketplace::{{account-id}}:AWSMarketplace/ReportingData/BillingEvent_V1/Dataset/CollectionsAndDisbursements_V1",
                "arn:aws:aws-marketplace::{{account-id}}:AWSMarketplace/ReportingData/BillingEvent_V1/Dataset/BilledRevenue_V1"
            ]
        }
    ]
}
```

In this policy, replace the following placeholder values:
+ {{account-id}} – Your AWS account ID (for example, `444455556666`).

The `Resource` array lists the dataset ARNs you want to grant access to. The example includes the following datasets:
+ `Usage_V1` – Usage data for your products.
+ `AgreementsAndRenewals_V1` – Agreement and renewal data.
+ `CollectionsAndDisbursements_V1` – Collections and disbursements data.
+ `BilledRevenue_V1` – Billed revenue data.

Remove or add dataset ARNs based on the specific data the agent needs to access.

### Example: Access to all datasets
<a name="agent-access-all-datasets"></a>

The following policy grants access to all current and future AWS Marketplace reporting data using a wildcard resource. Use this approach only if the agent requires access to all reporting datasets.

**Important**  
We recommend using the specific datasets policy instead of this wildcard approach. Granting access to all datasets gives the agent broader access than may be necessary.

```json
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:GetSellerReportingData"
            ],
            "Resource": [
                "arn:aws:aws-marketplace::{{account-id}}:AWSMarketplace/*"
            ]
        }
    ]
}
```

In this policy, replace {{account-id}} with your AWS account ID (for example, `444455556666`).

**Note**  
For information about creating IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *AWS Identity and Access Management User Guide*.