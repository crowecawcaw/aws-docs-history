

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Ordering Service Catalog products through the ServiceNow Service portal
<a name="service-portal"></a>

 The Connector for ServiceNow supports the ordering of Service Catalog products through Service Portal. You can use the **Service Catalog **and** Order Something** views. The release also includes pages and widgets you can add to Service Portal that enable users to view their provisioned products. 

**Note**  
The audience for the Service Portal Features section is a ServiceNow administrator or equivalent. The ServiceNow user requires permissions to modify the Service Portal.

## Service portal widgets
<a name="service-portal-widgets"></a>

 The Connector for ServiceNow includes widgets you can add to your Service Portal. It also includes two alternative view Portal Pages for the following: 
+ **My AWS Products** – Overview of all provisioned products the user owns
+ **AWS Product Details** – Details of a single provisioned product
+ **Search AWS Products** – Search for AWS Service Catalog products by providing AWS account, Region, and portfolio details. To access the new widgets, update the Service Portal Designer.

To access the new widgets, update the Service Portal Designer.

**To update the Service Portal Designer**

1. Go to [Create and edit a page using the Service Portal Designer](https://docs.servicenow.com/bundle/kingston-servicenow-platform/page/build/service-portal/task/t_ConfigureAPage.html).

1.  Following the instructions, choose the **Service Portal Index** page. 

1.  Under the **Order Something** container, add the **My AWS **widget. 

   The new widget appears on your main Service Portal view.

## Service portal pages
<a name="service-portal-pages"></a>

 This section describes the two new pages available in the Service Portal Beta release of the AWS Service Management Connector: **My AWSProducts** and **AWS Product Details**. You can add links to these pages on the Service Portal home page or other pages by using the usual page configuration mechanism in Service Portal. 

****My AWS Products****  
An overview of all provisioned products that the user owns. Terminated products display separately from current products in a collapsed panel on the initial page load. 

Use the following format to access the **My AWS Products** page. 

```
http://<insertinstancename>.service-now.com/sp?id=aws_sc_pp
```

****AWS Product Details****  
Details of a single provisioned product.

Use the following format to access the **AWS Product Details** page:

```
http://<insertinstancename>.service-now.com/sp?id=aws_sc_pp_details&sys_id=<provisioned product id>
```

**Search AWS Products**

Search feature for AWS Service Catalog products

Use the following format to access the **Search AWS Products** page:

```
           http://<insertinstancename>.service-now.com/sp?id=aws_sc_product_search>
```

**Note**  
Ensure that the end user has **x\_126749\_aws\_sc.productsearchaccess** to view and use this service portal 