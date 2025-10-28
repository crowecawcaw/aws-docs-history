# Send your model to Quick Suite

If you use Quick Suite and want to leverage SageMaker Canvas in your Quick Suite visualizations, you can build
an Amazon SageMaker Canvas model and use it as a _predictive field_ in
your Quick Suite dataset. A _predictive field_ is a field in
your Quick Suite dataset that can make predictions for a given column in your dataset, similar
to how Canvas users make single or batch predictions with a model. To learn more about
how to integrate Canvas predictive abilities into your Quick Suite datasets, see
[SageMaker Canvas integration](../../../quicksight/latest/user/sagemaker-canvas-integration.md "../../../quicksight/latest/user/sagemaker-canvas-integration.md") in
the [Quick Suite User
Guide](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md").

The following steps explain how you
can add a predictive field to your Quick Suite dataset using a Canvas model:

1. Open the Canvas application and build a model with your
   dataset.
2. After building the model in Canvas, send the model to Quick Suite. A
   schema file automatically downloads to your local machine when you send the model to
   Quick Suite. You upload this schema file to Quick Suite in the next step.
3. Open Quick Suite and choose a dataset with the same schema as the
   dataset you used to build your model. Add a predictive field to the
   dataset and do the following:
   1. Specify the model sent from Canvas.
   2. Upload the schema file that was downloaded in Step 2.

4. Save and publish your changes, and then generate predictions for the
   new dataset. Quick Suite uses the model to fill in the target column with
   predictions.
   In order to send a model from Canvas to Quick Suite, you must meet the following
   prerequisites:

- You must have both Canvas and Quick Suite set up. Your Quick Suite
  account must be created in the same AWS Region as your Canvas application. If your
  Quick Suite account’s home Region differs from your Canvas application’s Region,
  you must either [close](../../../quicksight/latest/user/closing-account.md "../../../quicksight/latest/user/closing-account.md") and recreate
  your Quick Suite account, or [set
  up a Canvas application](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites") in the same Region as your Quick Suite
  account. Your Quick Suite account must also contain the default namespace, which you
  set up when you first create your Quick Suite account. Contact your administrator to
  help you get access to Quick Suite. For more information, see [Setting up for
  Quick Suite](../../../quicksight/latest/user/setting-up.md "../../../quicksight/latest/user/setting-up.md") in the _Quick Suite User Guide_.
- Your user must have the necessary AWS Identity and Access Management (IAM)
  permissions to send your predictions to Quick Suite. Your
  administrator can set up the IAM permissions for your user. For more
  information, see [Grant Your Users Permissions to Send Predictions to Quick Suite](canvas-quicksight-permissions.md "canvas-quicksight-permissions.md").
- Quick Suite must have access to the Amazon S3 bucket that you’ve
  specified for Canvas application storage. For more information, see
  [Configure your Amazon S3 storage](canvas-storage-configuration.md "canvas-storage-configuration.md").
