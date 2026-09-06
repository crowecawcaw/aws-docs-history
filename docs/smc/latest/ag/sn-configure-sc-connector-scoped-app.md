

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS Service Management Connector scoped application
<a name="sn-configure-sc-connector-scoped-app"></a>

After installing and configuring the AWS Service Management Connector, you must configure the scoped application and applicable roles.

**To configure the AWS Service Management Connector scoped application permissions**

1. In your ServiceNow instance, create a user group called **Order\_AWS\_Products**. 

   Members of this group can order Service Catalog products. For instructions, see [Administer the Now Platform.](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/general/concept/intro-now-platform-landing.html)

1. Grant ServiceNow permissions to these users: 
   + **System Administrator (admin)**: For simplicity in this example, user **admin** is the administrator of the AWS Service Management scoped application. Grant this user both of the administrative permissions from the adapter:** x\_126749\_aws\_sc\_account\_admin,** **x\_126749\_aws\_sc\_portfolio\_manager**, **x\_126749\_ aws\_sc.appregistry\_manager**, **x\_126749\_ aws\_sc.automation\_manager**, **x\_126749\_aws\_sc.finding\_manager**,** ****x\_126749\_aws\_sc.opscenter\_manager**, **x\_126749\_aws\_sc.support\_case\_manager** and **x\_126749\_aws\_sc.change\_manager\_manager**, **x\_126749\_aws\_sc.productsearchaccess**, **x\_126749\_aws\_sc.cloudtrail\_event\_user**, and **x\_126749\_aws\_sc.health\_dashboard\_viewer**.

     Add **System Administrator** to the new ServiceNow group **Order\_AWS\_Products**. In a real scenario, these roles would likely be granted to different users or groups. 
   + **Abel Tuter**: The user **abel.tuter** is an illustrative end user. Grant Abel the new role **Order\_AWS\_Products**. This permission allows Abel to order products from AWS.