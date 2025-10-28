# Managing AWS Marketplace resale authorizations

As an ISV, you can authorize an AWS Channel Partner to resell your products by creating a resale authorization directly within Salesforce using the AWS Partner CRM Connector.
The connector allows you to specify a fixed rate per product dimension, which creates a wholesale price for the AWS Channel Partner.
The Channel Partner can then mark up the wholesale price when creating private offers for buyers. The connector enables you to manage the entire lifecycle of resale authorizations,
from creation and modification to deactivation and cloning, so you can handle all aspects of your channel partner relationships without leaving Salesforce.

###### Topics

- [Using the Resale authorization tab](#crm-resale-auth-tab "#crm-resale-auth-tab")
- [Creating an AWS Marketplace resale authorization](#crm-resale-auth-creation-steps "#crm-resale-auth-creation-steps")
- [Required fields for resale authorizations](#crm-required-resale-fields "#crm-required-resale-fields")
- [Deactivating a resale authorization](#crm-deactivate-resale-auth "#crm-deactivate-resale-auth")
- [Cloning resale authorizations](#crm-clone-resale-auth "#crm-clone-resale-auth")
- [Viewing and refreshing resale authorization status](#crm-view-refresh-auth-status "#crm-view-refresh-auth-status")

## Using the Resale authorization tab

You use the **Resale authorization** tab in the AWS Partner CRM connector to create and manage resale authorizations.

###### To start the tab

1. Sign in to your Salesforce organization as an AWS Marketplace user.
2. Choose **App launcher**, then search for and select **AWS Partner CRM connector**.
3. Choose the **Resale authorization** tab.

## Creating an AWS Marketplace resale authorization

###### Note

When creating a resale authorization, dynamic fields will appear based on your chosen
product, and the selections you make during the creation process.

The following steps explain how to create an AWS Marketplace resale authorization You have the option of creating a flexible payment schedule and a future dated agreement
based on the type of product selected. You can create a resale authorization and publish it to a channel partner, or save an authorization as a draft without releasing it.

1. On the **Resale Authorizations**
   tab, choose **New**.
2. On the **Create a Resale Authorization** page, complete the required fields.
3. (Optional) Create a flexible payment schedule
   1. In the **Product and
      Buyers** section, choose
      **Enable fixed units and allow
      buyers to pay for this product in installments**.
   2. Configure payments in the **Payment Schedule** section.

4. Choose **Create resale authorizations** to publish the offer to the channel partner.

—OR—

Choose **Save as draft** to complete the offer later without releasing it to the channel partner.

## Required fields for resale authorizations

You must complete the following fields and any options as listed here.

**Products and buyers**

**Products** — Choose from the list
of available products synched through the CRM connector.

**Buyer Accounts**

A comma-separated list of target buyer accounts for offer.

**Resale Authorization Details**

**Resale Authorization Name** – Enter a name

**Description** – Enter a description (viewable by the AWS Channel Partner)

**Reseller Account** – Enter the 12-digit AWS account number of the reseller.

**Resale Authorization Name**

Enter a name.

**Description**

Enter a description (viewable by the AWS Channel Partner).

**Reseller Account**

Enter the 12-digit AWS account number of the reseller.

**Contract duration (if applicable)**

**Standard**

**Custom Duration** – When you choose this option, enter **Custom Service Length**.

**Product pricing (if applicable)**

- Choices include **Usage model** or **Contract model**.
- For **Contract model**, you can enable FPS in the **Buyers and Products** section.

**Legal terms**

- Choose **Standard Contract for AWS
  Marketplace** or **Custom EULA for
  End User License Agreement** for the buyer.
- Optionally, choose **Reseller Contract for
  AWS Marketplace** or **Custom
  Contract for Reseller Agreement**.
- For **Custom EULA (Buyer)** and
  **Custom Contract (Reseller)**,
  ensure that you have configured the Amazon Simple Storage Service bucket for the
  seller account to store the custom EULA.

**Product dimensions**

Add or update offer rates and units to the chosen dimensions.

Choose **I want to enable zero-dollar pricing** to create a resale authorization in which any of the dimension rates are set to **$0**.

**Resale Authorization Duration**

Choose **Duration Type** and provide
details for the **Resale Authorization Expiration Date** as required.

**Renewals**

For **Is this offer intended to renew an existing paid subscription with an existing customer for the same underlying product?**, choose **Yes** or **No**, and enter the required details.

## Deactivating a resale authorization

1. On the **Resale Authorizations**
   tab, choose **New**
2. Under **Resale Authorization Name**, choose the name of the authorization that you want to deactivate.
3. Choose **Deactivate Resale Authorization**.
4. Choose **Refresh Resale Authorization
   Status**.

The authorization status changes to **Restricted** when the deactivation succeeds.

## Cloning resale authorizations

You clone a resale authorization when you need to change the details of an existing authorization. For example, you clone an authorization
when you need to provide a different EULA to a partner.

###### To clone a resale authorization

1. From the **Resale Authorizations**
   tab, choose **New**
2. From the list of resale authorizations, choose the
   **Resale Authorization Name**.
3. Choose **Clone Resale
   Authorization**
4. Review and edit the **Resale Authorization
   Details** section of the cloned authorization. If you use
   a custom EULA or a custom contract (reseller agreement) in the
   cloned authorization, you must re-upload the legal terms.
5. Choose **Create Resale
   Authorization**.

## Viewing and refreshing resale authorization status

1. On the **Resale Authorizations**
   tab, choose **New**
2. From the **Resale Authorizations**
   list, choose the **Resale Authorization Name**.
3. Choose **Refresh Resale Authorization
   Status**.
4. Choose **Proceed**.
5. Repeat steps 5 and 6 until the resale authorization status changes to
   **SUCCEEDED**.

Allow a 30 seconds before choosing the **Refresh Resale Authorization Status** button again. This ensures that each refresh request is fully processed
and preserves data integrity by preventing potential record duplication.
