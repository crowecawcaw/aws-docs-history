# Subscribe to AWS Marketplace for Trend Micro Endpoint Protection (EPS)

Trend Micro Endpoint Protection (EPS) is the primary component within AMS for operating system security. In order to
set up EPS once AMS landing zone creation is started, you need to log in to the shared services core account and
subscribe to the Trend Micro Deep Security AMI on AWS Marketplace. Your CSDM or CA will advise you.

1. Log in to the AWS console using the role or user that you specified in the Onboarding Questionnaire for
   `CustomerEPSSubscriptionIAMRoleOrUser`
2. Navigate to the **Switch Role** screen.

![AWS console dropdown menu showing account options and service status indicator.](images/image5.png)

![Switch Role dialog with account, role, display name, and color selection options.](images/image6.png)

    * Account: Provided by AMS
    * Role: `EPSMarketplaceSubscriptionRole`
    * Display Name: EPS Subscription Session


    To subscribe to Trend Micro Deep Security in the AWS Marketplace, follow these steps after you have switched the role in the console:




    	1. Navigate to [the AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").
    	2. Under **Find AWS Marketplace products that meet your needs**, select the following
    	 options:




    		1. **Vendors**: Trend Micro
    		2. **Pricing Plan**: Bring Your Own License if you have a license or By Hosts Billing
    		3. **Delivery Methods**: Amazon Machine Image
    	3. Click **Continue to Subscribe** in the right panel.
    	4. Review the **Terms and Conditions**, and click **Accept Terms** in the upper
    	 right corner.
    	5. Sign out of the account and confirm with your Cloud Architect that the procedure has been completed.

At this point AMS deploys infrastructure into your AMS environment and the environment is ready for you to use once
you have connected your network and set up your access.
