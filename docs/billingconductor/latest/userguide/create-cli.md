# Custom line items

Use AWS Billing Conductor to create personalized line items and apply them to designated AWS accounts
within a billing group.

You can allocate costs and discounts by using custom line items. You can calculate a
custom line item as a _flat charge_ or _percentage
charge_ value. You can configure the presentation for the **Flat** custom line item by using display settings.
You can configure specific services for the percentage custom line items through ChargeDetails.LineItemFilters.
You can also set an **Itemized** computation rule for the percentage custom line item to have the custom line item displayed next to each applicable line item.
Configure the percentage-based custom line item to include or exclude resources. These resources will
include billing group costs and other flat custom line items that are associated with a
billing group for a billing period. You can then set the custom line items to apply for one
month, or to reoccur for multiple months.

Custom Line Items will appears in Billing and Cost Management tools such as Bills Page, Cost Explorer and Cost and Usage Records with specific line item types, line item subtypes, or charge types.
For Custom Line Items which are presented under Billing Conductor service, the types will be **Fee** or **Credit**, depending on the type of the Custom Line Item.
For Custom Line Items which are presented under any other service, or for Itemized Custom Line Items, the types will be **Proforma_Fee** or **Proforma_Credit** ,
depending on the type of the Custom Line Item.

Common use cases for custom line item creation include, but are not limited to the
following:

- Allocating Support fees
- Allocating shared service costs
- Applying managed service fees
- Applying tax
- Distributing credits
- Distributing RI and Savings Plans savings (as opposed to On-Demand)
- Adding organizational credits and discount line items
