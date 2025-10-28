# Amazon SageMaker AI–Created Tracking

Entities

Amazon SageMaker AI automatically creates tracking entities for SageMaker AI jobs, models, model packages,
and endpoints if the data is available. There is no limit to the number of lineage entities
created by SageMaker AI.

For information on how you can manually create tracking entities, see [Manually Create Tracking Entities](lineage-tracking-manual-creation.md "lineage-tracking-manual-creation.md").

###### Topics

- [Tracking Entities for SageMaker AI Jobs](#lineage-tracking-auto-creation-jobs "#lineage-tracking-auto-creation-jobs")
- [Tracking Entities for Model
  Packages](#lineage-tracking-auto-creation-model-package "#lineage-tracking-auto-creation-model-package")
- [Tracking Entities for
  Endpoints](#lineage-tracking-auto-creation-endpoint "#lineage-tracking-auto-creation-endpoint")

## Tracking Entities for SageMaker AI Jobs

SageMaker AI creates a trial component for and associated with each SageMaker AI job. SageMaker AI creates
artifacts to track the job metadata and associations between each artifact and the
job.

Artifacts are created for the following job properties and associated with the Amazon
Resource Name (ARN) of the SageMaker AI job. The artifact `SourceUri` is listed in
parentheses.

###### Training Job

- The image that contains the training algorithm (`TrainingImage`).
- The data source of each input channel (`S3Uri`).
- The location for the model (`S3OutputPath)`.
- The location for the managed spot checkpoint data (`S3Uri`).

###### Processing Job

- The container to be run by the processing job (`ImageUri`).
- The data location for each processing input and processing output
  (`S3Uri`).

###### Transform Job

- The input data source to be transformed (`S3Uri`).
- The results of the transform (`S3OutputPath`).

###### Note

Amazon Simple Storage Service (Amazon S3) artifacts are tracked based on the Amazon S3 URI values provided to the
Create API, for example [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md"), and not on the Amazon S3 key and hash or etag values from each
file.

## Tracking Entities for Model

Packages

The following entities are created:

###### Model Packages

- A context for each model package group.
- An artifact for each model package.
- An association between each model package artifact and the context for each model
  package group to which the package belongs to.
- An action for the creation of a model package version.
- An association between the model package artifact and the creation action.
- An association between the model package artifact and each model package group
  context to which the package belongs to.
- Inference containers
  - An artifact for the image used in each container defined in the model
    package.
  - An artifact for the model used in each container.
  - An association between each artifact and the model package artifact.

- Algorithms
  - An artifact for each algorithm defined in the model package.
  - An artifact for the model created by each algorithm.
  - An association between each artifact and the model package artifact.

## Tracking Entities for

Endpoints

The following entities are created by Amazon SageMaker AI:

###### Endpoints

- A context for each endpoint
- An action for the model deployment that created each endpoint
- An artifact for each model deployed to the endpoint
- An artifact for the image used in the model
- An artifact for the model package for the model
- An artifact for each image deployed to the endpoint
- An association between each artifact and the model deployment action
