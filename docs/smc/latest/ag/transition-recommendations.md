

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Upgrading to AWS Service Management Connector from a previous version
<a name="transition-recommendations"></a>

To upgrade to AWS Service Management Connector from a previous Connector version in a ServiceNow Production instance, you must:
+  Install the Connector in a ServiceNow sandbox instance. 
+  Follow the Connector installation instructions starting at baseline permissions.
**Note**  
 There is a known issue with committing update sets that have a previous version of the Connector installed.   
Previewing the update set is successful. However, at the conclusion of the committing update, an error appears that states: “Version loading was stopped by DictionaryUpdateLoader….”   
We consider these errors as false positives. After further testing, we determined there is no impact on the update set. AWS logs a ServiceNow support case and provides a new release if needed. 
+  Compare the two versions to plan how you manage your ServiceNow Development. 
+  Determine how you want to address Service Catalog provisioned products in previous releases. 
+  Create a check list of all your transition action items that include, but are not limited to: 
  + Transition plan
    +  Decision point on Service Catalog provisioned products 
    +  Steps to update or install the Connector in ServiceNow development to production environments
  +  ServiceNow platform admin communications 
  +  End user communications 

## Delete application files
<a name="delete-application-files"></a>

(Optional) When you upgrade to the latest connector version, you may have application files that are no longer required. While these files don't pose any risks to the feature set, you can delete them by completing the following steps:

1. Navigate to **System Definition** and then **Fix Scripts**.

1. Open the context (right-click) menu for **Name**, and then choose **Import XML**.

1. Upload the [Fix Script](https://servicecatalogconnector.s3.amazonaws.com/AWSConnector513-RemoveDeletedAppFiles.xml).

1. Select `AWSConnector-RemoveDeletedAppFiles`.

1. Choose **Run Fix Script**.