# GENREL04-BP02 Implement a model catalog

Model catalogs store and manage model versions. They act as a
reliable store for models which may need to be deployed or rolled
back at any time. They also facilitate decoupled deployment
automation.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by helping to make sure the deployed model is
the appropriate model for the given use case.

**Benefits of establishing this best
practice:**
[Manage
change through automation](../framework/rel-dp.md "../framework/rel-dp.md") - Implementing a model catalog
helps to automate the process of deploying and rolling back model
versions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Model catalogs provide a centralized location to review models,
model version, and model cards. Traditionally, model catalogs are
meant to store model artifacts developed by customers. Foundation
models are rarely developed from scratch, and as a result,
foundation model catalogs should maintain first-party models,
third-party models, and custom models developed from third-party
models.

Customers should consider implementing a model catalog for
foundation models that records and tracks model access, model
versions, and model card information. Consider using the Amazon Bedrock model catalog in the AWS Management Console to track
available models. Amazon Bedrock's model catalog facilitates model
subscriptions to third-party models in the Amazon Bedrock
Marketplace as well. Model catalogs should provide a central
location for model management, particularly if there is a need to
roll back to a particular model or model version.

### Implementation steps

1. Navigate to the model catalog in Amazon Bedrock.
2. Select a model from the catalog.
3. Select the appropriate option from the list (for example,
   open in playground or customize).
4. For self-hosted models, consider the [bring
   your own endpoint feature](../../../bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.md "../../../bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.md").

## Resources

**Related practices:**

- [REL04-BP02](../reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.md "../reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.md")
- [REL07-BP01](../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md "../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md")

**Related guides, videos, and documentation:**

- [Amazon Bedrock API Reference](../../../bedrock/latest/APIReference/welcome.md "../../../bedrock/latest/APIReference/welcome.md")
- [Amazon Bedrock Marketplace](../../../bedrock/latest/userguide/amazon-bedrock-marketplace.md "../../../bedrock/latest/userguide/amazon-bedrock-marketplace.md")
- [Find
  serverless models with the Amazon Bedrock model catalog](../../../sagemaker-unified-studio/latest/userguide/model-catalog.md "../../../sagemaker-unified-studio/latest/userguide/model-catalog.md")
- [Bring
  your own endpoint](../../../bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.md "../../../bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.md")

**Related examples:**

- [Amazon Bedrock Marketplace: Access over 100 foundation models in one
  place](https://aws.amazon.com/blogs/aws/amazon-bedrock-marketplace-access-over-100-foundation-models-in-one-place/ "https://aws.amazon.com/blogs/aws/amazon-bedrock-marketplace-access-over-100-foundation-models-in-one-place/")
