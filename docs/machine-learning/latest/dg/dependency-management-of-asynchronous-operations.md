We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Dependency Management of Asynchronous Operations

Batch operations in Amazon ML depend on other operations in order
to complete successfully. To manage these dependencies, Amazon ML
identifies requests that have dependencies, and verifies that the
operations have completed. If the operations have not completed,
Amazon ML sets the initial requests aside until the operations
that they depend on have completed.

There are some dependencies between batch operations. For example,
before you can create an ML model, you must have created a
datasource with which you can train the ML model. Amazon ML cannot
train an ML model if there is no datasource available.

However, Amazon ML supports dependency management for asynchronous
operations. For example, you do not have to wait until data
statistics have been computed before you can send a request to
train an ML model on the datasource. Instead, as soon as the
datasource is created, you can send a request to train an ML model
using the datasource. Amazon ML does not actually start the
training operation until the datasource statistics have been
computed. The createMLModel request is put into a queue until the
statistics have been computed; once that is done, Amazon ML
immediately attempts to run the createMLModel operation.
Similarly, you can send batch prediction and evaluation requests
for ML models that have not finished training.

The following table shows the requirements to proceed with
different AmazonML actions

| **In order to…**                                  | **You must have…**                       |
| ------------------------------------------------- | ---------------------------------------- |
| Create an ML model (createMLModel)                | Datasource with computed data statistics |
| Create a batch prediction (createBatchPrediction) | Datasource<br>ML model                   |
| Create a batch evaluation (createBatchEvaluation) | Datasource<br>ML model                   |
