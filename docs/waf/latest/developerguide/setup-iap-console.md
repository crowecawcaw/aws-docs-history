**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Getting started with AWS WAF using the new console experience

This section guides you through setting up AWS WAF using the new new console experience, which provides simplified configuration workflows and enhanced security management capabilities.

## Access the new console experience

To access the new AWS WAF console experience:

Sign in to the new AWS Management Console and open the AWS WAF console at
[https://console.aws.amazon.com/wafv2-pro](https://console.aws.amazon.com/wafv2-pro "https://console.aws.amazon.com/wafv2-pro").

- In the navigation pane, locate and select **Try the new experience**.

###### Note

You can switch between console experiences at any time using the link in the navigation pane.

## Get started with a protection pack (web ACL)

This tutorial shows you how to create and configure a protection pack (web ACL) to protect your applications. Protection packs (Web ACLs) provide pre-configured security rules tailored to specific workload types.

In this tutorial, you'll learn how to:

- Create a protection pack (web ACL)
- Configure application-specific protection settings
- Add AWS resources to protect
- Choose and customize rules
- Configure logging and monitoring

###### Note

AWS typically bills you less than US $0.25 per day for the resources that you create during this tutorial. When you're finished, we recommend that you delete the resources to prevent incurring unnecessary charges.

### Step 1: Set up AWS WAF

If you haven't already followed the general setup steps in [Setting up your account to use the services](setting-up-waf.md "setting-up-waf.md"), do that now.

### Step 2: Create a protection pack (web ACL)

In this step, you'll create a protection pack (web ACL) and configure its basic settings to match your application type.

1. Sign in to the new AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2-pro](https://console.aws.amazon.com/wafv2-pro "https://console.aws.amazon.com/wafv2-pro").
2. In the navigation pane, choose **Resources &
   protection packs (web ACLs)**.
3. On the **Resources & protection packs (web ACLs)**
   page, choose **Add protection pack (web ACL)**.
4. Under **Tell us about your app**, for **App category**, select one or more app categories that best describe your application.
5. For **Traffic source**, choose the type of traffic your application handles:
   - **API** - For API-only applications
   - **Web** - For web-only applications
   - **Both API and Web** - For applications that handle both types of traffic

### Step 3: Add resources to protect

Now you'll specify which AWS resources to protect with your protection pack (web ACL).

1.  Under **Resources to protect**, choose **Add resources**.
2.  Choose the category of AWS resource to associate with this protection pack (web ACL):

        * Amazon CloudFront distributions
        * Regional resources

    For more information about resource types, see [Associating protection with an AWS resource](web-acl-associating.md "web-acl-associating.md").

### Step 4: Choose initial

protections

In this step, you'll select the rules for your protection pack (web ACL). For
first-time users, we recommend choosing the **Recommended**
option.

AWS WAF generates **Recommended** for you based on your
selections in the **Tell us about your app** section. These
packs implement security best practices for your application type.

- Choose **Next** to continue with the protection pack (web ACL) setup.

###### Note

If you're interested in creating custom rules or using the **You build it** option, we recommend first gaining experience with the pre-configured options.
For more information about creating custom protection packs (web ACLs) and rules, see [Creating a protection pack (web ACL) in AWS WAF](web-acl-creating.md "web-acl-creating.md").

### Step 5: Customize protection pack (web ACL) settings

Now you'll configure additional settings like default actions, rate limits, and logging.

1. Under **Name and description**, enter a name for your protection pack (web ACL). Optionally, enter a description.

###### Note

You can't change the name after you create the protection pack (web ACL). 2. Under **Customize protection pack (web ACL)**, configure the following settings:

    1. Under **Default rule actions**, choose the default action for requests that don't match any rules. For more information, see [Customized web requests and responses in
     AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").
    2. Under **Rule configuration**, customize these settings:




    	* **Default rate limits** - Set limits to protect against DDoS attacks
    	* **IP Addresses** - Configure IP allow/block lists
    	* **Country specific origins** - Manage access by country
    3. For **Logging destination**, configure where you want to store logs. For more information, see [AWS WAF logging destinations](logging-destinations.md "logging-destinations.md").

3. Review your settings and choose **Add
   protection pack (web ACL)**.

### Step 6: Clean up your resources

You've now successfully completed the tutorial. To prevent your account from accruing additional AWS WAF charges, you should either delete the protection pack (web ACL) you created or modify it to match your production needs.

###### To delete your protection pack (web ACL)

1. In the navigation pane, choose **Resources &
   protection packs (web ACLs)**.
2. Select the protection pack (web ACL) you created.
3. Choose the trash icon, then confirm the deletion by typing "delete".

###### Note

If you plan to use this protection pack (web ACL) in production, instead of deleting it, you should review and adjust the protection settings to match your application's security requirements.
