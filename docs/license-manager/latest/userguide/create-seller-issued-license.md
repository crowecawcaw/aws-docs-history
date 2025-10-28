# Create seller issued licenses in

License Manager

Use the following procedure to create a block of licenses to grant to customers using
the AWS Management Console. Alternatively, you can create the license using the [CreateLicense](../APIReference/API_CreateLicense.md "../APIReference/API_CreateLicense.md") API action.

###### To create a license using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Choose **Seller Issued Licenses** from the left menu.
3. Choose **Create license**.
4. For **License metadata**, provide the following
   information:
   - **License name** – The name, up to 150 characters, to
     display to buyers.
   - **License description** – An optional description, up to
     400 characters, that differentiates this license from other licenses.
   - **Product SKU** – The product SKU.
   - **Recipient** – The recipient's name (company or
     individual).
   - **Home Region** – The AWS Region for the license.
     Although licenses can be consumed globally, you can only change the license in
     the home region. You cannot change the home region for a license after you
     create it.
   - **License start date** – The date of activation.
   - **License end date** – The end date of the license, if
     applicable.

5. For **Consumption configuration**, provide the following
   information:
   - **Renewal frequency** – Whether to renew weekly, monthly,
     or not at all.
   - **Consumption configuration** – Choose
     **Provisional Consumption Configuration Options** if the
     license is to be used for continuous connectivity or
     **Borrow** if the license is to be used offline. Enter
     **Max time to live (minutes)** to set the length of
     availability of the license.

6. For **Issuer**, provide the following information:
   - **Enter an AWS KMS key** – License Manager uses this key to sign and
     verify the issuer. For more information, see [Cryptographic signing of licenses in License Manager](license-signing.md "license-signing.md").
   - **Issuer name** – The business name for the seller.
   - **Seller of record** – An optional business name.
   - **Agreement URL** – The URL to the license agreement.

7. For **Entitlement**, provide the following information about the
   capabilities that the license grants to recipients:
   - **Name** – The name of the recipient.
   - **Unit type** – Select the unit type, then provide the
     maximum count.
   - Check **Allow check in** if recipients must check in
     licenses before renewal.
   - Check **Overages allowed** if recipients can use the
     resource beyond the maximum count. This option might incur additional charges
     for the recipient.

8. Choose **Create license**.
