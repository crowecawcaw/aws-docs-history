

# Inference Gateway for Amazon SageMaker HyperPod Inference
<a name="sagemaker-hyperpod-model-deployment-inference-gateway"></a>

The Amazon SageMaker HyperPod Inference Gateway is a Kubernetes-native, large language model (LLM)-aware routing and orchestration layer for HyperPod clusters on Amazon EKS. It inspects inference requests, reads the model name from each request, and selects a model-serving pod based on GPU load, so that traffic for multiple models is routed efficiently through a single gateway endpoint.

The gateway routes each request through three layers. The Body-Based Router (BBR), a shared component, reads the `model` field from the request body, resolves a LoRA adapter name to its base model, and sets the `X-Gateway-Model-Name` and `X-Gateway-Base-Model-Name` headers. The gateway then matches those headers to an HTTPRoute and forwards the request to the `InferencePool` for the requested model. Within that pool, the Endpoint Picker (EPP/scheduler) chooses a model-serving pod by scoring candidates on model-server metrics such as queue depth and KV cache utilization, together with prefix-cache and LoRA adapter affinity. Each entry that you define under `spec.schedulers` runs its own Endpoint Picker, so this topic uses the terms Endpoint Picker, EPP, and scheduler interchangeably.

The Inference Gateway builds on the [HyperPod Inference Operator](sagemaker-hyperpod-model-deployment.md) instead of replacing it. While the operator continues to orchestrate model deployment, the gateway introduces an LLM-aware routing layer in front of the model-serving pods. The gateway does not depend on a specific model server or orchestration layer, and is delivered through the HyperPod Inference Amazon EKS add-on.

