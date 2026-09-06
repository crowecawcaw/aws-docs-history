

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Creating applications
<a name="create-apps"></a>

 You create applications to group resources and metadata. After you enter a name and description for your application, you can associate resources, attribute groups, and tags with it. You can also share your application with other accounts in your organization. 

When you create an application, AppRegistry vends a user tag called the `awsApplication` tag on your behalf. You can add this tag to resources to help identify which resources are associated with an application. 

------
#### [ myApplications in AWS Management Console ]

Use myApplications in the AWS Management Console to [create a new application](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/myApp-getting-started.html) and organize its resources. 

AWS recommends creating all of your new applications using myApplications in the AWS Management Console. This method ensures all of the resources added to the application are tagged with the `awsApplication` tag and provides you with the [additional features and benefits of myApplications](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/aws-myApplications.html#myApp-benefits). 

------
#### [ AppRegistry console ]

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose **Create application**. 

1.  Under **Application name and description**, enter a name for your application. You can optionally enter a description for your application. 

1.  (Optional) Under **Application share configuration**, choose **Turn on cross-account sharing** to share the application's visibility with accounts, organizational units, and organizations. For more information, see [Sharing resources with accounts in your organization](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html). 

1.  (Optional) Under **Resource collections**, select resources to associate to your application. For more information, see [Managing application definitions](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resource.html). 

1.  (Optional) Under **Attribute groups**, select one or more attribute groups to associate to your application. For more information, see [Managing attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attributes.html). 

1.  (Optional) Under **Application tags**, create tags using key-value pairs to assign metadata to your application. For more information, see [Managing tags](https://docs.aws.amazon.com/servicecatalog/latest/arguide/add-tags.html). 

1.  Confirm your application configuration, and then choose **Create application**. 

------