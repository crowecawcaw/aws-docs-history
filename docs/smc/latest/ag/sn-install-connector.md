

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Installing ServiceNow Connector scoped application
<a name="sn-install-connector"></a>

The AWS Service Management Connector for ServiceNow is a conventional, scoped application that was developed and released through a ServiceNow update set. Update sets are code changes to the base platform that lets developers move code across ServiceNow instances.

Download and install a certified version of the connector for no additional cost from the following locations:
+ [ ServiceNow store](https://store.servicenow.com/sn_appstore_store.do#!/store/application/f0b117a3db32320093a7d7a0cf961912/)
+ [ ServiceNow update set](https://servicecatalogconnector.s3.amazonaws.com/AWS_SC_update_set_5.1.12.zip): AWS Service Management Connector offers an update set for users who want to install the connector application in a ServiceNow Personal Developer Instance (PDI) or sandbox environment. 

If you don't already have a ServiceNow instance, start with the following first step. If you already have a ServiceNow instance, use the previous links to download and install the connector.

To install the connector, complete the following steps.

**Obtain a ServiceNow instance**

1. Open [ Obtaining a Personal Developer Instance](https://developer.servicenow.com/dev.do#!/guides/rome/developer-program/pdi-guide/obtaining-a-pdi).

1. Create ServiceNow developer program credentials.

1. Follow the instructions for requesting a ServiceNow instance.

1. Capture your instance details, including URL, administrative ID, and temporary password credentials.

**To install the update set**

1.  In your ServiceNow dashboard, enter **update sets** into the navigation panel in the upper left. 

1.  Choose **Retrieved Update Sets** from the results. 

1.  Choose **Import Update Set from XML** and upload the release XML file. 

1.  Choose the **AWS Service Management Connector for ServiceNow** update set. 

1.  Choose **Preview Update Set**, which makes ServiceNow validate the Connector update set. 

1.  Choose **Update**. 

1.  Choose **Commit Update Set** to apply the update set and create the application. This procedure should complete 100%. 