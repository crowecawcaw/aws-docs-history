

# Custom models in Clean Rooms ML
<a name="custom-models"></a>

With Clean Rooms ML, members of a collaboration can use a dockerized custom model algorithm that is stored in Amazon ECR to jointly analyze their data. To do this, the *model provider* must create an image and store it in Amazon ECR. Follow the steps in [Amazon Elastic Container Registry User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) to create a private repository that will contain the custom ML model. 

Any member of a collaboration can be the *model provider*, provided they have the correct permissions. All members of a collaboration can contribute data to the model. For the purpose of this guide, members contributing data are referred to as *data providers*. The member who creates the collaboration is the *collaboration creator*, and this member can be either the *model provider*, one of the *data providers*, or both.

The following topics describe the information necessary to create a custom ML model

**Topics**
+ [Custom ML modeling prerequisites](custom-model-prerequisites.md)
+ [Model authoring guidelines for the training container](custom-model-guidelines.md)
+ [Model authoring guidelines for the inference container](inference-model-guidelines.md)
+ [Receiving model logs and metrics](custom-model-logs.md)