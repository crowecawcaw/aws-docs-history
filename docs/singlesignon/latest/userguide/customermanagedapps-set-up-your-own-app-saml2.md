# Set up your own
 SAML 2.0 application

You can set up your own applications that allow identity federation using SAML
 2.0 and add them to IAM Identity Center. Most of the steps for setting up your own SAML 2.0
 applications are the same as setting up a SAML 2.0 application from the
 application catalog in the IAM Identity Center console. However, you must also provide
 additional SAML attribute mappings for your own SAML 2.0 applications. These
 mappings enable IAM Identity Center to populate the SAML 2.0 assertion correctly for your
 application. You can provide this additional SAML attribute mapping when you set
 up the application for the first time. You can also provide SAML 2.0 attribute
 mappings on the application details page in the IAM Identity Center console.

Use the following procedure to set up a SAML 2.0 trust relationship between
 IAM Identity Center and your SAML 2.0 application's service provider. Before you begin this
 procedure, make sure that you have the service provider's certificate and
 metadata exchange files so that you can finish setting up the trust.

###### To set up your own SAML 2.0 application

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications**.
3. Choose the **Customer managed** tab.
4. Choose **Add application**.
5. On the **Select application type** page, under
 **Setup preference**, choose **I have an
 application I want to set up**.
6. Under **Application type**, choose **SAML
 2.0**.
7. Choose **Next**.
8. On the **Configure application** page, under
 **Configure application**, enter a
 **Display name** for the application, such as
 `MyApp`. Then, enter a
 **Description**.
9. Under **IAM Identity Center metadata**, do the following:


	1. Under **IAM Identity Center SAML metadata file**, choose
	 **Download** to download the
	 identity provider metadata.
	2. Under **IAM Identity Center certificate**,
	 choose **Download** to download the
	 identity provider certificate.###### Note

You will need these files later when you set up the custom
 application from the service provider's website.
10. (Optional) Under **Application
 properties**, you can also specify the **Application start URL**, **Relay state**, and **Session duration**.
 For more information, see [Understand application properties in the IAM Identity Center
 console](appproperties.md "appproperties.md").
11. Under **Application metadata**, choose
 **Manually type your metadata values**. Then,
 provide the **Application ACS URL** and
 **Application SAML audience** values.
12. Choose **Submit**. You're taken to the
 details page of the application that you just added.
