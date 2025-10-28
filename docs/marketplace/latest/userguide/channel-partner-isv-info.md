# Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV

As an independent software vendor (ISV), you can authorize AWS Marketplace Channel Partners to resell your products by creating a selling authorization for that partner. The Channel Partner can use the selling authorization to create Channel Partner Private Offer (CPPO) to the end buyer. Supported product types include:

- AMI-based products
- Container-based products
- SaaS-based products
- Professional services products
  The following procedure outlines how ISVs can create a selling authorization for an AWS Marketplace Channel Partner. To use this feature, you must have permissions to use the **Selling authorizations** tab in the AWS Marketplace Management Portal. For more information, see [Policies for AWS Marketplace sellers](detailed-management-portal-permissions.md#seller-managed-policies "detailed-management-portal-permissions.md#seller-managed-policies").

## Create a selling authorization

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") with your AWS Marketplace Seller account.

###### Tip

Ensure that you are signed out from another AWS account before signing in with your AWS Marketplace Seller account. 2. Choose the **Selling authorizations** tab, and then choose **Create selling authorization**. 3. On the **Create selling authorization** page, enter the following details:

    * For **Selling authorization name**, enter a name for the authorization.


    ###### Note

    The information you enter in **Selling authorization name** will be visible to channel partners in their seller reports.
    * For **Reseller**, choose the AWS Marketplace Channel Partner (reseller) that you want to authorize from the dropdown list. You can select resellers by name or account ID.
    * For **Product type**, select the type of product, and then select one of your **Products** for which you want to create selling authorization.
    * Choose **Continue to authorization details**.

4.  On the **Specify details** page, enter the following details:
    - For **Selling authorization description**, enter a description.

    ###### Note

    The information you enter in **Selling authorization description** will be visible to channel partners in their seller reports.
    - For **Renewal**, indicate whether this authorization is intended to renew an existing paid subscription with an existing customer for the same product.
    - (Optional) Set one or more **Buyer account IDs** to specify that the selling authorization is only for those buyers.
    - You can choose **Save and exit** or choose **Next**. Choosing **Save and exit** at any step in the process will save your selling authorization as draft. Choosing **Next** takes you to the **Select duration and pricing** page.

5.  On the **Select duration and pricing** page, enter the following details:
    - For **Pricing model**, choose one of the following options:
      - **Contract pricing with installment plan** - You specify a fixed quantity for each dimension type, an hourly rate for overages, and an installment plan. Overages are charged at the hourly rate and billed separately.
      - **Contract pricing with upfront payments** - You specify a contract price for each dimension type and an hourly rate for additional usage. Buyers have the option to select the quantity to commit at the contract price for each dimension type and get invoiced for the full amount upon acceptance. Additional usage is charged at the hourly rate and billed separately.
      - **Usage pricing** - You specify hourly rate for each dimension type. Buyers are charged based on the hourly rate for their usage.

    - For **Currency**, choose the currency for the selling authorization.

    ###### Important

    Non-USD currencies are available for contract, contract with consumption, and pay-as-you-go pricing offers. Channel partners must create offers in the same currency as the resale authorization.

        + **Channel Partner Private Offers (CPPOs):** ISVs and channel partners will receive disbursements in the same currency, as agreed upon during CPPO creation.
        + **Currency restrictions:** CPPOs can only be created in the currency set in the resale authorization. If a channel partner wants to extend a CPPO in a different currency, they need to reach out to the ISV to ensure a resale authorization is issued in the new currency.
        + **Agreement Based Offers (ABO):** ABO will support changing the currency of the offer, as long as the seller and channel partner have configured the currency in their disbursement preferences.

    - For **Duration**, select the duration of the selling authorization.

    ###### Note

    The start date for resellers must be earlier than the date that the manufacturer has listed in the resale authorization.
    - The **Product Dimension** section shows you currently available contract dimensions in the product. You can choose the dimensions you want to include in the selling authorization and provide a quantity or price. Contract pricing with installment plan lets you enter quantity per dimension, Contract pricing with upfront payments lets you enter price per dimension.
    - Choose **Manage custom dimensions** to add dimensions to the product that will be available in this product for future offers and selling authorizations. Custom dimensions added to the product cannot be removed.
      You can have up to 200 contract and 200 usage dimensions in 1 product.
    - For **Price per usage dimension**, specify hourly rate for each dimension type. Buyers are charged based on the hourly rate for their usage. The public offer price is populated here by default.
    - For **Buyer installment plan**, enter the Contract total and generate installment plan based on desired frequency. This is required for Contract pricing with installment plan.
    - For **Pricing per instance type**, set usage prices for each instance type. The optional pricing tool allows you to bulk update prices by either applying a discount to public price or applying the same price to all instances.
    - For **Selling authorization availability**, choose one of the following options to limit the availability of how many private offers are created or until what specific time private offers can be created using this selling authorization:
      - **Single Use** – Allows for a single offer to be created by reseller until the specified end date
      - **Specific Time Duration** – Allows for multiple offers to be created by reseller until the specified end date
      - **No Set Time Duration** – Allows for multiple offers to be created by reseller until the selling authorization is manually deactivated

    - You can choose **Save and exit**, **Previous**, or **Next**. Choosing **Next** takes you to the **Configure legal terms** page.

6.  On the **Configure legal terms** page, enter the following details:
    - For **End user license agreement**, select Public EULA or Standard Contract for AWS Marketplace (SCMP) or upload Custom EULA.

    ###### Note

    Only custom EULAs are supported for professional services sellers.
    - (Optional) Select the **Reseller Contract for AWS Marketplace (RCMP)** or upload a custom contract to be included in the selling authorization.
    - You can choose **Save and exit**, **Previous**, or **Next**. Choosing **Next** takes you to the **Review and create** page.

7.  On the **Review and create** page, make sure all the information is correct. Once a selling authorization is published, it cannot be modified.
8.  Choose **Create selling authorizations** to publish the selling authorization to reseller.

## Manage selling authorizations

- The **Selling authorization created** table is updated to display relevant selling authorization details including **Selling authorization name**, **Product name**, **Reseller name**, **Created date**, **Expiration date** and **Status**.
- After selling authorizations are created, you cannot extend the expiry dates or modify any other details.
- You can **Deactivate** a selling authorization if you no longer want a reseller to use it. When you deactivate a selling authorization, new offers cannot be created using that selling authorization. Any offers already created are unaffected.
- You can also clone a selling authorization by selecting the selling authorization and choosing **Clone**. This prepopulates values into all the fields and allows for editing.

## Selling authorization status and actions

The following list describes the selling authorization status values and their meanings:

- _Draft_ - The selling authorization has been created but not yet activated.
- _Authorized_ - The selling authorization is active and can be used to create Channel Partner Private Offers (CPPOs). No CPPOs have been created yet.
- _Authorized (reusable)_ - The selling authorization has been used to create at least one CPPO and can be used to create additional CPPOs. This status is common for authorizations with a specific time duration or no set time duration.
- _Authorized (consumed)_ - The selling authorization has been fully utilized and cannot be used to create additional CPPOs. This typically occurs with single-use authorizations after a reseller creates a private offer.
- _Expired_ - The selling authorization's availability end date has passed. It can no longer be used to create CPPOs.
- _Deactivated_ - The independent software vendor (ISV) has manually deactivated the authorization. It can no longer be used to create CPPOs. This status is called "Restricted" in the API.

###### Note

The system determines the status based on several factors, including the selling authorization's inner status, availability end date, and offer extended status. Status values are assigned based on a priority order to resolve potential overlaps.
