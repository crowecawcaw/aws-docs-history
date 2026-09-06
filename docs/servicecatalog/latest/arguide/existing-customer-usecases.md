

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Tutorial: Existing AppRegistry application resources and the `awsApplication` tag
<a name="existing-customer-usecases"></a>

If you have existing AppRegistry application, AWS recommends that you retroactively apply the `awsApplication` tag to all of the resources in the application, and also ensure any future resources added to the application have the `awsApplication` tag applied. This tutorial provides instructions for both recommendations. 

**Note**  
Managing an application's resources by adding or removing the `awsApplication` tag requires specific permissions. Review the minimum permissions for the AppRegistry APIs in the [*AWS Service Catalog Developer Guide*](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html) and the Resource Groups APIs in the [*AWS Resource Groups API Reference*](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html). 

## Apply the `awsApplication` tag to the resources in an existing application
<a name="scar-app-usecase-1"></a>

In this situation, you have an existing AppRegistry application which includes resources that are *not* tagged with the `awsApplication` tag. The following procedure provides instructions to apply the `awsApplication` tag to those resources. 

**To tag an existing application's resources with the `awsApplication` tag:**

1. Identify the **application's tag value** (`awsApplication` tag value), which is expressed as an Amazon Resource Name (ARN).
   + Call the AppRegistry [`GetApplication` API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_GetApplication.html#API_app-registry_GetApplication_ResponseSyntax) and find the value in the `applicationTag` response parameter. 
   + Alternatively, you can navigate to the myApplications dashboard for the application and copy the `awsApplication` tag value from the [Application summary widget](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/myApp-app-dash.html#myApp-summary). 

1. After identifying the Application tag value, call the AppRegistry [`ListAssociatedResources` API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_ListAssociatedResources.html) to view a list of resources that are already in the application. 

1. Call the AppRegistry [`AssociateResource` API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html) with the `options` parameter value as `APPLY_APPLICATION_TAG`. 

   **Example CLI command**:

   ```
   aws servicecatalog-appregistry associate-resource --application {{application_ARN}} 
                           --resource-type {{type}} --resource {{name}} --option "APPLY_APPLICATION_TAG"
   ```

## Add more resources to an existing application by applying the `awsApplication` tag
<a name="scar-app-usecase-2"></a>

In this situation, you have an existing AppRegistry application to which you want to add new resources, and you want those resources to have the `awsApplication` tag applied. 

Use [myApplications in the AWS Management Console to add resources to an application](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/myApp-manage-resources.html#myApp-add-resources). Resources added to the application using myApplications are automatically tagged with the `awsApplication` tag. 

You can also use the AWS Resource Groups [`GroupResources` API](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupResources.html) to add resources to a specified group. The group is an application group, where the ARN is the `awsApplication` tag value. 

**To manually add resources to an application**: 

Call the Resource Groups `GroupResources` API and define the following parameters:
+ `Group` — The name or the Amazon resource name (ARN) of the application group to add resources to. 
+ `ResourceARNs` — The list of Amazon resource names (ARNs) of the resources to be added to the group. 

**Example CLI command**:

```
aws resourcegroups group-resources —-group "{{ApplicationGroup-ARN}}" —-resourceArns "{{Resource-ARNs}}"
```