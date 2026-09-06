

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Creating and managing resource shares in applications
<a name="share-apps"></a>

 This topic describes how to create and manage resource shares for AppRegistry applications. For information about creating applications, see [Creating applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-apps.html). 

**Note**  
 Before a member account can enable cross-account sharing, the management account in the organization must enable sharing. For more information, see [Sharing your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS Resource Access Manager User Guide*. 

**To create a resource shares for a new application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose **Create application**. 

1.  Under **Application name and description**, enter a name for your application. You can optionally enter a description for your application. 

1.  To enable sharing for a management account, under **Application share configuration**, choose **Enable**. 

   1.  On **Settings**, select **Enable sharing with AWS Organizations**, and then choose **Save settings**. 

1.  To enable sharing for a member account, under **Application share configuration**, choose **Turn on cross-account sharing**. 

   1.  For **Select Organization entity**, select your preferred organization entity (**AWS Organization Account**, **AWS Organization Unit**, or **AWS Organization**). 

   1.  For **ID**, enter the ID for your preferred organization entity. 

   1.  For **Share permission**, select **Allow associations** or **Read only**. 
      +  **Allow associations** when the selected account can associate resource collections and attribute groups to the application.
      +  **Read only** when the selected account can view the application only. 
**Note**  
 When you select **Turn on cross-account sharing**, you can display the organizational structure in a heirarchy or list view by choosing **Display organizational structure**.   
 You can add an organization entity by choosing **Add new**. You can delete an organization entity by choosing **Remove** next to the organization entity that you're deleting. 

1.  Complete your application configuration, and then choose **Create application**. 

**To create a resource share for an existing application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose the name of the application that you want to create a resource share for. Or select the application that you want to create a resource share for, and then choose **View**. You're directed to the **Application details** screen. 

1.  On **Application details**, choose **Share**, and then choose **Create new share**. 
**Tip**  
 The **Share** tab displays resource shares associated to the application. You can manage these resource shares by choosing **Manage in RAM console**. For more information, see [What is AWS Resource Access Manager?](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) in the *AWS Resource Access Manager User Guide*. 

1.  To enable sharing for a management account, under **Application share configuration**, choose **Enable**. 

   1.  On **Settings**, select **Enable sharing with AWS Organizations**, and then choose **Save settings**. 

1.  To enable sharing for a member account, under **Application share configuration**, choose **Turn on cross-account sharing**. 

   1.  For **Select Organization entity**, select your preferred organization entity (**AWS Organization Account**, **AWS Organization Unit**, or **AWS Organization**). 

   1.  For **ID**, enter the ID for your preferred organization entity. 

   1.  For **Share permission**, select **Allow associations** or **Read only**. 
      +  **Allow associations** when the selected account can associate resource collections and attribute groups to the application.
      +  **Read only** when the selected account can view the application only. 
**Note**  
 When you select **Turn on cross-account sharing**, you can display the organizational structure in a heirarchy or list view by choosing **Display organizational structure**.   
 You can add an organization entity by choosing **Add new**. You can delete an organization entity by choosing **Remove** next to the organization entity that you're deleting. 

1.  Confirm your resource share configuration, and then choose **Create share**. 