# Managing application resources

###### Note

You can also use myApplications in the AWS Management Console to add and remove resources from your applications. Review
[Managing resources](../../../awsconsolehelpdocs/latest/gsg/myApp-manage-resources.md "../../../awsconsolehelpdocs/latest/gsg/myApp-manage-resources.md") in the
AWS Management Console _Getting started guide_ for instructions.

An application resource is an object within an AWS service that you can tag with [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").
AWS customers and services use the `awsApplication` tag to add and remove resources from applications and identify which resources are associated with an application.

You add resources to your application after you define your application.
You can add and remove application resources with any of the existing methods for tagging resources, infrastructure as code, and the AppRegistry API.

To add and remove application resources with the AppRegistry API, use the [console procedures](associate-resources.md "associate-resources.md") or the AppRegistry `AssociateResource` and `DisassociateResource` APIs.
You can can add the `awsApplication` tag to a resource using the AppRegistry `AssociateResource` API with the `APPLY_APPLICATION_TAG` option.

###### Note

Adding and removing resources requires certain permissions.
For more information, see [AssociateResource](../dg/API_app-registry_AssociateResource.md "../dg/API_app-registry_AssociateResource.md") and
[DisassociateResource](../dg/API_app-registry_DisassociateResource.md "../dg/API_app-registry_DisassociateResource.md") in the _AWS Service Catalog AppRegistry Developer Guide_.

AppRegistry integrates with AWS Resource Groups. When you create an application, AWS Resource Groups creates an application resource group and a resource group for every AWS CloudFormation
stack or tag-based resource you associate with your application. You can list the resources in
your application by calling the Resource Groups `ListGroupResources` API on the application
resource group. Any resource tagged with the `awsApplication` tag for this application
will be a member of this group.

For information about resource types and related functionalities you can use with AppRegistry applications, see [Supported resource types for AppRegistry applications](supported-resource-types.md "supported-resource-types.md").

This section decribes how to manage application definitions as you create and associate deployed resources to applications in your local account and AWS Region.

###### Topics

- [Associating and disassociating application resources](associate-resources.md "associate-resources.md")
- [Controlling the resources associated to applications](control-tags.md "control-tags.md")
- [Supported resource types for AppRegistry applications](supported-resource-types.md "supported-resource-types.md")
