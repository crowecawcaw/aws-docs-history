# HyperPod inference

troubleshooting

This troubleshooting guide addresses common issues that can occur during SageMaker AI HyperPod
inference deployment and operation. These problems typically involve VPC networking
configuration, IAM permissions, Kubernetes resource management, and operator
connectivity issues that can prevent successful model deployment or cause deployments to
fail or remain in pending states.

This troubleshooting guide uses the following terminology: **Troubleshooting steps** are diagnostic procedures to identify and
investigate problems, **Resolution** provides the specific
actions to fix identified issues, and **Verification**
confirms that the solution worked correctly.

## Certificate download

timeout

When deploying a SageMaker AI endpoint, the creation process fails due to the inability to
download the certificate authority (CA) certificate in a VPC environment. For
detailed configuration steps, refer to the [Admin guide](https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/SageMakerHyperpod/hyperpod-inference/Hyperpod_Inference_Admin_Notebook.ipynb "https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/SageMakerHyperpod/hyperpod-inference/Hyperpod_Inference_Admin_Notebook.ipynb").

**Error message:**

The following error appears in the SageMaker AI endpoint CloudWatch logs:

```
Error downloading CA certificate: Connect timeout on endpoint URL: "https://****.s3.<REGION>.amazonaws.com/****/***.pem"
```

**Root cause:**

- This issue occurs when the inference operator cannot access the
  self-signed certificate in Amazon S3 within your VPC
- Proper configuration of the Amazon S3 VPC endpoint is essential for certificate
  access

**Resolution:**

1. If you don't have an Amazon S3 VPC endpoint:
   - Create an Amazon S3 VPC endpoint following the configuration in section
     5.3 of the [Admin guide](https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/SageMakerHyperpod/hyperpod-inference/Hyperpod_Inference_Admin_Notebook.ipynb "https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/SageMakerHyperpod/hyperpod-inference/Hyperpod_Inference_Admin_Notebook.ipynb").

2. If you already have an Amazon S3 VPC endpoint:
   - Ensure that the subnet route table is configured to point to the
     VPC endpoint (if using gateway endpoint) or that private DNS is
     enabled for interface endpoint.
   - Amazon S3 VPC endpoint should be similar to the configuration mentioned
     in section 5.3 Endpoint creation step

## Model deployment

stuck in pending state

When deploying a model, the deployment remains in a "Pending" state for an
extended period. This indicates that the inference operator is unable to initiate
the model deployment in your HyperPod cluster.

**Components affected:**

During normal deployment, the inference operator should:

- Deploy model pod
- Create load balancer
- Create SageMaker AI endpoint

**Troubleshooting steps:**

1. Check the inference operator pod status:

```
kubectl get pods -n hyperpod-inference-system
```

Expected output example:

```
NAME                                                           READY   STATUS    RESTARTS   AGE
hyperpod-inference-operator-controller-manager-65c49967f5-894fg   1/1     Running   0         6d13h
```

2. Review the inference operator logs and examine the operator logs for error
   messages:

```
kubectl logs hyperpod-inference-operator-controller-manager-5b5cdd7757-txq8f -n hyperpod-inference-operator-system
```

**What to look for:**

- Error messages in the operator logs
- Status of the operator pod
- Any deployment-related warnings or failures

###### Note

A healthy deployment should progress beyond the "Pending" state within a
reasonable time. If issues persist, review the inference operator logs for
specific error messages to determine the root cause.

## Model deployment

failed state troubleshooting

When a model deployment enters a "Failed" state, the failure could occur in one of
three components:

- Model pod deployment
- Load balancer creation
- SageMaker AI endpoint creation

**Troubleshooting steps:**

1. Check the inference operator status:

```
kubectl get pods -n hyperpod-inference-system
```

Expected output:

```
NAME                                                           READY   STATUS    RESTARTS   AGE
hyperpod-inference-operator-controller-manager-65c49967f5-894fg   1/1     Running   0         6d13h
```

2. Review the operator logs:

```
kubectl logs hyperpod-inference-operator-controller-manager-5b5cdd7757-txq8f -n hyperpod-inference-operator-system
```

**What to look for:**

The operator logs will indicate which component failed:

- Model pod deployment failures
- Load balancer creation issues
- SageMaker AI endpoint errors

## Checking model

deployment progress

To monitor the progress of your model deployment and identify potential issues,
you can use kubectl commands to check the status of various components. This helps
determine whether the deployment is progressing normally or has encountered problems
during the model pod creation, load balancer setup, or SageMaker AI endpoint configuration
phases.

**Method 1: Check the JumpStart model status**

```
kubectl describe jumpstartmodel.inference.sagemaker.aws.amazon.com/<model-name> -n <namespace>
```

**Key status indicators to monitor:**

1. Deployment Status
   - Look for `Status.State`: Should show
     `DeploymentComplete`
   - Check `Status.Deployment Status.Available
Replicas`
   - Monitor `Status.Conditions` for deployment
     progress

2. SageMaker AI Endpoint Status
   - Check `Status.Endpoints.Sagemaker.State`: Should show
     `CreationCompleted`
   - Verify `Status.Endpoints.Sagemaker.Endpoint Arn`

