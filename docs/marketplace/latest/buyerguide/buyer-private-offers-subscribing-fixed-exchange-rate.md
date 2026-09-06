

# Pay for private offers in multiple currencies
<a name="buyer-private-offers-subscribing-fixed-exchange-rate"></a>

Private offers support multiple currencies: USD, EUR, GBP, AUD, JPY, and INR. You can receive private offers in your preferred currency, eliminating foreign exchange variability for predictable invoicing.

**Buyers in India**  
Buyers in India receive private offers in Indian Rupee (INR) or US Dollar (USD) from sellers in India. For detailed information, see [Buyers in India FAQ](india-buyer-faq.md).

## Multi-currency private offers
<a name="multi-currency-private-offers"></a>

Private offers handle currency-specific invoicing and exchange rates differently based on the pricing model:
+ **Contract pricing** - Fixed exchange rate locked for the entire contract duration
+ **Contract with consumption** - Fixed rate for contract portion, monthly refresh for consumption charges
+ **Pay-as-you-go (PAYG)** - Monthly refresh of exchange rates

## Pay for a USD private offer in non-USD currency
<a name="usd-offer-in-non-usd-currency"></a>

If you receive a private offer in USD currency and your payment method is a non-USD currency, the conversion rate used is the current rate on date of the invoice. Depending on the private offer, the date of the invoice can be the private offer acceptance date or a later date. For example, for a contract-based private offer with no payment schedule, the invoice date is the offer acceptance date. For a private offer with a payment schedule, the invoice dates are the dates the installments are scheduled to be invoiced.

## Non-USD priced private offers
<a name="non-usd-private-offer"></a>

All AWS pricing remains in USD. However, you can receive a private offer in EUR, GBP, AUD, JPY, and INR (for buyers and sellers in India only) with no foreign exchange (FX) variability.

### Contracts only pricing offers
<a name="contracts-only-pricing-offers"></a>

1. Sellers can extend a private offer with contract pricing in your preferred payment currency. You can view and accept the private offer in your preferred currency, so you know how much you will pay without dealing with FX variability.

1. At offer acceptance, AWS converts the agreed-upon non-USD pricing to USD pricing and locks the FX rate for the entirety of the subscription. After offer acceptance, your invoices display both USD pricing, the fixed FX rate at the time of offer acceptance, and the non-USD pricing currency.

1. If you move to a new location where your invoices are generated from a different AWS Marketplace operator, your existing fixed FX offers are canceled. Contact the sellers to reissue a new offer in the currency you want to pay.

1. In rare cases, your charged amount in non-USD might have slight rounding differences due to FX conversion.

### Contracts with consumption pricing and pay-as-you-go pricing offers
<a name="contracts-with-consumption-and-payg-offers"></a>

For contracts with consumption pricing (CCP) and pay-as-you-go (PAYG) offers, exchange rate handling varies:
+ **Contract with consumption pricing (CCP)** – The contract portion maintains a fixed FX rate for the duration of the contract. The consumption charges beyond the contract appear on anniversary invoices. These invoices are separate from other consumption pricing products priced in USD. These invoices show USD pricing and a variable FX rate, but your non-USD unit price remains constant.
+ **Pay-as-you-go (PAYG) or usage-based pricing** – The PAYG or usage-based charges appear on anniversary invoices. These invoices are separate from other usage-based products priced in USD. These invoices show USD pricing and a variable FX rate, but your non-USD unit price remains constant.

For more information, see [Payment methods](buyer-paying-for-products.md#payment-methods).

**Important Note on Cost and Usage Reports (CUR)**  
When you purchase a Private Offer in a non-USD currency (EUR, GBP, JPY, AUD), please be aware that your AWS Cost and Usage Reports (CUR) will display all usage and costs in USD only. This is intended behavior, as CUR reports currently support pricing in USD only.  
While your invoices will reflect the original currency of your Private Offer with the locked exchange rate, the CUR data will show USD-converted amounts. For accurate financial reconciliation in your original offer currency, please refer to your invoices rather than relying solely on CUR reports.