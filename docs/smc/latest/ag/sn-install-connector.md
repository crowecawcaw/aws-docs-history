# Installing ServiceNow Connector scoped

application

The AWS Service Management Connector for ServiceNow is a conventional, scoped application that was
developed and released through a ServiceNow update set. Update sets are code changes
to the base platform that lets developers move code across ServiceNow
instances.

Download and install a certified version of the connector for no additional cost from
the following locations:

- [ServiceNow store](https://store.servicenow.com/sn_appstore_store.do#!/store/application/f0b117a3db32320093a7d7a0cf961912/ "https://store.servicenow.com/sn_appstore_store.do#!/store/application/f0b117a3db32320093a7d7a0cf961912/")
- [ServiceNow update set](https://servicecatalogconnector.s3.amazonaws.com/AWSSMCConnectorV513.xml "https://servicecatalogconnector.s3.amazonaws.com/AWSSMCConnectorV513.xml"): AWS Service Management Connector offers an update set for
  users who want to install the connector application in a ServiceNow Personal
  Developer Instance (PDI) or sandbox environment.
  If you don't already have a ServiceNow instance, start with the following first
  step. If you already have a ServiceNow instance, use the previous links to download
  and install the connector.

To install the connector, complete the following steps.

###### Obtain a ServiceNow instance

1. Open [Obtaining a Personal Developer Instance](https://developer.servicenow.com/dev.do#!/guides/rome/developer-program/pdi-guide/obtaining-a-pdi "https://developer.servicenow.com/dev.do#!/guides/rome/developer-program/pdi-guide/obtaining-a-pdi").
2. Create ServiceNow developer program credentials.
3. Follow the instructions for requesting a ServiceNow instance.
4. Capture your instance details, including URL, administrative ID, and
   temporary password credentials.

###### To install the update set

1. In your ServiceNow dashboard, enter `update sets`
   into the navigation panel in the upper left.
2. Choose **Retrieved Update Sets** from the results.
3. Choose **Import Update Set from XML** and upload the
   release XML file.
4. Choose the **AWS Service Management Connector for
   ServiceNow** update set.
5. Choose **Preview Update Set**, which makes ServiceNow
   validate the Connector update set.
6. Choose **Update**.
7. Choose **Commit Update Set** to apply the update set and
   create the application. This procedure should complete 100%.
