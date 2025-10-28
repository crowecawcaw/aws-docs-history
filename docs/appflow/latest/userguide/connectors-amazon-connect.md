# Amazon Connect connector for Amazon AppFlow

Amazon Connect is an AWS service that you can use to set up an omnichannel, cloud-based contact
center for your customers. Amazon Connect provides the Customer Profiles feature. This feature helps you
create unified customer profiles. These profiles combine customer information from external
applications with contact history from Amazon Connect. For example, you can combine contact information,
order history, and interaction history from software as a service (SaaS) applications like
Salesforce, Zendesk and other Amazon AppFlow connectors. The contact center agents for your organization
can use this consolidated information during customer support interactions.

If you use Amazon Connect, you can also use Amazon AppFlow to transfer data from supported data sources to
Customer Profiles.

For more information about Customer Profiles, see [Use Amazon Connect Customer
Profiles](../../../connect/latest/adminguide/customer-profiles.md "../../../connect/latest/adminguide/customer-profiles.md") in the _Amazon Connect Administrator Guide_

## Amazon AppFlow support for Amazon Connect

Amazon AppFlow supports Amazon Connect as follows.

**Supported as a data source?**
No. You can't use Amazon AppFlow to transfer data from Amazon Connect.

**Supported as a data destination?**
Yes. You can use Amazon AppFlow to transfer data to Amazon Connect.

**Supported Amazon Connect features**

Amazon AppFlow integrates only with the Customer Profiles feature.

## Transferring data to Amazon Connect with a

flow

To transfer data to Amazon Connect Customer Profiles, you create an Amazon AppFlow flow, and you
choose Amazon Connect as the data destination. Then, you use Amazon Connect to set up data mappings in
Customer Profiles. These mappings define how data from the data source is mapped to the customer
profile.

Before you can use Amazon AppFlow to transfer data to Customer Profiles, you must meet these
requirements:

- You have an Amazon Connect instance.
- You have enabled the Customer Profiles feature for your Amazon Connect instance. When you enable
  Customer Profiles, you create a customer profiles domain, which is the container for your
  customer data in Amazon Connect.
- You have configured Customer Profiles to encrypt your data under a KMS key.

For more information about creating a flow in Amazon AppFlow and setting up data mappings in Amazon Connect,
see [Set up integration
for external applications using Amazon AppFlow](../../../connect/latest/adminguide/integrate-external-applications-appflow.md "../../../connect/latest/adminguide/integrate-external-applications-appflow.md") in the _Amazon Connect Administrator Guide_.
