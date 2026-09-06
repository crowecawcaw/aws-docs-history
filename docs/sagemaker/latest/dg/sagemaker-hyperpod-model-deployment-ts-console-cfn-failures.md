

# Inference operator installation failures through SageMaker AI console
<a name="sagemaker-hyperpod-model-deployment-ts-console-cfn-failures"></a>

**Overview:** When installing the inference operator through the SageMaker AI console using Quick Install or Custom Install, the underlying CloudFormation stacks may fail due to various issues. This section covers common failure scenarios and their resolutions.

## Inference operator add-on installation failure through Quick or Custom install
<a name="sagemaker-hyperpod-model-deployment-ts-console-cfn-stack-failed"></a>

**Problem:** The HyperPod cluster creation completes successfully, but the inference operator add-on installation fails.

**Common causes:**
+ Pod capacity limits exceeded on cluster nodes. The inference operator installation requires a minimum of 13 pods. The minimum recommended instance type is `ml.c5.4xlarge`.
+ IAM permission issues
+ Resource quota constraints
+ Network or VPC configuration problems

### Symptoms and diagnosis
<a name="sagemaker-hyperpod-model-deployment-ts-console-cfn-symptoms"></a>

**Symptoms:**
+ Inference operator add-on shows CREATE\_FAILED or DEGRADED status in console
+ CloudFormation stack associated with the add-on is in CREATE\_FAILED state
+ Installation progress stops or shows error messages

**Diagnostic steps:**

1. Check the inference operator add-on status:

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health,Issues:issues}" \
       --output json
   ```

1. Check for pod limit issues:

   ```
   # Check current pod count per node
   kubectl get nodes -o json | jq '.items[] | {name: .metadata.name, allocatable: .status.allocatable.pods, capacity: .status.capacity.pods}'
   
   # Check pods running on each node
   kubectl get pods --all-namespaces -o wide | awk '{print $8}' | sort | uniq -c
   
   # Check for pod evictions or failures
   kubectl get events --all-namespaces --sort-by='.lastTimestamp' | grep -i "pod\|limit\|quota"
   ```

1. Check CloudFormation stack status (if using console installation):

   ```
   # List CloudFormation stacks related to the cluster
   aws cloudformation list-stacks \
       --region $REGION \
       --query "StackSummaries[?contains(StackName, '$EKS_CLUSTER_NAME') && StackStatus=='CREATE_FAILED'].{Name:StackName,Status:StackStatus,Reason:StackStatusReason}" \
       --output table
   
   # Get detailed stack events
   aws cloudformation describe-stack-events \
       --stack-name <stack-name> \
       --region $REGION \
       --query "StackEvents[?ResourceStatus=='CREATE_FAILED']" \
       --output table
   ```

### Resolution
<a name="sagemaker-hyperpod-model-deployment-ts-console-cfn-resolution"></a>

To resolve the installation failure, save the current configuration, delete the failed add-on, fix the underlying issue, and then reinstall the inference operator through the SageMaker AI console (recommended) or the AWS CLI.

**Step 1: Save the current configuration**
+ Extract and save the add-on configuration before deletion:

  ```
  # Save the current configuration
  aws eks describe-addon \
      --cluster-name $EKS_CLUSTER_NAME \
      --addon-name amazon-sagemaker-hyperpod-inference \
      --region $REGION \
      --query 'addon.configurationValues' \
      --output text > addon-config-backup.json
  
  # Verify the configuration was saved
  cat addon-config-backup.json
  
  # Pretty print for readability
  cat addon-config-backup.json | jq '.'
  ```

**Step 2: Delete the failed add-on**
+ Delete the inference operator add-on:

  ```
  aws eks delete-addon \
      --cluster-name $EKS_CLUSTER_NAME \
      --addon-name amazon-sagemaker-hyperpod-inference \
      --region $REGION
  
  # Wait for deletion to complete
  echo "Waiting for add-on deletion..."
  aws eks wait addon-deleted \
      --cluster-name $EKS_CLUSTER_NAME \
      --addon-name amazon-sagemaker-hyperpod-inference \
      --region $REGION 2>/dev/null || sleep 60
  ```

**Step 3: Fix the underlying issue**

Choose the appropriate resolution based on the failure cause:

If the issue is pod limit exceeded:

```
# The inference operator requires a minimum of 13 pods.
# The minimum recommended instance type is ml.c5.4xlarge.
#
# Option 1: Add instance group with higher pod capacity
# Different instance types support different maximum pod counts
# For example: m5.large (29 pods), m5.xlarge (58 pods), m5.2xlarge (58 pods)
aws sagemaker update-cluster \
    --cluster-name $HYPERPOD_CLUSTER_NAME \
    --region $REGION \
    --instance-groups '[{"InstanceGroupName":"worker-group-2","InstanceType":"ml.m5.xlarge","InstanceCount":2}]'

