# Custom models in Clean Rooms ML

With Clean Rooms ML, members of a collaboration can use a dockerized custom model algorithm
that is stored in Amazon ECR to jointly analyze their data. To do this, the _model
provider_ must create an image and store it in Amazon ECR. Follow the steps in
[Amazon Elastic Container Registry User Guide](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md") to create a private repository that will contain the custom ML model.

Any member of a collaboration can be the _model provider_, provided
they have the correct permissions. All members of a collaboration can contribute data to
the model. For the purpose of this guide, members contributing data are referred to as
_data providers_. The member who creates the collaboration is the
_collaboration creator_, and this member can be either the
_model provider_, one of the _data providers_,
or both.

The following topics describe the information necessary to create a custom ML
model

###### Topics

- [Custom ML modeling
  prerequisites](custom-model-prerequisites.md "custom-model-prerequisites.md")
- [Model authoring guidelines for the
  training container](custom-model-guidelines.md "custom-model-guidelines.md")
- [Model authoring guidelines for the
  inference container](inference-model-guidelines.md "inference-model-guidelines.md")
- [Receiving model logs and
  metrics](custom-model-logs.md "custom-model-logs.md")
