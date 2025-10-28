# Using Application details

The **Application details** screen shows the following information:

- The application's name and description
- When the application was created and who created the application
- The application's ID, ARN, and resource group ARN
- The application's share configuration
- The resources and attribute groups associated with the application, as well as the application's resource shares

You can also view the tags you create to organize application resources and [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags"), which is an AWS user tag that you can use to add resources to an application.

###### Note

For AppRegistry applications created before November 8th, 2023, AppRegistry creates the `awsApplication` tag
after you perform your first resource association. This tag’s value is a unique identifier for the application.
You can then apply the `awsApplication` tag to any other resources you want to add to the application.
For AppRegistry applications created after November 8th, 2023, AppRegistry creates the `awsApplication` tag
when you create the application.

You can perform the following actions from the **Application details** screen:

- View applications in AWS Systems Manager Application Manager.
  For more information, see [Viewing applications in AWS Systems Manager Application Manager](view-app-manager.md "view-app-manager.md").
- Delete and edit applications.
  For more information, see [Deleting applications](delete-apps.md "delete-apps.md") and [Editing applications](edit-apps.md "edit-apps.md").
- View and manage resources associated with applications.
  For more information, see [Associating and disassociating application resources](associate-resources.md "associate-resources.md").
- View and manage attribute groups associated with applications.
  For more information, see [Associating and disassociating attribute groups](associate-attr-groups.md "associate-attr-groups.md").
- View and manage resource shares associated with applications.
  For more information, see [Sharing application resources with accounts in your organization](sharing-definitions.md "sharing-definitions.md").
- View and manage tags you create to organize application resources and identify resources associated with an application.
  For more information, see [Managing tags](add-tags.md "add-tags.md") and [The `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").

###### Topics

- [Viewing Application details](view-app-details.md "view-app-details.md")
- [Viewing applications in AWS Systems Manager Application Manager](view-app-manager.md "view-app-manager.md")
