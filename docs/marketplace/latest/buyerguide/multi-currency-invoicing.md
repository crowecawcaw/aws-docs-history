# Multi-currency invoicing and payment considerations

When working with private offers in multiple currencies, several payment and invoicing considerations apply:

- As an AWS customer, you can select a currency as your preferred currency for AWS Marketplace invoices that are priced in USD. This preference is based on your location. For more information about supported currencies, see [Supported currencies](buyer-paying-for-products.md#supported-currencies "buyer-paying-for-products.md#supported-currencies").
- You can use payment profiles to manage payment methods when receiving invoices from multiple AWS service providers (seller of record). You can create payment profiles configured for each AWS service provider, specifying the currency and preferred payment method. For more information, see [Managing your payment profiles](../../../awsaccountbilling/latest/aboutv2/manage-paymentprofiles.md "../../../awsaccountbilling/latest/aboutv2/manage-paymentprofiles.md") in the _AWS Billing User Guide_.
- If you purchase a private offer that is priced in non-USD currency, that invoice will override both your preferred currency and the currency in payment profiles. An invoice will be generated in the offer currency.

###### Important

Check with your finance, accounting, and operations teams in your organization regarding these different payment and currency constructs before accepting a private offer from AWS Marketplace.
