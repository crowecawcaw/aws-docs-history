# Re-import a deleted sample dataset

Amazon SageMaker Canvas provides you with sample datasets for various use cases that highlight
the capabilities of Canvas. To learn more about the sample datasets that are available,
see [Sample datasets in Canvas](canvas-sample-datasets.md "canvas-sample-datasets.md").
If you no longer wish to use the sample datasets, you can delete them from the
**Datasets** page of your SageMaker Canvas application. However, these
datasets are still stored in the Amazon S3 bucket that you specified as the [Canvas storage location](canvas-storage-configuration.md "canvas-storage-configuration.md"),
so you can always access them later.

If you used the default Amazon S3 bucket, the bucket name follows the pattern
`sagemaker-`{region}`-`{account
ID}``. You can find the sample datasets in the directory
 path `Canvas/sample_dataset`.

If you delete a sample dataset from your SageMaker Canvas application and want to access
the sample dataset again, use the following procedure.

1. Navigate to the **Datasets** page in your SageMaker Canvas
   application.
2. Choose **Import data**.
3. From the list of Amazon S3 buckets, select the bucket that is your Canvas storage location.
   If using the default SageMaker AI-created Amazon S3 bucket, it follows the naming pattern `sagemaker-`{region}`-`{account
   ID}``.
4. Select the **Canvas** folder.
5. Select the **sample_dataset** folder, which contains all
   of the sample datasets for SageMaker Canvas.
6. Select the dataset you want to import, and then choose **Import
   data**.
