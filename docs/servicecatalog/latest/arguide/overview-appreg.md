

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Key concepts of AWS Service Catalog AppRegistry
<a name="overview-appreg"></a>

 This topic describes the key components of AppRegistry. 

**Topics**
+ [Applications](#ar-applications)
+ [The `awsApplication` tag](ar-user-tags.md)
+ [Resource tag-sync tasks](app-tag-sync.md)
+ [Attribute groups](#attr-groups)
+ [Tags](#ar-tags)
+ [Application sharing](#share-cross-account)

## Applications
<a name="ar-applications"></a>

 An application is a group of resources and metadata. When you create an application, you provide the application with a name and description. After you create an application, you can add a tag-based resource group or an CloudFormation stack resource group to it. You can also associate attribute groups and tags with the application. 

**Note**  
 When you create an application, AppRegistry vends a user tag called the `awsApplication` tag. This tag identifies resources associated with an application. For more information, see [The `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags). 

 You can create applications in [myApplications in the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/myApp-getting-started.html), in the AppRegistry console, and with the AWS CLI using the [AppRegistry API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations_AWS_Service_Catalog_App_Registry.html). You can also create applications with the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) or an [AWS SDK](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/software-development-kits.html) of your choice. 

 You can view and manage applications in [myApplications in the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/myApp-manage-apps.html), in the [AppRegistry console](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-app.html), and with the AWS CLI, as well as [in a set of AWS services](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html#what-is-appregistry-integrate). 

## Attribute groups
<a name="attr-groups"></a>

 Attribute groups are JSON objects that store application metadata. You associate attribute groups with applications to understand applications in the context of their associated metadata. 

**Example: Attribute group with metadata**  
 The following snippet shows an attribute group with metadata that includes a team name, department number, department name, and email address. 

```
{
 "Team" : "WebTeam",
 "Department": "10006",
 "ParentDept": "Research",
 "ContactAlias": "research@team.com"
}
```

 You can use the AppRegistry `AssociateAttributeGroup` API to apply metadata to an application. You can use the AppRegistry `DisassociateAttributeGroup` API to remove metadata from an application. 

 You can associate attribute groups with applications in the console and with the AWS CLI using the [AppRegistry API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations_AWS_Service_Catalog_App_Registry.html), with [CloudFormation stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html), or with [CDK constructs](https://aws.amazon.com/cdk/features/). 

 You can update an attribute group definition at any time with the AppRegistry `UpdateAttributeGroup` API. When you update an attribute group definition, the update applies to every application the attribute group is associated with. 

 You can share attribute groups to accounts, organizations, and organizational units with the following permissions: 
+  **Allow associations** 

   Allows IAM principals in shared accounts to associate and disassociate attribute groups. 
+  **Read only associations** 

   Allows IAM principals in shared accounts to view attribute groups 

 You can automate stack updates and metadata changes in a [continuous delivery and continuous integration pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html). This allows stakeholders to query and receive information about attribute groups 

 You can [view and manage attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attributes.html) in the console and with the AWS CLI. 

## Tags
<a name="ar-tags"></a>

 Tags are key-value pairs that act as metadata. You create tags using key-value pairs. You can add tags to applications and attribute groups, so you can group them by environment, owner, purpose, or other criteria. 

**Note**  
 This tag is not the same as the [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags). The `awsApplication` tag tag is an AWS user tag that AppRegistry vends when you create an application. You can add the `awsApplication` tag tag to resources, so you can identify which resources are associated with an application. 

**Example: AWS CLI output with `tags` parameter**  
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

 You can [view and manage tags](https://docs.aws.amazon.com/servicecatalog/latest/arguide/add-tags.html) in the console and with the AWS CLI. 

## Application sharing
<a name="share-cross-account"></a>

 Deploying applications across multiple AWS accounts is common and considered a best practice that can help isolate and manage business applications and data. With AppRegistry and AWS Resource Access Manager (AWS RAM), you can share applications and attribute groups with one or more accounts, organizations, and organizaional units. You can share applications and attributes in the console and AWS CLI using the [AWS Resource Access Manager API](https://docs.aws.amazon.com/ram/latest/APIReference/Welcome.html) and [infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html). Resources can be associated with shared applications. For more information, see [Sharing resources with accounts in your organization](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions). 