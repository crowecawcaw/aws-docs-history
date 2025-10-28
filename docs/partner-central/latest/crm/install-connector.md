# Installing the connector

The following sets of steps explain how to install and uninstall the AWS Partner Customer Relationship Management (CRM) connector.

###### Topics

- [Installing the connector](#first-install "#first-install")
- [Confirming the installation](#confirm-the-installation "#confirm-the-installation")
- [Uninstalling the connector](#uninstall-connector "#uninstall-connector")
- [Understanding Salesforce governor limits](#connector-limits "#connector-limits")

## Installing the connector

The following steps explain how to install the CRM connector in a Salesforce organization. Follow these steps to install the connector for the first time, and to install new versions of the connector.

###### Note

To complete these steps, you must have the following:

- An Enterprise, Professional, or Unlimited edition of Salesforce.
- Administrative access to your Salesforce organization.

###### To install a new version

1. Navigate to **AppExchange** and search for **AWS Partner CRM Connector**.

—OR—

Go to [https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000IYf0nUAD](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000IYf0nUAD "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000IYf0nUAD"). 2. Choose **Get it now**. 3. On the **Where do you want to install this package** page, choose **Install in sandbox**. 4. On the **Confirmation Installation Details** page, select the **I have read the terms and conditions** checkbox, then choose **Confirm and Install**. 5. Sign in to Salesforce.

###### Note

Make sure you sign in to the correct domain. As needed, choose **Use Custom Domain** and enter the correct domain name. 6. Choose the **Install for Administrators Only** option, then choose **Install**. 7. Choose the **Yes, grant access to these third-party web sites** checkbox, then choose **Continue**.

## Confirming the installation

To confirm package installation, choose **Home**, **Apps**, **Packaging**, **Installed Packages**.

If the new version of the connector doesn't appear on the list of installed packages, follow the steps in [Getting help](getting-help.md "getting-help.md") to contact support.

###### Note

After you confirm the installation, complete the steps listed in
[Upgrading the connector to the latest version](upgrading-from-previous-versions.md "upgrading-from-previous-versions.md") to install the latest features.

## Uninstalling the connector

Before uninstalling the AWS Partner Customer Relationship Management (CRM) connector, remove any user [ACE integration permission sets](crm-connector-pemissions-sets.md "crm-connector-pemissions-sets.md") and [AWS Marketplace integration permission sets](mkt-permissions-sets.md "mkt-permissions-sets.md").

###### To uninstall the connector

1. In Salesforce, choose **Home**, **Apps**,
   **Packaging**, **Installed Packages**.
2. Choose **Uninstall**.

## Understanding Salesforce governor limits

When implementing the AWS Partner CRM Connector, be aware of Salesforce governor limits,
particularly regarding SOQL query consumption. These limits can significantly impact your custom
business logic and overall system performance. We recommend reviewing Salesforce's official
documentation on governor limits and best practices for query optimization. For detailed guidance,
refer to the following Salesforce resources:

- [Salesforce governor lImits overview](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm") in the _Apex Developer Guide_
- [Best Practices for SQLS and SOSL](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm?q=SOSL+SOQL+best+practices+limits "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm?q=SOSL+SOQL+best+practices+limits")
