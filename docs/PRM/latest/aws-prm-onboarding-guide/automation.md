

# Automation
<a name="automation"></a>

Partner Revenue Measurement supports automation for each implementation method. Choose the automation approach that matches your implementation method.

## AWS Marketplace Metering
<a name="automation-marketplace-metering"></a>

AWS Marketplace Metering is a fully automated, zero-touch experience for partners. When you list an AMI or ML product on AWS Marketplace and customers purchase and use it, revenue attribution occurs automatically through existing product metadata. No additional implementation is required from partners.

For more information, see [AWS Marketplace Metering](marketplace-metering.md).

## Resource Tagging Automation
<a name="automation-resource-tagging"></a>

Automate resource tagging using infrastructure as code tools and bulk tagging utilities. For detailed instructions, see [Automated Tagging](automated-tagging.md) in the Resource Tagging chapter.

Supported automation tools:
+ AWS CloudFormation
+ AWS Cloud Development Kit (AWS CDK)
+ Terraform
+ AWS Tag Editor
+ AWS CLI

## User Agent String Automation
<a name="automation-user-agent"></a>

Automate User Agent string inclusion across all regular AWS API/CLI calls using AWS SDK Application ID configuration. For detailed instructions, see [Automated User Agent](automated-user-agent.md) in the User Agent String chapter.

Supported automation methods:
+ Shared AWS config file (`~/.aws/config`)
+ Environment variable (`AWS_SDK_UA_APP_ID`)
+ JVM system property (Java/Kotlin)