# Option 2: Scale existing node group to add more nodes
aws eks update-nodegroup-config \
    --cluster-name $EKS_CLUSTER_NAME \
    --nodegroup-name <nodegroup-name> \
    --scaling-config minSize=2,maxSize=10,desiredSize=5 \
    --region $REGION

# Option 3: Clean up unused pods
kubectl delete pods --field-selector status.phase=Failed --all-namespaces
kubectl delete pods --field-selector status.phase=Succeeded --all-namespaces
```

**Step 4: Reinstall the inference operator**

After fixing the underlying issue, reinstall the inference operator using one of the following methods:
+ **SageMaker AI console with Custom Install (recommended):** Reuse existing IAM roles and TLS bucket from your previous installation. For steps, see [Method 1: Install HyperPod Inference Add-on through SageMaker AI console (Recommended)](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-ui).
+ **AWS CLI with saved configuration:** Use the configuration you backed up in Step 1 to reinstall the add-on. For the full CLI installation steps, see [Method 2: Installing the Inference Operator using the AWS CLI](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-addon).

  ```
  aws eks create-addon \
      --cluster-name $EKS_CLUSTER_NAME \
      --addon-name amazon-sagemaker-hyperpod-inference \
      --addon-version v1.0.0-eksbuild.1 \
      --configuration-values file://addon-config-backup.json \
      --region $REGION
  ```
+ **SageMaker AI console with Quick Install:** Creates new IAM roles, TLS bucket, and dependency add-ons automatically. For steps, see [Method 1: Install HyperPod Inference Add-on through SageMaker AI console (Recommended)](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-ui).

**Step 5: Verify successful installation**

```
# Check add-on status
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health}" \
    --output table

# Verify pods are running
kubectl get pods -n hyperpod-inference-system

# Check operator logs
kubectl logs -n hyperpod-inference-system deployment/hyperpod-inference-controller-manager --tail=50
```

## Cert-manager installation failed due to Kueue webhook not ready
<a name="sagemaker-hyperpod-model-deployment-ts-console-kueue-webhook-race"></a>

**Problem:** The cert-manager add-on installation fails with a webhook error because the Task Governance (Kueue) webhook service has no available endpoints. This is a race condition that occurs when cert-manager tries to create resources before the Task Governance webhook pods are fully running. This can happen when Task Governance add-on is being installed along with the Inference operator during cluster creation.

### Symptoms and diagnosis
<a name="sagemaker-hyperpod-model-deployment-ts-console-kueue-symptoms"></a>

**Error message:**

```
AdmissionRequestDenied
Internal error occurred: failed calling webhook "mdeployment.kb.io": failed to call webhook: 
Post "https://kueue-webhook-service.kueue-system.svc:443/mutate-apps-v1-deployment?timeout=10s": 
no endpoints available for service "kueue-webhook-service"
```

**Root cause:**
+ Task Governance add-on installs and registers a mutating webhook that intercepts all Deployment creations
+ Cert-manager add-on tries to create Deployment resources before Task Governance webhook pods are ready
+ Kubernetes admission control calls the Task Governance webhook, but it has no endpoints (pods not running yet)

**Diagnostic step:**

1. Check cert-manager add-on status:

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name cert-manager \
       --region $REGION \
       --query "addon.{Status:status,Health:health,Issues:issues}" \
       --output json
   ```

### Resolution
<a name="sagemaker-hyperpod-model-deployment-ts-console-kueue-resolution"></a>

**Solution: Delete and reinstall cert-manager**

The Task Governance webhook becomes ready within 60 seconds. Simply delete and reinstall the cert-manager add-on:

1. Delete the failed cert-manager add-on:

   ```
   aws eks delete-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name cert-manager \
       --region $REGION
   ```

1. Wait 30-60 seconds for the Task Governance webhook to become ready, then reinstall the cert-manager add-on:

   ```
   sleep 60
   
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name cert-manager \
       --region $REGION
   ```