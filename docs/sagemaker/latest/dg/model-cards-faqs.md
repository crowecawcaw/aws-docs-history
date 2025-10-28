# Model card FAQs

Refer to the following FAQ items for answers to commonly asked questions about
Amazon SageMaker Model Card.

A: You can use models for a variety of business applications ranging from
predicting cyber attacks and approving loan applications to detecting the
category of an email. Each of these applications assumes a different level of
risk. For example, incorrectly detecting a cyber attack has much greater
business impact than incorrectly categorizing an email. Given these varied risk
profiles of a model, you can use model cards to provide a risk rating of
`low`, `medium`, or `high` for a model. If
you don’t know the risk of your model, you can set the status to
`unknown`. Customers are responsible for assigning the risk
profile for each model. Based on the risk rating, organizations may have
different rules in place for deploying those models to production. For more
information, see [Risk ratings](model-cards.md#model-cards-risk-rating "model-cards.md#model-cards-risk-rating").

The intended use of a model describes how you should use the model in your
production applications. This goes beyond technical requirements like the type
of instance to which you should deploy a model and instead refers to the types
of applications to create with the model, the scenarios in which you can expect
a reasonable performance from the model, or the type of data to use with the
model. We recommend providing this information in the model card for better
model governance. You can define a kind of model specification in the intended
use field and ensure that model developers and consumers follow this
specification while training and deploying their models. For more information,
see [Intended uses of a model](model-cards.md#model-cards-intended-uses "model-cards.md#model-cards-intended-uses").

When creating a model card using either the SageMaker Python SDK or the AWS
console, SageMaker AI automatically populates information about your trained model. This includes
comprehensive training details and all model information that's available through the
`describe-model` API call. If you work in Amazon SageMaker Studio, you can
auto-populate your model cards by calling the [DescribeModelPackage](../APIReference/API_DescribeModelPackage.md "../APIReference/API_DescribeModelPackage.md")API.

Amazon SageMaker Model Cards have a defined structure to them that cannot be modified. This
structure gives you guidance on what information should be captured in a model card. While
you cannot change the structure of the model card, there is some flexibility introduced
through custom properties in the **Additional information** section of
the model card.

Model cards have versions associated with them. A given model version is
immutable across all attributes other than the model card status. If you make
any other changes to the model card, such as evaluation metrics, description, or
intended uses, SageMaker AI creates a new version of the model card to reflect the
updated information. This is to ensure that a model card, once created, cannot
be tampered with.

Model cards are automatically updated whenever you make changes to your model package
versions in the Model Registry.

A: Yes. You can create model cards for models not trained in SageMaker AI, but no
information is automatically populated in the card. You must supply all the
information needed in the model card for non-SageMaker AI models.

A: Yes. You can export each version of a model card to a PDF, downloaded, and
share it.

A: Model cards are accessible through both SageMaker AI Console and Model Registry. When using Model Registry,
you will automatically receive a model card for each version of your model.

A: Model cards are intended to provide organizations with a mechanism to
document as much detail about their model as they like by following SageMaker AI’s
prescriptive guidance along with providing their own custom information. You can
introduce model cards at the very start of the ML process and use them to define
the business problem that the model should solve and any considerations to think
about while using the model. After a model is trained, you can populate the
model card associated with that model with information about the model and how
it was trained. Model cards are associated with models and are immutable once
associated with a model. This ensures that the model card is the single source
of truth for all the information related to a model, including how it was
trained and how it should be used.

The Model Registry is a catalog that stores metadata about your models. Each
entry in the model registry corresponds to a unique model version. That model
version contains information about the model such as where the model artifacts
are stored in Amazon S3, what container is needed to deploy the model,
and custom metadata that should be attached to the model. Each model package version
has a model card associated with it.

A: Model cards are integrated into the Model Registry object. Each version of a model package
in the Model Registry is linked to its corresponding model card. You can access the model card
schema for each version by using the [ModelPackageModelCard](../APIReference/API_ModelPackageModelCard.md "../APIReference/API_ModelPackageModelCard.md") API.

A: Yes, there is a one-to-one relationship between model cards and models in the Model Registry.
Each model version stored in the Model Registry has exactly one corresponding model card associated
with it.

A: No. You can upload the performance metrics computed by SageMaker Model Monitor
to the model card by uploading a metrics file to Amazon S3 and linking
that to the card, but there is no native integration between Model Monitor and
model cards. Model dashboards are integrated with Model Monitor. For more
information on model dashboards, see [Amazon SageMaker Model Dashboard](model_dashboard.md "model_dashboard.md").
