# Autoscale multi-container

endpoints

If you want to configure automatic scaling for a multi-container endpoint using the
`InvocationsPerInstance` metric, we recommend that the model in each
container exhibits similar CPU utilization and latency on each inference request.
This is recommended because if traffic to the multi-container endpoint shifts from a
low CPU utilization model to a high CPU utilization model, but the overall call
volume remains the same, the endpoint does not scale out and there may not be enough
instances to handle all the requests to the high CPU utilization model. For
information about automatically scaling endpoints, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md "endpoint-auto-scaling.md").
