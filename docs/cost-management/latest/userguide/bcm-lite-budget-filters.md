

# Budget filters in the AWS Billing and Cost Management console
<a name="bcm-lite-budget-filters"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

The following information is about budget filters in the AWS Billing and Cost Management console for our new AWS experience. You can use the following budget filters.

API operation  
Choose an action, such as `CreateBucket`.

Availability zone  
Choose the Availability Zone in which the resource that you want to create a budget for is running.

Billing entity  
Helps you identify whether your invoices or transactions are for AWS Marketplace or for purchases of other AWS services.

Charge type  
Different types of charges or fees.  
+ **Credit**: Any AWS credits that are applied to your account.
+ **Other out-of-cycle charges**: Any subscription charges that aren't upfront reservation charges or support charges.
+ **Refund**: Any refunds that you received. Refunds are listed as a separate line item in the data table. They don't appear as an item in the chart because they represent a negative value in the calculation of your costs. The chart displays only positive values.
+ **Reservation applied usage**: Usage that AWS applied reservation discounts to.
+ **Support fee**:
+ **Tax**: Any taxes that are associated with the charges or fees in your cost chart.
+ **Usage**: Usage that AWS didn't apply reservation discounts to.

Instance family  
Choose the family of instances to track using this budget.

Instance type  
Choose the type of instance that you want to track with this budget.

Invoicing entity  
The AWS entity that issues the invoice. Possible values include:  
+ **Amazon Web Services, Inc.** – The entity that issues invoices to customer globally, where applicable.
+ **Amazon Web Services India Private Limited** – The entity that issues invoices to customers based in India.
+ **Amazon Web Services South Africa Proprietary Limited** – The entity that issues invoices to customers in South Africa.

Legal entity  
The Seller of Record of a specific product or service. In most cases, the invoicing entity and legal entity are the same. The values might differ for third-party AWS Marketplace transactions. Possible values include:  
+ **Amazon Web Services, Inc.** – The entity that sells AWS services.
+ **Amazon Web Services India Private Limited** – The local Indian entity that acts as a reseller for AWS services in India.
Amazon Web Services EMEA SARL is the marketplace operator for your purchases if your account is located in EMEA (excluding Turkey and South Africa), and the seller is eligible in EMEA. Purchases include subscriptions. Amazon Web Services, Inc. is the marketplace operator for purchases if the seller isn't eligible for EMEA. For more information, see [AWS Europe](https://aws.amazon.com/legal/aws-emea/).

Purchase option  
Choose `On Demand Instances`, `Standard Reserved Instances`, or `Savings Plans`.

Service  
Choose an AWS service. This is only supported for cost budgets.

Tag  
If you activated any tags, choose a resource tag. A tag is a label that you can use to organize your resource costs and track them on a detailed level.

Usage type  
Usage types are the units each service uses to measure the usage for specific types of resources. If you choose a filter such as S3 and then choose a usage type value, such as DataTransfer-Out-Bytes (GB), your costs are limited to S3 DataTransfer-Out-Bytes (GB).  
You can create a usage budget only for a specific unit of measure. If you choose Usage type but not Usage type group, the budget monitors all of the available units of measure for the usage type.

Usage type group  
A usage type group is a collection of usage types that have the same unit of measure. If you choose both the Usage type group and the Usage type filters, Cost Explorer shows you usage types that are automatically constrained to the group unit of measure. For example, assume you choose the group EC2: Running Hours (Hrs), and then choose the EC2-Instances filter for Usage type. Cost Explorer shows you only the usage types that are measured in hours.