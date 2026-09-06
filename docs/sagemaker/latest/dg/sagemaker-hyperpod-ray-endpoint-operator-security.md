

# Security best practices for the HyperPod Ray Endpoint Operator
<a name="sagemaker-hyperpod-ray-endpoint-operator-security"></a>

The following best practices help you secure your HyperPod Ray Endpoint Operator deployment. For installation instructions, see [Installing the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator.md).

## Configure KMS signing
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-kms"></a>

We recommend that you install the HyperPod Ray Endpoint Operator with an AWS KMS key so that JWT signing keys are generated from AWS KMS rather than locally. This provides an out-of-band revocation mechanism: you can disable the AWS KMS key to invalidate all sessions without requiring cluster access. CloudTrail also records each key generation event, giving you an audit trail for signing key rotations. For setup instructions, see [Set up KMS signing (recommended)](sagemaker-hyperpod-ray-endpoint-operator.md#sagemaker-hyperpod-ray-endpoint-operator-kms-setup).

## Do not share presigned URLs
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-presigned-urls"></a>

A presigned URL grants authenticated access to one Ray cluster's dashboard, which includes job logs, scripts, metrics, and environment variables. Anyone with the URL can access the dashboard until the token expires. The token embedded in the URL is valid for 15 minutes. If the URL is accessed within that window, the resulting session remains valid for up to 6 hours unless you revoke all sessions.

Both the token and the session cookie are scoped to a single cluster's public endpoint and cannot be used to access other clusters through the HyperPod Ray Endpoint Operator's authenticated path.

## Do not store secrets in Ray job environment variables
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-secrets"></a>

Environment variables and entrypoint scripts are visible through the Ray dashboard. Use Kubernetes Secrets or Secrets Manager instead. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

## Use sagemaker\_ray:// for programmatic job submission
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-sagemaker-ray"></a>

The `sagemaker_ray://` address scheme handles authentication without exposing a URL in terminal output or logs. The [toolkit-for-ray-on-sagemaker-ai](https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/) Python library on the PyPI website registers this scheme, so Ray's standard Jobs CLI and Python SDK authenticate through the cluster's secured endpoint. The library is preinstalled in SageMaker AI Distribution images. For more information, see [Submitting jobs remotely with the toolkit library](sagemaker-hyperpod-ray-remote-job-submission.md).

```
ray job submit --address "sagemaker_ray://{{cluster-name}}/{{namespace}}" -- python train.py
```

## Restrict in-cluster access to Ray dashboards
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-in-cluster"></a>

The HyperPod Ray Endpoint Operator authenticates access through the public endpoint, but the Ray dashboard port (8265) on the head service is accessible from within the cluster network without authentication. To limit dashboard access from non-Ray workloads, enable Ray's Kubernetes RBAC authentication mode (`RAY_AUTH_MODE=token` and `RAY_ENABLE_K8S_TOKEN_AUTH=true` on the head container). This requires Ray 2.55 or later and KubeRay 1.6 or later. When enabled, the Ray head rejects requests that do not carry a valid Kubernetes ServiceAccount token with `ray:write` permission. For more information, see [KubeRay RBAC configuration](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/helm-chart-rbac.html) in the Ray documentation.

For stronger isolation between users who share a cluster, deploy RayClusters in separate namespaces and apply NetworkPolicies that restrict ingress on port 8265 to only Traefik pods in the operator namespace (`hyperpod-ray`). This requires a CNI plugin that enforces NetworkPolicies, such as the Amazon VPC CNI with `ENABLE_NETWORK_POLICY=true`. For more information, see [Kubernetes network policies](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html) in the *Amazon EKS User Guide*.

Additionally, scope down RBAC permissions for end users. Deny the following:
+ `pods/portforward` on Ray head pods
+ `pods/exec` on operator or Traefik pods
+ `create` on `roles` or `rolebindings`
+ `get` on `secrets`
+ `impersonate` on service accounts

For more information about Kubernetes RBAC, see [Identity and access management](https://docs.aws.amazon.com/eks/latest/userguide/security-iam.html) in the *Amazon EKS User Guide*.

## Use unique session names for shared execution roles
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-session-names"></a>

The HyperPod Ray Endpoint Operator identifies users by their full IAM principal ARN, which includes the role session name (for example, `arn:aws:sts::123456789012:assumed-role/DataScientist/alice`). If multiple users assume the same IAM role with the same session name, the operator cannot distinguish between them and treats them as the same identity.

To enable per-user access control when users share an execution role, configure unique session names for each user. For more information, see [sts:RoleSessionName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_rolesessionname) in the *IAM User Guide*.

## Revoking sessions
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-revoke"></a>

To revoke all sessions (requires cluster access), run the following commands. This invalidates sessions for all users on all Ray clusters in the Amazon EKS cluster.

```
kubectl patch secret hyperpod-ray-endpoint-operator-extensionapi-jwt-secret \
  -n hyperpod-ray --type merge -p '{"data":null}'

kubectl create job --from=cronjob/hyperpod-ray-endpoint-operator-jwt-rotator \
  manual-rotate -n hyperpod-ray
```

To revoke all sessions through AWS KMS (no cluster access required), disable the AWS KMS key in the AWS Management Console or by using the AWS CLI. For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the *AWS KMS Developer Guide*.

```
aws kms disable-key --key-id {{key-id}}
```

Existing signing keys expire within 30 minutes. Active sessions that were established with the previous signing keys remain valid until those keys are invalidated by the rotation. After the rotator generates new keys, sessions signed by the old keys can no longer be verified and are effectively revoked.

## Audit dashboard access
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-audit"></a>

We recommend that you install the Amazon CloudWatch Observability Amazon EKS add-on for log collection and retention. For more information, see [Install the CloudWatch Observability EKS add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html) in the *Amazon CloudWatch User Guide*.

The HyperPod Ray Endpoint Operator writes access logs to `/aws/containerinsights/{{eks-cluster-name}}/application` from the `authmiddleware` container. Search for:
+ `"Session established"` — logged when a JWT token is successfully exchanged for a session cookie.
+ `"cluster accessed"` — logged on every subsequent request that uses the session cookie.

## Keep the Helm chart updated
<a name="sagemaker-hyperpod-ray-endpoint-operator-security-helm-updates"></a>

**Important**  
The deployed chart does not receive security updates automatically. You must manually upgrade to a newer chart when it becomes available.

We recommend that you routinely update to the latest version of the HyperPod Ray Endpoint Operator Helm chart to ensure that you have the latest security fixes and improvements. When upgrading, change `install` to `upgrade` in the Helm command:

```
helm upgrade --install hyperpod-ray-endpoint-operator \
  ./helm_chart/HyperPodHelmChart/charts/hyperpod-ray-endpoint-operator \
  --namespace hyperpod-ray \
  --set region={{region}} \
  --set domain={{your-route53-domain}} \
  --set manager.enableEndpointsByDefault={{true|false}} \
  --set kmsKeyArn="arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
```