# Managing disbursements

After completing your initial disbursement setup during registration, you can manage your disbursement preferences, add multiple currencies, and monitor your payment history. For initial setup instructions, see [Set disbursement preferences](set-disbursement-preferences.md "set-disbursement-preferences.md").

## Modifying disbursement methods

You can update your existing disbursement methods or add new ones at any time:

###### To modify disbursement methods

1. Sign in to the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") and choose **Settings**.
2. Select the **Payment information** tab.
3. In the **Disbursement methods** section, choose **Add disbursement method** to create a new method, or select an existing method and choose **Edit**.
4. Update your currency, bank account, or schedule preferences as needed.
5. Choose **Save** or **Add disbursement method**.

## Currency restrictions and available currencies

AWS Marketplace supports disbursements in multiple currencies, but certain restrictions apply based on your bank account type:

- **US-based ACH accounts and Hyperwallet accounts** – Can only receive payments in USD
- **SWIFT bank accounts** – Required for non-USD disbursements and optional for USD
- **Multiple currencies** – Can be assigned to a single bank account where supported

Available currencies for disbursements include:

- United States dollar (USD)
- Euro (EUR)
- Great Britain pound (GBP)
- Australian dollar (AUD)
- Japanese yen (JPY)

## Disbursement timing and processing

AWS disburses payments using the following schedule:

- **Daily disbursements** – Occur when funds become available. You must have a positive balance to receive disbursements.
- **Monthly disbursements** – Occur on the day of the month you specify (1-28).

Payment processing details:

- Payments take approximately 1-2 business days to arrive in your bank account following the disbursement date
- Funds are disbursed only after they are collected from the customer
- The disbursement dashboard is updated 3-5 days after the disbursement
- AWS disburses payments using Automated Clearing House (ACH) transfer or SWIFT transfer

## Disbursement management options

AWS Marketplace provides several options for managing your disbursements:

- **Multiple disbursement methods** – You can set up different disbursement methods for different currencies
- **Schedule adjustments** – Change between daily and monthly disbursements, or adjust the day of the month for monthly disbursements
- **Currency management** – Add or remove currencies and assign them to appropriate bank accounts
- **Disbursement thresholds** – Set minimum amounts that must accumulate before payments are disbursed

## Best practices for managing disbursements

Consider these best practices when managing your disbursement preferences:

- Choose disbursement schedules that align with your business's cash flow needs.
- Set appropriate threshold amounts to minimize transaction fees. For international wire transfers, consider setting higher thresholds to offset wire transfer fees.
- If you expect high sales volume, more frequent disbursements may be beneficial.
- If you expect lower sales volume, less frequent disbursements with higher thresholds may be more cost-effective.
- Review your disbursement history regularly to ensure payments are being processed as expected.
- Keep your bank account information up to date to avoid payment delays.

## Multi-currency disbursement details

When you create a private offer, you must configure appropriate disbursement preferences and banking arrangements for each currency you plan to support.

### Bank account requirements

Before creating offers in non-USD currencies, you must:

- Set up a bank account that can receive disbursements in the target currency
- Configure disbursement preferences for each currency in your seller account
- Ensure your bank supports SWIFT transfers for international currencies

###### Important

Currency selection is only available if you have configured disbursement preferences for that currency. You must set up the appropriate bank account before creating offers in non-USD currencies.

### Disbursement process for multi-currency offers

Disbursements for multi-currency private offers work as follows:

- You receive disbursements in the same currency as the private offer
- Listing fees are deducted in the offer currency
- Disbursement timing may vary depending on the currency and banking requirements
- For channel partner offers, both the ISV and channel partner receive disbursements in the offer currency
