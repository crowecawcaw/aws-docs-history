# CloudFormation template sections

Every CloudFormation template consists of one or more sections, each serving a specific purpose.

The **Resources** section is required in every CloudFormation
template and forms the core of the template. This section specifies the stack resources and
their properties, such as an Amazon EC2 instance or an Amazon S3 bucket. Each resource is defined with a
unique logical ID, type, and specific configuration details.

The **Parameters** section, while optional, plays an important
role in making templates more flexible. It allows users to pass values at runtime when creating
or updating a stack. These parameters can be referenced in the `Resources` and
`Outputs` sections, enabling customization without altering the template itself.
For instance, you might use parameters to specify instance types or environment settings that
vary between deployments.

The **Outputs** section, also optional, defines the values that
are returned when viewing a stack’s properties. Outputs provide useful information such as
resource identifiers or URLs, which can be leveraged for operational purposes or for integration
with other stacks. This section helps users retrieve and use important details about the
resources created by the template.

Other optional sections include **Mappings**, which function
like lookup tables to manage conditional values. With mappings, you define key-value pairs and
use them with the `Fn::FindInMap` intrinsic function in the `Resources`
and `Outputs` sections. This is useful for scenarios where you need to adjust
configurations based on conditions such as AWS Region or environment.

**Metadata** and **Rules**
sections, though less commonly used, provide additional functionality. `Metadata` can
include additional information about the template, while `Rules` validates a
parameter or a combination of parameters during stack creation or updates, ensuring they meet
specific criteria. The **Conditions** section further enhances
flexibility by controlling whether certain resources are created or properties are assigned a
value based on conditions like environment type.

Lastly, the **Transform** section is used to apply macros
during the processing of the template. For serverless applications (also referred to as Lambda
applications), it specifies the version of the [AWS Serverless Application Model (AWS SAM)](https://github.com/awslabs/serverless-application-specification "https://github.com/awslabs/serverless-application-specification")
to use. When you specify a transform, you can use AWS SAM syntax to declare resources in your
template. The model defines the syntax that you can use and how it's processed. You can also use
the `AWS::Include` transform to include template snippets that are stored separately
from the main CloudFormation template.

The following topics provide more information and examples for using each section.

###### Topics

- [Resources](resources-section-structure.md "resources-section-structure.md")
- [Parameters](parameters-section-structure.md "parameters-section-structure.md")
- [Outputs](outputs-section-structure.md "outputs-section-structure.md")
- [Mappings](mappings-section-structure.md "mappings-section-structure.md")
- [Metadata](metadata-section-structure.md "metadata-section-structure.md")
- [Rules](rules-section-structure.md "rules-section-structure.md")
- [Conditions](conditions-section-structure.md "conditions-section-structure.md")
- [Transform](transform-section-structure.md "transform-section-structure.md")
- [Format version](format-version-structure.md "format-version-structure.md")
- [Description](template-description-structure.md "template-description-structure.md")
