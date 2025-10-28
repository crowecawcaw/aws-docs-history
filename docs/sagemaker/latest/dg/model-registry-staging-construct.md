# Staging Construct for your Model

Lifecycle

You can define a series of stages that models can progress through for your model
workflows and lifecycle with the Model Registry staging construct. This simplifies
tracking and managing models as they transition through development, testing, and
production stages. The following will provide information on staging constructs and
how to use them in your model governance.

The stage construct allows you to define a series of stages and statuses that
models progress through. At each stage, specific personas with the relevant
permissions can update the stage status. As a model advances through the stages, its
metadata is carried forward, providing a comprehensive view of the model's
lifecycle. This metadata can be accessed and reviewed by authorized personas at each
stage, enabling informed decision making. This includes the following
benefits.

- Model Life Cycle Permissions - Set permissions for designated personas to
  update a model stage state and enforce approval gates at critical transition
  points. Administrators can assign permission by using IAM policies and
  condition keys with the API. For example, you can restrict you data
  scientist from updating the Model Lifecycle stage transition from
  "Development" to "Production". For examples, see [Set up Staging
  Construct Examples](model-registry-staging-construct-set-up.md "model-registry-staging-construct-set-up.md").
- Model Life Cycle Events via Amazon EventBridge - You can consume the lifecycle stage
  events using EventBridge. This sets you up to receive event notifications when
  models change approval or staging state, enabling integration with
  third-party governance tools. See [Get event
  notifications for ModelLifeCycle](model-registry-staging-construct-event-bridge.md "model-registry-staging-construct-event-bridge.md") for an
  example.
- Search based on Model Life Cycle Fields - You can search and filter stage
  and stage status using the [`Search`](../APIReference/API_Search.md "../APIReference/API_Search.md") API.
- Audit Trails for Model Life Cycle Events - You can view the history of
  model approval and staging events for the model lifecycle
  transitions.
  The following topics will walk you through how to set up a stage construct on the
  administrator side and how to update a stage status from the user side.

###### Topics

- [Set up Staging
  Construct Examples](model-registry-staging-construct-set-up.md "model-registry-staging-construct-set-up.md")
- [Update a model
  package stage and status in Studio](model-registry-staging-construct-update-studio.md "model-registry-staging-construct-update-studio.md")
- [Update a model
  package stage and status example (boto3)](model-registry-staging-construct-update-boto3.md "model-registry-staging-construct-update-boto3.md")
- [Invoke ModelLifeCycle
  using the AWS CLI examples](model-registry-staging-construct-cli.md "model-registry-staging-construct-cli.md")
- [Get event
  notifications for ModelLifeCycle](model-registry-staging-construct-event-bridge.md "model-registry-staging-construct-event-bridge.md")
