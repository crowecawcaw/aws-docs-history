

# Upgrading the connector to the latest version
<a name="upgrading-from-previous-versions"></a>

The following topics explain how to upgrade the AWS Partner CRM connector to latest version. Upgrading involves adding buttons, sync log details, and mapping values to your opportunity records.

**Note**  
For information about upgrading an Amazon S3 integration, refer to [Upgrading from Amazon S3 to API-based integration](upgrade-crm-api.md) later in this guide.

**Topics**
+ [Adding the Import Resale Authorization button](#add-resale-authorization)
+ [Adding the Import Offer button](#import-offer-btn)
+ [Adding the Import Agreement button](#import-agreements-btn)
+ [Adding sync log details to the ACE opportunity Record page](#add-sync-log-details-ace)
+ [Adding mapping values to the Closed Lost Reason label](#map-closed-lost)

## Adding the Import Resale Authorization button
<a name="add-resale-authorization"></a>

The following steps explain how to add the **Import Resale Authorization** button to the **Resale authorization** section of an opportunity. The button enables you to import resale authorizations from AWS Marketplace.

**To add the button**

1. Sign in to your Salesforce organization as a system administrator.

1. Choose **Setup, Object Manager**, then choose **Resale authorization**.

1.  In the left navigation pane, choose **List View Button Layout**.

1. Choose **Edit** to open the list view editor.

1. In the **Custom Buttons** section, in the **Available Buttons** column, choose **Import Resale Authorization**.

1. Choose the right-arrow button to add **Import Resale Authorization** to the **Selected Buttons** list.

1. Choose **Save**.

After upgrading to version 2.2 or later, do the following:
+ To ensure that your product information is current, refresh your products on the **Refresh Products** tab.
+ Follow the procedures in this section to complete the transition to version 2.2.

## Adding the Import Offer button
<a name="import-offer-btn"></a>

The following steps explain how to add the **Import Offer** button. 

**To add the button**

1. Sign in to your Salesforce organization as a system administrator.

1. Choose **Setup, Object Manager**.

1. Choose **Private Offer**.

1. In the left navigation pane, choose **List View Button Layout**, then choose **Edit** to open the list view editor.

1. In the **Custom Buttons** section, in the **Available Buttons** column, choose **Import Offer**.

1. Choose the right-arrow button to add **Import Offer** to the **Selected Buttons** list.

1. Choose **Save**.

## Adding the Import Agreement button
<a name="import-agreements-btn"></a>

The following steps explain how to add the **Import Agreement** button to the **Agreements** section of an opportunity record. 

**To add the button**

1. Sign in to your Salesforce organization as a system administrator, choose **Setup**, then **Object Manager**.

1. Choose **Agreement**, and in the **Details** section, choose **Edit**.

1. Choose **Allow Search**.

1. Choose **Save**.

1. In the left navigation pane, choose **List View Button Layout**.

1. In the **Custom Buttons** section, in the **Available Buttons** column, choose **Import Agreement**, then choose the right-arrow button to add **Import Agreement** to the **Selected Buttons** list.

1. Choose **Save**.

## Adding sync log details to the ACE opportunity Record page
<a name="add-sync-log-details-ace"></a>

The following steps explain how to add sync log details to an ACE Opportunity Record page. 

**To add the log details**

1. Sign in to your Salesforce organization as a system administrator.

1. Choose **Setup, Object Manager**.

1. Choose **ACE Opportunity**.

1. In the left navigation pane, choose **ACE Opportunity Layout**.

1. Choose **Related Lists**.

1. Choose and move **Sync Log Details** to the **Related Lists** section of the page layout.

1. Choose **Save**.

1. Customize related lists for **Sync Log Details** and add **Created Date**, **Error Messages**, and **Status** fields to **Related Lists**. For more information, refer to [Customize Related Lists](https://help.salesforce.com/s/articleView?id=sf.customizing_related_lists.htm) in the Salesforce help.

1. Choose **Save**.

**Note**  
Version 2.2 of the CRM connector features a path for AWS-delivered ACE opportunities. For information about viewing that path, refer to [Enable Paths](https://help.salesforce.com/s/articleView?id=sf.emergency_response_create_paths.htm) in the Salesforce help.

## Adding mapping values to the Closed Lost Reason label
<a name="map-closed-lost"></a>

The following steps explain how to add automatic field mapping values to the **Closed Lost Reason** label of ACE opportunity objects.

**To add the mapping values**

1. Sign in to your Salesforce organization as a system administrator.

1. Choose the **ACE Mappings** tab.

1. In the navigation bar, choose **Opportunity**.

1. In the **Object Selector**, choose **ACE Opportunity**.

1. For the **Closed Lost Reason** label, choose **Edit Values**.

1. Choose **Auto Map**.

1. Choose **Next**.

1. Choose **Save**.