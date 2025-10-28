# Platform system administrator

components

To enable the AWS Service Management Connector scoped application named
**AWS Service Management**, the system admin must create a
discovery source, and configure specific platform tables, forms, and views.

###### Create a discovery source AWS Service Management Connector entry

You must create a new discovery data source, AWS Service Management
Connector.

**To enable AWS to report discovered CIs into your
CMDB**

1. Choose **System Definition**. Then select
   **Choice Lists**.
2. Choose **New**.
3. Create a new entry with these details:
   - **Table:**
     `Configuration Item [cmdb_ci]`
   - **Element:**
     `discovery_source`
   - **Label:**
     `AWS Service Management Connector`
   - **Value:**
     `AWS Service Management Connector`

###### Note

Make sure you are in Global mode in ServiceNow System Settings to modify
System Definitions.
