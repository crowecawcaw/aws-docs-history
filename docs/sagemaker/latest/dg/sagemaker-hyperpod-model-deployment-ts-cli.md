

# Inference operator installation failures through AWS CLI
<a name="sagemaker-hyperpod-model-deployment-ts-cli"></a>

**Overview:** When installing the inference operator through the AWS CLI, add-on installation may fail due to missing dependencies. This section covers common CLI installation failure scenarios and their resolutions.

## Inference add-on installation failed due to missing CSI drivers
<a name="sagemaker-hyperpod-model-deployment-ts-missing-csi-drivers"></a>

**Problem:** The inference operator add-on creation fails because required CSI driver dependencies are not installed on the EKS cluster.

**Symptoms and diagnosis:**

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

1. Check EKS add-on status:

   ```
   # List all add-ons
   aws eks list-addons --cluster-name $EKS_CLUSTER_NAME --region $REGION
   
   # Check specific CSI driver add-ons
   aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-mountpoint-s3-csi-driver --region $REGION 2>/dev/null || echo "S3 CSI driver not installed"
   aws eks describe-addon --cluster-name $EKS_CLUSTER_NAME --addon-name aws-fsx-csi-driver --region $REGION 2>/dev/null || echo "FSx CSI driver not installed"
   ```

1. Check inference operator add-on status:

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health,Issues:issues}" \
       --output json
   ```

**Resolution:**

**Step 1: Install missing S3 CSI driver**

1. Create IAM role for S3 CSI driver (if not already created):

   ```
   # Set up service account role ARN (from installation steps)
   export S3_CSI_ROLE_ARN=$(aws iam get-role --role-name $S3_CSI_ROLE_NAME --query 'Role.Arn' --output text 2>/dev/null || echo "Role not found")
   echo "S3 CSI Role ARN: $S3_CSI_ROLE_ARN"
   ```

1. Install S3 CSI driver add-on:

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name aws-mountpoint-s3-csi-driver \
       --addon-version v1.14.1-eksbuild.1 \
       --service-account-role-arn $S3_CSI_ROLE_ARN \
       --region $REGION
   ```

1. Verify S3 CSI driver installation:

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

1. Install FSx CSI driver add-on:

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

**Step 3: Verify all dependencies**

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
<a name="sagemaker-hyperpod-model-deployment-ts-crd-not-exist"></a>

**Problem:** Custom Resource Definitions (CRDs) are missing when you attempt to create model deployments. This issue occurs when you previously installed and deleted the inference add-on without cleaning up model deployments that have finalizers.

**Symptoms and diagnosis:**

**Root cause:**

If you delete the inference add-on without first removing all model deployments, custom resources with finalizers remain in the cluster. These finalizers must complete before you can delete the CRDs. The add-on deletion process doesn't wait for CRD deletion to complete, which causes the CRDs to remain in a terminating state and prevents new installations.

**To diagnose this issue**

1. Check whether CRDs exist.

   ```
   kubectl get crd | grep inference.sagemaker.aws.amazon.com
   ```

1. Check for stuck custom resources.

   ```
   # Check for JumpStartModel resources
   kubectl get jumpstartmodels -A
   
   # Check for InferenceEndpointConfig resources
   kubectl get inferenceendpointconfigs -A
   ```

1. Inspect finalizers on stuck resources.

   ```
   # Example for a specific JumpStartModel
   kubectl get jumpstartmodels <model-name> -n <namespace> -o jsonpath='{.metadata.finalizers}'
   
   # Example for a specific InferenceEndpointConfig
   kubectl get inferenceendpointconfigs <config-name> -n <namespace> -o jsonpath='{.metadata.finalizers}'
   ```

**Resolution:**

Manually remove the finalizers from all model deployments that weren't deleted when you removed the inference add-on. Complete the following steps for each stuck custom resource.

**To remove finalizers from JumpStartModel resources**

1. List all JumpStartModel resources across all namespaces.

   ```
   kubectl get jumpstartmodels -A
   ```

1. For each JumpStartModel resource, remove the finalizers by patching the resource to set metadata.finalizers to an empty array.

   ```
   kubectl patch jumpstartmodels <model-name> -n <namespace> -p '{"metadata":{"finalizers":[]}}' --type=merge
   ```

   The following example shows how to patch a resource named kv-l1-only.

   ```
   kubectl patch jumpstartmodels kv-l1-only -n default -p '{"metadata":{"finalizers":[]}}' --type=merge
   ```

1. Verify that the model instance is deleted.

   ```
   kubectl get jumpstartmodels -A
   ```

   When all resources are cleaned up, you should see the following output.

   ```
   Error from server (NotFound): Unable to list "inference.sagemaker.aws.amazon.com/v1, Resource=jumpstartmodels": the server could not find the requested resource (get jumpstartmodels.inference.sagemaker.aws.amazon.com)
   ```

1. Verify that the JumpStartModel CRD is removed.

   ```
   kubectl get crd | grep jumpstartmodels.inference.sagemaker.aws.amazon.com
   ```

   If the CRD is successfully removed, this command returns no output.

