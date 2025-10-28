# AWS SAM template

After you run the **sam init** command and complete its subsequent workflow, AWS SAM creates your application project directory, which is your AWS SAM project.
You define your serverless application by adding code to your AWS SAM project. While your AWS SAM project consists of a set of files and folders,
the file you primarily work with is your AWS SAM template (named `template.yaml`). In this template, you write the code to express resources,
event source mappings, and other properties that define your serverless application.

###### Note

A key element of the AWS SAM template is the AWS SAM template specification. This specification provides the short-hand syntax that, when compared to AWS CloudFormation,
allows to you use fewer lines of code to to define the resources, event source mappings, permissions, APIs, and other properties of your serverless application.

This section provides details on how you use sections in the AWS SAM template to define resources types, resource properties, data types,
resource attributes, intrinsic functions, and API Gateway extensions.

AWS SAM templates are an extension of AWS CloudFormation templates, with unique syntax types that use shorthand syntax with fewer lines of code than AWS CloudFormation. This
speeds up your development when building a serverless application. For more information, refer to
[AWS SAM resources and properties](sam-specification-resources-and-properties.md "sam-specification-resources-and-properties.md"). For the full reference for AWS CloudFormation templates, see [AWS CloudFormation Template Reference](../../../AWSCloudFormation/latest/UserGuide/template-reference.md "../../../AWSCloudFormation/latest/UserGuide/template-reference.md") in the
_AWS CloudFormation User Guide_.

When developing, you will often find it beneficial to break up your application code into
separate files to better organize and manage your application. A basic example of this is using a
separate file for your AWS Lambda function code rather than having this code in your AWS SAM template. Do this by organizing
your Lambda function code in a subdirectory of your project and referencing its local path within
your AWS Serverless Application Model (AWS SAM) template.

###### Topics

- [AWS SAM template anatomy](sam-specification-template-anatomy.md "sam-specification-template-anatomy.md")
- [AWS SAM resources and properties](sam-specification-resources-and-properties.md "sam-specification-resources-and-properties.md")
- [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md")
- [Resource attributes supported by AWS SAM](sam-specification-resource-attributes.md "sam-specification-resource-attributes.md")
- [API Gateway extensions for AWS SAM](sam-specification-api-gateway-extensions.md "sam-specification-api-gateway-extensions.md")
- [Intrinsic functions for AWS SAM](sam-specification-intrinsic-functions.md "sam-specification-intrinsic-functions.md")
