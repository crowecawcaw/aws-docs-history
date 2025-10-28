# Sharing resources with accounts in your organization

You can share applications and attribute groups to an account, organizational unit, or organization.

AppRegistry integrates with AWS Resource Access Manager (AWS RAM), so you can view a list of resource shares associated with applications and attribute groups.
For more information, see [What is AWS Resource Access Manager?](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") in the _AWS Resource Access Manager User Guide_.

When you create a resource share for an account, organization, or organizational unit, you can access the application or attribute group with the permission type that you select.
For more information, see [Sharing your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS Resource Access Manager User Guide_.

This section describes how to create and manage resource shares for applications and attribute groups.

###### Note

When you create an application, AppRegistry vends a user tag called _the `awsApplication` tag_.
You can add this tag to resources to identify which resources are associated with an application.
The `awsApplication` tag is included in all shared applications.
For more information, see [The `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").

###### Topics

- [Creating and managing resource shares in applications](share-apps.md "share-apps.md")
- [Creating and managing resource shares in attribute groups](share-attr-groups.md "share-attr-groups.md")
- [Using AWS Resource Access Manager to share resources](share-ram.md "share-ram.md")
