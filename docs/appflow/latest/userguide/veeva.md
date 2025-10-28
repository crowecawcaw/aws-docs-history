# Veeva

The following are the requirements and connection instructions for using Veeva with
Amazon AppFlow.

###### Note

You can use Veeva as a source only.

###### Topics

- [Requirements](#veeva-requirements "#veeva-requirements")
- [Connection instructions](#veeva-setup "#veeva-setup")
- [Extract Veeva VAULT documents with Amazon AppFlow](#veeva-document-extraction-feature "#veeva-document-extraction-feature")
- [Notes](#veeva-notes "#veeva-notes")
- [Supported destinations](#veeva-destinations "#veeva-destinations")
- [Related resources](#veeva-resources "#veeva-resources")

## Requirements

- You must provide Amazon AppFlow with your user name, password, and Veeva instance name.
- Your user account must have API access. For more information, see [API access permissions](https://docs-vdm.veevanetwork.com/doc/vndocad/Content/Network_topics/Whats_new/20R2.0/Users.htm#api "https://docs-vdm.veevanetwork.com/doc/vndocad/Content/Network_topics/Whats_new/20R2.0/Users.htm#api") in the Veeva documentation.

## Connection instructions

###### To connect to Veeva while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings** and
    then choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Veeva** from the **Source name** dropdown
    list.
8.  Choose **Connect** to open the **Connect to Veeva**
    dialog box.

        1. Under **User name**, enter the user name you use to log into
         Veeva.
        2. Under **Password**, enter your secret key.
        3. Under **Instance name**, enter the name of your Veeva instance.
        4. Under **Data encryption**, enter your AWS KMS key.
        5. Under **Connection name**, specify a name for your connection.
        6. Choose **Connect**.

    ![Veeva connection form with fields for user name, password, instance name, and connection name.](images/connection_setup-veeva-console.png)

Now that you are connected to your Veeva account, you can continue with the flow creation
steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#veeva-requirements "#veeva-requirements") section above.

## Extract Veeva VAULT documents with Amazon AppFlow

You can use Amazon AppFlow to extract documents from Veeva VAULT. Follow the steps below to
configure a flow to extract documents.

###### Step 1: Create a flow

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Choose **Create flow**.
3. For **Flow details**, enter a name and description for the flow.
4. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
   **Data encryption**, **Customize encryption settings** and
   then choose an existing CMK or create a new one.
5. (Optional) To add a tag, choose **Tags**, **Add tag**
   and then enter the key name and value.
6. Choose **Next**.

###### Step 2: Configure the flow

1.  Choose **Veeva VAULT** from the **Source name** dropdown
    list.
2.  Choose a Veeva VAULT connection from already existing connections or create a new
    connection.
3.  Choose **Veeva VAULT documents** from the radio options.
4.  Choose a **Veeva VAULT document type** from the dropdown.
5.  Choose **Document metadata and source files** option to extract source
    files along with associated metadata. Choose **Metadata only** option to only
    download Metadata. By default Metadata only is selected.
6.  If you select **Document metadata and source files.**

        1. Choose **versions** of the document you want to extract, By default
         only latest version of document is extracted, You can select all versions to be extracted.
        2. Choose **Renditions** options if required, By default Renditions are
         not included.

    ![Configure flow interface for Veeva connection with source details and download options.](images/flow_setup_veeva-document_extraction.png)

7.  Choose a destination from drop down menu.

###### Note

Currently Amazon AppFlow only supports Amazon S3 as a destination for document extraction. 8. Choose a **Bucket Name** and **Bucket Prefix**. 9. Select a trigger to run flow. You can select **Run on demand** or
**Run on Schedule**to run the flow. If you choose a scheduled trigger,you
can run flows at a maximum frequency of one flow run **per hour**. 10. Choose **Next**.

###### Step 3: Map data fields

1. You can choose a mapping method either to **Manually map the fields** or
   **Upload .csv file with mapped fields** to map fields from source to
   destination.
2. If you choose to **Manually map the fields** choose the fields from drop
   down list.
3. Options like **Add formula**, **Modify Values** and
   **Validations** are not supported for Veeva VAULT document extraction.
4. Choose **Next**.

###### Step 4 (Optional): Add filters

Specify a filter to determine which records to transfer. Amazon AppFlow enables you to filter
data fields by adding multiple filters and by adding criteria to a filter. If you want to filter
the documents by **Document subtype** or **Document
Classification** you can add the appropriate filters here.

1. Based on the selected field names choose appropriate filter condition.
2. Choose **Next**.

###### Step 5: Review and create

- Review the information for your flow. To change the information for a step, choose
  **Edit**. When you are finished, choose **Create flow**.

## Notes

- When you use Veeva as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per minute.

## Supported destinations

When you create a flow that uses Veeva as the data source, you can set the destination to any of the following connectors:

- Amazon Connect
- Amazon Honeycode
- Lookout for Metrics
- Amazon Redshift
- Amazon S3
- Marketo
- Salesforce
- Snowflake
- Upsolver
- Zendesk

You can also set the destination to any custom connectors that you
create with the Amazon AppFlow Custom Connector SDKs for [Python](https://github.com/awslabs/aws-appflow-custom-connector-python "https://github.com/awslabs/aws-appflow-custom-connector-python") or [Java](https://github.com/awslabs/aws-appflow-custom-connector-java "https://github.com/awslabs/aws-appflow-custom-connector-java") . You can download these SDKs from GitHub.

## Related resources

- [API access permissions](https://docs-vdm.veevanetwork.com/doc/vndocad/Content/Network_topics/Whats_new/20R2.0/Users.htm#api "https://docs-vdm.veevanetwork.com/doc/vndocad/Content/Network_topics/Whats_new/20R2.0/Users.htm#api") in the Veeva Product Support Portal
