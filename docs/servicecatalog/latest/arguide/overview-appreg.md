# Key concepts of AWS Service Catalog AppRegistry

This topic describes the key components of AppRegistry.

###### Topics

- [Applications](#ar-applications "#ar-applications")
- [The awsApplication tag](ar-user-tags.md "ar-user-tags.md")
- [Resource tag-sync tasks](app-tag-sync.md "app-tag-sync.md")
- [Attribute groups](#attr-groups "#attr-groups")
- [Tags](#ar-tags "#ar-tags")
- [Application sharing](#share-cross-account "#share-cross-account")

## Applications

An application is a group of resources and metadata. When you create an application, you provide the application with a name and description.
After you create an application, you can add a tag-based resource group or an AWS CloudFormation stack resource group to it.
You can also associate attribute groups and tags with the application.

###### Note

When you create an application, AppRegistry vends a user tag called the `awsApplication` tag.
This tag identifies resources associated with an application.
For more information, see [The `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").

You can create applications in [myApplications in the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md "../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md"), in the AppRegistry console, and with the AWS CLI using the [AppRegistry API](../dg/API_Operations_AWS_Service_Catalog_App_Registry.md "../dg/API_Operations_AWS_Service_Catalog_App_Registry.md").
You can also create applications with the [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") or an [AWS SDK](../../../whitepapers/latest/aws-overview/software-development-kits.md "../../../whitepapers/latest/aws-overview/software-development-kits.md") of your choice.

You can view and manage applications in [myApplications in the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/myApp-manage-apps.md "../../../awsconsolehelpdocs/latest/gsg/myApp-manage-apps.md"),
in the [AppRegistry console](create-app.md "create-app.md"),
and with the AWS CLI, as well as [in a set of AWS services](intro-app-registry.md#what-is-appregistry-integrate "intro-app-registry.md#what-is-appregistry-integrate").

## Attribute groups

Attribute groups are JSON objects that store application metadata.
You associate attribute groups with applications to understand applications in the context of their associated metadata.

###### Example: Attribute group with metadata

The following snippet shows an attribute group with metadata that includes a team name, department number, department name, and email address.

```
{
 "Team" : "WebTeam",
 "Department": "10006",
 "ParentDept": "Research",
 "ContactAlias": "research@team.com"
}
```

You can use the AppRegistry `AssociateAttributeGroup` API to apply metadata to an application.
You can use the AppRegistry `DisassociateAttributeGroup` API to remove metadata from an application.

You can associate attribute groups with applications in the console and with the AWS CLI using the [AppRegistry API](../dg/API_Operations_AWS_Service_Catalog_App_Registry.md "../dg/API_Operations_AWS_Service_Catalog_App_Registry.md"),
with [AWS CloudFormation stack resources](../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/resources-section-structure.md"), or with [CDK constructs](https://aws.amazon.com/cdk/features/ "https://aws.amazon.com/cdk/features/").

You can update an attribute group definition at any time with the AppRegistry `UpdateAttributeGroup` API.
When you update an attribute group definition, the update applies to every application the attribute group is associated with.

You can share attribute groups to accounts, organizations, and organizational units with the following permissions:

- **Allow associations**

Allows IAM principals in shared accounts to associate and disassociate attribute groups.

- **Read only associations**

Allows IAM principals in shared accounts to view attribute groups

You can automate stack updates and metadata changes in a [continuous delivery and continuous integration pipeline](../../../codepipeline/latest/userguide/concepts-continuous-delivery-integration.md "../../../codepipeline/latest/userguide/concepts-continuous-delivery-integration.md").
This allows stakeholders to query and receive information about attribute groups

You can [view and manage attribute groups](associate-attributes.md "associate-attributes.md") in the console and with the AWS CLI.

## Tags

Tags are key-value pairs that act as metadata.
You create tags using key-value pairs.
You can add tags to applications and attribute groups, so you can group them by environment, owner, purpose, or other criteria.

###### Note

This tag is not the same as the [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").
The `awsApplication` tag tag is an AWS user tag that AppRegistry vends when you create an application.
You can add the `awsApplication` tag tag to resources, so you can identify which resources are associated with an application.

###### Example: AWS CLI output with `tags` parameter

The following is an example of the output for an application created in the AWS CLI, which includes the `tags` and `applicationTag` parameters.

```
{
                    "application": {
                    "arn": "string",
                    "creationTime": "string",
                    "description": "string",
                    "id": "string",
                    "lastUpdatedTime": "string",
                    "name": "string",
                    "applicationTag": {"awsApplication":"arn:aws:resource-groups:us-east-1:234567891011:group/myExampleApp/012345example6789101112131"},
                    "tags": {
                        "myKey":"myValue"
                    }
                }
            }
```

You can [view and manage tags](add-tags.md "add-tags.md") in the console and with the AWS CLI.

## Application sharing

Deploying applications across multiple AWS accounts is common and considered a best practice that can help isolate and manage business applications and data.
With AppRegistry and AWS Resource Access Manager (AWS RAM), you can share applications and attribute groups with one or more accounts, organizations, and organizaional units.
You can share applications and attributes in the console and AWS CLI using the [AWS Resource Access Manager API](../../../ram/latest/APIReference/Welcome.md "../../../ram/latest/APIReference/Welcome.md") and [infrastructure as code](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md").
Resources can be associated with shared applications.
For more information, see [Sharing resources with accounts in your organization](sharing-definitions.md "sharing-definitions.md").
