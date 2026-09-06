

# Creating a dataset using a local text file
<a name="create-a-data-set-file"></a>

To create a dataset using a local text file data source, identify the location of the file, and then upload it. The file data is automatically imported into [SPICE](spice.md) as part of creating a dataset. 

**To create a dataset based on a local text file**

1. Check [Data source quotas](data-source-limits.md) to make sure that your target file doesn't exceed data source quotas.

   Supported file types include .csv, .tsv, .json, .clf, or .elf files.

1. On the Quick start page, choose **Data**.

1. Choose **Create ** then **New dataset**.

1. Choose **Upload a file**.

1. In the **Open** dialog box, browse to a file, select it, and then choose **Open**.

   A file must be 1 GB or less to be uploaded to Quick Sight.

1. To prepare the data before creating the dataset, choose **Edit/Preview data**. Otherwise, choose **Visualize** to create an analysis using the data as-is. 

   If you choose the former, you can specify a dataset name as part of preparing the data. If you choose the latter, a dataset with the same name as the source file is created. To learn more about data preparation, see [Preparing data in Amazon Quick Sight](preparing-data.md).