3. TLS Certificate Status
   - View `Status.Tls Certificate` details
   - Check certificate expiration in `Last Cert Expiry
Time`

**Method 2: Check the inference endpoint
configuration**

```
kubectl describe inferenceendpointconfig.inference.sagemaker.aws.amazon.com/<deployment_name> -n <namespace>
```

**Common status states:**

- `DeploymentInProgress`: Initial deployment phase
- `DeploymentComplete`: Successful deployment
- `Failed`: Deployment failed

###### Note

Monitor the Events section for any warnings or errors. Check replica count
matches expected configuration. Verify all conditions show `Status:
 True` for a healthy deployment.

## VPC ENI

permission issue

SageMaker AI endpoint creation fails due to insufficient permissions for creating network
interfaces in VPC.

**Error message:**

```
Please ensure that the execution role for variant AllTraffic has sufficient permissions for creating an endpoint variant within a VPC
```

**Root cause:**

The inference operator's execution role lacks the required Amazon EC2 permission to
create network interfaces (ENI) in VPC.

**Resolution:**

Add the following IAM permission to the inference operator's execution
role:

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterfacePermission"
     ],
    "Resource": "*"
}
```

**Verification:**

After adding the permission:

1. Delete the failed endpoint (if exists)
2. Retry the endpoint creation
3. Monitor the deployment status for successful completion

###### Note

This permission is essential for SageMaker AI endpoints running in VPC mode. Ensure
the execution role has all other necessary VPC-related permissions as
well.

## IAM trust

relationship issue

HyperPod inference operator fails to start with an STS AssumeRoleWithWebIdentity
error, indicating an IAM trust relationship configuration problem.

**Error message:**

```
failed to enable inference watcher for HyperPod cluster *****: operation error SageMaker: UpdateClusterInference,
get identity: get credentials: failed to refresh cached credentials, failed to retrieve credentials,
operation error STS: AssumeRoleWithWebIdentity, https response error StatusCode: 403, RequestID: ****,
api error AccessDenied: Not authorized to perform sts:AssumeRoleWithWebIdentity
```

**Resolution:**

Update the trust relationship of the inference operator's IAM execution role with
the following configuration.

Replace the following placeholders:

- `<ACCOUNT_ID>`: Your AWS account ID
- `<REGION>`: Your AWS region
- `<OIDC_ID>`: Your Amazon EKS cluster's OIDC provider ID

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Federated": "arn:aws:iam::111122223333:oidc-provider/oidc.eks.us-east-2.amazonaws.com/id/<OIDC_ID>"
 },
 "Action": "sts:AssumeRoleWithWebIdentity",
 "Condition": {
 "StringLike": {
 "oidc.eks.us-east-2.amazonaws.com/id/<OIDC_ID>:sub": "system:serviceaccount:<namespace>:<service-account-name>",
 "oidc.eks.us-east-2.amazonaws.com/id/<OIDC_ID>:aud": "sts.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

**Verification:**

After updating the trust relationship:

1. Verify the role configuration in IAM console
2. Restart the inference operator if necessary
3. Monitor operator logs for successful startup

## Missing NVIDIA GPU

plugin error

Model deployment fails with GPU insufficiency error despite having available GPU
nodes. This occurs when the NVIDIA device plugin is not installed in the HyperPod
cluster.

**Error message:**

```
0/15 nodes are available: 10 node(s) didn't match Pod's node affinity/selector,
5 Insufficient nvidia.com/gpu. preemption: 0/15 nodes are available:
10 Preemption is not helpful for scheduling, 5 No preemption victims found for incoming pod.
```

**Root cause:**

- Kubernetes cannot detect GPU resources without the NVIDIA device
  plugin
- Results in scheduling failures for GPU workloads

**Resolution:**

Install the NVIDIA GPU plugin by running:

```
kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/refs/tags/v0.17.1/deployments/static/nvidia-device-plugin.yml
```

**Verification steps:**

1. Check the plugin deployment status:

```
kubectl get pods -n kube-system | grep nvidia-device-plugin
```

2. Verify GPU resources are now visible:

```
kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\\.com/gpu
```

3. Retry model deployment

###### Note

Ensure NVIDIA drivers are installed on GPU nodes. Plugin installation is a
one-time setup per cluster. May require cluster admin privileges to
install.

## Inference operator

fails to start

Inference operator pod failed to start and is causing the following error message.
This error is due to permission policy on the operator execution role not being
authorized to perform `sts:AssumeRoleWithWebIdentity`. Due to this, the
operator part running on the control plane is not started.

**Error message:**

```
Warning Unhealthy 5m46s (x22 over 49m) kubelet Startup probe failed: Get "http://10.1.100.59:8081/healthz": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

**Root cause:**

- Permission policy of the inference operator execution role is not set to
  access authorization token for resources.

**Resolution:**

Set the following policy of the execution role of `EXECUTION_ROLE_ARN`
for the HyperPod inference operator:

```
HyperpodInferenceAccessPolicy-ml-cluster to include all resources
```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Verification steps:**

1. Change the policy.
2. Terminate the HyperPod inference operator pod.
3. The pod will be restarted without throwing any exceptions.
