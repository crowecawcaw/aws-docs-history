# Creating a dataset using a Microsoft Excel

file

To create a dataset using a Microsoft Excel file data source, upload an .xlsx file
from a local or networked drive. The data is imported into [SPICE](spice.md "spice.md").

For more information about creating new Amazon S3 datasets using Amazon S3 data sources, see
[Creating a dataset using an existing
Amazon S3 data source](create-a-data-set-existing.md#create-a-data-set-existing-s3 "create-a-data-set-existing.md#create-a-data-set-existing-s3") or [Creating a dataset using Amazon S3 files](create-a-data-set-s3.md "create-a-data-set-s3.md").

###### To create a dataset based on an excel file

1. Check [Data source quotas](data-source-limits.md "data-source-limits.md")
   to make sure that your target file doesn't exceed data source quotas.
2. On the Quick Suite start page, choose **Data**.
3. On the **Data** page, choose **Create**
   then **New dataset**.
4. Choose **Upload a file**.
5. In the **Open** dialog box, choose a file, and then choose
   **Open**.

A file must be 1 GB or less to be uploaded to Quick Sight. 6. If the Excel file contains multiple sheets, choose the sheet to import. You
can change this later by preparing the data. 7. ###### Note

On the following screens, you have multiple chances to prepare the data.
Each of these takes you to the **Prepare Data** screen.
This screen is the same one where you can access after the data import is
complete. It enables you to change the upload settings even after the upload
is complete.

Choose **Select** to confirm your settings. Or you can
choose **Edit/Preview data** to prepare the data
immediately.

A preview of the data appears on the next screen. You can't make changes
directly to the data preview. 8. If the data headings and content don't look correct, choose **Edit
settings and prepare data** to correct the file upload settings.

Otherwise, choose **Next**. 9. On the **Data Source Details** screen, you can choose
**Edit/Preview data**. You can specify a dataset name in
the **Prepare Data** screen.

If you don't need to prepare the data, you can choose to create an analysis
using the data as-is. Choose **Visualize**. Doing this names
the dataset the same as the source file, and takes you to the
**Analysis** screen. To learn more about data preparation
and excel upload settings, see [Preparing data in Amazon Quick Sight](preparing-data.md "preparing-data.md").

###### Note

If at anytime you want to make changes to the file, such as adding a new field,you
must make the change in Microsoft Excel and create a new dataset using the updated
version in Quick Sight. For more information about possible implications of
changing datasets, see [Things to consider when editing datasets](edit-a-data-set.md#change-a-data-set "edit-a-data-set.md#change-a-data-set") .
