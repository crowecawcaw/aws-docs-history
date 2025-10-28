# Step 7: Install and Configure Data Extraction Agents

AWS SCT uses a data extraction agent to migrate data from BigQuery to Amazon Redshift. The .zip file that you downloaded to install AWS SCT, includes the extraction agent installer file. In this walkthrough, we install the data extraction agent on Windows. However, you can install data extraction agents on Red Hat Enterprise Linux or Ubuntu. For more information, see [Installing extraction agents](../../../SchemaConversionTool/latest/userguide/agents.md#agents.Installing "../../../SchemaConversionTool/latest/userguide/agents.md#agents.Installing").

**To install and configure a data extraction agent**

1. Find the `aws-schema-conversion-tool-extractor-2.0.1.<version>.msi` file in the `agents` folder. The number of the `<version>` in the file name depends on the version of AWS SCT that you use. To migrate data from BigQuery to Amazon Redshift, make sure that you use an extraction agent version 665 or higher.
2. Run the file.
3. Choose **Next**, accept the terms of the License Agreement, and choose **Next** again.
4. Enter the path to the folder where you want to install the data extraction agent, and choose **Next**.
5. Choose **Install**.
6. On Windows, the data extraction agent installer launches the configuration wizard in the command prompt window. On Linux, run the `sct-extractor-setup.sh` file from the location where you installed the agent.
7. For **Listening port**, enter `8192`. This is the default value. You can choose another port.
8. For **Add a source vendor**, enter `no`. You don’t need to configure the data extraction agent to work with your BigQuery data warehouse because you don’t need a driver to connect to BigQuery.
9. For **Add the Amazon Redshift driver**, enter `yes` and then enter the path to the Amazon Redshift JDBC driver that you downloaded in [Step 4](bigquery-redshift-migration-step-4.md "bigquery-redshift-migration-step-4.md").
10. For **Working folder**, enter the folder where the data extraction agent can store its data. Choose the project folder and make sure that you don’t need admin rights to write data to this folder.
11. For **Enable SSL communication**, enter `no`. Then enter `yes` to confirm your choice. In this walkthrough, we don’t use SSL to connect to databases. If you use SSL, configure the agent.
