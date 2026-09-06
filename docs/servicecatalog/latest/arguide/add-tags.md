

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Managing tags
<a name="add-tags"></a>

 Tags act as metadata to organize application resources. You create tags using key-value pairs. You add tags to applications and attribute groups, so you can group them by environment, owner, purpose, or other criteria. 

**Note**  
 The tags discussed in this section are **not** the same as the [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags). The `awsApplication` tag is a tag AppRegistry vends on your behalf when you create an application, and AWS automatically applies it to all resources in the application. 

**Topics**
+ [Adding and deleting tags in a new application](#w2aac13c13b9)
+ [Adding and deleting tags from the Application details screen](#w2aac13c13c11)
+ [Adding and deleting tags in a new attribute group](#w2aac13c13c13)
+ [Adding and deleting tags from Attribute group details](#w2aac13c13c15)

## Adding and deleting tags in a new application
<a name="w2aac13c13b9"></a>

 The following procedure describes how to add and delete tags in a new application. For information about creating a new application, see [Creating applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-apps.html). 

**To add and delete tags in a new application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen where you can view all of your applications. 

1.  On **Applications**, choose **Create application**. 

1.  Under **Application name and description**, enter a name for your application. You can optionally enter a description for your application. 

1.  Under **Application tags**, choose **Add tag**, and then enter a Key/Value pair. 

   1.  To add another tag, choose **Add another**, and then enter a new key/value pair. You can create up to 50 tags for an application. 

   1.  To delete a tag, choose **Remove** next to the tag that you want to delete. 

1.  Complete your configuration, and then choose **Create application**. 

**Note**  
 AppRegistry creates and adds tags that begin with `aws`, such as `aws:servicecatalog:applicationName`. These are considered internal tags and can't be removed. 

## Adding and deleting tags from the Application details screen
<a name="w2aac13c13c11"></a>

 The following procedure describes how to add and delete tags from the **Application details** screen. For more information about using application details, see [Using application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-app-details.html). 

**To add and delete tags from Application details**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen where you can view all of your applications. 

1.  On **Applications**, choose the name of the application that you want to create a tag for. Or select the application that you want to create a tag for, and choose **View**. You're directed to the **Application details** screen. 

1.  On **Application details**, choose **Tags**. 

1.  Under **Add tags specific to this application**, enter a key/value pair, and then choose **Add tag**. 

   1.  To add another tag, enter a new key/value pair, and then choose **Add tag** again. You can create up to 50 tags for an application. 

   1.  To delete a tag, under **Application specific tags**, select the key/value pair that you want to remove, and then choose **Delete tag**. 

## Adding and deleting tags in a new attribute group
<a name="w2aac13c13c13"></a>

 The following procedure describes how to add and delete in a new attribute group. For information about creating a new attribute group, see [Creating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-attr-groups.html). 

**To add and delete tags in a new attribute group**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Attribute groups**. You're directed to the **Attribute groups** screen. 

1.  On **Attribute groups**, choose **Create attribute group**. 

1.  Under **New attribute group**, enter a name and description for your attribute group, and and provide the JSON schema that captures your metadata taxonomy. 

1.  Under **Add tags**, enter a key/value pair to assign metadata to your attribute group. 

   1.  To add another tag, choose **Add new item**, and then enter new key/value pair. You can create up to 50 tags for an attribute group. 

   1.  To delete a tag, choose **Remove** next to the tag that you want to delete. 

1.  Complete your configuration, and then choose **Create attribute group**. 

**Note**  
 AppRegistry creates and adds tags that begin with `aws`, such as `aws:servicecatalog:attributeGroupName` . These are considered internal tags and can't be removed. 

## Adding and deleting tags from Attribute group details
<a name="w2aac13c13c15"></a>

 The following procedure describes how to add and delete tags from the **Attribute group details** screen. For more information about using attribute group details, see [Using attribute group details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-attr-group-details.html). 

**To add and delete tags from Attribute group details**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Attribute groups**. You're directed to the **Attribute groups** screen where you can view all of your attribute groups. 

1.  On **Attribute groups**, choose the name of the attribute group that you want to create a tag for. Or select the attribute group that you want to create a tag for, and choose **View**. You're directed to the **Attribute groups details** screen. 

1.  On **Attribute group details**, choose **Tags**. 

1.  Under **Add tags specific to this attribute group**, enter a key/value pair, and then choose **Add tag**. 

   1.  To add another tag, enter a new key/value pair, and then choose **Add tag** again. You can create up to 50 tags for an attribute group. 

   1.  To delete a tag, under **Attribute group specific tags**, select the key/value pair that you want to remove, and then choose **Delete tag**. 