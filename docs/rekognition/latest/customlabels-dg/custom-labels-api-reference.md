# Amazon Rekognition Custom Labels API reference

The Amazon Rekognition Custom Labels API is documented as part of the Amazon Rekognition API reference content. This is a list of the
Amazon Rekognition Custom Labels API operations with links to the appropriate Amazon Rekognition API reference topic. Also, API reference links within this
document go to the appropriate Amazon Rekognition Developer Guide API reference topic. For information about using the API,
see .

## Training your model

### Projects

- [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md") — Creates your Amazon Rekognition Custom Labels project which is a logical grouping of resources (images, Labels, models) and operations (training, evaluation, and detection).
- [DeleteProject](../APIReference/API_DeleteProject.md "../APIReference/API_DeleteProject.md") — Deletes an Amazon Rekognition Custom Labels project.
- [DescribeProjects](../APIReference/API_DescribeProjects.md "../APIReference/API_DescribeProjects.md") — Returns a list of all your Amazon Rekognition Custom Labels projects.

### Project Policies

- [PutProjectPolicy](../APIReference/API_PutProjectPolicy.md "../APIReference/API_PutProjectPolicy.md") — Attaches a project policy to a
  Amazon Rekognition Custom Labels project in a trusting AWS account.
- [ListProjectPolicies](../APIReference/API_ListProjectPolicies.md "../APIReference/API_ListProjectPolicies.md") — Returns a list of the project
  policies attached to a project.
- [DeleteProjectPolicy](../APIReference/API_DeleteProjectPolicy.md "../APIReference/API_DeleteProjectPolicy.md") — Deletes an existing project
  policy.

### Datasets

- [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") — Creates a Amazon Rekognition Custom Labels dataset.
- [DeleteDataset](../APIReference/API_DeleteDataset.md "../APIReference/API_DeleteDataset.md") — Deletes an Amazon Rekognition Custom Labels dataset.
- [DescribeDataset](../APIReference/API_DescribeDataset.md "../APIReference/API_DescribeDataset.md") — Describes an Amazon Rekognition Custom Labels dataset.
- [DistributeDatasetEntries](../APIReference/API_DistributeDatasetEntries.md "../APIReference/API_DistributeDatasetEntries.md") — Distributes the entries (images) in a training dataset across the training
  dataset and the test dataset for a project.
- [ListDatasetEntries](../APIReference/API_ListDatasetEntries.md "../APIReference/API_ListDatasetEntries.md") — Returns a list of entries (images) in an Amazon Rekognition Custom Labels dataset.
- [ListDatasetLabels](../APIReference/API_ListDatasetLabels.md "../APIReference/API_ListDatasetLabels.md") — Returns a list of labels assigned to an Amazon Rekognition Custom Labels dataset.
- [UpdateDatasetEntries](../APIReference/API_UpdateDatasetEntries.md "../APIReference/API_UpdateDatasetEntries.md") — Adds or updates entries (images) in an Amazon Rekognition Custom Labels dataset.

### Models

- [CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md") — Trains your Amazon Rekognition Custom Labels model.
- [CopyProjectVersion](../APIReference/API_CopyProjectVersion.md "../APIReference/API_CopyProjectVersion.md") — Copies your Amazon Rekognition Custom Labels
  model.
- [DeleteProjectVersion](../APIReference/API_DeleteProjectVersion.md "../APIReference/API_DeleteProjectVersion.md") — Deletes an Amazon Rekognition Custom Labels model.
- [DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md") — Returns a list of all the Amazon Rekognition Custom Labels models within a specific project.

### Tags

- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") — Adds one or more key-value tags to an Amazon Rekognition Custom Labels model.
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") — Removes one or more tags from an Amazon Rekognition Custom Labels model.

## Using your model

- [DetectCustomLabels](../APIReference/API_DetectCustomLabels.md "../APIReference/API_DetectCustomLabels.md") — Analyzes an image with your custom labels model.
- [StartProjectVersion](../APIReference/API_StartProjectVersion.md "../APIReference/API_StartProjectVersion.md") — Starts your custom labels model.
- [StopProjectVersion](../APIReference/API_StopProjectVersion.md "../APIReference/API_StopProjectVersion.md") — Stops your custom labels model.
