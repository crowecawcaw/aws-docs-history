# Update the provisioned product in Service Catalog

The following procedure guides you through how to update your account in
Account Factory or move it to a new OU, by updating the account's provisioned product in
Service Catalog.

###### To update an Account Factory account or change its OU through Service Catalog

1. Sign in to the AWS Management Console, and open the AWS Service Catalog console at
   [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").

###### Note

You must sign in as a user with permissions to provision new products
in Service Catalog (for example, an IAM Identity Center user in `AWSAccountFactory` or
`AWSServiceCatalogAdmins` groups). 2. In the navigation pane, choose **Provisioning**, and then
choose **Provisioned products**. 3. For each of the member accounts listed, perform the following steps to
update all member accounts:

    1. Select a member account. You're directed to the
     *Provisioned product details* page for that
     account.
    2. On the *Provisioned product details* page,
     choose the **Events** tab.
    3. Make a note of the following parameters:




    	* **SSOUserEmail** (Available in provisioned
    	 product details)
    	* **AccountEmail** (Available in provisioned
    	 product details)
    	* **SSOUserFirstName** (Available in IAM Identity Center)
    	* **SSOUSerLastName** (Available in IAM Identity Center)
    	* **AccountName** (Available in IAM Identity Center)
    4. From **Actions**, choose
     **Update**.
    5. Choose the button next to the **Version** of the
     product you want to update, and choose
     **Next**.
    6. Provide the parameter values that were mentioned
     previously.




    	* If you want to keep the existing OU, for
    	 **ManagedOrganizationalUnit**, choose
    	 the OU that the account was already in.
    	* If you want to migrate the account to a new OU, for
    	 **ManagedOrganizationalUnit**, choose
    	 the new OU for the account.
     A central cloud administrator can find this information in the
     AWS Control Tower console, on the **Organization**
     page.
    7. Choose **Next**.
    8. Review your changes, and then choose **Update**.
     This process can take a few minutes per account.
