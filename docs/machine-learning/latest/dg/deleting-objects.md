We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Deleting Objects

When you no longer need your datasources, ML models, evaluations, and batch predictions, you
can delete them. Although there is no additional cost for keeping Amazon ML objects other than batch
predictions after you are done with them, deleting objects keeps your workspace uncluttered and
easier to manage. You can delete single or multiple objects using the Amazon Machine Learning (Amazon ML) console or
the API.

###### Warning

When you delete Amazon ML objects, the effect is immediate, permanent, and irreversible.

![Objects table showing completed evaluations, ML models, and datasources with creation times.](images/image58b.png)

## Deleting Objects (Console)

You can use the Amazon ML console to delete objects, including models. The procedure that you
use to delete a model depends on whether you're using the model to generate real-time
predictions or not. To delete a model used to generate real-time predictions, first delete the
real-time endpoint.

###### To delete Amazon ML objects (console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. Select the Amazon ML objects that you want to delete. To select more than one object, use
   the SHIFT key. To deselect all selected objects, use the
   ![Blue rectangular button with minus sign icon, indicating a removal or subtraction action.](images/deselect-all.png)
   or
   ![Blue checkmark icon indicating a completed or selected state.](images/deselect-all2.png)
   buttons.
3. For **Actions**, choose **Delete**.
4. In the dialog box, choose **Delete** to delete the model.

###### To delete an Amazon ML model with a real-time endpoint

(console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. Select the model that you want to delete.
3. For **Actions**, choose **Delete real-time
   endpoint**.
4. Choose **Delete** to delete the endpoint.
5. Select the model again.
6. For **Actions**, choose **Delete**.
7. Choose **Delete** to delete the model.

## Deleting Objects (API)

You can delete Amazon ML objects using the following API calls:

- `DeleteDataSource` - Takes the parameter `DataSourceId`.
- `DeleteMLModel` - Takes the parameter `MLModelId`.
- `DeleteEvaluation` - Takes the parameter `EvaluationId`.
- `DeleteBatchPrediction` - Takes the parameter
  `BatchPredictionId`.

For more information, see the [Amazon Machine Learning API
Reference](../APIReference.md "../APIReference.md").
