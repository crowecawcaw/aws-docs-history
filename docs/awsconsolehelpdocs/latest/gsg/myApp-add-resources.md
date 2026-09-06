

# Adding resources in myApplications
<a name="myApp-add-resources"></a>

Adding resources to your applications allows you to group them and manage their security, performance, and compliance. You can add resources to existing applications by searching for them and selecting them or by using existing tags and performing a tag-sync.

------
#### [ Search and select resources ]

**To search and select resources**

1. Open the [AWS Management Console](https://console.aws.amazon.com/).

1. In the left sidebar of the console, choose **myApplications**.

1. Search for and select an application.

1. Choose **Manage resources**.

1. Choose **Add resources**.

1. (Optional) Choose a [view](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-about.html).

1. Search for your resources. You can search by keyword, name or type, or choose a resource type.
**Note**  
 If you can't find the resource you're looking for, troubleshoot with AWS Resource Explorer. For more information, see [Troubleshooting Resource Explorer search issues](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html?icmp=docs_re_console_lm_troubleshooting) in the *Resource Explorer User Guide*. 

1. Select the checkbox next to the resources you want to add.

1. Choose **Add**.

------
#### [ Automatically add resources using tags ]

When you create an application, you can bulk-onboard resources by specifying an existing tag key-value pair. With this method, AWS automatically applies the `awsApplication` tag to all of the resources, and creates a tag-sync for the application’s resources by default. With tag-sync enabled, any resources that are tagged with the specified tag key-value pair are automatically added to the application.

 

**To add resources using existing tags**

1. Open the [AWS Management Console](https://console.aws.amazon.com/).

1. In the left sidebar of the console, choose **myApplications**.

1. Choose **Manage resources**.

1. Choose **Create tag-sync**.

1. Select an existing tag key and value:

   1. Select the **Role** used to tag resources. For more information, see [Tag-sync task required permissions](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role) in the *AWS Service Catalog AppRegistry Administrator Guide*.

   1. Select a **Tag key**.

   1. Select a **Tag value**.

   1. Review and accept the **I acknowledge that Group Lifecycle Events will be enabled to create a tag sync** notice. GLE allows AWS to notice changes to the resources tagged with your key-value pair.

1. Choose **Create tag sync**.

------