

# Managing extensions with the CloudFormation registry
<a name="registry"></a>

The CloudFormation registry serves as a centralized hub for managing extensions that can be integrated into the CloudFormation templates in your AWS account. Extensions include resource types, modules, and Hooks from AWS and third-party publishers, and your own custom extensions. The registry makes it easier to discover and provision extensions in your CloudFormation templates in the same manner you use AWS-provided resources.

This section describes how to use the CloudFormation registry to activate third-party extensions in your account, including:
+ Activating public extensions
+ Registering and activating private extensions

**Topics**
+ [Related documentation](#registry-related-documentation)
+ [CloudFormation registry concepts](registry-concepts.md)
+ [View the available and activated extensions in the CloudFormation registry](registry-view.md)
+ [Use third-party public extensions from the CloudFormation registry](registry-public.md)
+ [Use third-party private extensions that have been shared with you](registry-private.md)
+ [Edit configuration data for extensions in your account](registry-set-configuration.md)
+ [Record resource types in AWS Config](registry-config-record.md)

## Related documentation
<a name="registry-related-documentation"></a>

If you are a developer interested in creating your own extensions, see the following documentation:
+ [Developing modules using the CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html) in the *CloudFormation Command Line Interface User Guide*
+ [Creating resource types using the CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html) in the *CloudFormation Command Line Interface User Guide*
+ [Developing custom Hooks using the CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-develop.html) in the *CloudFormation Hooks User Guide*

Additionally, all provisionable AWS resource types available in the CloudFormation registry can be used with the AWS Cloud Control API, with their attributes and properties defined in a standard JSON schema. For more information, see the [Cloud Control API User Guide](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html). When using Cloud Control API to perform CRUDL (Create, Read, Update, Delete, List) operations on AWS resources, you can only do so on AWS resources within your own AWS account. 