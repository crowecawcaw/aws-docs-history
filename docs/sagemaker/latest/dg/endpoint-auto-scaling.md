# Automatic scaling of Amazon SageMaker AI models

Amazon SageMaker AI supports automatic scaling (auto scaling) for your hosted models. _Auto
scaling_ dynamically adjusts the number of instances provisioned for a model
in response to changes in your workload. When the workload increases, auto scaling brings
more instances online. When the workload decreases, auto scaling removes unnecessary
instances so that you don't pay for provisioned instances that you aren't using.

###### Topics

- [Auto scaling policy overview](endpoint-auto-scaling-policy.md "endpoint-auto-scaling-policy.md")
- [Auto scaling prerequisites](endpoint-auto-scaling-prerequisites.md "endpoint-auto-scaling-prerequisites.md")
- [Configure model auto scaling with
  the console](endpoint-auto-scaling-add-console.md "endpoint-auto-scaling-add-console.md")
- [Register a model](endpoint-auto-scaling-add-policy.md "endpoint-auto-scaling-add-policy.md")
- [Define a scaling policy](endpoint-auto-scaling-add-code-define.md "endpoint-auto-scaling-add-code-define.md")
- [Apply a scaling policy](endpoint-auto-scaling-add-code-apply.md "endpoint-auto-scaling-add-code-apply.md")
- [Instructions for editing a scaling
  policy](endpoint-auto-scaling-edit.md "endpoint-auto-scaling-edit.md")
- [Temporarily turn off
  scaling policies](endpoint-auto-scaling-suspend-scaling-activities.md "endpoint-auto-scaling-suspend-scaling-activities.md")
- [Delete a scaling policy](endpoint-auto-scaling-delete.md "endpoint-auto-scaling-delete.md")
- [Check the status of a scaling activity
  by describing scaling activities](endpoint-scaling-query-history.md "endpoint-scaling-query-history.md")
- [Scale an endpoint to zero
  instances](endpoint-auto-scaling-zero-instances.md "endpoint-auto-scaling-zero-instances.md")
- [Load testing your auto scaling
  configuration](endpoint-scaling-loadtest.md "endpoint-scaling-loadtest.md")
- [Use CloudFormation to create a scaling
  policy](endpoint-scaling-cloudformation.md "endpoint-scaling-cloudformation.md")
- [Update endpoints that use auto scaling](endpoint-scaling-update.md "endpoint-scaling-update.md")
- [Delete endpoints configured for auto
  scaling](endpoint-delete-with-scaling.md "endpoint-delete-with-scaling.md")
