# Managing email notifications for AWS Marketplace events

AWS Marketplace sends email notifications of updates to offers, agreements, subscriptions, products, security, billing and payments, and Private Marketplace. Independent software vendors
(ISVs), AWS Marketplace Channel Partners, and customers can receive email notifications. For examples and details of email notifications sent for offer and agreement updates, refer to [Event types](#event-types "#event-types").

AWS Marketplace sends email notifications to the email address associated with the [root user](../../../accounts/latest/reference/root-user.md "../../../accounts/latest/reference/root-user.md") of your
AWS account. To update the email address associated with your AWS account, refer to [Update the primary contact for your AWS account](../../../accounts/latest/reference/manage-acct-update-contact-primary.md "../../../accounts/latest/reference/manage-acct-update-contact-primary.md"). You can also [add custom email aliases](#adding-updating-email-addresses "#adding-updating-email-addresses") for notifications
and [unsubscribe recipients](#unsubscribe-notifications "#unsubscribe-notifications") from email
notifications.

###### Note

If you are missing AWS Marketplace emails, check your spam folder or adjust email settings. Email
notifications from AWS Marketplace are sent from `no-reply@marketplace.aws`. Providers such
as Google and Yahoo may filter these. For instructions, refer to [Prevent valid emails from going to Spam (Google)](https://support.google.com/mail/answer/1366858?sjid=4026678185875351798-NA#unmark_spam "https://support.google.com/mail/answer/1366858?sjid=4026678185875351798-NA#unmark_spam") or [Block and unblock email addresses in Yahoo
Mail](https://help.yahoo.com/kb/SLN28140.html "https://help.yahoo.com/kb/SLN28140.html").

###### Topics

- [Event types](#event-types "#event-types")
- [Field descriptions](#email-notification-field-descriptions "#email-notification-field-descriptions")
- [Manage notifications](#manage-notifications "#manage-notifications")

## Event types

The following event types are supported by email notifications for all products and pricing types, except for machine learning products.

### Offers

The following table shows the events for offers. An offer is a set of terms for a buyer's use of a product. For more information, refer to [Preparing a private offer for your AWS Marketplace product](private-offers-overview.md "private-offers-overview.md").

| Email                                 | Event                                                                                          | Recipient                              | Title                                                      | Fields                                                                                                                                                                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offer Published CP Notification CPPO  | Publication of AWS Marketplace Channel Partner private offer.                                  | Channel partner                        | AWS Marketplace Channel Partner private offer published    | Customer AWS account ID, ISV name, ISV AWS Account ID, Product name, Product ID, Offer ID, Opportunity ID, Offer published date, Offer expiration date                                                  |
| Offer Published ISV Notification CPPO | Publication of AWS Marketplace Channel Partner private offer.                                  | ISV                                    | AWS Marketplace Channel Partner private offer published    | Customer AWS account IDs, Channel partner, Channel partner AWS account ID, Product name, Product ID, Offer name, Offer ID, Opportunity ID, Offer published date, Offer expiration date, Wholesale price |
| OfferPubISVNotificationSCPO-1.0       | Seller publishes an AWS Marketplace Channel Partner private offer.                             | ISV or AWS Marketplace Channel Partner | Private offer published                                    | Customer AWS Account IDs, Product Name, Product ID, Offer Name, Offer ID, Offer Published Date, Offer Expiration Date, Total Contract Value                                                             |
| Reseller Opportunity Expired          | AWS Marketplace Channel Partner selling authorization expires.                                 | AWS Marketplace Channel Partner        | Offers: View expired selling authorization                 | ISV, Product Name, Product ID                                                                                                                                                                           |
| Reseller Opportunity Revoked          | ISV revokes AWS Marketplace Channel Partner selling authorization.                             | AWS Marketplace Channel Partner        | Offers: View deactivated selling authorization             | ISV, Product Name, Product ID                                                                                                                                                                           |
| Reseller Opportunity Created          | ISV creates a selling authorization or opportunity for the AWS Marketplace Channel<br>Partner. | AWS Marketplace Channel Partner        | Offers: Create private offer for new selling authorization | ISV, Product Name, Product ID, Selling authorization duration                                                                                                                                           |

### Agreements

ISVs and AWS Marketplace Channel Partners receive email notification when a buyer accepts a public offer, private offer, or a AWS Marketplace Channel Partner private offer. An agreement is created when an offer is accepted. Email notifications are also sent for agreement lifecycle events. These include agreement commencements, cancellations, replacements, and failures after buyer acceptance. The following table shows the emails that are sent for agreement events. Email notifications are currently available for select product types. Your specific product type may not have this feature yet.

| Email                                                              | Event                                                                                                                                    | Recipient                                                     | Title                                                               | Fields                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offer Accepted – private or public offer                           | AWS Marketplace customer accepts a public or private offer.                                                                              | ISV                                                           | Customer accepted an AWS Marketplace offer.                         | Customer company name, Customer AWS account ID, Product name, Product ID, Agreement ID, Agreement start date, Agreement end date, Agreement acceptance date, Purchase amount                                                                              |
| Offer Accepted – AWS Marketplace Channel Partner private offer.    | AWS Marketplace customer accepts an AWS Marketplace Channel Partner private offer.                                                       | ISV                                                           | Customer accepted an AWS Marketplace Channel Partner private offer. | Customer company name, Customer AWS account ID, Channel partner name, Channel partner AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date, Agreement acceptance date, Wholesale price  |
| Offer Accepted – AWS Marketplace Channel Partner private offer.    | AWS Marketplace customer accepts an AWS Marketplace Channel Partner private offer.                                                       | AWS Marketplace Channel Partner                               | Customer accepted an AWS Marketplace Channel Partner private offer. | Customer company name, Customer AWS account ID, ISV name, ISV AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date, Agreement acceptance date, Wholesale price, Margin, Purchase amount |
| Agreement Started – private offer                                  | An AWS Marketplace agreement for the contract or subscription product has started from a private offer with a future start date.         | ISV                                                           | An AWS Marketplace agreement has started                            | Customer AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date, Purchase amount                                                                                                          |
| Agreement Started – AWS Marketplace Channel Partner private offer  | An AWS Marketplace agreement for the contract or subscription product has started from an AWS Marketplace Channel Partner private offer. | ISV                                                           | An AWS Marketplace agreement has started.                           | Customer AWS account ID, Channel partner name, Channel partner AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date, Wholesale price                                                    |
| Agreement Started – Private offer                                  | Acceptance of an AWS Marketplace Channel Partner private offer starts the agreement for a contract or subsciption product.               | AWS Marketplace Channel Partner                               | An AWS Marketplace agreement has started.                           | Customer AWS account ID, ISV name, ISV AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date, Margin, Purchase amount                                                                    |
| Agreement Canceled – private or public Offer                       | Cancellation of a private or public offer agreement.                                                                                     | ISV                                                           | An AWS Marketplace agreement was cancelled.                         | Customer AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date                                                                                                                           |
| Agreement Canceled – AWS Marketplace Channel Partner private offer | Cancellation of an AWS Marketplace Channel Partner private offer agreement.                                                              | ISV                                                           | An AWS Marketplace agreement was cancelled.                         | Customer AWS account ID, Channel partner, Channel partner AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date                                                                          |
| Agreement Canceled – Channel Partner Private offer                 | Cancellation of an AWS Marketplace Channel Partner private offer agreement.                                                              | AWS Marketplace Channel Partner                               | An AWS Marketplace agreement was cancelled.                         | Customer AWS account ID, ISV, ISV AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID, Agreement start date, Agreement end date                                                                                                  |
| Compliance Failure – Seller of Record                              | An AWS Marketplace agreement fails because of a customer payment failure.                                                                | ISV or AWS Marketplace Channel Partner that created the offer | Action required: AWS Marketplace Agreement Creation Failure         | Subscribing AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID                                                                                                                                                                  |
| Payment Failure – Seller of Record                                 | An AWS Marketplace agreement fails because of a customer payment failure.                                                                | ISV or AWS Marketplace Channel Partner that created the offer | Payment failure for an AWS Marketplace agreement                    | Customer AWS account ID, Product name, Product ID, Offer name, Offer ID, Agreement ID                                                                                                                                                                     |
| Agreement Replaced – Private offer                                 | An AWS Marketplace agreement is replaced by another agreement.                                                                           | ISV                                                           | An AWS Marketplace agreement has been replaced                      | Company name, Customer AWS account ID, Product name, Product ID, Offer name, Offer ID, New agreement ID, Agreement start date, Agreement end date, New purchase amount                                                                                    |
| Agreement Replaced – Channel Partner Private offer                 | An AWS Marketplace agreement is replaced by another agreement.                                                                           | ISV                                                           | An AWS Marketplace agreement has been replaced                      | Company name, Customer AWS account ID, Channel partner, Channel partner AWS account ID, Product name, Product ID, Offer name, Offer ID, New agreement ID, Agreement start date, Agreement end date, Wholesale price                                       |
| Agreement Replaced – Channel Partner Private offer                 | An AWS Marketplace agreement is replaced by another agreement.                                                                           | AWS Marketplace Channel Partner                               | An AWS Marketplace agreement has been replaced                      | Company name, Customer AWS account ID, ISV name, ISV AWS account ID, Product name, Product ID, Offer name, Offer ID, New agreement ID, Agreement start date, Agreement end date, Wholesale price, Margin, New purchase amount                             |

### Disbursements

ISVs and Channel Partners receive an email notification if their disbursement is paused due to invalid bank account details.

| Email                                                  | Event                                                                               | Recipient                               | Title               | Fields       |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------- | --------------------------------------- | ------------------- | ------------ |
| Disbursement Paused – Invalid Bank Account Information | AWS Marketplace pauses disbursements to seller due to invalid bank account details. | ISV and AWS Marketplace Channel Partner | Disbursement Paused | Resource ARN |

The `Resource ARN` field shows the invalid bank account Amazon Resource Number (ARN). You can fix this issue by [adding the bank account](#add-bank-account-details "#add-bank-account-details") in the AWS Marketplace Management Portal (AMMP).

### Adding bank account details

Add bank account details in the AWS Marketplace Management Portal (AMMP) to fix invalid bank account ARN errors in disbursements.

The `Resource ARN` field displays the ARN of the invalid bank account. To fix the issue, add the bank account in the AWS Marketplace Management Portal. The following steps explain how.

###### To add bank account details

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") with your AWS Marketplace seller account.
2. On the menu bar, choose **Settings**.
3. Choose the **Payments information** tab.
4. In the **Bank accounts** section, choose **Add bank account**.
5. Add the bank account details and review them for accuracy. For more information, see [Step 3: Provide bank account information](provide-bank-information.md "provide-bank-information.md")
   earlier in this guide.
6. To receive payments from buyers, under **Disbursement methods**, choose **Add disbursement method**.
7. If prompted to verify Know Your Customer (KYC) and bank account, follow the verification steps.
8. Save your changes.

## Field descriptions

The following table shows descriptions of the fields referred to in the [Offers](#email-details-offers "#email-details-offers") and
[Agreements](#email-details-agreements "#email-details-agreements") tables.

| Field                          | Description                                                                                                                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer company name          | Name of the subscriber's company.                                                                                                                                                         |
| Customer AWS account ID        | ID of the AWS account subscribed to the product.                                                                                                                                          |
| ISV name                       | Seller business name.                                                                                                                                                                     |
| ISV AWS account ID             | ID of the seller's AWS account.                                                                                                                                                           |
| Product name                   | Title of the product.                                                                                                                                                                     |
| Product ID                     | Friendly, unique identifier for the software product.                                                                                                                                     |
| Offer name                     | Title of the offer.                                                                                                                                                                       |
| Offer ID                       | Identifier of the offer that the buyer signed.                                                                                                                                            |
| Offer visibility               | Whether the offer is a public, private, or an enterprise contract offer.                                                                                                                  |
| Agreement ID                   | A unique agreement data feed reference for the agreement signed between a proposer and an accepter to start using a product.                                                              |
| Agreement start date           | The date that the customer's product subscription starts, in the format `MM-DD-YYYY`. This date can be different than acceptance date for future dated agreements.                        |
| Agreement acceptance date      | The date when the customer subscribed to the product, in the format `MM-DD-YYYY`.                                                                                                         |
| Agreement end date             | The date when the contract expires, formatted in the format `MM-DD-YYYY`. For metered or pay-as-you-go subscriptions, this date is set to `JAN-1-9999`.                                   |
| Agreement end date             | The date when the contract expires, formatted in the format `MM-DD-YYYY`. For metered or pay-as-you-go subscriptions, this date is set to `JAN-1-9999`.                                   |
| Purchase amount                | The estimated cost of the agreement, otherwise known as total contract value. This applies to SaaS, professional services, and server product types and contract or annual pricing types. |
| Channel partner company name   | Name of the account that purchased a product or service at wholesale cost from an ISV to resell to a customer.                                                                            |
| Channel partner AWS account ID | ID of the AWS account of the AWS Marketplace Channel Partner that purchased a product or service from an ISV to resell to a customer.                                                     |
| Wholesale price                | The wholesale cost from an ISV to resell a product to the AWS Marketplace Channel Partner.                                                                                                |
| Currency code                  | The offer pricing currency associated with the estimated cost of the agreement.                                                                                                           |
| New agreement ID               | Agreement ID of a renewed or upgraded agreement.                                                                                                                                          |
| Offer published date           | Date when the seller published the offer.                                                                                                                                                 |
| Offer expiration date          | Date when the offer expires.                                                                                                                                                              |
| Opportunity ID                 | Unique identifier for a registered opportunity.                                                                                                                                           |
| Selling authorization duration | The length of time resellers are authorized to create offers using discounts, as specified in the selling authorization.                                                                  |

## Manage notifications

The following topics explain how to manage email notifications for events.

### Adding or updating email addresses

You can add up to 10 email addresses for custom email notifications using the
AWS Marketplace Management Portal.

###### To add or update email addresses

1. Sign in to the [AWS Marketplace Management Portal.](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/")
2. From **Settings**, choose the **Notifications**
   tab.
3. Under **Email for custom notifications**, choose **Add
   email address**.
4. For **Recipient details,** enter a custom email address in the
   **Email address** field.
5. (Optional) Choose **Add new recipients** to add another email
   address (up to 10 total).
6. Choose **Submit**.

### Unsubscribing recipients from

notifications

You can remove an email address so the recipient is unsubscribed from custom email
notifications.

###### To unsubscribe recipients from event notifications

1. Sign in to the [AWS Marketplace Management Portal.](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/")
2. From **Settings** choose the **Notifications**
   tab.
3. Under **Email for custom notifications**, choose **Update
   email address**.
4. For **Recipient details**, choose **Remove** to
   remove the email address.
5. Choose **Submit**.

###### Note

You can also unsubscribe using the link in the email.
