# Capacity Blocks pricing and billing

With Amazon EC2 Capacity Blocks for ML, you pay only for what you reserve. The price of a Capacity Block depends
on available supply and demand for Capacity Blocks at the time of purchase. You can view the
price of a Capacity Block offering before you reserve it. The price of the Capacity Block is charged
up front at the time the reservation is made. When you search for a Capacity Block across a
range of dates, we return the lowest-priced Capacity Block offering available. After you've
reserved a Capacity Block, the price doesn't change.

When you use a Capacity Block, you pay for the operating system you use when your instances
are running. For more information about operating system prices, see [Amazon EC2 Capacity Blocks for ML
Pricing](https://aws.amazon.com/ec2/capacityblocks/pricing/ "https://aws.amazon.com/ec2/capacityblocks/pricing/").

## Billing

The price of a Capacity Block offering is charged up front. Payment is billed to your
AWS account within 5 minutes to 12 hours after you purchase a Capacity Block. While your
payment is processing, your Capacity Block reservation resource remains in a state of
`payment-pending`. If your payment can't be processed at least 5
minutes before your block start time, or within 12 hours (whichever comes first),
your Capacity Block is released and the reservation state changes to
`payment-failed`.

After your payment is processed successfully, the Capacity Block resource state changes
from `payment-pending` to `scheduled`. You receive an invoice
that reflects the one-time upfront payment. In the invoice, you can associate the
paid amount with the Capacity Block reservation ID.

When your Capacity Block reservation begins, you are billed based only on the operating
system you use while your instances are running in the reservation. You can view
your usage and associated charges in your anniversary bill for the month of usage in
your AWS Cost and Usage Report.

###### Note

Savings Plans and Reserved Instance discounts don't apply to Capacity Blocks.

###### Viewing your bill

You can view your bill in the AWS Billing and Cost Management console. The upfront payment for your
Capacity Block appears in the month that you purchased the reservation.

After your reservation begins, your bill shows separate lines for the block
reservation used and unused time. You can use these line items to see how much time
was used in your reservation. You will see only a usage charge in the line for used
time if you use a premium operating system. For more information, see [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md "capacity-blocks-pricing-billing.md"). There is no additional charge
for unused time.

For more information, see [Viewing your
bill](../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md "../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md") in the _AWS Billing and Cost Management User Guide_.

If your Capacity Block starts in a different month then the month you purchased your
reservation, the upfront price and reservation usage show up under separate billing
months. In your AWS Cost and Usage Report, the Capacity Block reservation ID is listed in the
**reservation/ReservationARN** line item of your upfront fee and the **lineitem/ResourceID**
in your anniversary bill so that you can associate the usage to the corresponding
upfront price.
