We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Step 6: Clean Up

To avoid accruing additional Amazon Simple Storage Service (Amazon S3) charges, delete the data stored in Amazon S3. You
are not charged for other unused Amazon ML resources, but we recommend that you delete them to keep
your workspace clean.

###### To delete the input data stored in Amazon S3

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Navigate to the Amazon S3 location where you stored the `banking.csv` and
   `banking-batch.csv` files.
3. Select the `banking.csv`, `banking-batch.csv`, and
   `.writePermissionCheck.tmp` files.
4. Choose **Actions**, and then choose **Delete**.
5. When prompted for confirmation, choose **OK**.
   Although you aren't charged for keeping the record of the batch prediction that Amazon ML ran or
   the datasources, model, and evaluation that you created during the tutorial, we recommend that
   you delete them to prevent cluttering your workspace.

###### To delete the batch predictions

1. Navigate to the Amazon S3 location where you stored the output of the batch prediction.
2. Choose the `batch-prediction` folder.
3. Choose **Actions**, and then choose **Delete**.
4. When prompted for confirmation, choose **OK**.

###### To delete the Amazon ML resources

1. On the Amazon ML dashboard, select the following resources.
   - The `Banking Data 1` datasource
   - The `Banking Data 1_[percentBegin=0, percentEnd=70,
strategy=sequential]` datasource
   - The `Banking Data 1_[percentBegin=70, percentEnd=100,
strategy=sequential]` datasource
   - The `Banking Data 2` datasource
   - The `ML model: Banking Data 1` ML model
   - The `Evaluation: ML model: Banking Data 1`
     evaluation

2. Choose **Actions**, and then choose **Delete**.
3. In the dialog box, choose **Delete** to delete all selected
   resources.
   You have now successfully completed the tutorial. To continue using the console to create
   datasources, models, and predictions see the [Amazon Machine Learning Developer Guide](../dg.md "../dg.md").
   To learn how to use the API, see the [Amazon Machine Learning API
   Reference](../APIReference.md "../APIReference.md").
