# HyperPod inference troubleshooting

This troubleshooting guide addresses common issues that can occur during Amazon SageMaker HyperPod
inference deployment and operation. These problems typically involve VPC networking
configuration, IAM permissions, Kubernetes resource management, and operator
connectivity issues that can prevent successful model deployment or cause deployments to
fail or remain in pending states.

This troubleshooting guide uses the following terminology: **Troubleshooting steps** are diagnostic procedures to identify and
investigate problems, **Resolution** provides the specific
actions to fix identified issues, and **Verification**
confirms that the solution worked correctly.

**Quick reference: Find your issue**

Use the following categories to quickly locate the troubleshooting section relevant to your problem:

- **Add-on installation issues** - See [Inference add-on installation failed due to missing CSI drivers](#sagemaker-hyperpod-model-deployment-ts-missing-csi-drivers "#sagemaker-hyperpod-model-deployment-ts-missing-csi-drivers"), [Inference Custom Resource Definitions are missing during model deployment](#sagemaker-hyperpod-model-deployment-ts-crd-not-exist "#sagemaker-hyperpod-model-deployment-ts-crd-not-exist"), [Inference add-on installation failed due to missing cert-manager](#sagemaker-hyperpod-model-deployment-ts-missing-cert-manager "#sagemaker-hyperpod-model-deployment-ts-missing-cert-manager"), [Inference add-on installation failed due to missing ALB Controller](#sagemaker-hyperpod-model-deployment-ts-missing-alb "#sagemaker-hyperpod-model-deployment-ts-missing-alb"), [Inference add-on installation failed due to missing KEDA operator](#sagemaker-hyperpod-model-deployment-ts-missing-keda "#sagemaker-hyperpod-model-deployment-ts-missing-keda")
- **Permission and IAM issues** - See [VPC ENI permission issue](#sagemaker-hyperpod-model-deployment-ts-permissions "#sagemaker-hyperpod-model-deployment-ts-permissions"), [IAM trust relationship issue](#sagemaker-hyperpod-model-deployment-ts-trust "#sagemaker-hyperpod-model-deployment-ts-trust"), [Inference operator fails to start](#sagemaker-hyperpod-model-deployment-ts-startup "#sagemaker-hyperpod-model-deployment-ts-startup")
- **Deployment and resource issues** - See [Model deployment stuck in pending state](#sagemaker-hyperpod-model-deployment-ts-pending "#sagemaker-hyperpod-model-deployment-ts-pending"), [Model deployment failed state troubleshooting](#sagemaker-hyperpod-model-deployment-ts-failed "#sagemaker-hyperpod-model-deployment-ts-failed"), [Missing NVIDIA GPU plugin error](#sagemaker-hyperpod-model-deployment-ts-gpu "#sagemaker-hyperpod-model-deployment-ts-gpu")
- **Certificate and networking issues** - See [Certificate download timeout](#sagemaker-hyperpod-model-deployment-ts-certificate "#sagemaker-hyperpod-model-deployment-ts-certificate"), [Inference add-on installation failed due to missing cert-manager](#sagemaker-hyperpod-model-deployment-ts-missing-cert-manager "#sagemaker-hyperpod-model-deployment-ts-missing-cert-manager")

## Inference add-on installation failed due to missing CSI drivers

**Problem:** The inference operator add-on creation fails because required CSI driver dependencies are not installed on the EKS cluster.

### Symptoms and diagnosis

**Error messages:**

The following errors appear in the add-on creation logs or inference operator logs:

```
S3 CSI driver not installed (missing CSIDriver s3.csi.aws.com).
Please install the required CSI driver and see the troubleshooting guide for more information.

FSx CSI driver not installed (missing CSIDriver fsx.csi.aws.com).
Please install the required CSI driver and see the troubleshooting guide for more information.
```

**Diagnostic steps:**

1. Check if CSI drivers are installed:

```
# Check for S3 CSI driver
kubectl get csidriver s3.csi.aws.com
kubectl get pods -n kube-system | grep mountpoint

# Check for FSx CSI driver
kubectl get csidriver fsx.csi.aws.com
kubectl get pods -n kube-system | grep fsx
```

2. Check EKS add-on status:

```
# List all add-ons
aws eks list-addons --cluster-name $EKS_CLUSTER_NAME --region $REGION

# Check specific CSI driver add-ons
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-mountpoint-s3-csi-driver --region $REGION 2>/dev/null || echo "S3 CSI driver not installed"
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-fsx-csi-driver --region $REGION 2>/dev/null || echo "FSx CSI driver not installed"
```

3. Check inference operator add-on status:

```
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health,Issues:issues}" \
    --output json
```

### Resolution

**Step 1: Install missing S3 CSI driver**

1. Create IAM role for S3 CSI driver (if not already created):

```
# Set up service account role ARN (from installation steps)
export S3_CSI_ROLE_ARN=$(aws iam get-role --role-name $S3_CSI_ROLE_NAME --query 'Role.Arn' --output text 2>/dev/null || echo "Role not found")
echo "S3 CSI Role ARN: $S3_CSI_ROLE_ARN"
```

2. Install S3 CSI driver add-on:

```
aws eks create-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name aws-mountpoint-s3-csi-driver \
    --addon-version v1.14.1-eksbuild.1 \
    --service-account-role-arn $S3_CSI_ROLE_ARN \
    --region $REGION
```

3. Verify S3 CSI driver installation:

```
# Wait for add-on to be active
aws eks wait addon-active --cluster-name $EKS_CLUSTER_NAME --addon-name aws-mountpoint-s3-csi-driver --region $REGION

# Verify CSI driver is available
kubectl get csidriver s3.csi.aws.com
kubectl get pods -n kube-system | grep mountpoint
```

**Step 2: Install missing FSx CSI driver**

1. Create IAM role for FSx CSI driver (if not already created):

```
# Set up service account role ARN (from installation steps)
export FSX_CSI_ROLE_ARN=$(aws iam get-role --role-name $FSX_CSI_ROLE_NAME --query 'Role.Arn' --output text 2>/dev/null || echo "Role not found")
echo "FSx CSI Role ARN: $FSX_CSI_ROLE_ARN"
```

2. Install FSx CSI driver add-on:

```
aws eks create-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name aws-fsx-csi-driver \
    --addon-version v1.6.0-eksbuild.1 \
    --service-account-role-arn $FSX_CSI_ROLE_ARN \
    --region $REGION

# Wait for add-on to be active
aws eks wait addon-active --cluster-name $EKS_CLUSTER_NAME --addon-name aws-fsx-csi-driver --region $REGION

# Verify FSx CSI driver is running
kubectl get pods -n kube-system | grep fsx
```

### Verify All Dependencies

After installing the missing dependencies, verify they are running correctly before retrying the inference operator installation:

```
# Check all required add-ons are active
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-mountpoint-s3-csi-driver --region $REGION
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-fsx-csi-driver --region $REGION
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name metrics-server --region $REGION
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name cert-manager --region $REGION

# Verify all pods are running
kubectl get pods -n kube-system | grep -E "(mountpoint|fsx|metrics-server)"
kubectl get pods -n cert-manager
```

## Inference Custom Resource Definitions are missing during model deployment

**Problem:** Custom Resource Definitions (CRDs) are missing when you attempt to create model deployments. This issue occurs when you previously installed and deleted the inference add-on without cleaning up model deployments that have finalizers.

### Symptoms and diagnosis

**Root cause:**

If you delete the inference add-on without first removing all model deployments, custom resources with finalizers remain in the cluster. These finalizers must complete before you can delete the CRDs. The add-on deletion process doesn't wait for CRD deletion to complete, which causes the CRDs to remain in a terminating state and prevents new installations.

**To diagnose this issue**

1. Check whether CRDs exist.

```
kubectl get crd | grep inference.sagemaker.aws.amazon.com
```

2. Check for stuck custom resources.

```
# Check for JumpStartModel resources
kubectl get jumpstartmodels -A

# Check for InferenceEndpointConfig resources
kubectl get inferenceendpointconfigs -A
```

3. Inspect finalizers on stuck resources.

```
# Example for a specific JumpStartModel
kubectl get jumpstartmodels <model-name> -n <namespace> -o jsonpath='{.metadata.finalizers}'

# Example for a specific InferenceEndpointConfig
kubectl get inferenceendpointconfigs <config-name> -n <namespace> -o jsonpath='{.metadata.finalizers}'
```

### Resolution

Manually remove the finalizers from all model deployments that weren't deleted when you removed the inference add-on. Complete the following steps for each stuck custom resource.

**To remove finalizers from JumpStartModel resources**

1. List all JumpStartModel resources across all namespaces.

```
kubectl get jumpstartmodels -A
```

2. For each JumpStartModel resource, remove the finalizers by patching the resource to set metadata.finalizers to an empty array.

```
kubectl patch jumpstartmodels <model-name> -n <namespace> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

The following example shows how to patch a resource named kv-l1-only.

```
kubectl patch jumpstartmodels kv-l1-only -n default -p '{"metadata":{"finalizers":[]}}' --type=merge
```

3. Verify that the model instance is deleted.

```
kubectl get jumpstartmodels -A
```

When all resources are cleaned up, you should see the following output.

```
Error from server (NotFound): Unable to list "inference.sagemaker.aws.amazon.com/v1, Resource=jumpstartmodels": the server could not find the requested resource (get jumpstartmodels.inference.sagemaker.aws.amazon.com)
```

4. Verify that the JumpStartModel CRD is removed.

```
kubectl get crd | grep jumpstartmodels.inference.sagemaker.aws.amazon.com
```

If the CRD is successfully removed, this command returns no output.

**To remove finalizers from InferenceEndpointConfig resources**

1. List all InferenceEndpointConfig resources across all namespaces.

```
kubectl get inferenceendpointconfigs -A
```

2. For each InferenceEndpointConfig resource, remove the finalizers.

```
kubectl patch inferenceendpointconfigs <config-name> -n <namespace> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

The following example shows how to patch a resource named my-inference-config.

```
kubectl patch inferenceendpointconfigs my-inference-config -n default -p '{"metadata":{"finalizers":[]}}' --type=merge
```

3. Verify that the config instance is deleted.

```
kubectl get inferenceendpointconfigs -A
```

When all resources are cleaned up, you should see the following output.

```
Error from server (NotFound): Unable to list "inference.sagemaker.aws.amazon.com/v1, Resource=inferenceendpointconfigs": the server could not find the requested resource (get inferenceendpointconfigs.inference.sagemaker.aws.amazon.com)
```

4. Verify that the InferenceEndpointConfig CRD is removed.

```
kubectl get crd | grep inferenceendpointconfigs.inference.sagemaker.aws.amazon.com
```

If the CRD is successfully removed, this command returns no output.

**To reinstall the inference add-on**

After you clean up all stuck resources and verify that the CRDs are removed, reinstall the inference add-on. For more information, see [Installing the Inference Operator with EKS add-on](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-install-inference-operator-addon "sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-install-inference-operator-addon").

### Verification

1. Verify that the inference add-on is successfully installed.

```
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health}" \
    --output table
```

The Status should be ACTIVE and the Health should be HEALTHY. 2. Verify that CRDs are properly installed.

```
kubectl get crd | grep inference.sagemaker.aws.amazon.com
```

You should see the inference-related CRDs listed in the output. 3. Test creating a new model deployment to confirm that the issue is resolved.

```
# Create a test deployment using your preferred method
kubectl apply -f <your-model-deployment.yaml>
```

### Prevention

To prevent this issue, complete the following steps before you uninstall the inference add-on.

1. Delete all model deployments.

```
# Delete all JumpStartModel resources
kubectl delete jumpstartmodels --all -A

# Delete all InferenceEndpointConfig resources
kubectl delete inferenceendpointconfigs --all -A

# Wait for all resources to be fully deleted
kubectl get jumpstartmodels -A
kubectl get inferenceendpointconfigs -A
```

2. Verify that all custom resources are deleted.
3. After you confirm that all resources are cleaned up, delete the inference add-on.

## Inference add-on installation failed due to missing cert-manager

**Problem:** The inference operator add-on creation fails because the cert-manager EKS Add-On is not installed, resulting in missing Custom Resource Definitions (CRDs).

### Symptoms and diagnosis

**Error messages:**

The following errors appear in the add-on creation logs or inference operator logs:

```
Missing required CRD: certificaterequests.cert-manager.io.
The cert-manager add-on is not installed. Please install cert-manager and see the troubleshooting guide for more information.
```

**Diagnostic steps:**

1. Check if cert-manager is installed:

```
# Check for cert-manager CRDs
kubectl get crd | grep cert-manager
kubectl get pods -n cert-manager

# Check EKS add-on status
aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name cert-manager --region $REGION 2>/dev/null || echo "Cert-manager not installed"
```

2. Check inference operator add-on status:

```
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health,Issues:issues}" \
    --output json
```

### Resolution

**Step 1: Install cert-manager add-on**

1. Install the cert-manager EKS add-on:

```
aws eks create-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name cert-manager \
    --addon-version v1.18.2-eksbuild.2 \
    --region $REGION
```

2. Verify cert-manager installation:

```
# Wait for add-on to be active
aws eks wait addon-active --cluster-name $EKS_CLUSTER_NAME --addon-name cert-manager --region $REGION

# Verify cert-manager pods are running
kubectl get pods -n cert-manager

# Verify CRDs are installed
kubectl get crd | grep cert-manager | wc -l
# Expected: Should show multiple cert-manager CRDs
```

**Step 2: Retry inference operator installation**

1. After cert-manager is installed, retry the inference operator installation:

```
# Delete the failed add-on if it exists
aws eks delete-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION 2>/dev/null || echo "Add-on not found, proceeding with installation"

# Wait for deletion to complete
sleep 30

# Reinstall the inference operator add-on
aws eks create-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --addon-version v1.0.0-eksbuild.1 \
    --configuration-values file://addon-config.json \
    --region $REGION
```

2. Monitor the installation:

```
# Check installation status
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health}" \
    --output table

# Verify inference operator pods are running
kubectl get pods -n hyperpod-inference-system
```

## Inference add-on installation failed due to missing ALB Controller

**Problem:** The inference operator add-on creation fails because the AWS Load Balancer Controller is not installed or not properly configured for the inference add-on.

### Symptoms and diagnosis

**Error messages:**

The following errors appear in the add-on creation logs or inference operator logs:

```
ALB Controller not installed (missing aws-load-balancer-controller pods).
Please install the Application Load Balancer Controller and see the troubleshooting guide for more information.
```

**Diagnostic steps:**

1. Check if ALB Controller is installed:

```
# Check for ALB Controller pods
kubectl get pods -n kube-system | grep aws-load-balancer-controller
kubectl get pods -n hyperpod-inference-system | grep aws-load-balancer-controller

# Check ALB Controller service account
kubectl get serviceaccount aws-load-balancer-controller -n kube-system 2>/dev/null || echo "ALB Controller service account not found"
kubectl get serviceaccount aws-load-balancer-controller -n hyperpod-inference-system 2>/dev/null || echo "ALB Controller service account not found in inference namespace"
```

2. Check inference operator add-on configuration:

```
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health,ConfigurationValues:configurationValues}" \
    --output json
```

### Resolution

Choose one of the following options based on your setup:

**Option 1: Let the inference add-on install ALB Controller (Recommended)**

- Ensure the ALB role is created and properly configured in your add-on configuration:

```
# Verify ALB role exists
export ALB_ROLE_ARN=$(aws iam get-role --role-name alb-role --query 'Role.Arn' --output text 2>/dev/null || echo "Role not found")
echo "ALB Role ARN: $ALB_ROLE_ARN"

# Update your addon-config.json to enable ALB
cat > addon-config.json << EOF
{
  "executionRoleArn": "$EXECUTION_ROLE_ARN",
  "tlsCertificateS3Bucket": "$BUCKET_NAME",
  "hyperpodClusterArn": "$HYPERPOD_CLUSTER_ARN",
  "alb": {
    "enabled": true,
    "serviceAccount": {
      "create": true,
      "roleArn": "$ALB_ROLE_ARN"
    }
  },
  "keda": {
    "auth": {
      "aws": {
        "irsa": {
          "roleArn": "$KEDA_ROLE_ARN"
        }
      }
    }
  }
}
EOF
```

**Option 2: Use existing ALB Controller installation**

- If you already have ALB Controller installed, configure the add-on to use the existing installation:

```
# Update your addon-config.json to disable ALB installation
cat > addon-config.json << EOF
{
  "executionRoleArn": "$EXECUTION_ROLE_ARN",
  "tlsCertificateS3Bucket": "$BUCKET_NAME",
  "hyperpodClusterArn": "$HYPERPOD_CLUSTER_ARN",
  "alb": {
    "enabled": false
  },
  "keda": {
    "auth": {
      "aws": {
        "irsa": {
          "roleArn": "$KEDA_ROLE_ARN"
        }
      }
    }
  }
}
EOF
```

**Step 3: Retry inference operator installation**

1. Reinstall the inference operator add-on with the updated configuration:

```
# Delete the failed add-on if it exists
aws eks delete-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION 2>/dev/null || echo "Add-on not found, proceeding with installation"

# Wait for deletion to complete
sleep 30

# Reinstall with updated configuration
aws eks create-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --addon-version v1.0.0-eksbuild.1 \
    --configuration-values file://addon-config.json \
    --region $REGION
```

2. Verify ALB Controller is working:

```
# Check ALB Controller pods
kubectl get pods -n hyperpod-inference-system | grep aws-load-balancer-controller
kubectl get pods -n kube-system | grep aws-load-balancer-controller

# Check service account annotations
kubectl describe serviceaccount aws-load-balancer-controller -n hyperpod-inference-system 2>/dev/null
kubectl describe serviceaccount aws-load-balancer-controller -n kube-system 2>/dev/null
```

## Inference add-on installation failed due to missing KEDA operator

**Problem:** The inference operator add-on creation fails because the KEDA (Kubernetes Event Driven Autoscaler) operator is not installed or not properly configured for the inference add-on.

### Symptoms and diagnosis

**Error messages:**

The following errors appear in the add-on creation logs or inference operator logs:

```
KEDA operator not installed (missing keda-operator pods).
KEDA can be installed separately in any namespace or via the Inference addon.
```

**Diagnostic steps:**

1. Check if KEDA operator is installed:

```
# Check for KEDA operator pods in common namespaces
kubectl get pods -n keda-system | grep keda-operator 2>/dev/null || echo "KEDA not found in keda-system namespace"
kubectl get pods -n kube-system | grep keda-operator 2>/dev/null || echo "KEDA not found in kube-system namespace"
kubectl get pods -n hyperpod-inference-system | grep keda-operator 2>/dev/null || echo "KEDA not found in inference namespace"

# Check for KEDA CRDs
kubectl get crd | grep keda 2>/dev/null || echo "KEDA CRDs not found"

# Check KEDA service account
kubectl get serviceaccount keda-operator -A 2>/dev/null || echo "KEDA service account not found"
```

2. Check inference operator add-on configuration:

```
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Status:status,Health:health,ConfigurationValues:configurationValues}" \
    --output json
```

### Resolution

Choose one of the following options based on your setup:

**Option 1: Let the inference add-on install KEDA (Recommended)**

- Ensure the KEDA role is created and properly configured in your add-on configuration:

```
# Verify KEDA role exists
export KEDA_ROLE_ARN=$(aws iam get-role --role-name keda-operator-role --query 'Role.Arn' --output text 2>/dev/null || echo "Role not found")
echo "KEDA Role ARN: $KEDA_ROLE_ARN"

# Update your addon-config.json to enable KEDA
cat > addon-config.json << EOF
{
  "executionRoleArn": "$EXECUTION_ROLE_ARN",
  "tlsCertificateS3Bucket": "$BUCKET_NAME",
  "hyperpodClusterArn": "$HYPERPOD_CLUSTER_ARN",
  "alb": {
    "serviceAccount": {
      "create": true,
      "roleArn": "$ALB_ROLE_ARN"
    }
  },
  "keda": {
    "enabled": true,
    "auth": {
      "aws": {
        "irsa": {
          "roleArn": "$KEDA_ROLE_ARN"
        }
      }
    }
  }
}
EOF
```

**Option 2: Use existing KEDA installation**

- If you already have KEDA installed, configure the add-on to use the existing installation:

```
# Update your addon-config.json to disable KEDA installation
cat > addon-config.json << EOF
{
  "executionRoleArn": "$EXECUTION_ROLE_ARN",
  "tlsCertificateS3Bucket": "$BUCKET_NAME",
  "hyperpodClusterArn": "$HYPERPOD_CLUSTER_ARN",
  "alb": {
    "serviceAccount": {
      "create": true,
      "roleArn": "$ALB_ROLE_ARN"
    }
  },
  "keda": {
    "enabled": false
  }
}
EOF
```

**Step 3: Retry inference operator installation**

1. Reinstall the inference operator add-on with the updated configuration:

```
# Delete the failed add-on if it exists
aws eks delete-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION 2>/dev/null || echo "Add-on not found, proceeding with installation"

# Wait for deletion to complete
sleep 30

# Reinstall with updated configuration
aws eks create-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --addon-version v1.0.0-eksbuild.1 \
    --configuration-values file://addon-config.json \
    --region $REGION
```

2. Verify KEDA is working:

```
# Check KEDA pods
kubectl get pods -n hyperpod-inference-system | grep keda
kubectl get pods -n kube-system | grep keda
kubectl get pods -n keda-system | grep keda 2>/dev/null

# Check KEDA CRDs
kubectl get crd | grep scaledobjects
kubectl get crd | grep scaledjobs

# Check KEDA service account annotations
kubectl describe serviceaccount keda-operator -n hyperpod-inference-system 2>/dev/null
kubectl describe serviceaccount keda-operator -n kube-system 2>/dev/null
kubectl describe serviceaccount keda-operator -n keda-system 2>/dev/null
```

## Certificate download timeout

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

## Model deployment stuck in pending state

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

## Model deployment failed state troubleshooting

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

## Checking model deployment progress

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

## VPC ENI permission issue

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

## IAM trust relationship issue

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

## Missing NVIDIA GPU plugin error

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

## Inference operator fails to start

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
