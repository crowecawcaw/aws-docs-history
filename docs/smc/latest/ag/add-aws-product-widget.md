

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Adding the My AWS Products widget to the Service Portal view
<a name="add-aws-product-widget"></a>

We recommend ServiceNow administrators add the **My AWS Products** widget to the ServiceNow Portal view. The widget enables users to view their AWS product requests, view outputs, and perform post-operational actions such as update, terminate, and service actions (AWS Systems Manager documents). 

**To include the My AWS Products widget on the Service Portal view**

1.  Log in as system administrator in the ServiceNow standard user interface (Fulfiller view). 

1.  In the navigator panel, find **Service Portal**. 

1.  Choose **Service Portal Configuration**. 

1. Choose **Designer**. 

1. Search for **Service Portal** in the filter. 

1.  Choose the** Service Portal** box with a house image and the word **Index** in the lower right corner. 

1.  In the left panel in **Widgets**, enter **My AWS Products** in the **Filter Widget.** 

1.  Drag the widget to the Service Portal edit view to your desired location. 

1.  Preview your changes. 

**To include the Search AWS Products widget on the Service Portal view**

1. Log in as system administrator in the ServiceNow standard user interface (Fulfiller view).

1. In the navigator panel, find **Service Portal**.

1. Choose **Service Portal Configuration**.

1. Choose **Designer**.

1. Search for Service Portal in the filter.

1. Choose the Service Portal box with a house image and the word Index in the lower right corner.

1. In the left panel in **Widgets,** enter **AWS Custom Product Search in the Filter Widget**.

1. Drag the widget to the Service Portal edit view to your desired location.

1. Preview your changes.

**Note**  
Ensure that the end user has **x\_126749\_aws\_sc.productsearchaccess** to view and use the widget. 