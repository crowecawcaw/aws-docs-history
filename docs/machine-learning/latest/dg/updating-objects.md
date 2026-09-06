

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Updating Objects
<a name="updating-objects"></a>

Each object type has an operation that updates the details of an Amazon ML object (See [Amazon ML API Reference](https://docs.aws.amazon.com/machine-learning/latest/APIReference/)):
+ UpdateDataSource
+ UpdateMLModel
+ UpdateEvaluation
+ UpdateBatchPrediction

Each operation requires the object's ID to specify which object is being updated. You can update the names of all objects. You can't update any other properties of objects for datasources, evaluations, and batch predictions. For ML Models, you can update the ScoreThreshold field, as long as the ML model does not have a real-time prediction endpoint associated with it.