

# Preparing a dataset based on Salesforce data
<a name="prepare-salesforce-data"></a>

Use the following procedure to prepare a Salesforce dataset.

**To prepare a Salesforce dataset**

1. Open a Salesforce dataset for preparation by choosing one of the following options:
   + Create a new Salesforce dataset and choose **Edit/Preview data**. For more information about creating a new Salesforce dataset using a new Salesforce data source, see [Creating a dataset from Salesforce](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-salesforce.html). For more information about creating a new Salesforce dataset using an existing Salesforce data source, see [Create a dataset using an existing Salesforce data source](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-existing-salesforce.html).
   + Open an existing Salesforce dataset for editing from either the analysis page or the **Your Datasets** page. For more information about opening an existing dataset for data preparation, see [Editing datasets](https://docs.aws.amazon.com/quicksight/latest/user/edit-a-data-set.html).

1. (Optional) On the data preparation page, enter a name into the dataset name box in the application bar if you want to change the dataset name. This name defaults to the report or object name.

1. (Optional) Change the data element selection to see either reports or objects.

1. (Optional) Change the data selection to choose a different report or object.

   If you have a long list in the **Data** pane, you can search to locate a specific item by entering a search term into the **Search tables** box. Any item whose name contains the search term is shown. Search is case-insensitive and wildcards are not supported. Choose the cancel icon (**X**) to the right of the search box to return to viewing all items.

1. Prepare the data by doing one or more of the following:
   + [Selecting fields](https://docs.aws.amazon.com/quicksight/latest/user/selecting-fields.html)
   + [Editing field names and descriptions](https://docs.aws.amazon.com/quicksight/latest/user/changing-a-field-name.html)
   + [Changing a field data type](https://docs.aws.amazon.com/quicksight/latest/user/changing-a-field-data-type.html)
   + [Adding calculated fields](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-calculated-field-analysis.html)
   + [Filtering data in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html)

1. Check the [SPICE](spice.md) indicator to see if you have enough space to import the dataset. Importing data into SPICE is required for Salesforce datasets. Importing occurs when you choose either **Save & visualize** or **Save**.

   If you don't have enough SPICE capacity, you can remove fields from the dataset or apply a filter to decrease its size. For more information about adding and removing fields from a dataset, see [Selecting fields](https://docs.aws.amazon.com/quicksight/latest/user/selecting-fields.html).
**Note**  
The SPICE indicator doesn't update to reflect the potential savings of removing fields or filtering the data. It continues to reflect the size of the dataset as retrieved from the data source.

1. Choose **Save** to save your work, or **Cancel** to cancel it. 

   You might also see **Save & visualize**. This option appears based on the screen you started from. If this option isn't there, you can create a new visualization by starting from the dataset screen. 