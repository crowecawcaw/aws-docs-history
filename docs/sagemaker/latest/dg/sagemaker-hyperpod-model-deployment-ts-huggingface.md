

# Hugging Face Hub model deployment failures
<a name="sagemaker-hyperpod-model-deployment-ts-huggingface"></a>

**Overview:** When deploying models from Hugging Face Hub using the `huggingface` model source type, the deployment may fail during the model download phase. This section covers common failure scenarios and how to diagnose them using Kubernetes events and pod logs.

## Diagnosing Hugging Face deployment failures
<a name="sagemaker-hyperpod-model-deployment-ts-hf-diagnose"></a>

**Troubleshooting steps:**

1. Check the InferenceEndpointConfig status and events for error details:

   ```
   kubectl describe inferenceendpointconfig <name> -n <namespace>
   ```

   Look for events with reason `HuggingFaceDownloadFailed` and the `DeploymentFailed` condition in the status, which contain specific error messages.

1. If the init container is failing (pod shows `Init:CrashLoopBackOff` or `Init:Error`), check the init container logs:

   ```
   kubectl logs <pod-name> -c hf-model-downloader -n <namespace>
   ```

1. Check the pod status for init container exit codes:

   ```
   kubectl get pod <pod-name> -n <namespace> -o jsonpath='{.status.initContainerStatuses[0].state}'
   ```

## Invalid or expired Hugging Face token
<a name="sagemaker-hyperpod-model-deployment-ts-hf-token"></a>

**Symptoms:** Init container fails with `401 Unauthorized` or `Access denied` errors. The pod enters `CrashLoopBackOff`.

**Root cause:**
+ The Hugging Face API token in the Kubernetes Secret is invalid, expired, or revoked.
+ The token does not have access to the gated model.

**Resolution:**

1. Generate a new token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

1. For gated models, ensure you have accepted the model's license agreement on the Hugging Face Hub model page.

1. Update the Kubernetes Secret with the new token:

   ```
   kubectl delete secret <secret-name> -n <namespace>
   kubectl create secret generic <secret-name> \
     --from-literal=token=hf_NEW_TOKEN_HERE \
     -n <namespace>
   ```

1. Delete the failing pod to trigger a new download attempt:

   ```
   kubectl delete pod -l app=<iec-name> -n <namespace>
   ```

## Network connectivity failures
<a name="sagemaker-hyperpod-model-deployment-ts-hf-network"></a>

**Symptoms:** Init container fails with connection timeout or DNS resolution errors. The pod enters `CrashLoopBackOff`.

**Root cause:** The cluster nodes do not have outbound internet access to Hugging Face domains (`*.huggingface.co` and `*.hf.co`). This is common in private subnets without a NAT gateway.

**Resolution:**

1. Verify that your VPC has a NAT gateway configured for the private subnets where your cluster nodes run.

1. Verify that security groups allow outbound HTTPS (port 443) traffic.

1. Verify that network ACLs allow outbound traffic to the internet.

1. Test connectivity from within the cluster:

   ```
   kubectl run test-connectivity --image=curlimages/curl --rm -it --restart=Never -- \
     curl -sI https://huggingface.co
   ```

**Note**  
If outbound internet access is not available, consider using Amazon S3 or Amazon FSx as the model source instead. Download the model to Amazon S3 first, then deploy using the `s3` model source type.

## Model not found
<a name="sagemaker-hyperpod-model-deployment-ts-hf-model-not-found"></a>

**Symptoms:** Init container fails with `Repository Not Found` or `404` errors.

**Root cause:**
+ The `modelId` is incorrect or the model does not exist on Hugging Face Hub.
+ The model is private and the token does not have access.

**Resolution:**

1. Verify the model ID exists by visiting `https://huggingface.co/<org>/<model>` in your browser.

1. Ensure the `modelId` in your InferenceEndpointConfig is in the correct `org/model` format (for example, `mistralai/Mistral-7B-Instruct-v0.3`).