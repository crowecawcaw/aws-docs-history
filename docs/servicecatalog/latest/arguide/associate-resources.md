

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Associating and disassociating application resources
<a name="associate-resources"></a>

 An application resource is an object within an AWS service that you can tag with [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags), which is an AWS user tag that AppRegistry vends on your behalf. The following procedures describe how to associate and disassociated application resources. 

**Note**  
For AppRegistry applications created before November 8th, 2023, AppRegistry creates the `awsApplication` tag after you perform your first resource association. This tag’s value is a unique identifier for the application. You can then apply the `awsApplication` tag to any other resources you want to add to the application. For AppRegistry applications created after November 8th, 2023, AppRegistry creates the `awsApplication` tag when you create the application. 

**Topics**
+ [Associate application resources in a new application](#w2aac13b7c19c21b9)
+ [Associate application resources in an existing application](#w2aac13b7c19c21c11)
+ [Disassociate application resources from an application](#w2aac13b7c19c21c13)

## Associate application resources in a new application
<a name="w2aac13b7c19c21b9"></a>

 The following procedure describes how to associate application resources in a new application. 

**To associate application resources in a new application.**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose **Create application**. 

1.  Under **Application name and description**, enter a name and optional description for your application. 

1.  Under **Resource collections**, choose one or more provisioned products or CloudFormation stacks to associate to your application. 

1.  Choose **Create application**. 

## Associate application resources in an existing application
<a name="w2aac13b7c19c21c11"></a>

 The following procedure describes how to associate application resources in an existing application. 

**To associate application resources in an existing application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the left navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose the name of the application that you want to associate resources to. Or select the name of application that you want to associate resources to, and choose **View**. You're directed to the **Application details** screen. 

1.  Choose **Resource collections**, and then choose **Associate resource collection**. 

1.  Under **Resource collections**, choose one or more provisioned products or CloudFormation stacks to associate to your application. 

1.  Choose **Save changes**. 
**Note**  
 If you share an application with this account, and the application has read-only permissions, associate and disassociate actions are disabled for resource collections. 

## Disassociate application resources from an application
<a name="w2aac13b7c19c21c13"></a>

 The following procedure describes how to disassociate application resources from an existing application. 

**To disassociate application resources from an existing application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose the name of the application that you want to disassociate resources from. Or select the name of the application that you want to disassociate resources from, and choose **View**. You're directed to the **Application details** screen. 

1.  Choose **Resource collections**, select the resource that you want to disassociate from the application, and then choose **Disassociate**. 

1.  Confirm your disassociation, and then choose **Ok**. 
**Note**  
 If you share an application with this account, and the application has read-only permissions, associate and disassociate actions are disabled for resource collections. 