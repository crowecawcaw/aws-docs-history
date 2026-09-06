

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Associating and disassociating attribute groups
<a name="associate-attr-groups"></a>

 This topic describes how to associate and disassociate attribute groups in AppRegistry. 

**Topics**
+ [Associate attribute groups to a new application](#w2aac13b9c19b7)
+ [Associate attribute groups to an existing application from the Applications screen](#w2aac13b9c19b9)
+ [Associate attribute groups to an existing application from the Attribute groups screen](#w2aac13b9c19c11)
+ [Disassociate attribute groups from an existing application](#w2aac13b9c19c13)

## Associate attribute groups to a new application
<a name="w2aac13b9c19b7"></a>

 The following procedure describes how to associate attribute groups to a new application. 

**To associate attribute groups to a new application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose **Create application**. 

1.  Under **Application name and description**, enter a name for your application. You can optionally enter a description for your application. 

1.  Under **Attribute groups**, select one or more attribute groups from the dropdown menu to associate to your application. 

1.  Choose **Create application**. 

## Associate attribute groups to an existing application from the Applications screen
<a name="w2aac13b9c19b9"></a>

 The following procedure describes how to associate attribute groups to an existing application from the **Applications** screen. 

**To associate attribute groups to an existing application from the Applications screen**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose the name of the application that you want to associate an attribute group to. Or select the application that you want to associate an attribute group to, and then choose **View**. You're directed to the **Application details** screen. 

1.  Choose **Attribute groups**, and then choose **Associate attribute group**. 

1.  Under **Attribute groups**, select an attribute group from the dropdown menu to associate to your application, and then choose **Save changes**. 

## Associate attribute groups to an existing application from the Attribute groups screen
<a name="w2aac13b9c19c11"></a>

 The following procedure describes how to associate an attribute group to an existing application from the **Attribute groups** screen. 

**To associate attribute groups to an existing application from the Attribute groups screen**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Attribute groups**. You're directed to the **Attribute groups** screen. 

1.  On **Attribute groups**, choose **Create Attribute group**. 

1.  Under **New attribute group**, enter a name and description for your attribute group, and provide the JSON schema that captures your metadata taxonomy. 

    **Example: attribute group metadata** 

   ```
   {
    "Team" : "WebTeam",
    "Department": "10006",
    "ParentDept": "Research",
    "ContactAlias": "research@team.com"
   }
   ```

1.  Under **Assign attribute group to an application**, select one or more applications to associate to your attribute group. 

1.  Choose **Create attribute group**. 

## Disassociate attribute groups from an existing application
<a name="w2aac13b9c19c13"></a>

 The following procedure describes how to disassociate an attribute group from an existing application. 

**To disassociate attribute groups from an existing application**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) 

1.  From the navigation pane, choose **AppRegistry**, and then choose **Applications**. You're directed to the **Applications** screen. 

1.  On **Applications**, choose the name of the application that you want to disassociate an attribute group from. Or select the application that you want to disassociate an attribute group from, and then choose **View**. You're directed to the **Application details** screen. 

1.  Choose **Attribute groups**, and then select the attribute group that you want to disassociate from your application. 

1.  Choose **Disassociate**, confirm your disassociation, and then choose **Save changes**. 