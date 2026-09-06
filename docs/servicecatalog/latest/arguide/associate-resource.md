

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Managing application resources
<a name="associate-resource"></a>

**Note**  
You can also use myApplications in the AWS Management Console to add and remove resources from your applications. Review [Managing resources](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/myApp-manage-resources.html) in the AWS Management Console *Getting started guide* for instructions. 

 An application resource is an object within an AWS service that you can tag with [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags). AWS customers and services use the `awsApplication` tag to add and remove resources from applications and identify which resources are associated with an application. 

 You add resources to your application after you define your application. You can add and remove application resources with any of the existing methods for tagging resources, infrastructure as code, and the AppRegistry API. 

 To add and remove application resources with the AppRegistry API, use the [console procedures](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resources.html) or the AppRegistry `AssociateResource` and `DisassociateResource` APIs. You can can add the `awsApplication` tag to a resource using the AppRegistry `AssociateResource` API with the `APPLY_APPLICATION_TAG` option. 

**Note**  
 Adding and removing resources requires certain permissions. For more information, see [AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html) and [DisassociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DisassociateResource.html) in the *AWS Service Catalog AppRegistry Developer Guide*. 

AppRegistry integrates with AWS Resource Groups. When you create an application, AWS Resource Groups creates an application resource group and a resource group for every CloudFormation stack or tag-based resource you associate with your application. You can list the resources in your application by calling the Resource Groups `ListGroupResources` API on the application resource group. Any resource tagged with the `awsApplication` tag for this application will be a member of this group. 

For information about resource types and related functionalities you can use with AppRegistry applications, see [Supported resource types for AppRegistry applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/supported-resource-types.html). 

 This section decribes how to manage application definitions as you create and associate deployed resources to applications in your local account and AWS Region. 

**Topics**
+ [Associating and disassociating application resources](associate-resources.md)
+ [Controlling the resources associated to applications](control-tags.md)
+ [Supported resource types for AppRegistry applications](supported-resource-types.md)