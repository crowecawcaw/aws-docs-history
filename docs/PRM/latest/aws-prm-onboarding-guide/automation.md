# Automated Tagging

We encourage you to automate your tagging resources as much as possible. You can automate your tagging by adding a tag line to your AWS CloudFormation template, AWS Cloud Development Kit (AWS CDK), Terraform, or by using the AWS Tag Editor.

###### Warning

Only tag resources that are directly used or influenced by your partner solution.

## AWS CloudFormation

AWS CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS services such as Amazon EC2, Amazon Elastic Block Store (EBS), Amazon SNS, Elastic Load Balancing, and Application Auto Scaling to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. AWS CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack).

You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources. You can only tag AWS CloudFormation supported resources. For information about which resources you can tag with CloudFormation, see the [AWS resources and property types reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") in the AWS CloudFormation user guide. For more information on how to use CloudFormation, see the [Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md") in the AWS CloudFormation user guide.

###### Note

Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
Resources:
  MyResource:
    Type: 'AWS::EC2::Instance'
    Properties:
      Tags:
        - Key: "aws-apn-id"
          Value: "pc:5ugbbrmu7ud3u5hsipfzug61p"
```

## AWS Cloud Development Kit (AWS CDK)

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages. A tag in AWS CDK is applied to a given construct that also applies to all of its taggable children. These tags are included in the AWS CloudFormation template synthesized from your application and are applied to the AWS resources it deploys. For more information about AWS CDK tagging, see [Tagging](../../../cdk/v2/guide/tagging.md "../../../cdk/v2/guide/tagging.md") in the AWS Cloud Development Kit (AWS CDK) v2 developer guide.

###### Note

Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
{
    "Key" : "aws-apn-id",
    "Value" : "pc:5ugbbrmu7ud3u5hsipfzug61p"
}
```

## Terraform

###### Note

Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
resource "aws_instance" "example" {
  tags = {
    aws-apn-id = "pc:5ugbbrmu7ud3u5hsipfzug61p"
  }
}
```

## AWS Tag Editor

You can use the AWS Resource Groups and Tag Editor to tag resources in bulk using the console.

###### Important

For resources provisioned by infrastructure as code templates (CloudFormation, CDK, Terraform, etc.), it is recommended to update the templates instead of using Tag Editor.

###### Note

The AWS Tag Editor only works for resources running in the account.

###### To get started

1. Open the AWS Management Console.
2. Go to the Resource Groups & Tag Editor, Tagging, Tag Editor page.
3. Specify the Region(s) your resources are located. Example: us-east-1.
4. Choose the type of resources you want to bulk tag. Example: EC2, Lambda, and S3.
5. Choose **Search resources** to view the resources that meet the conditions you have selected.
6. Select all or a few of the listed resources you want to tag.
7. Choose **Manage tags of selected resources**.
8. Enter `aws-apn-id` in the **Tag Key** field.
9. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` in the **Tag Value** field (replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code).
10. Choose **Review**.
11. Choose **Apply tag changes**.

## AWS CLI

You can use the AWS CLI to tag resources in bulk using the command line.

###### Important

For resources provisioned by infrastructure as code templates (CloudFormation, CDK, Terraform, etc.), it is recommended to update the templates instead of using CLI commands.

###### Note

Replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code in the following example.

```
aws resourcegroupstaggingapi tag-resources \
    --resource-arn-list arn:aws:ec2:region:account-id:instance/i-1234567890abcdef0 \
    --tags aws-apn-id=pc:5ugbbrmu7ud3u5hsipfzug61p
```
