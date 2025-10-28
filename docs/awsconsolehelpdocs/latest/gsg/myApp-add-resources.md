# Adding resources in myApplications

Adding resources to your applications allows you to group them and manage their security, performance, and compliance. You can add resources to existing applications by searching for them and selecting them or by
using existing tags and performing a tag-sync.

Search and select resources

###### To search and select resources

1. Open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the left sidebar of the console, choose **myApplications**.
3. Search for and select an application.
4. Choose **Manage resources**.
5. Choose **Add resources**.
6. (Optional) Choose a [view](../../../resource-explorer/latest/userguide/manage-views-about.md "../../../resource-explorer/latest/userguide/manage-views-about.md").
7. Search for your resources. You can search by keyword, name or type, or choose a resource type.

###### Note

If you can't find the resource you're looking for, troubleshoot with AWS Resource Explorer. For more information, see [Troubleshooting Resource Explorer search issues](../../../resource-explorer/latest/userguide/troubleshooting_search.md "../../../resource-explorer/latest/userguide/troubleshooting_search.md") in the _Resource Explorer User Guide_. 8. Select the checkbox next to the resources you want to add. 9. Choose **Add**.

Automatically add resources using tags
When you create an application, you can bulk-onboard resources by specifying an existing tag key-value pair. With this method, AWS automatically applies the `awsApplication` tag to all of the resources, and creates a tag-sync for the application’s resources by default.
With tag-sync enabled, any resources that are tagged with the specified tag key-value pair are automatically added to the application.

###### To add resources using existing tags

1. Open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the left sidebar of the console, choose **myApplications**.
3. Choose **Manage resources**.
4. Choose **Create tag-sync**.
5. Select an existing tag key and value:
   1. Select the **Role** used to tag resources. For more information, see
      [Tag-sync task required permissions](../../../servicecatalog/latest/arguide/app-tag-sync.md#tag-sync-role "../../../servicecatalog/latest/arguide/app-tag-sync.md#tag-sync-role") in the
      _AWS Service Catalog AppRegistry Administrator Guide_.
   2. Select a **Tag key**.
   3. Select a **Tag value**.
   4. Review and accept the **I acknowledge that Group Lifecycle Events will be enabled to create a tag sync** notice.
      GLE allows AWS to notice changes to the resources tagged with your key-value pair.

6. Choose **Create tag sync**.
