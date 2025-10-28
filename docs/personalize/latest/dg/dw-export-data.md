# Processing data and importing it into Amazon Personalize

When you are finished analyzing and transforming your data, you are ready to process it and import it into Amazon Personalize.

- **[Processing data](#dw-process-data "#dw-process-data")** – Processing the data
  applies your transform to your entire dataset and outputs it to a destination you specify. In this case you specify an
  Amazon S3 bucket.
- **[Importing data into Amazon Personalize](#dw-import-into-personalize "#dw-import-into-personalize")**
  – To import processed data into Amazon Personalize, you run a Jupyter Notebook provided in SageMaker AI Studio Classic. This notebook creates
  your Amazon Personalize datasets and imports your data into them.

## Processing data

Before you import data into Amazon Personalize, you must apply your transform to your entire dataset and output it to an Amazon S3 bucket.
To do this, you create a destination node with the destination set to an Amazon S3 bucket,
and then launch a processing job for the transformation.

For step-by-step instructions on specifying a destination and launching a process job, see [Launch processing
jobs with a few clicks using Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/launch-processing-jobs-with-a-few-clicks-using-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/launch-processing-jobs-with-a-few-clicks-using-amazon-sagemaker-data-wrangler/") . When you add a destination, choose **Amazon S3**. You will
use this location when you import the processed data into Amazon Personalize.

When you finish processing your data, you are ready to import it from the Amazon S3 bucket into Amazon Personalize.

## Importing data into Amazon Personalize

After you process your data, you are ready to import it into Amazon Personalize. To import processed data into Amazon Personalize, you run a
Jupyter Notebook provided in SageMaker AI Studio Classic. This notebook creates your Amazon Personalize datasets and imports your data into
them.

###### To import processed data into Amazon Personalize

1. For the transformation you want to export, choose **Export to** and choose **Amazon Personalize (via
   Jupyter Notebook)**.
2. Modify the notebook to specify the Amazon S3 bucket you used as the data destination for the processing job. Optionally
   specify the domain for your dataset group. By default, the notebook creates a custom dataset group.
3. Review the notebook cells that create the schema. Verify that the schema fields have the expected types and attributes before
   running the cell.
   - Verify that fields that support null data have `null` listed in the list of types.
     The following example shows how to add `null` for a field.

   ```
   {
     "name": "GENDER",
     "type": [
       "null",
       "string"
     ],
     "categorical": true
   }
   ```

   - Verify that categorical fields have the categorical attribute set to true. The following example shows how to
     mark a field categorical.

   ```
   {
             "name": "SUBSCRIPTION_MODEL",
             "type": "string",
             "categorical": true
   }
   ```

   - Verify that textual fields have the textual attribute set to true. The following example shows how to mark
     a field as textual.

   ```
   {
         "name": "DESCRIPTION",
         "type": [
           "null",
           "string"
         ],
         "textual": true
   }
   ```

4. Run the notebook to create a schema, and create dataset, and import your data into the Amazon Personalize dataset. You run the
   notebook just as you would a notebook outside of SageMaker AI Studio Classic. For information on running Jupyter notebooks, see [Running Code](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running Code.html "https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running Code.html").
   For information on notebooks in SageMaker AI Studio Classic, see [Use Amazon SageMaker AI Notebooks](../../../sagemaker/latest/dg/notebooks.md "../../../sagemaker/latest/dg/notebooks.md") in the _Amazon SageMaker AI Developer Guide_.

After you complete the notebook, if you imported interactions data, you are ready to create recommenders or
custom resources. Or you can repeat the process with an items dataset or users dataset.

    * For information about creating a domain recommenders, see [Domain recommenders in Amazon Personalize](creating-recommenders.md "creating-recommenders.md").
    * For information about creating and deploying custom resources, see [Custom resources for training and deploying Amazon Personalize models](create-custom-resources.md "create-custom-resources.md").
