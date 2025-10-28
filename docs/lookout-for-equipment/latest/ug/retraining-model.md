On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Retraining your model

## Understanding retraining

This section explains model retraining in the context of Lookout for Equipment.

Because machines operating modes and health change over time (leading to [data drift](versioning-model.md "versioning-model.md") ), models developed for these machines
should be updated periodically to reflect these changes. Retraining is the process of
updating a machine learning model to take more recent information (that is, data and
[labels](labeling-data.md "labeling-data.md")) about the machine into consideration.
Retraining is the preferred method of addressing data drift.

When retraining a model Lookout for Equipment does not require you to run a new ingestion job. This is
an important benefit, because you may have many assets running in your factory and
setting up new ingestion jobs on thousands of machines could become an
inconvenience.

###### Note

You may have been running inference on some models before AWS released the
retraining feature for Lookout for Equipment. In that case, your inference data has not been collected and will not be available for retraining. In order to facilitate
the retraining process, you should [run a new
ingestion job](ingest-dataset.md "ingest-dataset.md") on those models.

By enabling retraining in Lookout for Equipment, you can [schedule](#retraining-model-scheduler-setup "#retraining-model-scheduler-setup") to have the system
generate updated models on an ongoing basis without pausing your data-gathering process.
Once a model is retrained it creates a new model [version](versioning-model.md "versioning-model.md").

You may choose to [manually](versioning-model.md#model-activation "versioning-model.md#model-activation") control the activation of new models utilizing [retraining metrics](#retraining-understanding-metrics "#retraining-understanding-metrics"), or you may
choose to allow Lookout for Equipment to activate your new models immediately utilizing managed mode,
when appropriate.

## Setting up your retraining

scheduler

This section describes how set up your retraining scheduler.

The following APIs will help you manage your retraining scheduler:

- [CreateRetrainingScheduler](API_CreateRetrainingScheduler.md "API_CreateRetrainingScheduler.md")
- [DescribeRetrainingScheduler](API_DescribeRetrainingScheduler.md "API_DescribeRetrainingScheduler.md")
- [ListRetrainingSchedulers](API_ListRetrainingSchedulers.md "API_ListRetrainingSchedulers.md")
- [StartRetrainingScheduler](API_StartRetrainingScheduler.md "API_StartRetrainingScheduler.md")
- [StopRetrainingScheduler](API_StopRetrainingScheduler.md "API_StopRetrainingScheduler.md")
- [DeleteRetrainingScheduler](API_DeleteRetrainingScheduler.md "API_DeleteRetrainingScheduler.md")

When you set up a retraining schedule, there are two modes to be aware of for managing
the selection of newly trained versions:

- In _manual mode_, the model is periodically retrained, but
  the new model versions are not [activated](versioning-model.md#model-activation "versioning-model.md#model-activation")
  until you indicate that it's time to activate them. This might be because you
  want to provide your own methodology, using [metrics that describe the
  model](#retraining-understanding-metrics "#retraining-understanding-metrics"), for determining if the newly trained version is better than
  the current version, or you might have a custom process to have extra testing
  done in a production environment which needs user sign-off.
- In _managed mode_, the model is periodically retrained, and
  then Lookout for Equipment automatically compares the metrics from the new
  version with the [metrics](#retraining-understanding-metrics "#retraining-understanding-metrics")
  version that is currently running. If Lookout for Equipment determines that the new version is
  more accurate than the current version, then Lookout for Equipment automatically activates the
  new version.

Both of these modes are set using the PromoteMode parameter in the [CreateRetrainingScheduler](API_CreateRetrainingScheduler.md "API_CreateRetrainingScheduler.md") API.

## Understanding retraining data

This section explains how data is used for retraining, including the way that
inference data is accumulated and stored.

When the inference scheduler is running, Lookout for Equipment accumulates and manages the inference
data that it successfully processes. This allows Lookout for Equipment to use inference data as an input
during retraining without the user having to manage providing the service updated data.
Lookout for Equipment encrypts the stored data using either a customer-owned AWS KMS key configured
as the model's ServerSideKmsKeyId, or, if there is no customer-owned AWS KMS key
provided, then using a Lookout for Equipment-owned AWS KMS key.

Sensor data used for retraining comes from both a) the dataset associated with the
model being retrained and b) the accumulated inference data for that model. Lookout for Equipment only
uses the data from those two sources that falls within the [LookbackWindow](API_CreateRetrainingScheduler.md "API_CreateRetrainingScheduler.md")
of the model’s retraining scheduler. If, within that window, there is an overlap between
the dataset and the accumulated inference data, the dataset takes priority.

During the retraining process, Lookout for Equipment also fetches labels from the location configured in
the model's [LabelsInputConfiguration](API_LabelsInputConfiguration.md "API_LabelsInputConfiguration.md").

## Understanding retraining

metrics

This section describes retraining metrics in the context of Lookout for Equipment.

If you are retraining in manual mode, then you may use these metrics to help you
decide whether to [activate](versioning-model.md#model-activation "versioning-model.md#model-activation") a new model version.

The following table lists the model promotion criterion.

| Old data has labels? | New data has labels? | Model promotion criterion                                               | Metrics shown?         |
| -------------------- | -------------------- | ----------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes                  | Yes                  | Select best model based on comparison metrics                           | Yes for both models    |
| Yes                  | No                   | Select old model                                                        | No for both models     |
| No                   | Yes                  | Select new model, if the new model meets the required quality threshold | Yes for new model only |
| No                   | No                   | Select new model                                                        | No for both models     | ### Model metrics The following `Model Metrics` are exposed in the [DescribeModelVersion](API_DescribeModelVersion.md "API_DescribeModelVersion.md") response. If a retrained model is the current active model version, then the same information is also returned in the [DescribeModel](API_DescribeModel.md "API_DescribeModel.md") response. <br>• **Recall:** The proportion of events that Lookout for Equipment correctly identified to the events that you labeled during the same period. For example, you may have labeled 10 events, but Lookout for Equipment only identified 9 of them. In this case, the recall is 90%. <br>• **Precision:** The proportion of true positives to total identified events. For example, if Lookout for Equipment identifies 10 events, but only 7 of those events correspond to events you labeled, then the precision is 70%. <br>• **MeanFractionalLeadTime:** A measurement of how quickly (relative to the length of the event), on average, Lookout for Equipment detects each event. For example, a typical event at your facility may last 10 hours. On average, it may take the model 3 hours to identify the event. In this case, the mean fractional lead time is 0.7. <br>• **AUC:** Area Under the Receiver Operating Characteristic Curve (AUC) measures the ability of a machine learning model to predict a higher score for positive examples as compared to negative examples. A value between 0 and 1 that indicates how well your model is able to separate the categories in your dataset. A value of 1 indicates that it was able to separate the categories perfectly. For more information, see ["A Visual Explanation of Receiver Operating Characteristic Curves and Area Under the Curve"](https://mlu-explain.github.io/roc-auc/ "https://mlu-explain.github.io/roc-auc/") at the _MLU Explain_ website. ### Model quality If new data has labels, Lookout for Equipment uses the metrics to perform a quality assessment of the model. To get the quality assessment, check the `ModelQuality` field in the response from [DescribeModel](API_DescribeModel.md "API_DescribeModel.md"), [DescribeModelVersion](API_DescribeModelVersion.md "API_DescribeModelVersion.md"), [ListModels](API_ListModels.md "API_ListModels.md"), [ListModelVersions](API_ListModelVersions.md "API_ListModelVersions.md"), or [CreateInferenceScheduler](API_CreateInferenceScheduler.md "API_CreateInferenceScheduler.md"). If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is `POOR_QUALITY_DETECTED`. Otherwise, the value is `QUALITY_THRESHOLD_MET`. If the model is unlabeled, the model quality can't be assessed and the value of `ModelQuality` is `CANNOT_DETERMINE_QUALITY`. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model. If the previous model was labeled, Lookout for Equipment compares the metrics of each model on the new data to determine if the new model should be promoted. The quality assessment for the new model does not affect this comparison. If the previous model was unlabeled, Lookout for Equipment promotes the new model if the quality threshold is met. For information about using labels with your models, see [Understanding labeling](understanding-labeling.md "understanding-labeling.md"). For information about improving the quality of a model, see [Best practices with Amazon Lookout for Equipment](best-practices.md "best-practices.md"). |
