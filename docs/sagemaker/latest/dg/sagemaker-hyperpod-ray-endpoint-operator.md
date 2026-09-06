

# Installing the HyperPod Ray Endpoint Operator
<a name="sagemaker-hyperpod-ray-endpoint-operator"></a>

The HyperPod Ray Endpoint Operator generates authenticated public endpoints for Ray clusters on HyperPod. After installation, you can access the Ray Dashboard securely from anywhere with internet access, submit and monitor jobs, and view logs and cluster metrics without setting up `kubectl port-forward`.

**Important**  
Before you install, review [Security best practices for the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator-security.md) for guidance on securing your deployment.

## Prerequisites
<a name="sagemaker-hyperpod-ray-endpoint-operator-prereqs"></a>
+ The SageMaker Spaces add-on is **Active** with web browser access enabled. The HyperPod Ray Endpoint Operator depends on it. For more information, see [Setting up the Spaces add-on](sagemaker-hyperpod-ray-spaces-addon-setup.md).
+ `kubectl` and `helm` installed, with `kubectl` configured for your cluster.
+ The Amazon EKS Pod Identity Agent add-on is installed on your cluster (required for KMS signing). For more information, see [Set up the EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) in the *Amazon EKS User Guide*.

For general information about installing operators on HyperPod, see [Installing operators](https://docs.aws.amazon.com/sagemaker/latest/dg/operator-install.html).

## How authentication works
<a name="sagemaker-hyperpod-ray-endpoint-operator-how-auth-works"></a>

The HyperPod Ray Endpoint Operator uses short-lived JSON Web Tokens (JWTs) to authenticate access to Ray cluster dashboards. When you request a dashboard URL, the operator verifies your identity through the Amazon EKS API server, confirms that you created the Ray cluster, and returns a presigned URL. When you open this URL, the operator exchanges the token for a session cookie.

The token and session cookie are both scoped to a single Ray cluster's public endpoint. They cannot be used to access other clusters through the HyperPod Ray Endpoint Operator's authenticated path.

JWTs are signed with keys that rotate every 30 minutes. When an AWS KMS key is configured, the rotator uses AWS KMS to generate signing key material. When no AWS KMS key is configured, the rotator generates signing keys locally. We recommend that you configure an AWS KMS key, because it provides an out-of-band revocation mechanism and an CloudTrail audit trail for key generation events.

## Set up KMS signing (recommended)
<a name="sagemaker-hyperpod-ray-endpoint-operator-kms-setup"></a>

The HyperPod Ray Endpoint Operator rotates signing keys every 30 minutes. When an AWS KMS key is configured, the rotator uses it to generate new signing key material. This provides two additional capabilities that are not available with locally generated keys:
+ You can disable the AWS KMS key to revoke all sessions without requiring cluster access.
+ CloudTrail records each key generation event for auditing.

To set up KMS signing, complete the following steps.

1. Create an AWS KMS key. For more information, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS KMS Developer Guide*.

   ```
   aws kms create-key \
     --key-spec SYMMETRIC_DEFAULT \
     --key-usage ENCRYPT_DECRYPT \
     --description "HyperPod Ray Endpoint Operator JWT signing"
   ```

1. Create an IAM role with the following minimum permissions policy. For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "kms:GenerateDataKey",
         "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
       }
     ]
   }
   ```

1. Create the Pod Identity association. For more information, see [Configuring a Kubernetes service account to assume an IAM role with EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-association.html) in the *Amazon EKS User Guide*.

   ```
   aws eks create-pod-identity-association \
     --cluster-name {{eks-cluster-name}} \
     --namespace hyperpod-ray \
     --service-account hyperpod-ray-endpoint-operator-jwt-rotator \
     --role-arn arn:aws:iam::{{account-id}}:role/{{role-name}}
   ```

## Install the HyperPod Ray Endpoint Operator
<a name="sagemaker-hyperpod-ray-endpoint-operator-install"></a>

1. Clone the `sagemaker-hyperpod-cli` repository and check out the latest release tag.

   ```
   git clone https://github.com/aws/sagemaker-hyperpod-cli.git
   cd sagemaker-hyperpod-cli
   git checkout $(git tag --sort=-v:refname | head -n 1)
   ```

1. Install with KMS-based signing (recommended).

   ```
   helm upgrade --install hyperpod-ray-endpoint-operator \
     ./helm_chart/HyperPodHelmChart/charts/hyperpod-ray-endpoint-operator \
     --namespace hyperpod-ray \
     --create-namespace \
     --set region={{region}} \
     --set domain={{your-route53-domain}} \
     --set manager.enableEndpointsByDefault={{true|false}} \
     --set kmsKeyArn="arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
   ```

   To install without KMS (signing keys are generated locally):

   ```
   helm upgrade --install hyperpod-ray-endpoint-operator \
     ./helm_chart/HyperPodHelmChart/charts/hyperpod-ray-endpoint-operator \
     --namespace hyperpod-ray \
     --create-namespace \
     --set region={{region}} \
     --set domain={{your-route53-domain}} \
     --set manager.enableEndpointsByDefault={{true|false}}
   ```

   Where:
   + `domain` is the Route 53 domain that the SageMaker Spaces add-on was configured with.
   + `manager.enableEndpointsByDefault` controls whether authenticated dashboard endpoints are created automatically for every Ray resource. When set to `true`, all Ray resources (`RayCluster`, `RayJob`, `RayService`, `RayCronJob`) get endpoints automatically; individual resources can opt out by adding `access.sagemaker.amazonaws.com/enabled: "false"` to their metadata annotations. When set to `false`, no endpoints are created unless a resource explicitly opts in with `access.sagemaker.amazonaws.com/enabled: "true"`.

1. Confirm the operator pods are running.

   ```
   kubectl get pods -n hyperpod-ray
   ```

## Generate a presigned URL
<a name="sagemaker-hyperpod-ray-endpoint-operator-presigned-url"></a>

After you install the HyperPod Ray Endpoint Operator, generate a presigned URL for a Ray cluster dashboard by using the HyperPod CLI:

```
hyp create ray-dashboard-connection \
  --cluster-name {{ray-cluster-name}} \
  --namespace {{namespace}}
```

This command authenticates through your current kubeconfig context, verifies that you are the cluster owner, and returns a short-lived presigned URL. Open the URL in a browser to access the Ray dashboard.

**Note**  
To generate a presigned URL, your Kubernetes user or service account must have permission to `create` `RayDashboardConnection` resources in the `connection.access.sagemaker.amazonaws.com` API group.

For programmatic job submission, use the [toolkit-for-ray-on-sagemaker-ai](https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/) Python library on the PyPI website with the `sagemaker_ray://` address scheme instead of generating URLs manually:

```
ray job submit --address "sagemaker_ray://{{cluster-name}}/{{namespace}}" -- python train.py
```

The `sagemaker_ray://` address scheme handles authentication without exposing a URL in terminal output or logs.

## Uninstalling
<a name="sagemaker-hyperpod-ray-endpoint-operator-uninstall"></a>

```
helm uninstall hyperpod-ray-endpoint-operator -n hyperpod-ray
```

## Next steps
<a name="sagemaker-hyperpod-ray-endpoint-operator-next-steps"></a>

After installation, review [Security best practices for the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator-security.md) for best practices on securing in-cluster access, managing sessions, and auditing dashboard usage.