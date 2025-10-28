AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Managing resources in the Resource Explorer console

The Resource Explorer console supports resource quick-actions and integrations with several other
AWS services, allowing you to perform the most common resource management tasks and
providing additional resource information from one console.

## Resource Explorer console integrations with other AWS

services

**Amazon Q Developer Ask Amazon Q** — When you select one or
more resources, choosing **Actions**, **Help me with this
resource** opens a chat panel where you can ask Amazon Q for more information
about those resources. For example, you can ask for details about a specific resource or
list resources based on criteria such as AWS Region or state. To learn more, review
[Chatting about your resources](../../../amazonq/latest/qdeveloper-ug/chat-actions.md "../../../amazonq/latest/qdeveloper-ug/chat-actions.md") in the _Amazon Q Developer User
Guide_.

## Resource Actions in the Resource Explorer console

The Resource **Actions** menu enables you to perform common resource
management tasks on a selection of up to 400 resources from within the Resource Explorer console.

###### Topics

- [Manage resource tags](#console_manage_tags "#console_manage_tags")
- [Create application](#console_create_application "#console_create_application")
- [Add to application](#console_add_to_application "#console_add_to_application")
- [Export resources to a .csv file](#console_export_tags "#console_export_tags")

### Manage resource tags

You can select up to 400 resources and apply _tags_ to them.
Tags are key and value pairs that act as metadata for organizing your AWS
resources and can help you manage, identify, organize, search for, and filter
resources.

###### Note

Tags are not encrypted and should not be used to store sensitive data, such as
personally identifiable information (PII) or personal health information (PHI).

Each tag has two parts:

- A _tag key_ (for example, CostCenter, Environment, or
  Project). Tag keys are case sensitive.
- A _tag value_ (for example, 111122223333 or
  Production). Like tag keys, tag values are case sensitive.

The resources in your selection do not need to all reside in the AWS Region you
currently have selected. The following behaviors apply when tagging resources in the
Resource Explorer console:

- Global resources, such as `iam::Role`, are resources you can
  use from anywhere. In the Resource Explorer console, global resources do not display a
  region.
- If any of the selected resources already have a tag key and you specify a
  new value for that key, the newly specified tag key-value pair is applied to
  all of the selected resources.
- After updating tags with bulk tagging in the Resource Explorer console, the tag
  changes are not immediately reflected in the resources' tag count. After
  bulk tagging changes are applied, new resource searches may take up to 30
  seconds to reflect new tagging details.

###### Note

AWS recommends not including AWS CloudFormation stacks in your resource selection when
managing tags in the Resource Explorer console. Instead, you should manage tags on
AWS CloudFormation stacks only using AWS CloudFormation. Tagging AWS CloudFormation stacks from Resource Explorer can cause
unexpected tagging behavior, resulting in downtime or other issues.

**Minimum permissions**

To add or remove tags from a resource, you need the permissions required for the
service to which the resource belongs. For example, to tag Amazon EC2 instances, your
must have permissions to the tagging actions in that service's API. For more
information, review [Grant
permission to tag Amazon EC2 resources during creation](../../../AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md "../../../AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md") in the _Amazon EC2
User Guide_.

To perform the steps in the following procedure, you must have the following
permissions:

- **Action**:
  `tag:GetTagKeys`
- **Action**: `tag:GetTagValues`
- **Action**: `tag:TagResources`
- **Action**: `tag:UntagResources`

###### To manage tags for a selection of resources

1. On the **Resources** page, start by choosing the view
   that you want to use. You can choose from among only those views that you
   have permissions to access.
2. (Optional) Submit a [Resource
   query](using-search.md "using-search.md").
3. In **Resources**, select up to 400 resources.
4. For **Actions**, choose **Manage tags**.
5. Select an **existing tag** or **create a new
   tag** to apply to all of the selected resources.
6. Choose **Apply**.

### Create application

You can select up to 400 resources and create a new application that includes
those resources. The application is visible in [myApplications](../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md "../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md") in the AWS Management Console. All resources in the selection must
meet the following requirements to be successfully added to a new application:

- Resources must be in the same AWS Region because an application can only
  exist in a single region.
- Global resources can only be added to an application that resides in the
  global resource's home region. To add a global resource to an application,
  apply [the
  `awsApplication` tag](../../../servicecatalog/latest/arguide/ar-user-tags.md "../../../servicecatalog/latest/arguide/ar-user-tags.md") to the resource. You can
  learn more about global AWS services and their resources in the [Global services](../../../whitepapers/latest/aws-fault-isolation-boundaries/global-services.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/global-services.md") AWS whitepaper.
- Resources must be supported by the [Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference/supported-services.md "../../../resourcegroupstagging/latest/APIReference/supported-services.md").
- Resources must reside in the same AWS account.
- Resources must not already be in an application.

###### Note

AWS recommends not including AWS CloudFormation stacks in your resource selection when
creating an application in the Resource Explorer console. Creating an application that
includes a AWS CloudFormation stack requires a stack update because all resources added
to your application are tagged with the `awsApplication` tag. Manual
configurations performed after the stack was last updated may not be reflected
after this update. This can cause downtime or other application issues. For more
information, see [Update behaviors of stack resources](../../../servicecatalog/latest/arguide/overview-appreg.md#tag-sync-role "../../../servicecatalog/latest/arguide/overview-appreg.md#tag-sync-role") in the _AWS CloudFormation User
Guide_.

**Minimum permissions**

To create a new application, or add resources to an existing application, you need
additional permissions to tag resources and to perform application actions in Resource Groups
and AWS Service Catalog.

To perform the steps in the following procedure, you must have the following
permissions:

- **Action:**
  `tag:TagResources`
- **Action:**
  `resource-groups:Tag`
- **Action:**
  `resource-groups:CreateGroup`
- **Action:**
  `resource-groups:GroupResources`
- **Action:**
  `servicecatalog:CreateApplication`
- **Action:**
  `servicecatalog:TagResource`

###### To create an application from a selection of resources

1. On the **[Resource search](https://console.aws.amazon.com/resource-explorer/home#/search "https://console.aws.amazon.com/resource-explorer/home#/search")** page, start by choosing the view that you want to use.
   You can choose from among only those views that you have permissions to
   access.
2. (Optional) Submit a [Resource
   query](using-search.md "using-search.md").
3. In **Resources**, select up to 400 resources.
4. For **Actions**, choose **Create
   application**.
5. In **Create application**, enter the
   **application name** and select a
   **Region**.
6. (Optional) Add **Tags** and **Attribute
   groups**.
7. Choose **Create**.

After creating the new application, resource searches may take several minutes to
reflect new tagging details.

### Add to application

You can select up to 400 resources and add those resources to an existing
application. All resources in the selection must meet the following requirements to
be successfully added to an application:

- Resources must be in the same AWS Region because an application can only
  exist in a single region.
- Global resources can only be added to an application that resides in the
  global resource's home region. To add a global resource to an application,
  apply [the
  `awsApplication` tag](../../../servicecatalog/latest/arguide/ar-user-tags.md "../../../servicecatalog/latest/arguide/ar-user-tags.md") to the resource. You can
  learn more about global AWS services and their resources in the [Global services](../../../whitepapers/latest/aws-fault-isolation-boundaries/global-services.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/global-services.md") AWS whitepaper.
- Resources must be supported by the [Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference/supported-services.md "../../../resourcegroupstagging/latest/APIReference/supported-services.md").
- Resources must reside in the same AWS account.
- Resources must not already be in an application.

###### Note

AWS recommends not including AWS CloudFormation stacks in your resource selection when
adding resources to an application in the Resource Explorer console. Adding a AWS CloudFormation stack
to the application requires a stack update because all resources added to your
application are tagged with the `awsApplication` tag. Manual
configurations performed after the stack was last updated may not be reflected
after this update. This can cause downtime or other application issues. For more
information, see [Update behaviors of stack resources](../../../servicecatalog/latest/arguide/overview-appreg.md#tag-sync-role "../../../servicecatalog/latest/arguide/overview-appreg.md#tag-sync-role") in the _AWS CloudFormation User
Guide_.

**Minimum permissions**

To create a new application, or add resources to an existing application, you need
additional permissions to tag resources and to perform application actions in Resource Groups
and AWS Service Catalog.

To perform the steps in the following procedure, you must have the following
permissions:

- **Action:**
  `tag:TagResources`
- **Action:**
  `resource-groups:Tag`
- **Action:**
  `resource-groups:CreateGroup`
- **Action:**
  `resource-groups:GroupResources`
- **Action:**
  `servicecatalog:CreateApplication`
- **Action:**
  `servicecatalog:TagResource`

###### To add a selection of resources to an application

1. On the **[Resource search](https://console.aws.amazon.com/resource-explorer/home#/search "https://console.aws.amazon.com/resource-explorer/home#/search")** page, start by choosing the view that you want to use.
   You can choose from among only those views that you have permissions to
   access.
2. (Optional) Submit a [Resource
   query](using-search.md "using-search.md").
3. In **Resources**, select up to 400 resources.
4. For **Actions**, choose **Add to
   application**.
5. In **Applications**, select the desired application.
6. Choose **Next**.
7. (Optional) If necessary, choose **Remove resources from their
   application** to remove resources from their current
   application and add them to your newly selected application.
8. Choose **Confirm**.
9. Select the final acknowledgement about removing resources from their
   current application to your newly selected application, and then choose
   **Confirm**.

After creating the new application, resource searches may take several minutes to
reflect new tagging details.

### Export resources to a .csv file

You can export the results of a **Resource query** to a
comma-separated values (.csv) file. The .csv file includes the identifier, resource
type, Region, AWS account, the total number of tags, and a column for each unique
tag key in the collection. The .csv file can help you configure your AWS resources
in your organization, or determine where there are overlaps or inconsistencies in
tagging across resources.

1. In the results of your **Resources** query, choose
   **Actions**, **Export CSV**.

For searches using search operators (calling the
`ListResources` API) where results may return more than 1,000
matches, pagination is progressive and loads pages in groups of 10. For
example, exporting to CSV from page 10 exports 1,000 results. Exporting from
page 11 paginates through page 20, exports up to 2,000 results. 2. If prompted by your browser, choose to open the .csv file, or save it to a
convenient location.
