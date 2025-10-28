# Managing Amazon Rekognition Custom Labels resources

This section gives you an overview of the Amazon Rekognition Custom Labels resources you use to train and
manage a model. Also included is overview information for using the AWS SDK to train and
use a model.

Amazon Rekognition Custom Labels relies on three different resources to detect your custom labels: projects,
datasets, and models.

- Projects - Used to group other resouces like datasets, model versions, and model
  evaluations together.
- Datasets - Defines images and associated metadata for use in training and testing
  models. You can create a dataset by using a SageMaker AI format manifest file or by copying
  an existing Amazon Rekognition Custom Labels dataset.
- Models - The mathematical model that actually predicts the presence of objects,
  scenes, and concepts in images by identifying patterns in images used to train the
  model.

###### Topics

- [Managing an Amazon Rekognition Custom Labels project](managing-project.md "managing-project.md")
- [Managing datasets](managing-dataset.md "managing-dataset.md")
- [Managing an Amazon Rekognition Custom Labels model](managing-model.md "managing-model.md")
