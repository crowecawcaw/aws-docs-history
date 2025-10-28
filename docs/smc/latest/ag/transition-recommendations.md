# Upgrading to AWS

Service Management Connector from a previous version

To upgrade to AWS Service Management Connector from a previous Connector
version in a ServiceNow Production instance, you must:

- Install the Connector in a ServiceNow sandbox instance.
- Follow the Connector installation instructions starting at baseline
  permissions.

###### Note

There is a known issue with committing update sets that have a
previous version of the Connector installed.

Previewing the update set is successful. However, at the conclusion of
the committing update, an error appears that states: “Version loading
was stopped by DictionaryUpdateLoader….”

We consider these errors as false positives. After further testing, we
determined there is no impact on the update set. AWS logs
a ServiceNow support case and provides a new release if needed.

- Compare the two versions to plan how you manage your ServiceNow
  Development.
- Determine how you want to address Service Catalog provisioned products in previous
  releases.
- Create a check list of all your transition action items that include, but
  are not limited to:
  - Transition plan
    - Decision point on Service Catalog provisioned products
    - Steps to update or install the Connector in ServiceNow
      development to production environments

  - ServiceNow platform admin communications
  - End user communications

## Delete application

files

(Optional) When you upgrade to the latest connector version, you
may have application files that are no longer required. While these
files don't pose any risks to the feature set, you can delete them by
completing the following steps:

1. Navigate to **System Definition** and then
   **Fix Scripts**.
2. Open the context (right-click) menu for **Name**, and then choose **Import XML**.
3. Upload the [Fix Script](https://servicecatalogconnector.s3.amazonaws.com/AWSConnector513-RemoveDeletedAppFiles.xml "https://servicecatalogconnector.s3.amazonaws.com/AWSConnector513-RemoveDeletedAppFiles.xml").
4. Select `AWSConnector-RemoveDeletedAppFiles`.
5. Choose **Run Fix Script**.
