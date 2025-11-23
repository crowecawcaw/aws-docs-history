# Creating CodeArtifact resources with AWS CloudFormation

CodeArtifact is integrated with AWS CloudFormation, a service that helps you model and set up your
AWS resources so that you can spend less time creating and managing your resources and infrastructure.
You create a template that describes all the AWS resources that you want, and
CloudFormation takes care of provisioning and configuring those resources for you.

When you use CloudFormation, you can reuse your template to set up your CodeArtifact resources
consistently and repeatedly. Just describe your resources once and then provision the same
resources over and over in multiple accounts and AWS Regions.

## CodeArtifact and CloudFormation templates

To provision and configure resources for CodeArtifact and related services, you must
understand [CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates
are formatted text files in JSON or YAML. These templates describe the resources that you want to
provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation
Designer to help you get started with CloudFormation templates. For more information, see [What is AWS
CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

CodeArtifact supports creating domains, repositories, and package groups in CloudFormation. For
more information, including examples of JSON and YAML templates, see the following topics in the _CloudFormation User Guide_:

- [AWS::CodeArtifact::Domain](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.md")
- [AWS::CodeArtifact::Repository](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.md")
- [AWS::CodeArtifact::PackageGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.md")

## Preventing deletion of CodeArtifact resources

CodeArtifact repositories contain critical aplication dependencies that may not be easy to recreate
if lost. To protect CodeArtifact resources against accidential deletion when managing CodeArtifact resources with CloudFormation,
include the `DeletionPolicy` and `UpdateRetainPolicy` attributes with a value of `Retain` on
all domains and
respositories. This will prevent deletion if the resource is removed from the stack template, or the entire stack is
accidentially deleted. The following YAML snippet shows a basic domain and repository with these attributes:

```
Resources:
    MyCodeArtifactDomain:
        Type: 'AWS::CodeArtifact::Domain'
        DeletionPolicy: Retain
        UpdateReplacePolicy: Retain
        Properties:
            DomainName: "my-domain"

    MyCodeArtifactRepository:
        Type: 'AWS::CodeArtifact::Repository'
        DeletionPolicy: Retain
        UpdateReplacePolicy: Retain
        Properties:
            RepositoryName: "my-repo"
            DomainName: !GetAtt MyCodeArtifactDomain.Name
```

For more information about these attributes, see
[DeletionPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.md") and
[UpdateReplacePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md")
in the _AWS CloudFormation User Guide_.

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
