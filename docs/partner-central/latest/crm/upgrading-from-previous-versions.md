# Upgrading the connector to the latest version

The following topics explain how to upgrade the AWS Partner CRM connector to latest version. Upgrading involves adding buttons, sync log details, and mapping values to your
opportunity records.

###### Note

For information about upgrading an Amazon S3 integration, refer to [Upgrading from a CRM with Amazon S3 integration to the Partner Central
API](upgrade-crm-api.md "upgrade-crm-api.md") later in this guide.

###### Topics

- [Adding the Import Resale Authorization button](#add-resale-authorization "#add-resale-authorization")
- [Adding the Import Offer button](#import-offer-btn "#import-offer-btn")
- [Adding the Import Agreement button](#import-agreements-btn "#import-agreements-btn")
- [Adding sync log details to the ACE opportunity Record
  page](#add-sync-log-details-ace "#add-sync-log-details-ace")
- [Adding mapping values to the Closed Lost Reason label](#map-closed-lost "#map-closed-lost")

## Adding the Import Resale Authorization button

The following steps explain how to add the **Import Resale Authorization**
button to the **Resale authorization** section of an opportunity. The button
enables you to import resale authorizations from AWS Marketplace.

###### To add the button

1. Sign in to your Salesforce organization as a system administrator.
2. Choose **Setup, Object Manager**, then choose **Resale authorization**.
3. In the left navigation pane, choose **List View Button Layout**.
4. Choose **Edit** to open the list view editor.
5. In the **Custom Buttons** section, in the **Available Buttons** column, choose **Import Resale Authorization**.
6. Choose the right-arrow button to add **Import Resale Authorization** to the **Selected Buttons** list.
7. Choose **Save**.

After upgrading to version 2.2 or later, do the following:

- To ensure that your product information is current, refresh your products on the
  **Refresh Products** tab.
- Follow the procedures in this section to complete the transition to version 2.2.

## Adding the Import Offer button

The following steps explain how to add the **Import Offer** button.

###### To add the button

1. Sign in to your Salesforce organization as a system administrator.
2. Choose **Setup, Object Manager**.
3. Choose **Private Offer**.
4. In the left navigation pane, choose **List View Button Layout**, then choose **Edit** to open the list view editor.
5. In the **Custom Buttons** section, in the **Available Buttons** column, choose **Import Offer**.
6. Choose the right-arrow button to add **Import Offer** to the **Selected Buttons** list.
7. Choose **Save**.

## Adding the Import Agreement button

The following steps explain how to add the **Import Agreement** button to
the **Agreements** section of an opportunity record.

###### To add the button

1. Sign in to your Salesforce organization as a system administrator, choose **Setup**, then **Object Manager**.
2. Choose **Agreement**, and in the **Details** section, choose **Edit**.
3. Choose **Allow Search**.
4. Choose **Save**.
5. In the left navigation pane, choose **List View Button Layout**.
6. In the **Custom Buttons** section, in the **Available
   Buttons** column, choose **Import Agreement**, then choose the right-arrow button to add **Import Agreement**
   to the **Selected Buttons** list.
7. Choose **Save**.

## Adding sync log details to the ACE opportunity Record

page

The following steps explain how to add sync log details to an ACE Opportunity Record page.

###### To add the log details

1. Sign in to your Salesforce organization as a system administrator.
2. Choose **Setup, Object Manager**.
3. Choose **ACE Opportunity**.
4. In the left navigation pane, choose **ACE Opportunity Layout**.
5. Choose **Related Lists**.
6. Choose and move **Sync Log Details** to the **Related Lists** section of the page layout.
7. Choose **Save**.
8. Customize related lists for **Sync Log Details** and add **Created Date**, **Error Messages**,
   and **Status** fields to **Related Lists**. For more information, refer to
   [Customize Related Lists](https://help.salesforce.com/s/articleView?id=sf.customizing_related_lists.htm "https://help.salesforce.com/s/articleView?id=sf.customizing_related_lists.htm") in the Salesforce help.
9. Choose **Save**.

###### Note

Version 2.2 of the CRM connector features a path for AWS-delivered ACE opportunities. For
information about viewing that path, refer to [Enable Paths](https://help.salesforce.com/s/articleView?id=sf.emergency_response_create_paths.htm "https://help.salesforce.com/s/articleView?id=sf.emergency_response_create_paths.htm") in the Salesforce help.

## Adding mapping values to the Closed Lost Reason label

The following steps explain how to add automatic field mapping values to the
**Closed Lost Reason** label of ACE opportunity objects.

###### To add the mapping values

1. Sign in to your Salesforce organization as a system administrator.
2. Choose the **ACE Mappings** tab.
3. In the navigation bar, choose **Opportunity**.
4. In the **Object Selector**, choose **ACE Opportunity**.
5. For the **Closed Lost Reason** label, choose **Edit Values**.
6. Choose **Auto Map**.
7. Choose **Next**.
8. Choose **Save**.
