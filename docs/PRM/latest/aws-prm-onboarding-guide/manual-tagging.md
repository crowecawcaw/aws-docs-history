

# Manual Implementation
<a name="manual-tagging"></a>

**Note**  
Partner Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.

## Constructing Your Tag Key and Value
<a name="tag-key-construction"></a>

You need two components to construct your resource tag:

1. **Tag Key** — requires your Partner Central AWS account ID (the 12-digit AWS account linked to your AWS Partner Central account).
   + Format: `aws-apn-id-{{partner-central-aws-account-id}}`
   + Example: `aws-apn-id-012345678901`
   + Where to find it: Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/dashboard). Your 12-digit AWS account ID is in the upper right corner of the Partner Central homepage. For more information on the account ID, see [Viewing your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html) in the IAM User Guide.

1. **Tag Value** — requires your product code from your AWS Marketplace listing.
   + Format: `pc:{{product-code}}`
   + Example: `pc:5ugbbrmu7ud3u5hsipfzug61p`
   + Where to find it: See [Retrieve your product code](product-code-retrieval.md).

**Alternative:** Use the Partner Revenue Measurement agent in the Partner Central dashboard in AWS console to look up the correct tag key name and value for your listing.

**Note**  
The existing `aws-apn-id` key continues to work, and resources tagged with it require no additional changes. Use the new `aws-apn-id-{{partner-central-aws-account-id}}` tag key for all future attributions, including single-partner scenarios. When more than one Partner tags the same resource, each tagged Partner receives revenue attribution.

**Note**  
Revenue attributed through the existing `aws-apn-id` key and the new key both appear under the "Resource Tagging" method in the [Attributed Revenue Dashboard](https://console.aws.amazon.com/partnercentral/home), with no changes to the dashboard.

## 3-Step Implementation Process
<a name="tagging-implementation"></a>

1. [Construct your tag key and value](#tag-key-construction)

1. Add the tag to your resources:
   + Tag Key: `aws-apn-id-{{partner-central-aws-account-id}}`
   + Tag Value: `pc:{{product-code}}`
   + Example Key: `aws-apn-id-012345678901`
   + Example Value: `pc:5ugbbrmu7ud3u5hsipfzug61p`

1. Apply via automated or manual methods listed below

**Note**  
Ensure the tag fits within the [50-tag-per-resource limit](https://docs.aws.amazon.com/tag-editor/latest/userguide/reference.html) and does not conflict with existing customer tag policies.

## Tagging via AWS Management Console
<a name="console-tagging"></a>

You can manually tag your resources using the AWS Management Console.

**To get started**

1. Go to your AWS Management Console.

1. Go to the resources you want to tag. Example: Amazon RDS.

1. Choose **Add tags**.

1. Enter `aws-apn-id-012345678901` as the **Tag key** (replace `012345678901` with your Partner Central AWS account ID).

1. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` as the **Tag value** (replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code).

1. Choose **Save**.

Repeat the steps above for all associated resources such as Snapshots. For more information about tagging resources, see the [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the Amazon Elastic Compute Cloud user guide for Linux instances.

**Important**  
If the resource is managed by infrastructure as code (CloudFormation, Terraform, CDK), adding tags via the console causes drift detection on the next IaC run. For IaC-managed resources, always apply tags through the IaC tool instead.

## Tagging via AWS CLI
<a name="cli-manual-tagging"></a>

You can tag specific resources using the AWS CLI.

**Note**  
Replace `012345678901` with your Partner Central AWS account ID and `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
aws ec2 create-tags --resources i-1234567890abcdef0 \
  --tags Key=aws-apn-id-012345678901,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

**Important**  
If the resource is managed by infrastructure as code (CloudFormation, Terraform, CDK), adding tags via CLI causes drift detection on the next IaC run. For IaC-managed resources, always apply tags through the IaC tool instead.

## Best Practices
<a name="tagging-best-practices"></a>
+ Use the account-suffixed tag key format: `aws-apn-id-{{partner-central-aws-account-id}}`. For how to construct your tag key, see [Constructing Your Tag Key and Value](#tag-key-construction)
+ Ensure `pc:` prefix in the tag value
+ Validate product code format
+ Document all tagged resources
+ Monitor tag compliance and revenue attribution

**Note**  
Once a resource is tagged with a partner's product code, AWS continues to attribute revenue to the product until the tag is removed or the resource is shut down.

## Tag Management
<a name="tag-management"></a>

**Tag Conflicts:** Multiple partners can independently tag the same resource using the partner-unique tag key in the format `aws-apn-id-{{partner-central-aws-account-id}}`, with the tag value `pc:{{product-code}}`. However, there is a cap of 10 partners per resource, if more than 10 partners tag the same resource, partners beyond the cap will not receive attribution. The legacy `aws-apn-id` tag key continues to attribute revenue for previously tagged resources. Use the new `aws-apn-id-{{partner-central-aws-account-id}}` tag key for all future attributions, including single-partner scenarios. For how to construct your tag key, see [Constructing Your Tag Key and Value](#tag-key-construction).

**Tag Removal:** Any user with account access can remove tags. Both customers and partners (with account access) can remove tags.