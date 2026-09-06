

# Manual Implementation
<a name="manual-tagging"></a>

**Note**  
Partner Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.

## 3-Step Implementation Process
<a name="tagging-implementation"></a>

1. [Get your product code from AWS Marketplace Management Portal](product-code-retrieval.md)

1. Add the tag to your resources:
   + Tag Key: `aws-apn-id`
   + Tag Value: `pc:<product-code>`
   + Example: `pc:5ugbbrmu7ud3u5hsipfzug61p`

1. Apply via automated or manual methods listed below

**Note**  
Ensure the `aws-apn-id` tag fits within the [50-tag-per-resource limit](https://docs.aws.amazon.com/tag-editor/latest/userguide/reference.html) and does not conflict with existing customer tag policies.

## Tagging via AWS Management Console
<a name="console-tagging"></a>

You can manually tag your resources using the AWS Management Console.

**To get started**

1. Go to your AWS Management Console.

1. Go to the resources you want to tag. Example: Amazon RDS.

1. Choose **Add tags**.

1. Enter `aws-apn-id` as the **Tag key**.

1. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` as the **Tag value** (replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code).

1. Choose **Save**.

Repeat the steps above for all associated resources such as Snapshots. For more information about tagging resources, see the [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the Amazon Elastic Compute Cloud user guide for Linux instances.

**Important**  
If the resource is managed by infrastructure as code (CloudFormation, Terraform, CDK), adding tags via the console causes drift detection on the next IaC run. For IaC-managed resources, always apply tags through the IaC tool instead.

## Tagging via AWS CLI
<a name="cli-manual-tagging"></a>

You can tag specific resources using the AWS CLI.

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
aws ec2 create-tags --resources i-1234567890abcdef0 \
  --tags Key=aws-apn-id,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

**Important**  
If the resource is managed by infrastructure as code (CloudFormation, Terraform, CDK), adding tags via CLI causes drift detection on the next IaC run. For IaC-managed resources, always apply tags through the IaC tool instead.

## Best Practices
<a name="tagging-best-practices"></a>
+ Always use lowercase 'aws-apn-id' key
+ Ensure 'pc:' prefix in value
+ Validate product code format
+ Document all tagged resources
+ Monitor tag compliance and revenue attribution

**Note**  
Once a resource is tagged with a partner's product code, AWS continues to attribute revenue to the product until the tag is removed or the resource is shut down.

## Tag Management
<a name="tag-management"></a>

**Tag Conflicts:** Since an AWS resource can only have one tag with the `aws-apn-id` key, only one partner identifier is allowed per resource. For multi-partner scenarios, consider using the [User Agent String](user-agent-string.md) method instead. If you must use resource tagging, coordinate with the other partner and the customer to determine tag ownership before making changes.

**Tag Removal:** Any user with account access can remove tags. Both customers and partners (with account access) can remove tags.