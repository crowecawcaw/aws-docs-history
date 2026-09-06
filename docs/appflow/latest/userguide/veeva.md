

# Veeva
<a name="veeva"></a>

The following are the requirements and connection instructions for using Veeva with Amazon AppFlow.

**Note**  
You can use Veeva as a source only.

**Topics**
+ [Requirements](#veeva-requirements)
+ [Connection instructions](#veeva-setup)
+ [Extract Veeva VAULT documents with Amazon AppFlow](#veeva-document-extraction-feature)
+ [Notes](#veeva-notes)
+ [Supported destinations](#veeva-destinations)
+ [Related resources](#veeva-resources)

## Requirements
<a name="veeva-requirements"></a>
+ You must provide Amazon AppFlow with your user name, password, and Veeva instance name.
+  Your user account must have API access. For more information, see [API access permissions](https://docs-vdm.veevanetwork.com/doc/vndocad/Content/Network_topics/Whats_new/20R2.0/Users.htm#api) in the Veeva documentation.

## Connection instructions
<a name="veeva-setup"></a>

**To connect to Veeva while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Veeva** from the **Source name** dropdown list.

1. Choose **Connect** to open the **Connect to Veeva** dialog box.

   1. Under **User name**, enter the user name you use to log into Veeva.

   1. Under **Password**, enter your secret key.

   1. Under **Instance name**, enter the name of your Veeva instance.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Connect to Veeva dialog with fields for user name, password, instance name, encryption, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-veeva-console.png)

Now that you are connected to your Veeva account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#veeva-requirements) section above.

## Extract Veeva VAULT documents with Amazon AppFlow
<a name="veeva-document-extraction-feature"></a>

You can use Amazon AppFlow to extract documents from Veeva VAULT. Follow the steps below to configure a flow to extract documents.

**Step 1: Create a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

**Step 2: Configure the flow**

1. Choose **Veeva VAULT** from the **Source name** dropdown list.

1. Choose a Veeva VAULT connection from already existing connections or create a new connection.

1. Choose **Veeva VAULT documents** from the radio options.

1. Choose a **Veeva VAULT document type** from the dropdown.

1. Choose **Document metadata and source files** option to extract source files along with associated metadata. Choose **Metadata only** option to only download Metadata. By default Metadata only is selected.

1. If you select **Document metadata and source files.** 

   1. Choose **versions** of the document you want to extract, By default only latest version of document is extracted, You can select all versions to be extracted. 

   1. Choose **Renditions** options if required, By default Renditions are not included.  
![Configure flow page showing Veeva source settings with document type, download options, and version selections.](http://docs.aws.amazon.com/appflow/latest/userguide/images/flow_setup_veeva-document_extraction.png)

1. Choose a destination from drop down menu.
**Note**  
Currently Amazon AppFlow only supports Amazon S3 as a destination for document extraction.

1. Choose a **Bucket Name** and **Bucket Prefix**.

1. Select a trigger to run flow. You can select **Run on demand** or ** Run on Schedule**to run the flow. If you choose a scheduled trigger,you can run flows at a maximum frequency of one flow run **per hour**.

1. Choose **Next**.

**Step 3: Map data fields**

1. You can choose a mapping method either to **Manually map the fields** or ** Upload .csv file with mapped fields ** to map fields from source to destination.

1. If you choose to **Manually map the fields** choose the fields from drop down list.

1. Options like **Add formula**, **Modify Values** and **Validations** are not supported for Veeva VAULT document extraction. 

1. Choose **Next**.

**Step 4 (Optional): Add filters**

Specify a filter to determine which records to transfer. Amazon AppFlow enables you to filter data fields by adding multiple filters and by adding criteria to a filter. If you want to filter the documents by **Document subtype** or **Document Classification** you can add the appropriate filters here.

1. Based on the selected field names choose appropriate filter condition.

1. Choose **Next**.

**Step 5: Review and create**
+ Review the information for your flow. To change the information for a step, choose **Edit**. When you are finished, choose **Create flow**. 

## Notes
<a name="veeva-notes"></a>
+ When you use Veeva as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per minute.

## Supported destinations
<a name="veeva-destinations"></a>

When you create a flow that uses Veeva as the data source, you can set the destination to any of the following connectors: 
+ Amazon Connect Customer
+ Amazon Honeycode
+ Lookout for Metrics
+ Amazon Redshift
+ Amazon S3
+ Marketo
+ Salesforce
+ Snowflake
+ Upsolver
+ Zendesk

You can also set the destination to any custom connectors that you create with the Amazon AppFlow Custom Connector SDKs for [ Python](https://github.com/awslabs/aws-appflow-custom-connector-python) or [Java ](https://github.com/awslabs/aws-appflow-custom-connector-java). You can download these SDKs from GitHub.

## Related resources
<a name="veeva-resources"></a>
+  [API access permissions](https://docs-vdm.veevanetwork.com/doc/vndocad/Content/Network_topics/Whats_new/20R2.0/Users.htm#api) in the Veeva Product Support Portal 