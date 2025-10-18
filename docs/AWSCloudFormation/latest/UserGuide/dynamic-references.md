# Get values stored in other services using dynamic
 references

Dynamic references provide a convenient way for you to specify external values stored and
 managed in other services and decouple sensitive information from your
 infrastructure-as-code templates. CloudFormation retrieves the value of the specified reference
 when necessary during stack and change set operations.

With dynamic references, you can:


* Use secure strings – For sensitive data,
 always use secure string parameters in AWS Systems Manager Parameter Store or secrets in
 AWS Secrets Manager to ensure your data is encrypted at rest.
* Limit access – Restrict access to the
 Parameter Store parameters or Secrets Manager secrets to only authorized principals and
 roles.
* Rotate credentials – Regularly rotate your
 sensitive data stored in Parameter Store or Secrets Manager to maintain a high level of
 security.
* Automate rotation – Leverage the automatic
 rotation features of Secrets Manager to periodically update and distribute your sensitive data
 across your applications and environments.

## General considerations


The following are the general considerations for you to consider before you specify
 dynamic references in your CloudFormation templates:



* Avoid including dynamic references, or any sensitive data, in resource
 properties that are part of a resource's primary identifier. CloudFormation may use
 the actual plaintext value in the primary resource identifier, which could be a
 security risk. This resource ID may appear in any derived outputs or
 destinations.


To determine which resource properties comprise a resource type's primary
 identifier, refer to the resource reference documentation for that resource in
 [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html"). In the **Return values** section,
 the `Ref` function return value represents the resource properties
 that comprise the resource type's primary identifier.
* You can include up to 60 dynamic references in a stack template.
* If you're using transforms (like `AWS::Include` or
 `AWS::Serverless`), CloudFormation doesn't resolve dynamic references
 before applying the transform. Instead, it passes the literal string of the
 dynamic reference to the transform, and resolves the references when you execute
 the change set using the template.
* Dynamic references can't be used for secure values (like those stored in
 Parameter Store or Secrets Manager) in custom resources.
* Dynamic references are also not supported in
 `AWS::CloudFormation::Init` metadata and Amazon EC2
 `UserData` properties.
* Don't create a dynamic reference that ends with a backslash (\). CloudFormation
 can't resolve these references, which will cause stack operations to
 fail.

The following topics provide information and other considerations for using dynamic
 references.

###### Topics

* [Get a plaintext value from Systems Manager Parameter
 Store](dynamic-references-ssm.md "dynamic-references-ssm.md")
* [Get a secure string value from
 Systems Manager Parameter Store](dynamic-references-ssm-secure-strings.md "dynamic-references-ssm-secure-strings.md")
* [Get a secret or secret value from
 Secrets Manager](dynamic-references-secretsmanager.md "dynamic-references-secretsmanager.md")
