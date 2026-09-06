

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Versioning your model
<a name="versioning-model"></a>

Machines' (assets') operating modes and health change over the course of their lifetimes. This is often referred to as *data drift*. Machines also go through expected, and unexpected, maintenance operations. Models developed for these machines must therefore be updated periodically to reflect these changes.

In the past, each training resulted in a separate model. When multiple models where related to the same asset, the only way to indicate that association was with the naming of the models (for example, pumpA\_model1, pumpA\_model2, and so forth), and you had to manage that association on your own.

With model versioning, you can store different versions of a model under the same model name, and then decide which model version you want to maintain as your [active version](#model-activation). After you set your active version, Lookout for Equipment utilizes that version when it runs inference on your asset's sensor data.

Model versioning also helps maintain traceability and history of a given model, and its corresponding machine, over time.

## Understanding model versioning
<a name="understanding-versioning"></a>

Currently, there are three ways to generate a model version:
+ Training a model for the first time. In this case, as the parent model is created, so is a corresponding model version, which may be called Version 1.
+ Importing a model from another account. In this case, if a model of the same name *does not* already exist in the target account, then the imported model becomes Version 1. If the imported model *does* already exist in the target account (and uses the same name), then the imported model gets the next available version number.
+ Retraining a model. In this case, a new version is created. It has the same name as the parent model, but a version number incremented by 1. Note that the new version number will be 1 more than the *most recent* version number, regardless of which version is currently active.

The following APIs will help you work with, and understand, model versioning.
+ [ListModelVersions:](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListModelVersions.html) all model versions for a given model, including the model version, model version ARN, and status. This list appears in the data type [ModelVersionSummary](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ModelVersionSummary.html).
+ [DescribeModelVersion:](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeModelVersion.html) This API gives you relevant information (such as the data start and end times and the creation time). If the model fails, then this API will indicate why it failed.

## Understanding model status
<a name="model-status"></a>

During the importation of a model, it will be in the state: `IMPORT_IN_PROGRESS`.

After you import a model, it will be in one of three states:
+ `SUCCESS`
+ `FAILED`
+ `CANCELED`

## Activating your model
<a name="model-activation"></a>

This section describes how to set one of your model versions as the active model. The active model is the one that the inference scheduler uses during inferencing.

By default, [in managed mode](retraining-model.md#retraining-model-scheduler-setup), the most recent version is active. However, if you are not satisfied with the most recent version, you can select a previous version.

Caveats to consider:
+ If you try activating a model while inference is currently running, then that inference execution will continue to use the model that was active when inference began. Lookout for Equipment will pick up the newly activated model the next time you run inference.
+ You cannot activate a model in the `FAILED` state.

The following API will help you in activating a model:

[UpdateActiveModelVersion:](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateActiveModelVersion.html) This activates a particular model. You can only activate a model that is in the `SUCCESS` state.