

# Configuring the connector for a Partner Central API integration
<a name="p-c-api-integration"></a>

The following sections explain how to configure the CRM connector for use with the AWS Partner Central APIs.

To create and manage opportunities in Salesforce, configure the CRM connector for use with a Partner Central API integration.

**Note**  
Managing leads requires an earlier CRM with Amazon S3 integration. For more information, refer to [Configuring the connector for a CRM with Amazon S3 integration](s3-config.md) later in this guide.

**Topics**
+ [Entering connection authentication details](#config-p-c-apis)
+ [Entering the system settings](#p-c-api-system-settings)
+ [Testing the connection](#p-c-apis-testing)
+ [Using flow templates](flow-templates.md)

## Entering connection authentication details
<a name="config-p-c-apis"></a>

Partners start the integration process by entering the details needed to connect to the Partner Central sales endpoint. Follow each set of steps in the order listed, and complete each set before proceeding to the next one.

**To enter connection authentication details**

1. In Salesforce, open the **AWS guided setup** tab. For information about opening that tab, refer to [Using guided setup](use-guided-setup.md) earlier in this guide. 

1. Expand **Step 1: AWS connection authentication details** and choose **Start.**

1. On the **Named credentials** page, choose **New earlier**. 

1. In the **New named credential** form, enter the values from the following table.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/partner-central/latest/crm/p-c-api-integration.html)

1. Choose **Save**. 

1. Return to the **AWSGuided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials. 

## Entering the system settings
<a name="p-c-api-system-settings"></a>

The following steps explain how to enter the correct system configuration settings for the integration.

1. In Salesforce, open the **AWS guided setup** tab. For information about opening that tab, refer to [Using guided setup](use-guided-setup.md) earlier in this guide. 

1. Expand **Step 2: System configuration settings** and choose **Start.** 

1. Locate **AWS Partner CRM Connector Settings**, and choose **Manage**. 

1. Choose **New**, then enter the values from the following table.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/partner-central/latest/crm/p-c-api-integration.html)

1. Choose **Save**. 

1. Return to the **AWS guided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials.

## Testing the connection
<a name="p-c-apis-testing"></a>

Before testing the connection, ensure that you have completed all the above steps.

**To test the AWS Partner Central API connection**

1. Expand **Step 4: Test configuration for Partner Central API integration**.

1. Choose **Test**.

If the connection succeeds, you receive a confirmation message.