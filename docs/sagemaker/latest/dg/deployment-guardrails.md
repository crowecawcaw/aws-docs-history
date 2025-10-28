# Deployment guardrails for updating models in production

Deployment guardrails are a set of model deployment options in Amazon SageMaker AI Inference to update
your machine learning models in production. Using the fully managed deployment options, you can
control the switch from the current model in production to a new one. Traffic shifting modes in
blue/green deployments, such as canary and linear, give you granular control over the traffic
shifting process from your current model to the new one during the course of the update. There
are also built-in safeguards such as auto-rollbacks that help you catch issues early and
automatically take corrective action before they significantly impact production.

Deployment guardrails provide the following benefits:

- **Deployment safety while updating production environments.** A
  regressive update to a production environment can cause unplanned downtime and business
  impact, such as increased model latency and high error rates. Deployment guardrails help you
  mitigate those risks by providing best practices and built-in operational safety
  guardrails.
- **Fully managed deployment.** SageMaker AI takes care of setting up and
  orchestrating these deployments and integrates them with endpoint update mechanisms.
  You do not need to build and maintain orchestration, monitoring, or rollback mechanisms. You can
  leverage SageMaker AI to set up and orchestrate these deployments and focus on leveraging ML for your
  applications.
- **Visibility.** You can track the progress of your
  deployment through the [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") API or
  through Amazon CloudWatch Events (for [supported endpoints](deployment-guardrails-exclusions.md "deployment-guardrails-exclusions.md")). To learn more about
  events in SageMaker AI, see the Endpoint deployment state change section in [Events that Amazon SageMaker AI sends to
  Amazon EventBridge](automating-sagemaker-with-eventbridge.md "automating-sagemaker-with-eventbridge.md"). Note that if your endpoint uses any of the features in the [Exclusions](deployment-guardrails-exclusions.md "deployment-guardrails-exclusions.md") page,
  you cannot use CloudWatch Events.

###### Note

Deployment guardrails only apply to
[Asynchronous inference](async-inference.md "async-inference.md") and [Real-time inference](realtime-endpoints.md "realtime-endpoints.md")
endpoint types.

## How to get started

We support two types of deployments to update models in production: blue/green deployments and rolling deployments.

- [Blue/Green Deployments](deployment-guardrails-blue-green.md "deployment-guardrails-blue-green.md"):
  You can shift traffic from your old fleet (the blue fleet) to a new fleet (green fleet) with the updates. Blue/green deployments offer
  [multiple traffic shifting modes](deployment-guardrails-blue-green.md "deployment-guardrails-blue-green.md").
  A traffic shifting mode is a configuration that specifies how SageMaker AI routes endpoint traffic to a new fleet containing your updates. The
  following traffic shifting modes provide you with different levels of control over the endpoint update process:
  - [Use all at once traffic shifting](deployment-guardrails-blue-green-all-at-once.md "deployment-guardrails-blue-green-all-at-once.md") shifts all of your endpoint traffic from the blue fleet to the green fleet.
    Once the traffic shifts to the green fleet, your pre-specified Amazon CloudWatch alarms begin
    monitoring the green fleet for a set amount of time (the _baking
    period_). If no alarms trip during the baking period, then SageMaker AI terminates the
    blue fleet.
  - [Use canary traffic shifting](deployment-guardrails-blue-green-canary.md "deployment-guardrails-blue-green-canary.md") shifts one small portion of your traffic (a _canary_)
    to the green fleet and monitor it for a baking period. If the canary succeeds on the green
    fleet, then SageMaker AI shifts the rest of the traffic from the blue fleet to the green fleet
    before terminating the blue fleet.
  - [Use linear traffic shifting](deployment-guardrails-blue-green-linear.md "deployment-guardrails-blue-green-linear.md")
    provides even more customization over the number of traffic-shifting steps and the
    percentage of traffic to shift for each step. While canary shifting lets you shift traffic
    in two steps, linear shifting extends this to _n_
    linearly spaced steps.

- [Use rolling deployments](deployment-guardrails-rolling.md "deployment-guardrails-rolling.md"): You can update your endpoint
  as SageMaker AI incrementally provisions capacity and shifts traffic to a new fleet in steps of a batch size that you specify. Instances on the
  new fleet are updated with the new deployment configuration, and if no CloudWatch alarms trip during the baking period, then SageMaker AI cleans up
  instances on the old fleet. This option gives you granular control over the instance count or capacity percentage shifted during each step.

You can create and manage your deployment through the [UpdateEndpoint](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md") and [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") SageMaker API and
AWS Command Line Interface commands. See the individual deployment pages for more details on how to set
up your deployment. Note that if your endpoint uses any of the features listed in the [Exclusions](deployment-guardrails-exclusions.md "deployment-guardrails-exclusions.md") page,
you cannot use deployment guardrails.

To follow guided examples that shows how to use deployment guardrails, see our example
[Jupyter notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-inference-deployment-guardrails "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-inference-deployment-guardrails") for the canary and linear traffic shifting modes.
