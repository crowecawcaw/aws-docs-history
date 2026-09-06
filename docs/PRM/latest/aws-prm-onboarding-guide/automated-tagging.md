

# Automated Tagging
<a name="automated-tagging"></a>

We encourage you to automate your tagging resources as much as possible. You can automate your tagging by adding a tag line to your AWS CloudFormation template, AWS Cloud Development Kit (AWS CDK), Terraform, or by using the AWS Tag Editor.

**Warning**  
Only tag resources that are directly used or influenced by your partner solution.

## AWS CloudFormation
<a name="cloudformation-tagging"></a>

**Stack-level propagation (recommended):** Tags applied at the stack level propagate automatically to all resources in the stack that support tagging. This is the simplest approach when your entire stack belongs to your partner solution.

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following examples.

```
aws cloudformation create-stack --stack-name my-stack \
  --template-body file://template.yaml \
  --tags Key=aws-apn-id,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

**Note**  
Most common resource types (EC2, S3, RDS, Lambda, ECS, etc.) support stack-level tag propagation. However, some resources do not — for example, EBS volumes created from block device mappings. Use per-resource tagging as a fallback for those specific resources.

**Per-resource tagging:** Add the tag directly to individual resource definitions when you need to tag only specific resources within a stack, or when different resources need different attribution.

```
Resources:
  MyResource:
    Type: 'AWS::EC2::Instance'
    Properties:
      Tags:
        - Key: "aws-apn-id"
          Value: "pc:5ugbbrmu7ud3u5hsipfzug61p"
```

For information about which resources you can tag with CloudFormation, see the [AWS resources and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation user guide.

## AWS Cloud Development Kit (AWS CDK)
<a name="cdk-tagging"></a>

A tag in AWS CDK is applied to a given construct and all of its taggable children. For more information, see [Tagging](https://docs.aws.amazon.com/cdk/v2/guide/tagging.html) in the AWS CDK v2 developer guide.

**Stack-level propagation (recommended):** Tag the stack to propagate to all resources.

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following examples.

```
Tags.of(stack).add('aws-apn-id', 'pc:5ugbbrmu7ud3u5hsipfzug61p');
```

**Per-resource tagging:**

```
{
    "Key" : "aws-apn-id",
    "Value" : "pc:5ugbbrmu7ud3u5hsipfzug61p"
}
```

## Terraform
<a name="terraform-tagging"></a>

**Provider-level default tags (recommended):** The `default_tags` block applies the tag to every resource Terraform creates or manages through that provider.

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following examples.

```
provider "aws" {
  default_tags {
    tags = {
      aws-apn-id = "pc:5ugbbrmu7ud3u5hsipfzug61p"
    }
  }
}
```

**Note**  
Some Terraform resource types do not support `default_tags` (e.g., `aws_autoscaling_group`). If you also define the same tag key in a resource's `tags` block, Terraform raises a conflict. Use either `default_tags` or per-resource tags for the `aws-apn-id` tag, not both on the same resource.

**Per-resource tagging:** Add the tag to individual resource blocks when you need to tag only specific resources.

```
resource "aws_instance" "example" {
  tags = {
    aws-apn-id = "pc:5ugbbrmu7ud3u5hsipfzug61p"
  }
}
```

## AWS Tag Editor
<a name="tag-editor-bulk-tagging"></a>

You can use the AWS Resource Groups and Tag Editor to tag resources in bulk using the console.

**Important**  
For resources provisioned by infrastructure as code templates (CloudFormation, CDK, Terraform, etc.), it is recommended to update the templates instead of using Tag Editor.

**Note**  
The AWS Tag Editor only works for resources running in the account.

**To get started**

1. Open the AWS Management Console.

1. Go to the Resource Groups & Tag Editor, Tagging, Tag Editor page.

1. Specify the Region(s) your resources are located. Example: us-east-1.

1. Choose the type of resources you want to bulk tag. Example: EC2, Lambda, and S3.

1. Choose **Search resources** to view the resources that meet the conditions you have selected.

1. Select all or a few of the listed resources you want to tag.

1. Choose **Manage tags of selected resources**.

1. Enter `aws-apn-id` in the **Tag Key** field.

1. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` in the **Tag Value** field (replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code).

1. Choose **Review**.

1. Choose **Apply tag changes**.

## AWS CLI
<a name="cli-tagging"></a>

You can use the AWS CLI to tag resources in bulk using the command line.

**Important**  
For resources provisioned by infrastructure as code templates (CloudFormation, CDK, Terraform, etc.), it is recommended to update the templates instead of using CLI commands.

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
aws resourcegroupstaggingapi tag-resources \
    --resource-arn-list arn:aws:ec2:region:account-id:instance/i-1234567890abcdef0 \
    --tags aws-apn-id=pc:5ugbbrmu7ud3u5hsipfzug61p
```

## API/SDK Bulk Tagging
<a name="sdk-bulk-tagging"></a>

Use the Resource Groups Tagging API to tag multiple resources across different service types in a single call. This is the most efficient approach for large-scale tagging.

**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
import boto3

tagging = boto3.client('resourcegroupstaggingapi')
tagging.tag_resources(
    ResourceARNList=[
        'arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0',
        'arn:aws:s3:::my-bucket'
    ],
    Tags={'aws-apn-id': 'pc:5ugbbrmu7ud3u5hsipfzug61p'}
)
```

**Important**  
For resources managed by infrastructure as code (CloudFormation, CDK, Terraform), always apply tags through the IaC tool instead. SDK/CLI tagging of IaC-managed resources causes drift detection on the next IaC run.