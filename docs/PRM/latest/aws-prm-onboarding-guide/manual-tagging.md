# Manual Implementation

###### Note

Partner Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.

## 3-Step Implementation Process

1. [Get your product code from AWS Marketplace Management Portal](product-code-retrieval.md "product-code-retrieval.md")
2. Add the tag to your resources:
   - Tag Key: `aws-apn-id`
   - Tag Value: `pc:<product-code>`
   - Example: `pc:5ugbbrmu7ud3u5hsipfzug61p`

3. Apply via automated or manual methods listed below

###### Note

Ensure the `aws-apn-id` tag fits within the [50-tag-per-resource limit](../../../tag-editor/latest/userguide/reference.md "../../../tag-editor/latest/userguide/reference.md") and does not conflict with existing customer tag policies.

## Tagging via AWS Management Console

You can manually tag your resources using the AWS Management Console.

###### To get started

1. Go to your AWS Management Console.
2. Go to the resources you want to tag. Example: Amazon RDS.
3. Choose **Add tags**.
4. Enter `aws-apn-id` as the **Tag key**.
5. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` as the **Tag value** (replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code).
6. Choose **Save**.

Repeat the steps above for all associated resources such as Snapshots. For more information about tagging resources, see the [Tag your Amazon EC2 resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") in the Amazon Elastic Compute Cloud user guide for Linux instances.

###### Important

If the resource is managed by infrastructure as code (CloudFormation, Terraform, CDK), adding tags via the console causes drift detection on the next IaC run. For IaC-managed resources, always apply tags through the IaC tool instead.

## Tagging via AWS CLI

You can tag specific resources using the AWS CLI.

###### Note

Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
aws ec2 create-tags --resources i-1234567890abcdef0 \
  --tags Key=aws-apn-id,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

###### Important

If the resource is managed by infrastructure as code (CloudFormation, Terraform, CDK), adding tags via CLI causes drift detection on the next IaC run. For IaC-managed resources, always apply tags through the IaC tool instead.

## Best Practices

- Always use lowercase 'aws-apn-id' key
- Ensure 'pc:' prefix in value
- Validate product code format
- Document all tagged resources
- Monitor tag compliance and revenue attribution

###### Note

Once a resource is tagged with a partner's product code, AWS continues to attribute revenue to the product until the tag is removed or the resource is shut down.

## Tag Management

**Tag Conflicts:** Since an AWS resource can only have one tag with the `aws-apn-id` key, only one partner identifier is allowed per resource. For multi-partner scenarios, consider using the [User Agent String](user-agent-string.md "user-agent-string.md") method instead. If you must use resource tagging, coordinate with the other partner and the customer to determine tag ownership before making changes.

**Tag Removal:** Any user with account access can remove tags. Both customers and partners (with account access) can remove tags.
