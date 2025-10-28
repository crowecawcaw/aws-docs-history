# Creating applications

You create applications to group resources and metadata.
After you enter a name and description for your application, you can associate resources, attribute groups, and tags with it.
You can also share your application with other accounts in your organization.

When you create an application, AppRegistry vends a user tag called the `awsApplication` tag on your behalf.
You can add this tag to resources to help identify which resources are associated with an application.

myApplications in AWS Management Console
Use myApplications in the AWS Management Console to [create a new application](../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md "../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md")
and organize its resources.

AWS recommends creating all of your new applications using myApplications in the AWS Management Console. This method
ensures all of the resources added to the application are tagged with the `awsApplication` tag and provides you with
the [additional features and benefits of myApplications](../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md#myApp-benefits "../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md#myApp-benefits").

AppRegistry console

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose **Create application**.
4. Under **Application name and description**,
   enter a name
   for your application.
   You can optionally enter a description
   for your application.
5. (Optional)
   Under **Application share configuration**,
   choose **Turn on cross-account sharing**
   to share the application's visibility
   with accounts, organizational units, and organizations.
   For more information,
   see [Sharing resources with accounts in your organization](sharing-definitions.md "sharing-definitions.md").
6. (Optional)
   Under **Resource collections**,
   select resources
   to associate
   to your application.
   For more information,
   see [Managing application definitions](associate-resource.md "associate-resource.md").
7. (Optional)
   Under **Attribute groups**,
   select one or more attribute groups
   to associate
   to your application.
   For more information,
   see [Managing attribute groups](associate-attributes.md "associate-attributes.md").
8. (Optional)
   Under **Application tags**,
   create tags
   using key-value pairs
   to assign metadata
   to your application.
   For more information,
   see [Managing tags](add-tags.md "add-tags.md").
9. Confirm your application configuration,
   and then choose **Create application**.
