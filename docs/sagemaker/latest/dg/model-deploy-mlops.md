# Model Deployment in SageMaker AI

Once you train and approve a model for production, use SageMaker AI to deploy your model to an
endpoint for real-time inference. SageMaker AI provides multiple inference options so that
you can pick the option that best suits your workload. You also configure your endpoint
by choosing the instance type and number of instances you need for optimal performance.
For details about model deployment, see [Deploy models for inference](deploy-model.md "deploy-model.md").

After you deploy your models to production, you might want to explore ways to further
optimize model performance while maintaining availability of your current models. For example,
you can set up a shadow test to try out a different model or model serving infrastructure
before committing to the change. SageMaker AI deploys
the new model, container, or instance in shadow mode and routes to it a copy of the inference
requests in real time within the same endpoint. You can log the responses of the
shadow variant for comparison. For details about shadow testing, see [Shadow tests](shadow-tests.md "shadow-tests.md"). If you decide to go ahead and change your model,
deployment guardrails help you control
the switch from the current model to a new one. You can select such methods
as blue/green or canary testing of the traffic shifting process to maintain granular control
during the update. For information
about deployment guardrails, see [Deployment guardrails for updating models in production](deployment-guardrails.md "deployment-guardrails.md").
