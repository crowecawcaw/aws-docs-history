We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Step 3: Create an ML Model

After you've created the training datasource, you use it to create an ML model, train the
model, and then evaluate the results. The ML model is a collection of patterns that Amazon ML finds
in your data during training. You use the model to create predictions.

###### To create an ML model

1. Because the Get started wizard creates both a training datasource and a model, Amazon Machine Learning
   (Amazon ML) automatically uses the training datasource that you just created, and takes you
   directly to the **ML model settings** page. On the **ML model
   settings** page, for **ML model name**, make sure that the
   default, `ML model: Banking Data 1`, is displayed.

Using a friendly name, such as the default, helps you easily identify and manage the ML
model. 2. For **Training and evaluation settings**, ensure that
**Default** is selected.

![Select training and evaluation settings interface with Default option selected.](images/image19.png) 3. For **Name this evaluation**, accept the default,
`Evaluation: ML model: Banking Data 1`. 4. Choose **Review**, review your settings, and then choose
**Finish**.

After you choose **Finish**, Amazon ML adds your model to the processing
queue. When Amazon ML creates your model, it applies the defaults and performs the following
actions:

    * Splits the
     training
     datasource into two sections, one containing 70% of the data and one containing the
     remaining 30%
    * Trains the ML model on the section that contains 70% of the input data
    * Evaluates the model using the remaining 30% of the input data

While your model is in the queue, Amazon ML reports the status as
**Pending**. While Amazon ML creates your model, it reports the status as
**In Progress**. When it has completed all actions, it reports the status
as **Completed**. Wait for the evaluation to complete before
proceeding.
Now you are ready to [review your model's
performance and set a cut-off score](step-4-review-model-and-set-cutoff.md "step-4-review-model-and-set-cutoff.md").

For more information about training and evaluating models, see [Training ML Models](training-ml-models.md "training-ml-models.md") and [evaluate an ML model](evaluating_models.md "evaluating_models.md").
