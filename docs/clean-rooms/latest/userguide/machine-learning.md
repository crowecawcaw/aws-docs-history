

# AWS Clean Rooms ML
<a name="machine-learning"></a>

AWS Clean Rooms ML allows two or more parties to run machine learning models on their data without the need to share their data with each other. The service provides privacy-enhancing controls that allow data owners to safe-guard their data and their model IP. You can use AWS authored models or bring your own custom model.

For a more detailed explanation of how this works, see [Cross-account jobs](ml-behaviors.md#ml-behaviors-cross-account-jobs).

For more information about the capabilities of Clean Rooms ML models, see the following topics. 

**Topics**
+ [AWS Clean Rooms ML terminology](#ml-terminology)
+ [How AWS Clean Rooms ML works with AWS models](#ml-how-it-works)
+ [How AWS Clean Rooms ML works with custom models](#custML-how-it-works)
+ [AWS models in Clean Rooms ML](aws-models.md)
+ [Custom models in Clean Rooms ML](custom-models.md)

## AWS Clean Rooms ML terminology
<a name="ml-terminology"></a>

It is important to understand the following terminology when using Clean Rooms ML:
+ *Training data provider* – The party that contributes the training data, creates and configures a lookalike model, and then associates that lookalike model with a collaboration.
+ *Seed data provider* – The party that contributes the seed data, generates a lookalike segment, and exports their lookalike segment.
+ *Training data* – The training data provider's data, which is used to generate a lookalike model. The training data is used to measure similarity in user behaviors.

  The training data must contain a user ID, item ID, and timestamp column. Optionally, the training data can contain other interactions as numerical or categorical features. Examples of interactions are a list of videos watched, items purchased, or articles read. 
+ *Seed data* – The seed data provider's data, which is used to create a lookalike segment. The seed data can be provided directly or it can come from the results of an AWS Clean Rooms query. The lookalike segment output is a set of users from the training data that most closely resembles the seed users.
+ *Lookalike model* – A machine learning model of the training data that is used to find similar users in other datasets.

  When using the API, the term *audience model* is used equivalently to lookalike model. For example, you use the [CreateAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateAudienceModel.html) API to create a lookalike model.
+ *Lookalike segment* – A subset of the training data that most closely resembles the seed data.

  When using the API, you create a lookalike segment with the [StartAudienceGenerationJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.html) API.

The training data provider's data is never shared with the seed data provider and the seed data provider's data is never shared with the training data provider. The lookalike segment output is shared with the training data provider, but never the seed data provider.

## How AWS Clean Rooms ML works with AWS models
<a name="ml-how-it-works"></a>

![An overview of how AWS Clean Rooms ML works with AWS models.](http://docs.aws.amazon.com/clean-rooms/latest/userguide/images/howItWorksML.png)


Working with lookalike models requires that two parties, a training data provider and a seed data provider, work sequentially in AWS Clean Rooms to bring their data into a collaboration. This is the workflow that the training data provider must complete first:

1. The training data provider's data must be stored in a AWS Glue data catalog table of user-item interactions. At a minimum, the training data must contain a user ID column, interaction ID column, and a timestamp column.

1. The training data provider registers the training data with AWS Clean Rooms.

1. The training data provider creates a lookalike model that can be shared with multiple seed data providers. The lookalike model is a deep neural network that can take up to 24 hours to train. It isn't automatically retrained and we recommend that you retrain the model weekly.

1. The training data provider configures the lookalike model, including whether to share relevance metrics and the Amazon S3 location of the output segments. The training data provider can create multiple configured lookalike models from a single lookalike model.

1. The training data provider associates the configured audience model to a collaboration that's shared with a seed data provider.

This is the workflow that the seed data provider must complete next:

1. The seed data provider's data can be stored in an Amazon S3 bucket or it can come from the results of query.

1. The seed data provider opens the collaboration that they share with the training data provider.

1. The seed data provider creates a lookalike segment from the Clean Rooms ML tab of the collaboration page. 

1. The seed data provider can evaluate the relevance metrics, if they were shared, and export the lookalike segment for use outside AWS Clean Rooms.

## How AWS Clean Rooms ML works with custom models
<a name="custML-how-it-works"></a>

With Clean Rooms ML, members of a collaboration can use a dockerized custom model algorithm that is stored in Amazon ECR to jointly analyze their data. To do this, the *model provider* must create an image and store it in Amazon ECR. Follow the steps in [Amazon Elastic Container Registry User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) to create a private repository that will contain the custom ML model. 

Any member of a collaboration can be the *model provider*, provided they have the correct permissions. All members of a collaboration can contribute training data, inference data, or both to the model. For the purpose of this guide, members contributing data are referred to as *data providers*. The member who creates the collaboration is the *collaboration creator*, and this member can be either the *model provider*, one of the *data providers*, or both.

At the highest level, here are the steps that must be completed to perform custom ML modeling:

1. The collaboration creator creates a collaboration and assigns each member the proper member abilities and payment configuration. The collaboration creator must assign the member ability to either receive model outputs or receive inference results to the appropriate member in this step because it can't be updated after the collaboration is created. For more information, see [Creating and joining the collaboration in AWS Clean Rooms ML](create-custom-ml-collaboration.md).

1. The model provider configures and associates their containerized ML model to the collaboration and ensures privacy constraints are set for exported data. For more information, see [Configuring a model algorithm in AWS Clean Rooms ML](configure-model-algorithm.md).

1. The data providers contribute their data to the collaboration and ensure their privacy needs are specified. Data providers must allow the model to access their data. For more information, see [Contributing training data in AWS Clean Rooms ML](custom-model-training-data.md) and [Associating the configured model algorithm in AWS Clean Rooms ML](associate-model-algorithm.md).

1. A collaboration member creates the ML configuration, which defines where the model artifacts or inference results are exported to.

1. A collaboration member creates an ML input channel that provides input to the training container or inference container. The ML input channel is a query that defines the data to be used in the context of the model algorithm.

1. A collaboration member invokes model training using the ML input channel and the configured model algorithm. For more information, see [Creating a trained model in AWS Clean Rooms ML](create-trained-model.md).

1. (Optional) The model trainer invokes the model export job and the model artifacts are sent to the model results receiver. Only members with a valid ML configuration and the member ability to receive model output can receive model artifacts. For more information, see [Exporting model artifacts from AWS Clean Rooms ML](export-model-artifacts.md).

1. (Optional) A collaboration member invokes model inference using the ML input channel, the trained model ARN, and the inference configured model algorithm. The inference results are sent to the inference output receiver. Only members with a valid ML configuration and the member ability to receive inference output can receive inference results.

Here are the steps that must be completed by the *model provider*:

1. Create a SageMaker AI compatible Amazon ECR docker image. Clean Rooms ML supports only SageMaker AI compatible docker images.

1. After you have created a SageMaker AI compatible docker image, push the image to Amazon ECR. Follow the directions in [Amazon Elastic Container Registry User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) to create a container training image.

1. Configure the model algorithm for use in Clean Rooms ML.

   1. Provide the Amazon ECR repository link and any arguments necessary to configure the model algorithm.

   1. Provide a service access role that allows Clean Rooms ML to access the Amazon ECR repository.

   1. Associate the configured model algorithm with the collaboration. This includes providing a privacy policy that defines controls for container logs, failure logs, CloudWatch metrics, and limits about how much data can be exported from the container results.

Here are the steps that must be completed by the *data provider* to collaborate with a custom ML model:

1. Configure an existing AWS Glue table with a custom analysis rule. This allows a specific set of pre-approved queries or pre-approved accounts to use your data.

1. Associate your configured table with a collaboration and provide a service access role that can access your AWS Glue tables.

1. [Add a collaboration analysis rule](add-collaboration-analysis-rule.md) to the table that allows the configured model algorithm association to access the configured table.

1. After the model and data are associated and configured in Clean Rooms ML, the member with the ability to run queries provides an SQL query and selects the model algorithm to use.

 After model training is finished, that member initiates the export of model training artifacts or inference results. These artifacts or results are sent to the member with the ability to received trained model output. The results receiver must configure their `MachineLearningConfiguration` before they can receive model output.