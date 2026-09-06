

# Update the provisioned product in Service Catalog
<a name="update-provisioned-product"></a>

The following procedure guides you through how to update your account in Account Factory or move it to a new OU, by updating the account's provisioned product in Service Catalog.

**Note**  
If you have disabled IAM Identity Center in your landing zone settings, the SSO user parameters (`SSOUserEmail`, `SSOUserFirstName`, and `SSOUserLastName`) are not used during account provisioning. If desired, you can provide placeholder values for these required parameters and modify them later by following the instructions in this section.

**To update an Account Factory account or change its OU through Service Catalog**

1. Sign in to the AWS Management Console, and open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/). 
**Note**  
You must sign in as a user with permissions to provision new products in Service Catalog (for example, an IAM Identity Center user in `AWSAccountFactory` or `AWSServiceCatalogAdmins` groups).

1. In the navigation pane, choose **Provisioning**, and then choose **Provisioned products**.

1.  For each of the member accounts listed, perform the following steps to update all member accounts:

   1. Select a member account. You're directed to the *Provisioned product details* page for that account.

   1. On the *Provisioned product details* page, choose the **Events** tab.

   1. Make a note of the following parameters:
      +  **SSOUserEmail** (Available in provisioned product details)
      +  **AccountEmail** (Available in provisioned product details)
      +  **SSOUserFirstName** (Available in IAM Identity Center) 
      +  **SSOUSerLastName** (Available in IAM Identity Center) 
      +  **AccountName** (Available in IAM Identity Center) 

   1. From **Actions**, choose **Update**.

   1. Choose the button next to the **Version** of the product you want to update, and choose **Next**.

   1. Provide the parameter values that were mentioned previously.
      + If you want to keep the existing OU, for **ManagedOrganizationalUnit**, choose the OU that the account was already in.
      + If you want to migrate the account to a new OU, for **ManagedOrganizationalUnit**, choose the new OU for the account.

       A central cloud administrator can find this information in the AWS Control Tower console, on the **Organization** page.

   1. Choose **Next**.

   1. Review your changes, and then choose **Update**. This process can take a few minutes per account.