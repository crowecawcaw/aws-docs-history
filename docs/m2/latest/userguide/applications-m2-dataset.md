AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Import data sets for AWS Mainframe Modernization applications

With AWS Mainframe Modernization you can import data sets to use with your applications. You can specify the
data sets to be imported in a JSON file stored in an Amazon S3 bucket, or you can specify data
set configuration values separately. After you import the data sets, you can review the details
of the import task to confirm that the data sets that you wanted were imported. All cataloged
data sets for an application are listed together in the console.

Use the AWS Mainframe Modernization console to import data sets for a AWS Mainframe Modernization application.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md") and in [Create an AWS Mainframe Modernization application](applications-m2-create.md "applications-m2-create.md").

## Import a data set

###### To import a data set

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the application that you want to
   import data sets for was created.
3. On the **Applications** page, choose the application that you want to
   import data sets for.
4. On the application details page, choose **Data sets**.
5. Choose **Import**.
6. Do one of the following:
   - Choose **Use data set configuration JSON file in an Amazon S3 bucket**
     and provide the location of the data set configuration.
   - Choose **Specify the data set configuration values separately** with
     guided configuration. Refer [AWS Mainframe Modernization data set definition reference](datasets-m2-definition.md "datasets-m2-definition.md") for specific definition
     details.

   Enter the name, data set organization (VSAM, GDG, PO, PS), location, and external Amazon S3
   location, and parameter settings for each data set configuration value.
   In guided configuration you can also choose **Generate JSON** to review JSON configuration from your input.

7. Choose **Submit**.
