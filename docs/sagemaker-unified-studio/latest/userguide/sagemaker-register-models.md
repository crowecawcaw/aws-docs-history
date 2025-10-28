# Model registry

Use the model registry to catalog your models and manage model deployment to production.

You catalog models by creating model (package) groups that contain different versions of a
model. You can create a model group that tracks all the models that you train to solve a
particular problem. You can then register each model you train and the model registry adds
it to the model group as a new model version.

You can create categories of model groups by organizing them into collections. A typical
workflow might include the following tasks:

1. Create a model group.
2. Create an ML pipeline that trains a model.
   For information about pipelines, see [Pipelines](sagemaker-pipelines.md "sagemaker-pipelines.md").
3. For each run of the ML pipeline, create a model version that you register in the
   model group you created in the first step.
4. Add your model group to one or more collections.
   For details about how to work with the model registry, see [Model Registry, Model
   Versions, and Model Groups](../../../sagemaker/latest/dg/model-registry-models.md "../../../sagemaker/latest/dg/model-registry-models.md") in the _Amazon SageMaker AI Developer Guide_.

## Create a model group

A model group contains different versions of a model. Follow these steps to create a
model group:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **Model Registry**. The model registry page displays the
   models that are registered to your project.
3. Choose **Model Groups**. The page displays the
   model groups that are defined for your project.
4. From the actions menu, choose **Create model group**.
5. Provide a name for the model group. Optionally, you can add keys to the model group.
6. Choose **Register model group** to create the model group.
7. Confirm that your newly-created model appears in the list of model
   groups.

## Create a collection

Follow these steps to create a collection:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **Model Registry**. The model registry page displays the
   models that are registered to your project.
3. Choose **Collections**. The collections page displays the
   collections that are defined for your project.
4. In the **Actions** drop-down menu, choose **Create collection**.
5. Provide a name for the collection.
6. (Optional) To add model groups to the collection, complete these steps:
   1. Choose **Select model groups**.
   2. Select up to 10 model groups that you want to add.

7. Choose **Create** to create the collection.

## Register a model version

The model registry is structured as several model (package) groups with model packages
in each group. Each model package in a model group corresponds to a trained model. The
version of each model package is a numerical value that starts at 1 and is incremented
with each new model package added to a model group. The model packages used in the model
registry are versioned, and **must** be associated with a
model group.

Follow these steps to register a model version:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **Model Registry**. The model registry page displays the
   models that are registered to your project.
3. Choose **Register**.
4. From the **Register Model** page,
   Choose the type of model artifact:
   - JumpStart – Choose from the list of models.
   - Jobs – Choose a training job
   - Bring-your-model – Enter the location of your models

5. Choose **Register**.
6. Create a model group, or find an existing model group.
7. Choose **Register**.

For more information, see [Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") in the _Amazon SageMaker AI Developer Guide_.
