# Preparing a dataset based on file data

Use the following procedure to prepare a dataset based on text or Microsoft Excel
files from either your local network or Amazon S3.

###### To prepare a dataset based on text or Microsoft Excel files from a local network

or S3

1. Open a file dataset for data preparation by choosing one of the following
   options:
   - Create a new local file dataset, and then choose
     **Edit/Preview data**. For more information about
     creating a new dataset from a local text file, see [Creating a dataset using a local text
     file](../../../quicksight/latest/user/create-a-data-set-file.md "../../../quicksight/latest/user/create-a-data-set-file.md"). For more information about creating a new dataset from
     a Microsoft Excel file, see [Creating a dataset using a Microsoft Excel
     file](../../../quicksight/latest/user/create-a-data-set-excel.md "../../../quicksight/latest/user/create-a-data-set-excel.md").
   - Create a new Amazon S3 dataset, and then choose **Edit/Preview
     data**. For more information about creating a new Amazon S3
     dataset using a new Amazon S3 data source, see [Creating a dataset using Amazon S3 files](../../../quicksight/latest/user/create-a-data-set-s3.md "../../../quicksight/latest/user/create-a-data-set-s3.md").
     For more information about creating a new Amazon S3 dataset using an existing
     Amazon S3 data source, see [Creating a dataset using an existing Amazon S3 data
     source](../../../quicksight/latest/user/create-a-data-set-existing-s3.md "../../../quicksight/latest/user/create-a-data-set-existing-s3.md").
   - Open an existing Amazon S3, text file, or Microsoft Excel dataset for
     editing, from either the analysis page or the **Your
     Datasets** page. For more information about opening an
     existing dataset for data preparation, see [Editing datasets](../../../quicksight/latest/user/edit-a-data-set.md "../../../quicksight/latest/user/edit-a-data-set.md").

2. (Optional) On the data preparation page, enter a new name into the dataset
   name box on the application bar.

This name defaults to the file name for local files. For example, it defaults
to `Group 1` for Amazon S3 files. 3. Review the file upload settings and correct them if necessary. For more
information about file upload settings, see [Choosing file upload settings](../../../quicksight/latest/user/choosing-file-upload-settings.md "../../../quicksight/latest/user/choosing-file-upload-settings.md").

###### Important

If you want to change upload settings, make this change before you make
any other changes to the dataset. New upload settings cause Amazon Quick Sight to
reimport the file. This process overwrites all of your other changes. 4. Prepare the data by doing one or more of the following:

    * [Selecting fields](../../../quicksight/latest/user/selecting-fields.md "../../../quicksight/latest/user/selecting-fields.md")
    * [Editing field names and
     descriptions](../../../quicksight/latest/user/changing-a-field-name.md "../../../quicksight/latest/user/changing-a-field-name.md")
    * [Changing a field data type](../../../quicksight/latest/user/changing-a-field-data-type.md "../../../quicksight/latest/user/changing-a-field-data-type.md")
    * [Adding calculated fields](../../../quicksight/latest/user/adding-a-calculated-field-analysis.md "../../../quicksight/latest/user/adding-a-calculated-field-analysis.md")
    * [Filtering data in Amazon Quick Sight](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md")

5. Check the [SPICE](spice.md "spice.md") indicator to see
   if you have enough capacity to import the dataset. File datasets automatically
   load into SPICE. The import happens when you choose either
   **Save & visualize** or **Save**.

If you don't have access to enough SPICE capacity, you can make
the dataset smaller by using one of the following options:

    * Apply a filter to limit the number of rows.
    * Select fields to remove from the dataset.

###### Note

The SPICE indicator doesn't update to how much space you
save by removing fields or filtering the data. It continues to reflect the
SPICE usage from the last import. 6. Choose **Save** to save your work, or
**Cancel** to cancel it.

You might also see **Save & visualize**. This option
appears based on the screen that you started from. If this option isn't there,
you can create a new visualization by starting from the dataset screen.

## Preparing a dataset based on a Microsoft

Excel file

Use the following procedure to prepare a Microsoft Excel dataset.

###### To prepare a Microsoft Excel dataset

1. Open a text file dataset for preparation by choosing one of the following
   options:
   - Create a new Microsoft Excel dataset, and then choose
     **Edit/Preview data**. For more information
     about creating a new Excel dataset, see [Creating a dataset using a Microsoft Excel
     file](../../../quicksight/latest/user/create-a-data-set-excel.md "../../../quicksight/latest/user/create-a-data-set-excel.md").
   - Open an existing Excel dataset for editing. You can do this from
     the analysis page or the **Your Datasets** page.
     For more information about opening an existing dataset for data
     preparation, see [Editing datasets](../../../quicksight/latest/user/edit-a-data-set.md "../../../quicksight/latest/user/edit-a-data-set.md").

2. (Optional) On the data preparation page, enter a name into the dataset
   name box in the application bar. If you don't rename the dataset, its name
   defaults to the Excel file name.
3. Review the file upload settings and correct them if necessary. For more
   information about file upload settings, see [Choosing file upload settings](../../../quicksight/latest/user/choosing-file-upload-settings.md "../../../quicksight/latest/user/choosing-file-upload-settings.md").

###### Important

If it's necessary to change upload settings, make this change
before you make any other changes to the dataset. Changing upload
settings causes Amazon Quick Sight to reimport the file. This process overwrites
any changes you have made so far. 4. (Optional) Change the worksheet selection. 5. (Optional) Change the range selection. To do this, open **Upload
Settings** from the on-dataset menu beneath the login name at
upper right. 6. Prepare the data by doing one or more of the following:

    * [Selecting fields](../../../quicksight/latest/user/selecting-fields.md "../../../quicksight/latest/user/selecting-fields.md")
    * [Editing field names and
     descriptions](../../../quicksight/latest/user/changing-a-field-name.md "../../../quicksight/latest/user/changing-a-field-name.md")
    * [Changing a field data type](../../../quicksight/latest/user/changing-a-field-data-type.md "../../../quicksight/latest/user/changing-a-field-data-type.md")
    * [Adding calculated fields](../../../quicksight/latest/user/adding-a-calculated-field-analysis.md "../../../quicksight/latest/user/adding-a-calculated-field-analysis.md")
    * [Filtering data in
     Quick Sight](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md")

7. Check the [SPICE](spice.md "spice.md") indicator to
   see if you have enough space to import the dataset. Amazon Quick Sight must import
   Excel datasets into SPICE. This import happens when you
   choose either **Save & visualize** or
   **Save**.

If you don't have enough SPICE capacity, you can choose to
make the dataset smaller using one of the following methods:

    * Apply a filter to limit the number of rows.
    * Select fields to remove from the dataset.
    * Define a smaller range of data to import.

###### Note

The SPICE indicator doesn't update to reflect your
changes until after your load them. It shows the SPICE
usage from the last import. 8. Choose **Save** to save your work, or
**Cancel** to cancel it.

You might also see **Save & visualize**. This option
appears based on the screen that you started from. If this option isn't
there, you can create a new visualization by starting from the dataset
screen.
