

# Creating applications in myApplications
<a name="myApp-getting-started"></a>

You can create a new application or [Onboard existing AppRegistry Applications in myApplications](myApp-step1-onboard-existing.md) created before November 8, 2023 to get started with myApplications. When you create a new application, you can add resources by searching for them and selecting them or by using existing tags.

**To create a new application**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. Expand the left sidebar and choose **myApplications**.

1. Choose **Create application**.

1. Enter an application name.

1. (Optional) Enter an application description.

1.  (Optional) Add [tags](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html). Tags are key-value pairs that are applied to resources to hold metadata about those resources. 
**Note**  
The AWS application tag is automatically applied to newly created applications. For more information, see [The AWS application tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags) in the *AWS Service Catalog AppRegistry Administrator Guide*.

1.  (Optional) Add [attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-attr-groups.html). You can use attribute groups to store application metadata. 

1.  Choose **Next**. 

1. (Optional) Add resources:

------
#### [ Search and select resources ]

**Note**  
 To search and add resources, you must turn on AWS Resource Explorer. For more information, see [Getting started with AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started.html).   
 All added resources are tagged with the AWS application tag. 

**To add resources using search**

   1. Choose **Search and select resources**.

   1. Choose **Select resources**.

   1. (Optional) Choose a [view](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-about.html).

   1. Search for your resources. You can search by keyword, name or type, or choose a resource type.
**Note**  
 If you can't find the resource you're looking for, troubleshoot with AWS Resource Explorer. For more information, see [Troubleshooting Resource Explorer search issues](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html?icmp=docs_re_console_lm_troubleshooting) in the *Resource Explorer User Guide*. 

   1. Select the checkbox next to the resources you want to add.

   1. Choose **Add**.

   1. Choose **Next**.

   1. Review your choices.

------
#### [ Automatically add resources using tags ]

   When you create an application, you can bulk-onboard resources by specifying an existing tag key-value pair. With this method, AWS automatically applies the `awsApplication` tag to all of the resources tagged with the specified key-value pair, and creates a tag-sync for the application’s resources by default. With tag-sync enabled, any resources that are tagged with the specified tag key-value pair are automatically added to the application. For information about resolving tag-sync errors, see [Resolving tag-sync errors in myApplications](sync-error.md).

   

**Note**  
Adding resources to an application using tags requires permissions to create an AppRegistry application, group and ungroup resources, and tag and untag resources. You can either add the Resource Groups [`ResourceGroupsTaggingAPITagUntagSupportedResources`](https://docs.aws.amazon.com/ARG/latest/userguide/security_iam_awsmanpol.html#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources) AWS managed policy, or you can create and maintain your own custom policy. The following permissions must be added to a user's policy statement in IAM:  
`servicecatalog:CreateApplication` 
`resource-groups:GroupResources` 
`resource-groups:UngroupResources` 
`tag:TagResources` 
`tag:UntagResources` 

**To add resources using existing tags**

   1. Choose **Automatically add resources using tags**.

   1. Select an existing tag key and value:

      1. Select the **Role** used to tag resources. For more information, see [Tag-sync required permissions](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role) in the *AWS Service Catalog AppRegistry Administrator Guide*.

      1. Select a **Tag key**.

      1. Select a **Tag value**.

      1. (Optional) Choose **Preview resources** to preview which resources are tagged with the tag key-value pair.

      1. Review and accept the **I acknowledge that Group Lifecycle Events will be enabled to create a tag sync** notice. GLE allows AWS to notice changes to the resources tagged with your key-value pair.

   1. Choose **Next**.

   1. Review your application details, the selected tag key-value pair, and the preview of the resources that will be added to the application.
**Note**  
By default, creating an application using an existing tag key-value pair creates a tag-sync. After setup, tag-sync also continuously manages the application's resources, adding or removing resources as they are tagged or untagged with the specified key-value pair. You can manage tag-sync from the Manage resources page of the application.

------

1. If associating a CloudFormation stack, select the checkbox at the bottom of the page.
**Note**  
Adding an CloudFormation stack to the application requires a stack update because all resources added to your application are tagged with the AWS application tag. Manual configurations performed after the stack was last updated may not be reflected after this update. This can cause downtime or other application issues. For more information, see [Update behaviors of stack resources](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#tag-sync-role) in the *CloudFormation User Guide*.

1.  Choose **Create application**. 