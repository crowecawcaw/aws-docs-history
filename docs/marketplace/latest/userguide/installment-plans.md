# Private offer installment plans

As an AWS Marketplace seller, you can use installment plans—also known as _flexible
payment schedules_—to extend private offers with a custom payment schedule.
Installment plans are available for private offers on certain product and pricing types. For
more information, see [Product types eligible for private offers](../buyerguide/buyer-private-offers.md#buyer-private-offers-types "../buyerguide/buyer-private-offers.md#buyer-private-offers-types"). The payment schedule can be spread over
the accepted contract duration, with the buyer making payments in regular installments.

For multiyear and custom-duration Amazon Machine Image (AMI) products, set the number of instances for each instance type included in the offer and the hourly pricing for any additional launched instances.
After the buyer launches the specified number of instances, any additional instances launched are charged at the hourly rate specified in the private offer.

You can't modify the payment schedule on a private offer that has been extended to and subscribed by a buyer. To change an accepted offer, you must [create a new offer](creating-private-offer.md "creating-private-offer.md").

## Creating an installment plan for a private offer

When creating a private offer, you can set a custom payment schedule with an installment plan.

###### To create an installment plan for a private offer

1. Create a private offer for your product. Follow the steps in [Drafting and publishing the private
   offer](creating-private-offer.md#drafting-and-publishing-private-offer "creating-private-offer.md#drafting-and-publishing-private-offer") earlier in this section.
2. On the **Configure offer pricing and duration** page, for **Product pricing**, choose **Contract pricing with installment plan**.
3. Choose the contract duration for this offer and specify the offer details. For more information, see [Preparing a private offer for your AWS Marketplace product](private-offers-overview.md "private-offers-overview.md").
4. Under **Buyer installment plan**, enter the following parameters:
   - **Contract total**
   - (Optional) If you want the first payment to be different from the others, enter an **Initial payment**. The remaining balance will be divided equally among subsequent payments.
   - **Frequency**

   Choose **Monthly**, **Quarterly**, **Annually**, or **Custom**. If you choose **Custom**, also enter the **Number of installments**.

   You can add up to 60 payments. You also have the option to make adjustments to each payment line item. Each time you adjust a payment line item, the **Total amount due from buyer** is updated.
   - **First invoice date**

5. Choose **Generate installment plan**. You will receive an error message if an invoice date falls outside the duration of the contract.
6. After you verify all invoice amounts and dates, confirm that the **Total amount due from buyer** matches the total price that you want your buyer to pay over the course of the private offer. To finish creating the private offer, complete the remaining steps in [Drafting and publishing the private
   offer](creating-private-offer.md#drafting-and-publishing-private-offer "creating-private-offer.md#drafting-and-publishing-private-offer").

After the buyer has accepted the private offer, they will be invoiced at 00:00 UTC on the invoice dates that you defined in the payment schedule. You receive the payment for each invoice after AWS Marketplace receives the payment from the buyer. Only one invoice date can occur before the offer acceptance date. If the private offer is accepted after the first invoice date in the payment schedule, the first invoice will be generated immediately after the offer is accepted. After your buyers are subscribed, they can see all the payments on the schedule and on their AWS invoice, helping them track their spending.

## Installment plan reporting

Reporting for private offers with installment plans appears in section 4 of the monthly billed revenue report. For more information, refer to [Section 4: Contracts with
flexible payment schedule](monthly-billed-revenue-report.md#section-4-contracts-with-flexible-payments "monthly-billed-revenue-report.md#section-4-contracts-with-flexible-payments").
