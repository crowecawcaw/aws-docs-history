

# Creating CodeArtifact resources with AWS CloudFormation
<a name="cloudformation-codeartifact"></a>

CodeArtifact is integrated with AWS CloudFormation, a service that helps you model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation takes care of provisioning and configuring those resources for you.

When you use CloudFormation, you can reuse your template to set up your CodeArtifact resources consistently and repeatedly. Just describe your resources once and then provision the same resources over and over in multiple accounts and AWS Regions. 

## CodeArtifact and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for CodeArtifact and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

CodeArtifact supports creating domains, repositories, and package groups in CloudFormation. For more information, including examples of JSON and YAML templates, see the following topics in the *CloudFormation User Guide*:
+ [AWS::CodeArtifact::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html)
+ [AWS::CodeArtifact::Repository](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html)
+ [AWS::CodeArtifact::PackageGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html) 

## Preventing deletion of CodeArtifact resources
<a name="preventing-deletion-cloudformation"></a>

CodeArtifact repositories contain critical application dependencies that may not be easy to recreate if lost. To protect CodeArtifact resources against accidental deletion when managing CodeArtifact resources with CloudFormation, include the `DeletionPolicy` and `UpdateReplacePolicy` attributes with a value of `Retain` on all domains and repositories. This prevents deletion if the resource is removed from the stack template, or the entire stack is accidentally deleted. The following YAML snippet shows a basic domain and repository with these attributes:

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

For more information about these attributes, see [DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) and [UpdateReplacePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)