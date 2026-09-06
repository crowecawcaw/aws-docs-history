

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with Parameter Store
<a name="parameter-store-working-with"></a>

Parameter Store lets you create, organize, and manage configuration data and secrets that your applications use at runtime.

In this section, you learn how to work with parameters throughout their lifecycle–creating and organizing them, applying policies, managing versions and labels, and controlling access. You can perform these tasks using the AWS Management Console, the AWS Command Line Interface, or AWS Tools for Windows PowerShell.

Parameter Store centralizes configuration data such as environment variables, service endpoint URLs, resource identifiers, approved AMI IDs, and application tuning parameters, so you can update values without modifying application code. Parameters are stored as key-value pairs, can be organized hierarchically, and support versioning and optional encryption with AWS Key Management Service.

**Topics**
+ [Creating Parameter Store parameters in Systems Manager](sysman-paramstore-su-create.md)
+ [Searching for Parameter Store parameters in Systems Manager](parameter-search.md)
+ [Assigning parameter policies in Parameter Store](parameter-store-policies.md)
+ [Working with parameter hierarchies in Parameter Store](sysman-paramstore-hierarchies.md)
+ [Preventing access to Parameter Store API operations](parameter-store-policy-conditions.md)
+ [Working with parameter labels in Parameter Store](sysman-paramstore-labels.md)
+ [Working with parameter versions in Parameter Store](sysman-paramstore-versions.md)
+ [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md)
+ [Working with parameters in Parameter Store using Run Command commands](sysman-param-runcommand.md)
+ [Using native parameter support in Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md)
+ [Deleting parameters from Parameter Store](deleting-parameters.md)