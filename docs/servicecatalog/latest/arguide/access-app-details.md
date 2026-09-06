

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Using Application details
<a name="access-app-details"></a>

 The **Application details** screen shows the following information: 
+  The application's name and description 
+  When the application was created and who created the application 
+  The application's ID, ARN, and resource group ARN 
+  The application's share configuration 
+  The resources and attribute groups associated with the application, as well as the application's resource shares 

 You can also view the tags you create to organize application resources and [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags), which is an AWS user tag that you can use to add resources to an application. 

**Note**  
For AppRegistry applications created before November 8th, 2023, AppRegistry creates the `awsApplication` tag after you perform your first resource association. This tag’s value is a unique identifier for the application. You can then apply the `awsApplication` tag to any other resources you want to add to the application. For AppRegistry applications created after November 8th, 2023, AppRegistry creates the `awsApplication` tag when you create the application. 

 You can perform the following actions from the **Application details** screen: 
+  View applications in AWS Systems Manager Application Manager. For more information, see [Viewing applications in AWS Systems Manager Application Manager](https://docs.aws.amazon.com/servicecatalog/latest/arguide/view-app-manager.html). 
+  Delete and edit applications. For more information, see [Deleting applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/delete-apps.html) and [Editing applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/edit-apps.html). 
+  View and manage resources associated with applications. For more information, see [Associating and disassociating application resources](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resources.html). 
+  View and manage attribute groups associated with applications. For more information, see [Associating and disassociating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attr-groups.html). 
+  View and manage resource shares associated with applications. For more information, see [Sharing application resources with accounts in your organization](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html). 
+  View and manage tags you create to organize application resources and identify resources associated with an application. For more information, see [Managing tags](https://docs.aws.amazon.com/servicecatalog/latest/arguide/add-tags.html) and [The `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags). 

**Topics**
+ [Viewing Application details](view-app-details.md)
+ [Viewing applications in AWS Systems Manager Application Manager](view-app-manager.md)