**To remove finalizers from InferenceEndpointConfig resources**

1. List all InferenceEndpointConfig resources across all namespaces.

   ```
   kubectl get inferenceendpointconfigs -A
   ```

1. For each InferenceEndpointConfig resource, remove the finalizers.

   ```
   kubectl patch inferenceendpointconfigs <config-name> -n <namespace> -p '{"metadata":{"finalizers":[]}}' --type=merge
   ```

   The following example shows how to patch a resource named my-inference-config.

   ```
   kubectl patch inferenceendpointconfigs my-inference-config -n default -p '{"metadata":{"finalizers":[]}}' --type=merge
   ```

1. Verify that the config instance is deleted.

   ```
   kubectl get inferenceendpointconfigs -A
   ```

   When all resources are cleaned up, you should see the following output.

   ```
   Error from server (NotFound): Unable to list "inference.sagemaker.aws.amazon.com/v1, Resource=inferenceendpointconfigs": the server could not find the requested resource (get inferenceendpointconfigs.inference.sagemaker.aws.amazon.com)
   ```

1. Verify that the InferenceEndpointConfig CRD is removed.

   ```
   kubectl get crd | grep inferenceendpointconfigs.inference.sagemaker.aws.amazon.com
   ```

   If the CRD is successfully removed, this command returns no output.

**To reinstall the inference add-on**

After you clean up all stuck resources and verify that the CRDs are removed, reinstall the inference add-on. For more information, see [Installing the Inference Operator with EKS add-on](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-install-inference-operator-addon).

**Verification:**

1. Verify that the inference add-on is successfully installed.

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health}" \
       --output table
   ```

   The Status should be ACTIVE and the Health should be HEALTHY.

1. Verify that CRDs are properly installed.

   ```
   kubectl get crd | grep inference.sagemaker.aws.amazon.com
   ```

   You should see the inference-related CRDs listed in the output.

1. Test creating a new model deployment to confirm that the issue is resolved.

   ```
   # Create a test deployment using your preferred method
   kubectl apply -f <your-model-deployment.yaml>
   ```

**Prevention:**

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

1. Verify that all custom resources are deleted.

1. After you confirm that all resources are cleaned up, delete the inference add-on.

## Inference add-on installation failed due to missing cert-manager
<a name="sagemaker-hyperpod-model-deployment-ts-missing-cert-manager"></a>

**Problem:** The inference operator add-on creation fails because the cert-manager EKS Add-On is not installed, resulting in missing Custom Resource Definitions (CRDs).

**Symptoms and diagnosis:**

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

1. Check inference operator add-on status:

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health,Issues:issues}" \
       --output json
   ```

**Resolution:**

**Step 1: Install cert-manager add-on**

1. Install the cert-manager EKS add-on:

   ```
   aws eks create-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name cert-manager \
       --addon-version v1.18.2-eksbuild.2 \
       --region $REGION
   ```

1. Verify cert-manager installation:

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

1. Monitor the installation:

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
<a name="sagemaker-hyperpod-model-deployment-ts-missing-alb"></a>

**Problem:** The inference operator add-on creation fails because the AWS Load Balancer Controller is not installed or not properly configured for the inference add-on.

**Symptoms and diagnosis:**

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

1. Check inference operator add-on configuration:

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health,ConfigurationValues:configurationValues}" \
       --output json
   ```

**Resolution:**

Choose one of the following options based on your setup:

**Option 1: Let the inference add-on install ALB Controller (Recommended)**
+ Ensure the ALB role is created and properly configured in your add-on configuration:

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
+ If you already have ALB Controller installed, configure the add-on to use the existing installation:

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

1. Verify ALB Controller is working:

   ```
   # Check ALB Controller pods
   kubectl get pods -n hyperpod-inference-system | grep aws-load-balancer-controller
   kubectl get pods -n kube-system | grep aws-load-balancer-controller
   
   # Check service account annotations
   kubectl describe serviceaccount aws-load-balancer-controller -n hyperpod-inference-system 2>/dev/null
   kubectl describe serviceaccount aws-load-balancer-controller -n kube-system 2>/dev/null
   ```

## Inference add-on installation failed due to missing KEDA operator
<a name="sagemaker-hyperpod-model-deployment-ts-missing-keda"></a>

**Problem:** The inference operator add-on creation fails because the KEDA (Kubernetes Event Driven Autoscaler) operator is not installed or not properly configured for the inference add-on.

**Symptoms and diagnosis:**

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

1. Check inference operator add-on configuration:

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query "addon.{Status:status,Health:health,ConfigurationValues:configurationValues}" \
       --output json
   ```

**Resolution:**

Choose one of the following options based on your setup:

**Option 1: Let the inference add-on install KEDA (Recommended)**
+ Ensure the KEDA role is created and properly configured in your add-on configuration:

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
+ If you already have KEDA installed, configure the add-on to use the existing installation:

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

1. Verify KEDA is working:

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