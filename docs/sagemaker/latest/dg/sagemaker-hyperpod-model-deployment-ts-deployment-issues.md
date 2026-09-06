

# Model deployment issues
<a name="sagemaker-hyperpod-model-deployment-ts-deployment-issues"></a>

**Overview:** This section covers common issues that occur during model deployment, including pending states, failed deployments, and monitoring deployment progress.

## Model deployment stuck in pending state
<a name="sagemaker-hyperpod-model-deployment-ts-pending"></a>

When deploying a model, the deployment remains in a "Pending" state for an extended period. This indicates that the inference operator is unable to initiate the model deployment in your HyperPod cluster.

**Components affected:**

During normal deployment, the inference operator should:
+ Deploy model pod
+ Create load balancer
+ Create SageMaker AI endpoint

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

1. Review the inference operator logs and examine the operator logs for error messages:

   ```
   kubectl logs hyperpod-inference-operator-controller-manager-5b5cdd7757-txq8f -n hyperpod-inference-operator-system
   ```

**What to look for:**
+ Error messages in the operator logs
+ Status of the operator pod
+ Any deployment-related warnings or failures

**Note**  
A healthy deployment should progress beyond the "Pending" state within a reasonable time. If issues persist, review the inference operator logs for specific error messages to determine the root cause.

## Model deployment failed state troubleshooting
<a name="sagemaker-hyperpod-model-deployment-ts-failed"></a>

When a model deployment enters a "Failed" state, the failure could occur in one of three components:
+ Model pod deployment
+ Load balancer creation
+ SageMaker AI endpoint creation

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

1. Review the operator logs:

   ```
   kubectl logs hyperpod-inference-operator-controller-manager-5b5cdd7757-txq8f -n hyperpod-inference-operator-system
   ```

**What to look for:**

The operator logs will indicate which component failed:
+ Model pod deployment failures
+ Load balancer creation issues
+ SageMaker AI endpoint errors

## Checking model deployment progress
<a name="sagemaker-hyperpod-model-deployment-ts-progress"></a>

To monitor the progress of your model deployment and identify potential issues, you can use kubectl commands to check the status of various components. This helps determine whether the deployment is progressing normally or has encountered problems during the model pod creation, load balancer setup, or SageMaker AI endpoint configuration phases.

**Method 1: Check the JumpStart model status**

```
kubectl describe jumpstartmodel.inference.sagemaker.aws.amazon.com/<model-name> -n <namespace>
```

**Key status indicators to monitor:**

1. Deployment Status
   + Look for `Status.State`: Should show `DeploymentComplete`
   + Check `Status.Deployment Status.Available Replicas`
   + Monitor `Status.Conditions` for deployment progress

1. SageMaker AI Endpoint Status
   + Check `Status.Endpoints.Sagemaker.State`: Should show `CreationCompleted`
   + Verify `Status.Endpoints.Sagemaker.Endpoint Arn`

1. TLS Certificate Status
   + View `Status.Tls Certificate` details
   + Check certificate expiration in `Last Cert Expiry Time`

**Method 2: Check the inference endpoint configuration**

```
kubectl describe inferenceendpointconfig.inference.sagemaker.aws.amazon.com/<deployment_name> -n <namespace>
```

**Common status states:**
+ `DeploymentInProgress`: Initial deployment phase
+ `DeploymentComplete`: Successful deployment
+ `Failed`: Deployment failed

**Note**  
Monitor the Events section for any warnings or errors. Check replica count matches expected configuration. Verify all conditions show `Status: True` for a healthy deployment.