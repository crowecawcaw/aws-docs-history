# Setting up your India billing

If you sign up for a new account and choose India for your contact and billing address,
your user agreement is with Amazon Web Services India Private Limited (AWS India), a local AWS seller in India. AWS India
manages your billing, and your invoice total is listed in rupees instead of dollars.

###### Contents

- [Signing up for AWS India](manage-account-payment-aispl.md#aisplsignup "manage-account-payment-aispl.md#aisplsignup")
- [Managing your AWS India account](manage-account-payment-aispl.md#manage-aispl-account "manage-account-payment-aispl.md#manage-aispl-account")
  - [Adding or editing a Permanent Account Number](manage-account-payment-aispl.md#aispl-add-pan "manage-account-payment-aispl.md#aispl-add-pan")
  - [Editing multiple Permanent Account Numbers](manage-account-payment-aispl.md#aispl-edit-pan "manage-account-payment-aispl.md#aispl-edit-pan")
  - [Editing multiple Goods and Services Tax
    numbers](manage-account-payment-aispl.md#aispl-edit-gst "manage-account-payment-aispl.md#aispl-edit-gst")
  - [Viewing a tax invoice](manage-account-payment-aispl.md#aispl-view-tax "manage-account-payment-aispl.md#aispl-view-tax")

- [Changing the seller of record to or from
  AWS India](manage-account-payment-aispl.md#aispl-edit-SOR "manage-account-payment-aispl.md#aispl-edit-SOR")

## Signing up for AWS India

AWS India is a local seller of AWS in India. To sign up for an AWS India account, see
[Manage accounts in India](../../../accounts/latest/reference/managing-accounts-india.md "../../../accounts/latest/reference/managing-accounts-india.md") in the _AWS Account Management
Reference Guide_.

## Managing your AWS India account

Use the [Account Settings](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") page to perform the
following tasks:

- Creating and editing your customer verification
- Manage customer verification
- Editing your username, password, or email address
- Add, update, or remote alternate contacts
- Editing your contact information

For more information about these tasks, see [Managing your AWS India account](../../../accounts/latest/reference/managing-accounts-india.md#manage-aispl-account "../../../accounts/latest/reference/managing-accounts-india.md#manage-aispl-account") in the
_AWS Account Management Reference Guide_.

Use the [Tax Settings](https://console.aws.amazon.com/billing/home#/tax "https://console.aws.amazon.com/billing/home#/tax") page of the Billing and Cost Management console to
perform the following tasks:

- [Adding or editing a Permanent Account Number](#aispl-add-pan "#aispl-add-pan")
- [Editing multiple Permanent Account Numbers](#aispl-edit-pan "#aispl-edit-pan")
- [Editing multiple Goods and Services Tax
  numbers](#aispl-edit-gst "#aispl-edit-gst")
- [Viewing a tax invoice](#aispl-view-tax "#aispl-view-tax")

### Adding or editing a Permanent Account Number

You can add your Permanent Account Number (PAN) to your account and edit it.

###### To add or edit a PAN

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Tax Settings**.
3. On the **Tax Settings** navigation bar, choose
   **Edit**.
4. For **Permanent Account Number (PAN)**, enter your PAN,
   and then choose **Update**.

### Editing multiple Permanent Account Numbers

You can edit multiple Permanent Account Numbers (PANs) in your account.

###### To edit multiple PAN numbers

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Tax Settings**.
3. Under **Manage Tax Registration Numbers**, select the PAN
   numbers that you want to edit.
4. For **Manage Tax Registration**, choose
   **Edit**.
5. Update the fields that you want to change, and then choose
   **Update**.

### Editing multiple Goods and Services Tax

numbers

You can edit multiple Goods and Services Tax numbers (GSTs) in your account.

###### To edit multiple GST numbers

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Tax Settings**.
3. Under **Manage Tax Registration Numbers**, select the GST
   numbers that you want to edit or choose **Edit
   all**.
4. For **Manage Tax Registration**, choose
   **Edit**.
5. Update the fields that you want to change and choose
   **Update**.

### Viewing a tax invoice

You can view your tax invoices in the console.

###### To view a tax invoice

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Bills**.
3. Scroll down and choose the **Invoices** tab.
4. On the **Tax invoices** section, choose an invoice link
   that is mentioned under **Document ID**.

###### Note

The **Tax invoices** section only appears if there are tax
invoices available.

## Changing the seller of record to or from

AWS India

You can change your AWS account seller of record (SOR) of your AWS account to another SOR by updating your billing or tax information. This does not apply if your AWS India account is operating in the legacy model where the functionality isn't available. When you edit your country or region in your AWS account billing or tax details,
the SOR for your account will automatically change if the service provider of the new location is
different from your current location.

If you're changing your account to or from AWS India, you do not need to update your
default payment method if it is set to invoice or wire transfer. If your default payment
method is credit or debit card, you are required to reconfirm your default payment card
details. This is to ensure the payment method is stored separately from the transactions
outside of AWS India. For more information, see [Viewing eligible credit or debit cards for AWS India invoices](edit-aispl-payment-method.md#aispl-payment-view "edit-aispl-payment-method.md#aispl-payment-view").

###### Note

If you have an AWS India account with a credit or debit card as your default payment
method and you have e-mandate set up for automatic payments, you must deactivate the
e-mandate before you can edit your default payment preferences.

To change the SOR of your AWS account, you can edit this information using the
following options:

To change the SOR using billing information

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Payment
   preferences**.
3. In the **Default payment preferences** section,
   choose **Edit**.
4. Enter the new billing address.
5. In the **Payment currency** section, choose a
   default currency from the list of accepted currencies of your new
   SOR.
6. (If your default payment method is credit or debit card) Under the
   **Confirm payment method** section, reenter the
   details of your default payment card to confirm usage under the new
   service provider.

To change default cards under the new SOR, add your card at a
later time and change your default payment method setting. 7. Choose **Save changes**.

After a few minutes, your changes including the updated SOR appears on the
**Payment preferences** page.

To change the SOR using billing and tax information
To move your account to a different SOR, you must update the tax
registration number (TRN) associated with the account and provide a new,
valid TRN. You can also delete the TRN associated with the account. The new
SOR of your account automatically resolves based on the country of your new
tax address, and your current billing address, in order of availability and
priority. When your account’s SOR changes, you will receive a notification
that your account is moving in or out of AWS India.

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Tax
   Settings**.
3. Select your account and choose **Manage tax
   registration**, then choose either
   **Edit**, **Edit all**, or
   **Delete TRN**.
4. (If your default payment method is credit or debit card) On the
   navigation pane, choose **Payment
   preferences**.
5. Choose **Add payment method** to reenter the
   details of your default payment card, or add a new payment
   card.
6. After the card is saved, choose **Set as
   default**.

The **Default payment preferences** section alerts you
that your previous default payment method is not eligible for use in the new
SOR. Refresh the page after you add your payment card for this alert to
disappear.

If you're unable to change the SOR using the preceding procedures, your account is likely operating in the legacy model where the functionality isn't available. We are currently migrating AWS India account from the legacy to the new model where the functionality is available. The expected completion date is December 2025.
