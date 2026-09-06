

# Ray Dashboard access and remote job submission
<a name="sagemaker-hyperpod-ray-dashboard"></a>

The Ray Dashboard shows cluster state, jobs, logs, and metrics. It grants read and write access to the cluster: a user with the dashboard can submit jobs, kill actors, and change cluster state. Control who reaches it.

HyperPod exposes the dashboard through an authenticated browser link scoped to an identity, so you do not use `kubectl port-forward`. The following pages set up that path and control access to it.

**Topics**
+ [Installing the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator.md)
+ [Security best practices for the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator-security.md)
+ [Access strategies and security best practices](sagemaker-hyperpod-ray-dashboard-access-strategies.md)
+ [Generating a dashboard connection URL](sagemaker-hyperpod-ray-dashboard-connection-url.md)
+ [Submitting jobs remotely with the toolkit library](sagemaker-hyperpod-ray-remote-job-submission.md)