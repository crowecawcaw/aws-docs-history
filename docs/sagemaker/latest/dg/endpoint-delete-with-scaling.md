# Delete endpoints configured for auto

scaling

If you delete an endpoint, Application Auto Scaling checks to see whether any of the models on that
endpoint are targets for auto scaling. If any are and you have permission to deregister
the model, Application Auto Scaling deregisters those models as scalable targets without notifying you.
If you use a custom permission policy that doesn't provide permission for the [DeregisterScalableTarget](../../../autoscaling/application/APIReference/API_DeregisterScalableTarget.md "../../../autoscaling/application/APIReference/API_DeregisterScalableTarget.md") action, you must request access to this action
before deleting the endpoint.

###### Note

As an IAM user, you might not have sufficient permission to delete an endpoint
if another user configured auto scaling for a variant on that endpoint.
