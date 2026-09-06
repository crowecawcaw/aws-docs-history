

# Working with CloudFormation templates
<a name="template-guide"></a>

An AWS CloudFormation template defines the AWS resources you want to create, update, or delete as part of a stack. It consists of several sections, but the only required section is the [Resources](resources-section-structure.md) section, which must declare at least one resource. 

You can create templates using the following methods:
+ **AWS Infrastructure Composer** – A visual interface for designing templates.
+ **Text Editor** – Write templates directly in JSON or YAML syntax.
+ **IaC generator** – Generate templates from resources provisioned in your account that are not currently managed by CloudFormation. The IaC generator works with a wide range of resource types that are supported by the Cloud Control API in your Region.

This section provides a comprehensive guide on how to use the different sections of a CloudFormation template and how to start creating stack templates. It covers the following topics:

**Topics**
+ [Where templates get stored](#where-they-get-stored)
+ [Validating templates](#template-validation)
+ [Getting started with templates](#getting-started)
+ [Sample templates](#sample-templates)
+ [Template format](template-formats.md)
+ [Template sections](template-anatomy.md)
+ [Infrastructure Composer](infrastructure-composer-for-cloudformation.md)
+ [AWS CloudFormation Language Server](ide-extension.md)
+ [IaC generator](generate-IaC.md)
+ [Get values stored in other services](dynamic-references.md)
+ [Get AWS values](pseudo-parameter-reference.md)
+ [Get stack outputs](using-cfn-stack-exports.md)
+ [Specify existing resources at runtime](cloudformation-supplied-parameter-types.md)
+ [Walkthroughs](walkthroughs.md)
+ [Template snippets](template-snippets.md)
+ [Windows-based stacks](cfn-windows-stacks.md)
+ [Use CloudFormation-supplied resource types](cloudformation-supplied-resource-types.md)
+ [Create reusable resource configurations with modules](modules.md)

## Where templates get stored
<a name="where-they-get-stored"></a>

**Amazon S3 bucket**  
You can store CloudFormation templates in an Amazon S3 bucket. When creating or updating a stack, you can specify the S3 URL of the template instead of uploading it directly.

If you upload templates directly through the AWS Management Console or AWS CLI, an S3 bucket is automatically created for you. For more information, see [Create a stack from the CloudFormation console](cfn-console-create-stack.md).

**Git repository**  
With [Git sync](git-sync.md), you can store templates in a Git repository. When creating or updating a stack, you can specify the Git repository location and branch containing the template instead of uploading it directly or referencing an S3 URL. CloudFormation automatically monitors the specified repository and branch for template changes. For more information, see [Create a stack from repository source code with Git sync](git-sync-create-stack-from-repository-source-code.md).

## Validating templates
<a name="template-validation"></a>

**Syntax validation**  
You can verify the JSON or YAML syntax of your template by using the [validate-template](service_code_examples.md#validate-template-sdk) CLI command or by specifying your template on the console. The console performs validation automatically. For more information, see [Create a stack from the CloudFormation console](cfn-console-create-stack.md). 

However, these methods only verify the syntax of your template and don't validate the property values that you specified for a resource.

**Additional validation tools**  
For more complex validations and best practice checks, you can use additional tools like:
+ [CloudFormation Linter (cfn-lint)](https://github.com/aws-cloudformation/cfn-lint) – Validate templates against the [CloudFormation resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html). Includes checking valid values for resource properties and best practices.
+ [CloudFormation Rain (rain fmt)](https://github.com/aws-cloudformation/rain) – Format your CloudFormation templates to a consistent standard or reformat a template from JSON to YAML (or YAML to JSON). It preserves comments when using YAML and switches the use of intrinsic functions to the short syntax where possible.

## Getting started with templates
<a name="getting-started"></a>

To get started with creating a CloudFormation template, follow these steps:

1. **Choose resources** – Identify the AWS resources you want to include in your stack, such as EC2 instances, VPCs, security groups, and more.

1. **Write the template** – Write the template in JSON or YAML format, defining the resources and their properties.

1. **Save the template** – Save the template locally with a file extension like: `.json`, `.yaml`, or `.txt`.

1. **Validate the template** – Validate the template using the methods described in the [Validating templates](#template-validation) section.

1. **Create a stack** – Create a stack using the validated template. 

### Plan to use the CloudFormation template reference
<a name="additional-resources"></a>

As you write your templates, you can find documentation for the detailed syntax for different resource types in the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html).

Often, your stack templates will require intrinsic functions to assign property values that are not available until runtime and special attributes to control the behavior of resources. As you write your template, refer to the following resources for guidance:
+ [Intrinsic function reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference.html) – Some commonly used intrinsic functions include:
  + `Ref` – Retrieves the value of a parameter or the physical ID of a resource.
  + `Sub` – Substitutes placeholders in strings with actual values.
  + `GetAtt` – Returns the value of an attribute from a resource in the template.
  + `Join` – Joins a set of values into a single string.
+ [Resource attribute reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-product-attribute-reference.html) – Some commonly used special attributes include:
  + `DependsOn` – Use this attribute to specify that one resource must be created after another.
  + `DeletionPolicy` – Use this attribute to specify how CloudFormation should handle the deletion of a resource.

## Sample templates
<a name="sample-templates"></a>

CloudFormation provides open-source stack templates that you can use to get started. For more information, see [CloudFormation Sample Templates](https://github.com/aws-cloudformation/aws-cloudformation-templates) on the GitHub website.

Keep in mind that these templates are not meant to be production-ready. You should take the time to learn how they work, adapt them to your needs, and make sure that they meet your company's compliance standards.

Each template in this repository passes [CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint) (cfn-lint) checks, and also a basic set of AWS CloudFormation Guard rules based on the Center for Internet Security (CIS) Top 20, with exceptions for some rules where it made sense to keep the sample focused on a single use case.