You define a gateway with the `InferenceGatewayConfig` custom resource. A single `InferenceGatewayConfig` describes one gateway: the shared Body-Based Router, TLS termination, request authentication, and one scheduler for each model the gateway serves. For the full schema, see [InferenceGatewayConfig CRD reference](#sagemaker-hyperpod-model-deployment-inference-gateway-crd).

**Important**  
Endpoints created by the Inference Gateway have no request-level authentication or authorization by default. Unless you configure `spec.auth.jwt` on the `InferenceGatewayConfig`, the gateway accepts any request that reaches it; access is restricted only by your VPC and network controls. We strongly recommend enabling JWT authentication on every gateway. To configure authentication, see [Prerequisites and deployment](#sagemaker-hyperpod-model-deployment-inference-gateway-prereqs) and `spec.auth` under [spec fields](#sagemaker-hyperpod-model-deployment-inference-gateway-spec).

## Prerequisites and deployment
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-prereqs"></a>

The Inference Gateway is delivered as part of the HyperPod Inference Amazon EKS add-on. Installing the add-on makes the gateway available, so no separate installation is required. You then turn on gateway routing for a model through the `spec.inferenceGateway.enabled` field on the model's `InferenceEndpointConfig` resource. For the version in which a capability was introduced, see [Amazon SageMaker HyperPod Inference release notes](sagemaker-hyperpod-inference-release-notes.md).

Before you route traffic through the gateway, verify the following:

Deployed model-serving pods  
Each scheduler routes to model-serving pods selected by a label selector. Deploy your models with the HyperPod Inference Operator, and note the labels applied to their pods so that you can reference them in the gateway configuration. To list the labels on your model pods, run the following command:  

```
kubectl get pods -n NAMESPACE --show-labels
```

Model server versions  
The Inference Gateway requires vLLM v0.9.2 or later and SGLang v0.3.5.post1 or later. On earlier vLLM versions, the KV cache metric is published under a different name from the one the gateway reads. Requests are still routed using the remaining signals, but KV cache utilization is ignored and no error is reported. Earlier SGLang versions do not support the `--enable-metrics` flag and the container fails to start. Start SGLang with this flag so the gateway can read the metrics it needs for routing decisions.

Add-on version  
The Inference Gateway is available starting with version `v2.0.0-eksbuild.2` of the Amazon SageMaker HyperPod Inference add-on. Install or update to the latest available version of the add-on. If your cluster does not recognize the `InferenceGatewayConfig` resource, the add-on is running an earlier version that does not include the gateway.

Cluster dependencies  
+ cert-manager must be installed on the cluster for the auto-issue TLS path, which the gateway uses when `spec.tls` is set without an `acmArn`.
+ The AWS Load Balancer Controller must be installed for the Application Load Balancer endpoint type.
+ The gateway uses the `hyperpod-inference-system` namespace.

TLS certificate  
To terminate HTTPS at the gateway, either provide an existing ACM certificate ARN or let the gateway auto-issue a certificate. Auto-issue uses cert-manager and imports the certificate into ACM. This flow requires the operator execution role to have the `acm:ImportCertificate`, `acm:AddTagsToCertificate`, `acm:DescribeCertificate`, and `acm:DeleteCertificate` permissions through IRSA.

Request authentication (recommended)  
We strongly recommend enabling JWT authentication on every gateway by setting `spec.auth.jwt` on the `InferenceGatewayConfig`. When `spec.auth` is omitted, the gateway has no request-level authentication and access is restricted only by your VPC and network controls. To enable JWT authentication, have the following ready before you author the `InferenceGatewayConfig`: an OIDC issuer URL, the HTTPS JWKS endpoint that publishes the issuer's signing keys, and the audience values (or required claims) that tokens for this gateway must carry. See `spec.auth` under [spec fields](#sagemaker-hyperpod-model-deployment-inference-gateway-spec) for the full schema.

### Set up the certificate issuer IAM role
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-prereqs-certrole"></a>

When the gateway auto-issues a TLS certificate, cert-manager generates the certificate in the cluster and the gateway controller imports it into ACM. Because the import is an AWS API call, the controller needs AWS credentials. Provide them by creating an IAM role that the `inference-gateway-controller` service account in the `hyperpod-inference-system` namespace assumes through IAM roles for service accounts (IRSA).

**Important**  
TLS auto-issue is enabled by default, and the gateway controller reads this role when it starts. Create the role before you install the add-on.

Set the following environment variables and retrieve the OIDC issuer for your cluster.

```
export CLUSTER=EKS_CLUSTER_NAME
export REGION=REGION
export ACCOUNT=AWS_ACCOUNT_ID
export ROLE_NAME=CERT_ISSUER_ROLE_NAME

export OIDC_ID=$(aws eks describe-cluster --name $CLUSTER --region $REGION \
  --query 'cluster.identity.oidc.issuer' --output text | sed 's|https://||')
```

Create a trust policy that allows the gateway controller service account to assume the role.

```
cat > trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Federated": "arn:aws:iam::${ACCOUNT}:oidc-provider/${OIDC_ID}"
    },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {
        "${OIDC_ID}:sub": "system:serviceaccount:hyperpod-inference-system:inference-gateway-controller",
        "${OIDC_ID}:aud": "sts.amazonaws.com"
      }
    }
  }]
}
EOF
```

Create the role and attach the `AmazonSageMakerHyperPodInferenceGatewayAccess` managed policy. The policy grants the ACM permissions that the controller needs to import, tag, describe, and delete the certificates it creates.

```
aws iam create-role --role-name $ROLE_NAME --assume-role-policy-document file://trust-policy.json
aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayAccess
```

Provide this role ARN as `inferenceGateway.serviceAccount.roleArn` when you install the add-on.

**Note**  
If the role already exists from another cluster, verify that its trust policy includes the OIDC provider for this cluster.

### Install the add-on
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-prereqs-install"></a>

The HyperPod Inference add-on installs both the Inference Operator and the Inference Gateway. Install it with the following command. For `inferenceGateway.serviceAccount.roleArn`, use the certificate issuer role that you created in the preceding section. Replace the remaining placeholder values with the roles and bucket for your account.

```
aws eks create-addon \
  --cluster-name $CLUSTER --region $REGION \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --addon-version v2.0.0-eksbuild.2 \
  --configuration-values '{
    "executionRoleArn": "arn:aws:iam::<ACCOUNT>:role/<EXEC_ROLE>",
    "tlsCertificateS3Bucket": "<TLS_BUCKET>",
    "inferenceOperator": { "enabled": true },
    "inferenceGateway": {
      "enabled": true,
      "serviceAccount": { "roleArn": "arn:aws:iam::<ACCOUNT>:role/<CERT_ISSUER_ROLE_NAME>" }
    },
    "keda": { "enabled": true, "auth": { "aws": { "irsa": { "enabled": true, "roleArn": "arn:aws:iam::<ACCOUNT>:role/<KEDA_IRSA_ROLE>" } } } },
    "alb": { "enabled": true, "serviceAccount": { "create": true, "roleArn": "arn:aws:iam::<ACCOUNT>:role/<ALB_IRSA_ROLE>" } },
    "jumpstartGatedModelDownloadRoleArn": "arn:aws:iam::<ACCOUNT>:role/<JUMPSTART_ROLE>"
  }'
```

If the add-on is already installed on the cluster, replace `create-addon` with `update-addon` and add `--resolve-conflicts OVERWRITE`. The rest of the command is unchanged. `OVERWRITE` applies the configuration values in the command over the existing add-on configuration.

Confirm that the gateway controller is running and that the gateway resources are registered.

```
kubectl rollout status deploy/inference-gateway-controller \
  -n hyperpod-inference-system --timeout=150s

kubectl get crd inferencegatewayconfigs.inference.sagemaker.aws.amazon.com

kubectl get gatewayclass inference-gateway
```

Confirm that the add-on itself is active and reports no health issues.

```
aws eks describe-addon \
  --cluster-name $CLUSTER --region $REGION \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --query 'addon.{version:addonVersion,status:status,health:health.issues}'
```

## Integration with the HyperPod Inference Operator
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-operator-integration"></a>

The HyperPod Inference Operator and the Inference Gateway have distinct responsibilities. The operator owns model deployment, orchestration, and the wiring that attaches a model to the gateway. The gateway owns request routing and generates the routing resources for each scheduler. For more information about deploying models with the operator, see [Deploying models on Amazon SageMaker HyperPod](sagemaker-hyperpod-model-deployment.md).

HyperPod Inference Operator  
Reconciles the model custom resources `InferenceEndpointConfig` and `JumpStartModel` (group `inference.sagemaker.aws.amazon.com`, version `v1`). The operator creates the model Deployment and Service, the Application Load Balancer, KEDA autoscaling, the cert-manager certificate, and the SageMaker AI endpoint registration. When the gateway is enabled for a model, the operator also wires that model into the gateway.

Inference Gateway  
Owns request routing, from the Body-Based Router through the gateway and HTTPRoute to the Endpoint Picker, and generates the downstream routing resources for each scheduler: the `InferencePool`, Endpoint Picker configuration, HTTPRoute, and `EnvoyExtensionPolicy`.

**Note**  
The operator's model custom resources use version `v1`, while the gateway's `InferenceGatewayConfig` resource uses version `v1alpha1`. Both belong to the `inference.sagemaker.aws.amazon.com` group.

You attach a model to the gateway through the operator, on the model's `InferenceEndpointConfig` (or `JumpStartModel`) resource, using the `spec.inferenceGateway` field:

`spec.inferenceGateway.enabled` (Optional, Boolean)  
Whether this model is attached to the gateway. Default: `false`.

`spec.inferenceGateway.name` (Optional, String)  
The name of the `InferenceGatewayConfig` resource to attach to. Models that share a name and namespace share one gateway. When this field is empty, the operator generates a name of the form `inf-igw-<uuid>`.

The following snippet shows the `inferenceGateway` opt-in on an `InferenceEndpointConfig` resource.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: my-model
spec:
  # ... model deployment fields ...
  inferenceGateway:
    enabled: true
    name: my-gateway        # Optional. When empty, the operator generates inf-igw-<uuid>.
```

The operator mirrors the attachment state on the model resource under `status.inferenceGateway`, which reports a `State` of `Pending`, `Ready`, or `Failed`, and the `Name` of the attached `InferenceGatewayConfig`. You cannot set `inferenceGateway.enabled` together with `intelligentRoutingSpec.enabled` on the same model; these fields are mutually exclusive.

When the gateway is enabled for a model, the operator creates or updates a single `InferenceGatewayConfig` resource and merges an entry for the model into its `spec.schedulers` list. The operator sets the scheduler `name`, `modelName`, `targetPort`, and `modelSelector`, and defaults `scheduler` to `llm-d` when it first creates the entry. On later reconciliations, the operator preserves customer-provided values such as `scheduler`, `weights`, and `loraAdapters`. The Body-Based Router is enabled automatically when more than one scheduler is present.

The operator does not delete the `InferenceGatewayConfig` resource or the downstream routing resources. When you disable the gateway for a model or delete the model, the operator removes only that model's scheduler entry. The gateway controller owns cleanup of the routing resources.

You can author an `InferenceGatewayConfig` in two ways, and the two paths coexist on the same resource:
+ Enable the gateway per model through the operator, by setting `spec.inferenceGateway.enabled` on the model's `InferenceEndpointConfig`. The operator authors and maintains the scheduler entry for the model.
+ Author the `InferenceGatewayConfig` resource directly, as shown in [Examples](#sagemaker-hyperpod-model-deployment-inference-gateway-examples).

The gateway components and the `InferenceGatewayConfig` CRD must be installed through the HyperPod Inference Amazon EKS add-on before a model resource with the gateway enabled can be reconciled. For operator add-on installation, see [Installing the Inference Operator with EKS add-on](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-install-inference-operator-addon). For deploying the model-serving pods that a scheduler routes to, see [Deploy foundation models and custom fine-tuned models](sagemaker-hyperpod-model-deployment-deploy.md).

**Note**  
Maintaining the health of the SageMaker HyperPod Inference Operator is a shared responsibility between AWS and the customer. AWS is responsible for delivering and maintaining the SageMaker HyperPod Inference Operator. Following installation, the customer is responsible for monitoring the operational health of the operator within their cluster.

## InferenceGatewayConfig CRD reference
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-crd"></a>

You configure the Inference Gateway with a single `InferenceGatewayConfig` custom resource. The resource is a singleton for a given gateway: it holds the shared Body-Based Router configuration and a list of per-model schedulers. The controller generates the underlying `InferencePool`, Endpoint Picker, HTTPRoute, and `EnvoyExtensionPolicy` resources for each scheduler; you author only the `InferenceGatewayConfig` resource.


**InferenceGatewayConfig resource metadata**  

| Property | Value | 
| --- | --- | 
| Kind | InferenceGatewayConfig | 
| Group | inference.sagemaker.aws.amazon.com | 
| Version | v1alpha1 | 
| Plural | inferencegatewayconfigs | 
| Short name | igwc | 
| Scope | Namespaced | 
| Status subresource | /status | 

### spec fields
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-spec"></a>

The `spec` field of the `InferenceGatewayConfig` resource contains the shared Body-Based Router configuration, TLS settings, the required list of schedulers, and optional observability and pod-default settings.

`bbr` (Required)  
Configuration for the shared Body-Based Router. Contains the following fields:    
`bbr.enabled` (Required, Boolean)  
Whether the Body-Based Router is enabled. The router must be enabled when more than one scheduler is configured.  
`bbr.replicas` (Optional, Integer)  
Number of Body-Based Router replicas. Minimum: `1`. Default: `2`.  
`bbr.defaultBackend` (Optional)  
The backend that receives requests that the router cannot match to a scheduler. Contains a `name` string and a `port` integer (default: `8000`).  
`bbr.maxRequestBodyBytes` (Optional, Integer)  
Maximum request body size, in bytes, that the router buffers to read the `model` field. Default and maximum: `268435456` (256 MiB).

`tls`  
HTTPS termination configuration for the gateway. Contains an `acmArn` field that references an existing ACM certificate. If `tls` is set with an empty `acmArn`, the gateway auto-issues a certificate with cert-manager and imports it into ACM.

`auth` (Optional, Recommended)  
Request authentication configuration. We strongly recommend enabling JWT bearer-token authentication on every gateway; when omitted, the gateway has no request-level authentication. Load balancer health check routes remain unauthenticated so that health probes can succeed without a token.  
Contains `auth.jwt.provider` with the following fields:    
`name` (Required, String)  
Unique name for the provider.  
`issuer` (Required, String)  
OIDC issuer URL (`https://...`). The gateway validates the token's `iss` claim against this value.  
`remoteJWKS.uri` (Required, String)  
HTTPS JWKS endpoint used to verify the JWT signature.  
`audiences` (Optional, List)  
Accepted `aud` claim values (up to 8). At least one of `audiences` or `requiredClaims` must be set.  
`requiredClaims` (Optional, List)  
Claim-based authorization (up to 16 entries). Each entry has `name`, `valueType` (`String` or `StringArray`), and `values` (1–128 entries, each 1–1024 characters). When set, the gateway denies requests by default and admits only tokens whose claim values match.

`observability` (Optional)  
Observability configuration. Contains `metrics.enabled`, which controls the OpenTelemetry metrics sidecar. Metrics are enabled by default.

`podDefaults` (Optional)  
Default pod settings applied to both the Body-Based Router and Endpoint Picker pods. Supports `resources`, `nodeSelector`, `tolerations`, `affinity`, `labels`, `annotations`, `env`, and `envFrom`.

`schedulers` (Required, List)  
A list of per-model scheduler configurations, keyed by `name`. At least one scheduler is required, and you can define up to 100. Each entry is a `SchedulerSpec`, described in [SchedulerSpec fields](#sagemaker-hyperpod-model-deployment-inference-gateway-scheduler).

### SchedulerSpec fields
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-scheduler"></a>

Each entry in `spec.schedulers` configures routing and endpoint selection for one model. A scheduler names the generated `InferencePool`, Endpoint Picker, HTTPRoute, and `EnvoyExtensionPolicy` resources.

`name` (Required, String)  
The scheduler name. Used to name the generated `InferencePool`, Endpoint Picker, HTTPRoute, and `EnvoyExtensionPolicy` resources. Maximum length: 63 characters.

`modelSelector` (Required)  
A Kubernetes label selector that selects the model-serving pods this scheduler routes to.

`modelName` (Required, String)  
The model name matched against the `model` field in the request body and used as the HTTPRoute header match. Must be unique across schedulers. Maximum length: 253 characters.

`targetPort` (Optional, Integer)  
The port on the model-serving pods that receives forwarded traffic. Range: 1–65535. Default: `8000`.

`appProtocol` (Optional, String)  
The application protocol used to reach the model-serving pods. Valid values: `http`, `kubernetes.io/h2c`. Default: `http`.

`scheduler` (Optional, String)  
The scheduler type, which selects the Endpoint Picker image. Valid values: `llm-d`, `epp`. Default: `llm-d`.

`engineType` (Optional, String)  
The inference engine running in the model-serving pods. This value selects the set of Prometheus metric names that the Endpoint Picker scrapes. Valid values: `vllm`, `sglang`. Default: `vllm`.

`weights` (Optional)  
Scoring weights the Endpoint Picker uses to rank candidate pods. All weights are non-negative integers. Mutually exclusive with `configMapRef`. Supported weights:    
`queue`  
Weight for pending request queue depth. Default: `2`.  
`kvCache`  
Weight for KV cache utilization. Default: `2`.  
`prefix`  
Weight for prefix-cache affinity. Default: `3`.  
`lru`  
Weight for least-recently-used scoring. Valid only when `scheduler` is `llm-d`.  
`loraAffinity`  
Weight for LoRA adapter affinity.  
`runningRequests`  
Weight for the number of running requests on a pod.  
`predictedLatency`  
Weight for predicted request latency.

`configMapRef` (Optional)  
A reference to a ConfigMap that supplies a custom Endpoint Picker configuration, as an alternative to `weights`. Contains a required `name` and a `key` (default: `default-plugins.yaml`). Mutually exclusive with `weights`.

`replicas` (Optional, Integer)  
Number of Endpoint Picker replicas for this scheduler. Minimum: `1`. Default: `2`. When `replicas` is greater than 1, the Endpoint Picker runs in high availability with leader election.

`env` and `envFrom` (Optional)  
Environment variables appended to this scheduler's Endpoint Picker container.

`loraAdapters` (Optional, List)  
LoRA adapter names served behind this scheduler's model. Maximum: 50 items, each up to 253 characters.

`routeTimeout` (Optional, String)  
The HTTPRoute request timeout, as a Gateway API duration (for example, `30s` or `5m`). Set to `0s` to disable the timeout.

`logLevel` (Optional, Integer)  
The Endpoint Picker log verbosity. Range: 0–5.

### Validation rules
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-validation"></a>

The `InferenceGatewayConfig` resource enforces the following validation rules. A resource that violates any of these rules is rejected.
+ The Body-Based Router must be enabled (`bbr.enabled: true`) when more than one scheduler is configured.
+ `modelName` must be unique across all schedulers.
+ Within a scheduler, `weights` and `configMapRef` are mutually exclusive.
+ The `weights.lru` weight is valid only when the scheduler's `scheduler` type is `llm-d`.

### status fields
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-status"></a>

The controller reports the observed state of the gateway in the `status` subresource.

`conditions`  
Standard Kubernetes conditions describing the overall state of the gateway configuration.

`schedulers`  
Per-scheduler status. Each entry contains:    
`name`  
The scheduler name.  
`conditions`  
Conditions describing the state of this scheduler.  
`currentScheduler`  
The scheduler type currently in effect for this entry.  
`rolloutState`  
The rollout state of the scheduler. One of `Pending`, `Progressing`, `Available`, or `Degraded`.

`observedGeneration`  
The generation of the resource most recently reconciled by the controller.

`tls`  
TLS status, reported in auto-issue mode only. Contains `acmArn`, `issuedAt`, and `dnsNames`.

## Kubernetes RBAC permissions
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-rbac"></a>

The Inference Gateway runs as a single controller under the Kubernetes service account `inference-gateway-controller` in the `hyperpod-inference-system` namespace. The Body-Based Router, the per-scheduler Endpoint Pickers, the Gateway controller, and the `InferenceGatewayConfig` reconciler all run under this one controller. Its cluster-scoped permissions are granted by a `ClusterRole` named `sagemaker-inference-gateway-controller-supplement` and a matching `ClusterRoleBinding`. Together they supplement the service account and permissions that the bundled Gateway chart already provides. These permissions are scoped and least-privilege, and the controller does not run as cluster administrator.

The following table lists the controller's cluster-scoped permissions, grouped by purpose. In this table, *full access* means the `create`, `get`, `list`, `watch`, `update`, `patch`, and `delete` verbs.


**Inference Gateway controller permissions**  

| API group | Resources | Verbs | Purpose | 
| --- | --- | --- | --- | 
| inference.sagemaker.aws.amazon.com | inferencegatewayconfigs, including its status and finalizers subresources | get, list, watch, update, and patch for inferencegatewayconfigs; get, update, and patch for its status; update for its finalizers | Reconcile the InferenceGatewayConfig resource, write its status, and manage its finalizer. | 
| gateway.networking.k8s.io | httproutes, gateways, gatewayclasses | Full access for httproutes and gateways; get, list, watch, create, and patch for gatewayclasses | Program request routing through the Gateway API. | 
| inference.networking.k8s.io | inferencepools | Full access | Create the routing backend for each scheduler. | 
| inference.networking.x-k8s.io | inferencepools, inferenceobjectives, inferencemodelrewrites | get, list, watch | Read routing intent for endpoint selection. | 
| gateway.envoyproxy.io | envoyextensionpolicies, envoyproxies, httproutefilters, clienttrafficpolicies, securitypolicies | Full access | Configure the gateway data plane and its telemetry. | 
| Core ("") | configmaps, services, serviceaccounts, events, secrets, pods | Full access for configmaps, services, and serviceaccounts; create and patch for events; get, list, and watch for secrets and pods | Manage the generated workloads and read routing and serving state. | 
| apps | deployments | Full access | Manage the Body-Based Router and Endpoint Picker deployments. | 
| rbac.authorization.k8s.io | roles, rolebindings | Full access | Create the per-scheduler Endpoint Picker Role. | 
| discovery.k8s.io, coordination.k8s.io | endpointslices; leases | get, list, and watch for endpointslices; get, list, watch, create, update, and patch for leases | Endpoint discovery and Endpoint Picker leader election. | 
| networking.k8s.io | ingresses, networkpolicies | Full access | Provision the Application Load Balancer path through the AWS Load Balancer Controller. | 
| cert-manager.io | issuers, certificates (with get, list, and watch on core secrets) | Full access | Auto-issue a TLS certificate when spec.tls is set without an acmArn. | 
| apiextensions.k8s.io | customresourcedefinitions | create; and get, update, patch, and delete restricted by resource name to the specific Gateway API CRDs the gateway manages | Install the custom resource definitions the gateway depends on. | 

**Note**  
The `create` verb on `customresourcedefinitions` is not restricted to specific resource names. The controller installs the Gateway API custom resource definitions it depends on by applying them at startup from its own container image, because their combined size exceeds the Amazon EKS add-on payload limit. Kubernetes does not allow the `create` verb to be restricted to named resources, so this permission is necessarily broad. All other operations on custom resource definitions—`get`, `update`, `patch`, and `delete`—are restricted to the specific custom resource definitions the gateway manages. This permission allows defining only those CRD types; it does not grant access to the data of any custom resource.

The controller also creates the following namespaced roles at runtime, depending on your gateway configuration:
+ *Body-Based Router*—A namespaced `Role` that grants `get`, `list`, and `watch` on `configmaps`, which the router reads to resolve LoRA adapters. When the router runs across multiple namespaces, this is a `ClusterRole` instead.
+ *Endpoint Picker*—A namespaced `Role` that grants read access to `pods`. When an Endpoint Picker runs with more than one replica, the controller also creates a leader-election `Role` for `leases` and `events`. When Prometheus metrics are enabled, the controller creates an optional `ClusterRole` that grants `create` on `tokenreviews` and `subjectaccessreviews` and read access to the `/metrics` endpoint.

**Note**  
When you enable the gateway through the HyperPod Inference Operator, the operator's own controller holds permission to create and update `InferenceGatewayConfig` resources. For how the operator wires a model into the gateway, see [Integration with the HyperPod Inference Operator](#sagemaker-hyperpod-model-deployment-inference-gateway-operator-integration).

Some of these permissions apply only when the corresponding feature is enabled.

## Observability
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-observability"></a>

The Inference Gateway emits Prometheus metrics from every gateway component. Both the Body-Based Router and each Endpoint Picker expose a standard Prometheus `/metrics` endpoint on their pods. Body-Based Router pods run in the `hyperpod-inference-system` namespace; Endpoint Picker pods run in the same namespace as the `InferenceGatewayConfig`. Metrics cover per-model request counters and durations, scheduling latency and per-plugin execution time inside the Endpoint Picker, and aggregated pool metrics such as average KV cache utilization and queue depth. Model-server pod metrics (for example, from vLLM or SGLang) are emitted by the model server itself; the Endpoint Picker scrapes them to score candidate pods.

When `spec.observability.metrics.enabled` is `true` (the default), the gateway controller injects an OpenTelemetry Collector sidecar into every Body-Based Router and Endpoint Picker pod. The sidecar forwards these metrics to the HyperPod inference observability stack, where the built-in Grafana dashboards surface them alongside model-server and cluster metrics. For setup and dashboard details, see [Implementing inference observability on HyperPod clusters](sagemaker-hyperpod-model-deployment-observability.md). Set the field to `false` to skip sidecar injection. For the field reference, see `observability` under [spec fields](#sagemaker-hyperpod-model-deployment-inference-gateway-spec).

To view the gateway metrics in Amazon Managed Grafana, open the *Inference Dashboards* folder and select the *Inference Gateway* dashboard. The dashboard reports gateway-wide availability, request rate, and end-to-end latency, per-scheduler throughput, latency, and errors for each model, and the rate at which the Body-Based Router resolves model names from request bodies.

## Examples
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-examples"></a>

The following examples show common `InferenceGatewayConfig` configurations and how to invoke the gateway.

### Minimal multi-model configuration
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-examples-multimodel"></a>

This example routes to an llm-d scheduler with auto-issued TLS. Because `tls` is set to an empty object, the gateway auto-issues a certificate and imports it into ACM.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: InferenceGatewayConfig
metadata:
  name: inference-gateway-demo
  namespace: inference-gateway
spec:
  bbr:
    enabled: true
  tls: {}                       # Auto-issue a certificate via cert-manager and import to ACM.
  schedulers:
    - name: llama
      modelName: "meta-llama/Llama-3.2-1B-Instruct"
      modelSelector:
        matchLabels:
          app: vllm-llama
      targetPort: 8000
      scheduler: llm-d
```

### SGLang scheduler with explicit weights
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-examples-sglang"></a>

This example uses the `epp` scheduler type with the `sglang` engine and sets explicit Endpoint Picker scoring weights.

```
spec:
  bbr:
    enabled: true
  schedulers:
    - name: qwen7b
      modelName: "Qwen/Qwen2.5-7B-Instruct"
      modelSelector:
        matchLabels:
          app: sglang-qwen7b
      targetPort: 8000
      scheduler: epp
      engineType: sglang
      logLevel: 4
      weights:
        kvCache: 2
        prefix: 3
        runningRequests: 2
```

### LoRA adapter ConfigMap
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-examples-lora"></a>

The Body-Based Router discovers LoRA adapters and their base model from a ConfigMap labeled for BBR management. The router uses this mapping to resolve an adapter name in the request body to its base model.

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: deepseek-adapters
  labels:
    inference.networking.k8s.io/bbr-managed: "true"
data:
  baseModel: deepseek/vllm-deepseek-r1
  adapters: |
    - ski-resorts
    - movie-critique
```

### Invoke the gateway
<a name="sagemaker-hyperpod-model-deployment-inference-gateway-examples-invoke"></a>

The gateway serves an OpenAI-compatible inference endpoint. This is the runtime invocation contract for sending inference requests through the gateway; it is not an AWS API operation. Send requests to the gateway endpoint with the `model` field set to the `modelName` of the target scheduler. The Body-Based Router reads this field to route the request.

```
curl https://your-gateway-endpoint/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```