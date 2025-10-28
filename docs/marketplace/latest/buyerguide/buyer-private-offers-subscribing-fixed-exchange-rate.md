# Pay for private offers in multiple currencies

Private offers support multiple currencies: USD, EUR, GBP, AUD, and JPY. You can receive private offers in your preferred currency, eliminating foreign exchange variability for predictable invoicing.

## Multi-currency private offers

Private offers handle currency-specific invoicing and exchange rates differently based on the pricing model:

- **Contract pricing** - Fixed exchange rate locked for the entire contract duration
- **Contract with consumption** - Fixed rate for contract portion, monthly refresh for consumption charges
- **Pay-as-you-go (PAYG)** - Monthly refresh of exchange rates

## Pay for a USD private offer in non-USD

currency

If you receive a private offer in USD currency and your payment method is a non-USD
currency, the conversion rate used is the current rate on date of the invoice. Depending on
the private offer, the date of the invoice can be the private offer acceptance date or a later
date. For example, for a contract-based private offer with no payment schedule, the invoice
date is the offer acceptance date. For a private offer with a payment schedule, the invoice
dates are the dates the installments are scheduled to be invoiced.

## Pay for a non-USD private offer

All AWS pricing remains in USD today. However, you can receive a private offer in four
other currencies: EUR, GBP, AUD, and JPY, with no foreign exchange variability. Sellers can
extend a private offer with contract pricing in your preferred payment currency. You will be
able to view and accept the private offer in your preferred currency, so you know how much you
will be paying without having to deal with foreign exchange variability.

At offer acceptance, AWS will convert the agreed-upon non-USD pricing to USD pricing and
lock the foreign exchange rate for the entirety of the subscription. Post-offer acceptance,
your invoices will display both USD pricing, the fixed foreign exchange rate at the time of
offer acceptance, and the non-USD pricing currency. In a scenario where you have moved to a
new location where your invoices are generated from a different AWS Marketplace operator, your existing
fixed foreign exchange offers will be canceled. Contact the sellers to re-issue a new offer in
the currency you would like to pay. It's important to note that in rare cases, your charged
amount in non-USD will have slight rounding differences due to foreign exchange
conversion.

For contract with consumption pricing (CCP) and pay-as-you-go (PAYG) offers, exchange rate handling varies:

- **Contract with consumption pricing (CCP)** - The contract portion maintains a fixed exchange rate for the duration, while consumption charges beyond the contract use monthly updated exchange rates.
- **Pay-as-you-go (PAYG)** - Exchange rates are updated monthly to maintain consistent local currency pricing for all usage-based charges.

## Pay for consumption-based charges

For consumption-based charges in multi-currency private offers, billing depends on the pricing model. Contract with consumption pricing (CCP) offers maintain the contract currency for consumption charges, with exchange rates updated monthly. Pay-as-you-go (PAYG) offers use monthly updated exchange rates to maintain consistent local currency pricing. An example of consumption-based charges is additional usage outside of what is included in the contract. For more information, see [Paying for products in AWS Marketplace](buyer-paying-for-products.md#payment-methods "buyer-paying-for-products.md#payment-methods").
