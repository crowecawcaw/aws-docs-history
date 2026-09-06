

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Export data sets for AWS Mainframe Modernization applications
<a name="applications-m2-dataset.export"></a>

With AWS Mainframe Modernization you can export data sets to use with your applications. You can specify the data sets to be exported in a JSON file stored in an Amazon S3 bucket, or you can specify data set configuration values separately. After you export the data sets, you can review the details of the export task to confirm that the data sets that you wanted were exported.

Use the AWS Mainframe Modernization console to export data sets for a AWS Mainframe Modernization application.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md) and in [Create an AWS Mainframe Modernization application](applications-m2-create.md).

## Export a data set
<a name="applications-m2-dataset-export.console"></a>

**To export a dataset**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where the application that you want to import data sets for was created.

1. On the **Applications** page, choose the application that you want to export data sets for.

1. On the application details page, choose **Data sets**.

1. Choose **Export**.

1. Do one of the following:
   + Choose **Use data set configuration JSON file in an Amazon S3 bucket** and provide the location of the data set configuration.
   + Choose **Specify the data set configuration values separately** with guided configuration. For more information, see [AWS Mainframe Modernization data set definition reference](datasets-m2-definition.md).

     Enter the dataset name, external Amazon S3 location, and parameter settings for each data set configuration value. In guided configuration you can also choose **Generate JSON** to review JSON configuration from your input.

1. Choose **Submit**.