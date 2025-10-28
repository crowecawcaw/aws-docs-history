# Configure Lambda functions with external VPCs in Infrastructure Composer

To start configuring a Lambda function with a VPC that is defined on another template, use the **Lambda Function**
enhanced component card. This card represents a Lambda function using the AWS Serverless Application Model (AWS SAM) `AWS::Serverless::Function`
resource type.

###### To configure a Lambda function with a VPC from an external template

1. From the **Lambda Function** resource properties panel, expand the **VPC settings (advanced)**
   dropdown section.
2. Select **Assign to external VPC**.
3. Provide values for the security groups and subnets to configure for the Lambda function.
   See [Security group and subnet identifiers](using-composer-services-vpc-tag.md#using-composer-services-vpc-configure-ids "using-composer-services-vpc-tag.md#using-composer-services-vpc-configure-ids") for details.
4. **Save** your changes.
