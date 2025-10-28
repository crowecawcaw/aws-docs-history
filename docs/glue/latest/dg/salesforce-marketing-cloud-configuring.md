# Configuring Salesforce Marketing Cloud

Before you can use AWS Glue to transfer data from Salesforce Marketing Cloud, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have a Salesforce Marketing Cloud account. For more information, see [Creating a Salesforce Marketing Cloud account](#salesforce-marketing-cloud-configuring-creating-salesforce-marketing-cloud-account "#salesforce-marketing-cloud-configuring-creating-salesforce-marketing-cloud-account").
- Your Salesforce Marketing Cloud account is enabled for API access. API access is enabled by default for the Enterprise, Unlimited, Developer, and Performance editions.

If you meet these requirements, you’re ready to connect AWS Glue to your Salesforce Marketing Cloud account. For typical connections, you don't need do anything else in Salesforce Marketing Cloud.

## Creating a Salesforce Marketing Cloud account

For Salesforce Marketing cloud, you need to contact the vendor for account creation. If you or your company has an association with Salesforce, contact your Salesforce account manager to request a Salesforce Marketing Cloud license.
Otherwise, you can request contact from a Salesforce representative as follows:

1. Go to https://www.salesforce.com/in/products/marketing-cloud/overview/ and choose **Sign up**.
2. Select the **Contact Us** link on the top right of the page.
3. Enter the required information in the form and choose **Contact Me**.

A Salesforce representative will contact you to discuss your requirements.

## Creating a project and OAuth 2.0 credentials

To get a project and OAuth 2.0 credentials:

1. Log into your [Salesforce Marketing Cloud instance](https://mc.login.exacttarget.com/hub-cas/login "https://mc.login.exacttarget.com/hub-cas/login") with your username and password and authenticate using your registered mobile number.
2. Click on your profile at the top right corner and then go to **Setup**.
3. Under **Platform Tools** choose **Apps** and then choose **Installed Packages**.

![The screen shot shows how to access the Installed Packages page.](images/sfmc-platform-tools.png) 4. On the **Installed Packages** page, click **New** at the top right corner. Provide the name and description of the package.

Save the package. After the package is saved, you can view the package details. 5. On the **Details** page of the package, under the **Component** section, choose **Add Component**.

![The screen shot shows how to add a component from the Details page of the package.](images/sfmc-add-component.png) 6. Select the **Component Type** as 'API Integration' and click **Next**. 7. Select the **Integration Type** as 'Server-to-Server' (which has the client credentials OAuth grant type) and click **Next**. 8. Add the scopes based on your requirements and click **Save**.
