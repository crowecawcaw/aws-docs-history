

# Connect Customer connector for Amazon AppFlow
<a name="connectors-amazon-connect"></a>

Connect Customer is an AWS service that you can use to set up an omnichannel, cloud-based contact center for your customers. Connect Customer provides the Customer Profiles feature. This feature helps you create unified customer profiles. These profiles combine customer information from external applications with contact history from Connect Customer. For example, you can combine contact information, order history, and interaction history from software as a service (SaaS) applications like Salesforce, Zendesk and other Amazon AppFlow connectors. The contact center agents for your organization can use this consolidated information during customer support interactions.

If you use Connect Customer, you can also use Amazon AppFlow to transfer data from supported data sources to Customer Profiles.

For more information about Customer Profiles, see [Use Amazon Connect Customer Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles.html) in the *Connect Customer Administrator Guide*

## Amazon AppFlow support for Connect Customer
<a name="amazon-connect-support"></a>

Amazon AppFlow supports Connect Customer as follows.

**Supported as a data source?**  
No. You can't use Amazon AppFlow to transfer data from Connect Customer.

**Supported as a data destination?**  
Yes. You can use Amazon AppFlow to transfer data to Connect Customer.

**Supported Connect Customer features**  
Amazon AppFlow integrates only with the Customer Profiles feature.

## Transferring data to Connect Customer with a flow
<a name="amazon-connect-transfer-data"></a>

To transfer data to Connect Customer Customer Profiles, you create an Amazon AppFlow flow, and you choose Connect Customer as the data destination. Then, you use Connect Customer to set up data mappings in Customer Profiles. These mappings define how data from the data source is mapped to the customer profile.

Before you can use Amazon AppFlow to transfer data to Customer Profiles, you must meet these requirements:
+ You have an Connect Customer instance.
+ You have enabled the Customer Profiles feature for your Connect Customer instance. When you enable Customer Profiles, you create a customer profiles domain, which is the container for your customer data in Connect Customer.
+ You have configured Customer Profiles to encrypt your data under a KMS key.

For more information about creating a flow in Amazon AppFlow and setting up data mappings in Connect Customer, see [Set up integration for external applications using Amazon AppFlow](https://docs.aws.amazon.com/connect/latest/adminguide/integrate-external-applications-appflow.html) in the *Connect Customer Administrator Guide*.