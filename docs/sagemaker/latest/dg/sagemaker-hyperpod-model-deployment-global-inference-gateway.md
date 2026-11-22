

# Global Inference Gateway for Amazon SageMaker HyperPod Inference

The Amazon SageMaker HyperPod Global Inference Gateway gives you a single, managed HTTPS endpoint that sends each inference request to the best available model deployment across multiple HyperPod clusters. The clusters can be in the same AWS Region or in different Regions. For every request, the Global Inference Gateway reads the requested model, looks at the live load and health of every cluster that serves that model, and forwards the request to the cluster that is best placed to answer it. If that cluster is overloaded or unavailable, the request fails over to the next-best cluster.

Each HyperPod cluster keeps its own in-cluster [Inference Gateway](sagemaker-hyperpod-model-deployment-inference-gateway.md), which picks the model-serving pod within that cluster. The Global Inference Gateway adds a routing layer above those in-cluster gateways, called members, and picks the member for each request based on its current load (KV cache usage and queue depth), recent error rate, and Region proximity.

Use a Global Inference Gateway when you want to:
+ Serve the same model from several HyperPod clusters behind one endpoint.
+ Keep serving when a cluster, an Availability Zone, or a Region has a problem.
+ Use spare GPU capacity in other clusters or Regions when one cluster is busy.
+ Change how traffic is balanced across clusters without changing client code.

## How it works
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-how-it-works"></a>

A Global Inference Gateway is made of the following parts.

**Global Inference Gateway**  
A regional AWS resource that you create with the SageMaker API. It has an ARN of the form `arn:aws:sagemaker:<region>:<account-id>:global-inference-gateway/<gateway-id>` and an HTTPS endpoint (`EndpointUrl`) that your clients call. SageMaker AI runs and scales the routing fleet behind the endpoint for you. The fleet runs in the Region where you create the Global Inference Gateway, and routes requests to members in that Region or in other supported Regions.

**Member (in-cluster Inference Gateway)**  
An in-cluster inference gateway that you have added to the Global Inference Gateway. A member is identified by three values: the HyperPod cluster ARN, the Kubernetes namespace, and the name of its `InferenceGatewayConfig` resource. A Global Inference Gateway has 1 to 10 members.

**Global routing**  
A setting on an `InferenceGatewayConfig` resource (`spec.globalRouting.enabled`). When it is turned on, the in-cluster inference gateway is published privately over AWS PrivateLink so that a Global Inference Gateway can reach it without a public endpoint. It also starts sending load and health metrics for its models to the Global Inference Gateway.

**Execution role**  
An IAM role in your account that the Global Inference Gateway assumes to reach your member clusters: to read the in-cluster gateway's configuration, register itself with the cluster, and read the cluster gateway's TLS certificate.

The request flow is as follows:

1. A client sends a SigV4-signed HTTPS request to the Global Inference Gateway endpoint. The request body names the model in its `model` field.

1. The Global Inference Gateway authenticates the caller, checks that the caller belongs to the gateway's owning account, and authorizes the request with IAM.

1. It finds every member that currently serves the requested model (a base model name or a LoRA adapter name), and scores each one from its latest metrics: KV cache headroom, queue depth, Region proximity, and error rate.

1. It forwards the request over a private, mutually authenticated TLS connection to the highest-scoring member.

1. The member's in-cluster inference gateway routes the request to a model-serving pod, and the response is returned to the client. Streaming responses are passed through as they are produced.

1. If the chosen member returns a throttling or availability error, the request is retried once on the next-best member.

Each member reports its load and health to the Global Inference Gateway every few seconds. The Global Inference Gateway sends traffic only to members that have reported metrics, and stops sending traffic to a member that reports it can't serve or that hasn't reported for 30 minutes. A member whose metrics are only stale keeps being scored on its last reported load.

### How it relates to the in-cluster inference gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-how-it-relates-to-the-in-cluster-inference-gateway"></a>

The Global Inference Gateway and the in-cluster inference gateway form a two-tier routing system:


**How it relates to the in-cluster inference gateway**  

|  | Tier 1: In-cluster Inference Gateway | Tier 2: Global Inference Gateway | 
| --- | --- | --- | 
| Question it answers | Which pod in this cluster should serve the request? | Which cluster should serve the request? | 
| Where it runs | In your HyperPod cluster, installed by the HyperPod Inference add-on | Managed by SageMaker AI, in the Region where you create it | 
| Signals it uses | Per-pod model server state: KV cache utilization, queue depth, prefix cache, and LoRA adapter affinity | Per-cluster model server state reported by each member (KV cache utilization, queue depth, error rate), plus Region proximity | 
| How you set it up | Add-on plus an InferenceGatewayConfig (or spec.inferenceGateway on a model) | Turn on global routing on each in-cluster gateway, then one SageMaker API create call | 
| Endpoint | One endpoint per cluster | One endpoint for all member clusters, unchanged as you add or remove clusters | 

Each tier is useful on its own. A cluster with only the in-cluster inference gateway gets model-aware routing within that cluster. Adding a Global Inference Gateway adds cross-cluster and cross-Region routing and failover, with no change to your models or to the in-cluster configuration other than turning on global routing. Your in-cluster gateways keep serving their own endpoints while they are members, so applications that call a cluster directly keep working.

Both tiers route on model server signals rather than generic load balancer metrics such as connection count or CPU, and neither depends on a specific model server: any server that publishes the standard metrics that the in-cluster inference gateway reads (for example vLLM or SGLang) works.

## Steps to set up a Global Inference Gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-steps-to-set-up"></a>

To set up a Global Inference Gateway, complete these steps in order:

1. [Prerequisites](#sagemaker-hyperpod-model-deployment-global-inference-gateway-prerequisites)

1. [Plan your Global Inference Gateway](#sagemaker-hyperpod-model-deployment-global-inference-gateway-plan-your-global-inference-gateway)

1. [Step 1: Enable global routing on each in-cluster inference gateway](#sagemaker-hyperpod-model-deployment-global-inference-gateway-step-1-enable-global-routing-on-each-in-cluster-inference-gateway)

1. [Step 2: Create the execution role](#sagemaker-hyperpod-model-deployment-global-inference-gateway-step-2-create-the-execution-role)

1. [Step 3: Create a Global Inference Gateway](#sagemaker-hyperpod-model-deployment-global-inference-gateway-step-3-create-a-global-inference-gateway)

1. [Verify your setup](#sagemaker-hyperpod-model-deployment-global-inference-gateway-verify-your-setup)

1. [Step 4: Invoke the Global Inference Gateway](#sagemaker-hyperpod-model-deployment-global-inference-gateway-step-4-invoke-the-global-inference-gateway)

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-prerequisites"></a>

Before you create a Global Inference Gateway, make sure you have the following:

1. One or more Amazon SageMaker HyperPod clusters orchestrated by Amazon EKS, in the same AWS account, in [supported Regions](#sagemaker-hyperpod-model-deployment-global-inference-gateway-supported-regions). To create one, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md).

1. On each cluster, the Amazon SageMaker HyperPod Inference add-on, version `v3.0.0-eksbuild.1`, with the Inference Gateway turned on, and an `InferenceGatewayConfig` that serves your models. Global routing also uses the AWS Load Balancer Controller, which the add-on installs, and cert-manager, which the console's Quick Install adds. If you installed the add-on with the AWS CLI, install cert-manager as described in [Required Add-ons](sagemaker-hyperpod-model-deployment-setup.md#sagemaker-hyperpod-model-deployment-setup-required-addons). For setup, see [Inference Gateway for Amazon SageMaker HyperPod Inference](sagemaker-hyperpod-model-deployment-inference-gateway.md).

1. Model servers that publish the metrics the in-cluster inference gateway reads: vLLM v0.9.2 or later, or SGLang v0.3.5.post1 or later started with `--enable-metrics`. The Global Inference Gateway routes to a member only when it reports KV cache utilization and queue depth, so a member on an earlier vLLM version receives no traffic.

1. The add-on configured with a TLS certificate bucket (`tlsCertificateS3Bucket`). The in-cluster gateway uploads its global routing certificate to this bucket, and the Global Inference Gateway reads it to verify the cluster's identity. The AWS managed policies in this guide grant access only to buckets whose names begin with `hyperpod-tls`. If your bucket has a different name, add the bucket statements in [Step 1a](#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions) and [Step 2b](#sagemaker-hyperpod-model-deployment-global-inference-gateway-2b-attach-the-permissions-policy).

1. Subnets in at least two Availability Zones of the cluster VPC tagged with `kubernetes.io/role/internal-elb=1`, so that the internal Network Load Balancer for global routing spans two or more Availability Zones.

1. Free IP addresses in the HyperPod cluster's subnets, in at least one Availability Zone that supports an interface endpoint for Amazon Kinesis Data Streams. The controller places the metrics endpoint there.

1. The same model name served by every member that should receive traffic for that model. The Global Inference Gateway routes on the `model` field in the request body, so members are interchangeable only when they serve the model under the same name.

1. The latest version of the AWS CLI. For instructions, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### IAM permissions for the administrator
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-iam-permissions-for-the-administrator"></a>

The IAM user or role that creates and manages Global Inference Gateways needs the following permissions. Add them as an IAM policy attached to that user or role, for example as an inline policy or a customer managed policy. Replace `<region>`, `<account-id>`, and `<execution-role-name>` with your values. For how to attach a policy, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageGlobalInferenceGateways",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateGlobalInferenceGateway",
        "sagemaker:DescribeGlobalInferenceGateway",
        "sagemaker:UpdateGlobalInferenceGateway",
        "sagemaker:DeleteGlobalInferenceGateway",
        "sagemaker:AddInferenceGateway",
        "sagemaker:RemoveInferenceGateway",
        "sagemaker:ListInferenceGateways",
        "sagemaker:AddTags",
        "sagemaker:ListTags"
      ],
      "Resource": "arn:aws:sagemaker:<region>:<account-id>:global-inference-gateway/*"
    },
    {
      "Sid": "ListGlobalInferenceGateways",
      "Effect": "Allow",
      "Action": "sagemaker:ListGlobalInferenceGateways",
      "Resource": "*"
    },
    {
      "Sid": "PassExecutionRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::<account-id>:role/<execution-role-name>"
    }
  ]
}
```

## Plan your Global Inference Gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-plan-your-global-inference-gateway"></a>

Before you start, decide how you want to set up your Global Inference Gateway. You can change members and routing weights later, but the Region and the access model are easier to get right up front.


**Plan your Global Inference Gateway**  

| Decision | Options | Learn more | 
| --- | --- | --- | 
| Region for the Global Inference Gateway | Any supported Region. Clients call its EndpointUrl, and SageMaker AI runs the routing fleet in that Region. Region proximity is measured from this Region, not from the client, so create it in the Region where most of your clients are. | [Supported Regions](#sagemaker-hyperpod-model-deployment-global-inference-gateway-supported-regions) | 
| Members | 1 to 10 in-cluster inference gateways, in the same account. The clusters can be in the same Region or in different Regions, but not in opt-in Regions. Each in-cluster gateway can belong to only one Global Inference Gateway. | [Quotas and limits](#sagemaker-hyperpod-model-deployment-global-inference-gateway-quotas-and-limits) | 
| Routing | The default weights, or your own. Raise RegionProximity to keep traffic in the gateway's Region, QueueDepth when response time matters most, or KVHeadroom for long prompts and responses. | [Choosing routing weights](#sagemaker-hyperpod-model-deployment-global-inference-gateway-choosing-routing-weights) | 
| How clients connect | The public EndpointUrl, or privately from your VPC through AWS PrivateLink. | [Invoke privately with AWS PrivateLink](#sagemaker-hyperpod-model-deployment-global-inference-gateway-invoke-privately-with-aws-privatelink) | 
| Which API clients use | OpenAI-compatible paths (/v1/chat/completions, /v1/completions, /v1/embeddings), or the AWS SDK operations, which return typed errors. | [Step 4](#sagemaker-hyperpod-model-deployment-global-inference-gateway-step-4-invoke-the-global-inference-gateway) | 
| End-user authentication | If your in-cluster gateways use JWT authentication, clients pass the end user's token in a separate header. | [Pass an end-user token to your clusters](#sagemaker-hyperpod-model-deployment-global-inference-gateway-pass-an-end-user-token-to-your-clusters) | 
| Execution role scope | The AWS managed policy, which covers all clusters in the account and TLS buckets named hyperpod-tls\*, or an inline policy scoped to specific clusters and your bucket. | [Step 2b](#sagemaker-hyperpod-model-deployment-global-inference-gateway-2b-attach-the-permissions-policy) | 

## Step 1: Enable global routing on each in-cluster inference gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-step-1-enable-global-routing-on-each-in-cluster-inference-gateway"></a>

Repeat this step on every HyperPod cluster that you want to add as a member.

**Identify the in-cluster inference gateway to add**

Each member is an `InferenceGatewayConfig` resource on a HyperPod cluster. You identify it by three values:
+ `ClusterArn`: the ARN of the HyperPod cluster.
+ `Namespace`: the namespace of the `InferenceGatewayConfig`.
+ `Name`: the name of the `InferenceGatewayConfig`.

The `InferenceGatewayConfig` routes to the model-serving pods that its schedulers select. For how to configure it, see [Inference Gateway for Amazon SageMaker HyperPod Inference](sagemaker-hyperpod-model-deployment-inference-gateway.md).

To list the in-cluster inference gateways on a cluster with their namespaces, run:

```bash
kubectl get inferencegatewayconfig --all-namespaces
```

**Note**  
If you deploy models with the HyperPod Inference Operator and set `spec.inferenceGateway.enabled: true`, the operator creates the `InferenceGatewayConfig` for you, in the model's namespace. Its name is `spec.inferenceGateway.name`, or `inf-igw-<uuid>` if you don't set one. Set the name explicitly so that it's predictable and the same on every cluster.

**Confirm the in-cluster gateway serves your model**

Before you turn on global routing, send a request to the in-cluster inference gateway's own endpoint and confirm that it answers for your model, as described in [Invoke the gateway](sagemaker-hyperpod-model-deployment-inference-gateway.md#sagemaker-hyperpod-model-deployment-inference-gateway-examples-invoke). If this request fails, requests through the Global Inference Gateway fail too. Resolve any issues before you continue.

### 1a. Grant the gateway controller the global routing permissions
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions"></a>

When global routing is turned on, the inference gateway controller creates a VPC endpoint service in front of an internal Network Load Balancer, and uploads the gateway's certificate to your TLS bucket. After you add the in-cluster gateway to a Global Inference Gateway, the controller also creates an interface VPC endpoint and a security group for it. The metrics publisher sends metrics through this endpoint. The controller uses the same IAM role that it uses for TLS auto-issue (the role passed as `inferenceGateway.serviceAccount.roleArn` when you install the add-on).

Attach the `AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess` AWS managed policy to that role. Keep the `AmazonSageMakerHyperPodInferenceGatewayAccess` policy that the role already has for TLS auto-issue.

```bash
aws iam attach-role-policy --role-name <controller-role-name> \
  --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess
```

The policy lets the controller do the following, only in your account:
+ **Endpoint service:** Create and manage the VPC endpoint service in front of the gateway's Network Load Balancer, and let a Global Inference Gateway in another Region connect to it. The controller uses `ec2:DescribeRegions` to include any opt-in Regions that your account has enabled.
+ **Metrics endpoint:** Create the interface VPC endpoint for Amazon Kinesis Data Streams, and its security group, so that the metrics publisher can send metrics. The controller can modify or delete only the endpoints and security groups that it created. Without these permissions, the controller can't create the metrics endpoint, so it doesn't start the metrics publisher, and the member doesn't receive traffic.
+ **Certificate:** Upload the gateway's certificate to your TLS bucket, and use your AWS KMS key through Amazon S3 if the bucket is encrypted with a customer managed key. The controller uploads the certificate every 60 to 75 minutes, so a certificate that's deleted or overwritten is restored within that time. If you change `tlsCertificateS3Bucket`, the controller uses the new bucket after its next restart.
+ **Cluster lookup:** Describe your HyperPod cluster, to find its subnets.

**Note**  
The policy's Amazon S3 permissions apply only to buckets whose names begin with `hyperpod-tls`. If your TLS bucket has a different name, also add the following statements to the controller role's permissions policy. Replace `<tls-bucket>` with your bucket name.

```json
[
  {
    "Sid": "WriteGlobalRoutingCertificate",
    "Effect": "Allow",
    "Action": ["s3:PutObject", "s3:PutObjectTagging"],
    "Resource": "arn:aws:s3:::<tls-bucket>/*gig/*/*-certificate-*.pem",
    "Condition": {
      "StringEquals": {
        "s3:RequestObjectTag/CreatedBy": "HyperPodInference",
        "aws:ResourceAccount": "${aws:PrincipalAccount}"
      },
      "ForAllValues:StringEquals": { "s3:RequestObjectTagKeys": ["CreatedBy"] }
    }
  },
  {
    "Sid": "DeleteGlobalRoutingCertificate",
    "Effect": "Allow",
    "Action": "s3:DeleteObject",
    "Resource": "arn:aws:s3:::<tls-bucket>/*gig/*/*-certificate-*.pem",
    "Condition": { "StringEquals": { "aws:ResourceAccount": "${aws:PrincipalAccount}" } }
  }
]
```

### 1b. Create the metrics publisher role
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-1b-create-the-metrics-publisher-role"></a>

A metrics publisher in the cluster sends the gateway's load and health to the Global Inference Gateway. The Global Inference Gateway uses these metrics to discover which models each member serves, so it doesn't route to a member until its publisher is running. The publisher runs as the Kubernetes service account `hyperpod-inference-system/inference-gateway-metrics-publisher` and uses its own IAM role through IAM roles for service accounts (IRSA).

**To create the metrics publisher role**

1. Set the following variables, and get your cluster's OIDC issuer.

   ```bash
   export CLUSTER=<eks-cluster-name>
   export REGION=<region>
   export ACCOUNT=<account-id>
   export OIDC_ID=$(aws eks describe-cluster --name $CLUSTER --region $REGION \
     --query 'cluster.identity.oidc.issuer' --output text | sed 's|https://||')
   ```

1. Create a trust policy that lets the publisher's service account assume the role.

   ```bash
   cat > publisher-trust-policy.json <<EOF
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Principal": { "Federated": "arn:aws:iam::${ACCOUNT}:oidc-provider/${OIDC_ID}" },
       "Action": "sts:AssumeRoleWithWebIdentity",
       "Condition": {
         "StringEquals": {
           "${OIDC_ID}:sub": "system:serviceaccount:hyperpod-inference-system:inference-gateway-metrics-publisher",
           "${OIDC_ID}:aud": "sts.amazonaws.com"
         }
       }
     }]
   }
   EOF
   ```

1. Create the role, and attach the `AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess` AWS managed policy. The metrics stream belongs to the Global Inference Gateway and is encrypted with an AWS KMS key that the service manages. The policy allows `kinesis:PutRecords` to write metrics, and `kms:GenerateDataKey` through Kinesis so that Kinesis can encrypt them.

   ```bash
   aws iam create-role --role-name AmazonSageMakerInferenceGatewayMetricsPublisherRole \
     --assume-role-policy-document file://publisher-trust-policy.json
   aws iam attach-role-policy --role-name AmazonSageMakerInferenceGatewayMetricsPublisherRole \
     --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess
   ```

### 1c. Update the add-on
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-1c-update-the-add-on"></a>

Update the HyperPod Inference add-on with the metrics publisher role.

**Important**  
`--configuration-values` replaces the add-on's whole configuration, so any value you leave out goes back to its default. Include every value the add-on already has, such as the operator execution role, the TLS bucket, KEDA, the AWS Load Balancer Controller, and the JumpStart role. If the cluster already has a TLS bucket, keep using it.

1. Read the add-on's current configuration.

   ```bash
   aws eks describe-addon --cluster-name $CLUSTER --region $REGION \
     --addon-name amazon-sagemaker-hyperpod-inference \
     --query addon.configurationValues --output text
   ```

1. Update the add-on with those values, plus `inferenceGateway.metricsPublisher`.

   ```bash
   aws eks update-addon \
     --cluster-name $CLUSTER --region $REGION \
     --addon-name amazon-sagemaker-hyperpod-inference \
     --addon-version v3.0.0-eksbuild.1 \
     --resolve-conflicts OVERWRITE \
     --configuration-values '{
       "executionRoleArn": "arn:aws:iam::<account-id>:role/<operator-execution-role>",
       "tlsCertificateS3Bucket": "<tls-bucket>",
       "inferenceOperator": { "enabled": true },
       "inferenceGateway": {
         "enabled": true,
         "serviceAccount": { "roleArn": "arn:aws:iam::<account-id>:role/<cert-issuer-role>" },
         "metricsPublisher": {
           "serviceAccount": { "roleArn": "arn:aws:iam::<account-id>:role/AmazonSageMakerInferenceGatewayMetricsPublisherRole" }
         }
       },
       "alb": { "enabled": true, "serviceAccount": { "create": true, "roleArn": "arn:aws:iam::<account-id>:role/<alb-irsa-role>" } }
     }'
   ```

1. When the update finishes, confirm that the add-on is `ACTIVE` with no health issues, that the controller has rolled out, and that the in-cluster gateway still answers.

   ```bash
   aws eks describe-addon --cluster-name $CLUSTER --region $REGION \
     --addon-name amazon-sagemaker-hyperpod-inference \
     --query 'addon.{version:addonVersion,status:status,health:health.issues}'
   kubectl rollout status deploy/inference-gateway-controller -n hyperpod-inference-system --timeout=150s
   ```

### 1d. Turn on global routing
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-1d-turn-on-global-routing"></a>

Set `spec.globalRouting.enabled` to `true` on the `InferenceGatewayConfig` that you want to add as a member.

```yaml
apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: InferenceGatewayConfig
metadata:
  name: my-gateway
  namespace: my-namespace
spec:
  bbr:
    enabled: true
  tls: {}
  globalRouting:
    enabled: true
  schedulers:
    - name: llama
      modelName: meta-llama/Llama-3.1-8B-Instruct
      modelSelector:
        matchLabels:
          app: llama
      targetPort: 8000
```

To turn it on for an existing configuration, run:

```bash
kubectl -n my-namespace patch inferencegatewayconfig my-gateway --type merge \
  -p '{"spec":{"globalRouting":{"enabled":true}}}'
```

No additional access configuration is required. The controller configures the endpoint service to accept connections only from the SageMaker Global Inference Gateway service, in every supported Region that your account can use.

### 1e. Verify
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-1e-verify"></a>

Wait until the configuration reports `Ready` for global routing.

To check the global routing status, run the following command:

```bash
kubectl -n my-namespace get inferencegatewayconfig my-gateway
```

The output should look similar to the following:

```
NAME         READY   GLOBAL-ROUTING   VPCE-SERVICE                                              AGE
my-gateway   True    Ready            com.amazonaws.vpce.us-west-2.vpce-svc-0123456789abcdef0   5m
```

If `GLOBAL-ROUTING` doesn't reach `Ready`, see [Global Inference Gateway troubleshooting guide](sagemaker-hyperpod-model-deployment-ts-global-inference-gateway.md).

**Note**  
The metrics publisher starts only after you add the in-cluster gateway to a Global Inference Gateway (Step 3). Until then, the `MetricsPublisherReady` condition doesn't apply.

## Step 2: Create the execution role
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-step-2-create-the-execution-role"></a>

The Global Inference Gateway uses an execution role in your account to read and update the configuration of each member cluster. It never accesses your clusters with its own identity. The role, the Global Inference Gateway, and every member cluster must be in the same AWS account.

### 2a. Create the role
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-2a-create-the-role"></a>

Create a trust policy that allows the Global Inference Gateway service to assume the role only for Global Inference Gateways in your account.. The `aws:SourceAccount` and `aws:SourceArn` conditions prevent another account's Global Inference Gateway from using your role (the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html)).

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "global-inference-gateway.sagemaker.amazonaws.com" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "<account-id>" },
        "ArnLike": { "aws:SourceArn": "arn:aws:sagemaker:*:<account-id>:global-inference-gateway/*" }
      }
    }
  ]
}
```

After you create the Global Inference Gateway, you can restrict the role to it by replacing `global-inference-gateway/*` with `global-inference-gateway/<gateway-id>`. Keep the wildcard until then: the ID is assigned at creation, and the Global Inference Gateway assumes the role while it is being created.

### 2b. Attach the permissions policy
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-2b-attach-the-permissions-policy"></a>

Attach the `AmazonSageMakerGlobalInferenceGatewayExecutionAccess` AWS managed policy to the execution role.

```bash
aws iam attach-role-policy --role-name <execution-role-name> \
  --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerGlobalInferenceGatewayExecutionAccess
```

The policy lets the role describe HyperPod clusters, call the Kubernetes API of their EKS clusters, and read the gateway certificates from your TLS bucket, only in your account. Kubernetes RBAC limits what the role can do in each cluster (see [Step 2c](#sagemaker-hyperpod-model-deployment-global-inference-gateway-2c-grant-the-role-access-to-each-members-kubernetes-api)).

Use an inline policy instead if your TLS bucket name doesn't begin with `hyperpod-tls`, or if you want to limit the role to specific clusters. Scope each statement to your member clusters and TLS bucket.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DescribeMemberCluster",
      "Effect": "Allow",
      "Action": "sagemaker:DescribeCluster",
      "Resource": "arn:aws:sagemaker:<cluster-region>:<account-id>:cluster/<cluster-id>"
    },
    {
      "Sid": "MemberKubernetesApi",
      "Effect": "Allow",
      "Action": ["eks:AccessKubernetesApi", "eks:MutateViaKubernetesApi"],
      "Resource": "arn:aws:eks:<cluster-region>:<account-id>:cluster/<eks-cluster-name>"
    },
    {
      "Sid": "ReadGatewayCertificate",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<tls-bucket>/gig/*",
      "Condition": { "StringEquals": { "s3:ExistingObjectTag/CreatedBy": "HyperPodInference" } }
    }
  ]
}
```

### 2c. Grant the role access to each member's Kubernetes API
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-2c-grant-the-role-access-to-each-members-kubernetes-api"></a>

On each member's EKS cluster, create an access entry that maps the execution role to the Kubernetes group `sagemaker-global-inference-gateway`. The cluster's authentication mode must include `API` (`API` or `API_AND_CONFIG_MAP`). Don't attach any access policies. The HyperPod Inference add-on already grants this group the minimum permissions that the Global Inference Gateway needs:
+ read access to `InferenceGatewayConfig` resources
+ write access to the ConfigMap that records gateway membership

```bash
aws eks create-access-entry \
  --cluster-name <eks-cluster-name> --region <cluster-region> \
  --principal-arn arn:aws:iam::<account-id>:role/<execution-role-name> \
  --type STANDARD \
  --kubernetes-groups sagemaker-global-inference-gateway
```

If `create-access-entry` fails with an invalid principal error right after you create the role, wait a few seconds for the role to propagate in IAM, and then run it again.

## Step 3: Create a Global Inference Gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-step-3-create-a-global-inference-gateway"></a>

Create the Global Inference Gateway with one or more members, up to 10 (see [Quotas and limits](#sagemaker-hyperpod-model-deployment-global-inference-gateway-quotas-and-limits)). Each member is the HyperPod cluster ARN, the namespace, and the name of an `InferenceGatewayConfig` that has global routing turned on.

```bash
aws sagemaker create-global-inference-gateway \
  --region us-west-2 \
  --name my-global-gateway \
  --execution-role-arn arn:aws:iam::<account-id>:role/<execution-role-name> \
  --gateways '[
    {"ClusterArn": "arn:aws:sagemaker:us-west-2:<account-id>:cluster/<cluster-id-1>", "Namespace": "my-namespace", "Name": "my-gateway"},
    {"ClusterArn": "arn:aws:sagemaker:us-east-1:<account-id>:cluster/<cluster-id-2>", "Namespace": "my-namespace", "Name": "my-gateway"}
  ]'
```

The response returns immediately with `Status` set to `CREATING`.

```json
{
  "Arn": "arn:aws:sagemaker:us-west-2:<account-id>:global-inference-gateway/k3x9p2m7q1ab",
  "Id": "k3x9p2m7q1ab",
  "Name": "my-global-gateway",
  "Status": "CREATING",
  "ExecutionRoleArn": "arn:aws:iam::<account-id>:role/<execution-role-name>",
  "Gateways": [ ... ]
}
```

Optionally, pass `--routing` to set your own routing weights. If you omit it, the default weights are used. For details, see [Routing behavior](#sagemaker-hyperpod-model-deployment-global-inference-gateway-routing-behavior).

### Wait for the Global Inference Gateway to become active
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-wait-for-the-global-inference-gateway-to-become-active"></a>

Creation typically takes 5 to 10 minutes, and can take up to 20 minutes. To check the status, run `describe-global-inference-gateway` with the Global Inference Gateway's name, ID, or ARN.

```bash
aws sagemaker describe-global-inference-gateway --region us-west-2 --identifier my-global-gateway
```

When the Global Inference Gateway is ready, `Status` is `ACTIVE` and the response includes the `EndpointUrl`. The output should look similar to the following:

```json
{
  "Arn": "arn:aws:sagemaker:us-west-2:<account-id>:global-inference-gateway/k3x9p2m7q1ab",
  "Id": "k3x9p2m7q1ab",
  "Name": "my-global-gateway",
  "ExecutionRoleArn": "arn:aws:iam::<account-id>:role/<execution-role-name>",
  "Status": "ACTIVE",
  "EndpointUrl": "https://k3x9p2m7q1ab.<...>.us-west-2.on.aws",
  "VpcEndpointServiceName": "com.amazonaws.vpce.us-west-2.vpce-svc-0123456789abcdef0",
  "CreationTime": "2026-11-12T23:00:00Z"
}
```

`Routing` is returned only if you set weights at create or update.

When `Status` is `ACTIVE`, check each member's status:

```bash
aws sagemaker list-inference-gateways --region us-west-2 --identifier my-global-gateway
```

```json
{
  "InferenceGatewaySummaries": [
    {"ClusterArn": "arn:aws:sagemaker:us-west-2:<account-id>:cluster/<cluster-id-1>", "Namespace": "my-namespace", "Name": "my-gateway", "Status": "ACTIVE"},
    {"ClusterArn": "arn:aws:sagemaker:us-east-1:<account-id>:cluster/<cluster-id-2>", "Namespace": "my-namespace", "Name": "my-gateway", "Status": "ACTIVE"}
  ]
}
```

A member becomes `ACTIVE` only after the Global Inference Gateway has reached it over its private connection. If a member can't be reached, it is marked `FAILED` with a `FailureReason`, and the Global Inference Gateway stays `ACTIVE` and serves traffic from the remaining members.

**Note**  
After the Global Inference Gateway becomes `ACTIVE`, it can take up to about 2 minutes before the first request is routed, while the members' first metrics arrive. Until then, requests return `ServiceUnavailableException` (503).

## Verify your setup
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-verify-your-setup"></a>

Use the following checks to confirm that each part of the setup worked. Run the `kubectl` checks against each member cluster, and use each cluster's Region in the `aws eks` check.


**Verify your setup**  

| Check | How to verify | Expected result | 
| --- | --- | --- | 
| Each in-cluster gateway is ready for global routing (Step 1) | kubectl -n my-namespace get inferencegatewayconfig my-gateway | READY is True, GLOBAL-ROUTING is Ready, and VPCE-SERVICE is set | 
| The execution role can reach each member cluster (Step 2) | aws eks describe-access-entry --cluster-name <eks-cluster-name> --region <cluster-region> --principal-arn arn:aws:iam::<account-id>:role/<execution-role-name> | kubernetesGroups is ["sagemaker-global-inference-gateway"] and type is STANDARD | 
| The Global Inference Gateway is active (Step 3) | aws sagemaker describe-global-inference-gateway --region us-west-2 --identifier my-global-gateway | Status is ACTIVE, and EndpointUrl is set | 
| Every member is active (Step 3) | aws sagemaker list-inference-gateways --region us-west-2 --identifier my-global-gateway | Every member's Status is ACTIVE | 
| Each member's metrics publisher is running | kubectl -n my-namespace get inferencegatewayconfig my-gateway -o jsonpath='{.status.conditions[?(@.type=="MetricsPublisherReady")].status}' | True | 

If a check fails, see [Global Inference Gateway troubleshooting guide](sagemaker-hyperpod-model-deployment-ts-global-inference-gateway.md).

## Step 4: Invoke the Global Inference Gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-step-4-invoke-the-global-inference-gateway"></a>

Send requests to the `EndpointUrl` from `describe-global-inference-gateway`. Every request must be signed with SigV4 for the service name `sagemaker` in the Global Inference Gateway's Region, by an IAM principal in the account that owns the Global Inference Gateway.

### IAM permissions for callers
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-iam-permissions-for-callers"></a>

Callers must be IAM principals in the account that owns the Global Inference Gateway. Requests from other accounts are denied, even if their IAM policies allow them. Grant callers the following actions on the Global Inference Gateway's ARN.


**IAM permissions for callers**  

| Action | Used by | 
| --- | --- | 
| sagemaker:InvokeGlobalInferenceGateway | The InvokeGlobalInferenceGateway operation, and OpenAI-compatible requests that don't set "stream": true | 
| sagemaker:InvokeGlobalInferenceGatewayWithResponseStream | The InvokeGlobalInferenceGatewayWithResponseStream operation, and OpenAI-compatible requests that set "stream": true | 

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sagemaker:InvokeGlobalInferenceGateway",
        "sagemaker:InvokeGlobalInferenceGatewayWithResponseStream"
      ],
      "Resource": "arn:aws:sagemaker:<region>:<account-id>:global-inference-gateway/<gateway-id>"
    }
  ]
}
```

### Option 1: OpenAI-compatible API
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-option-1-openai-compatible-api"></a>

The Global Inference Gateway accepts OpenAI-compatible requests on the following paths and passes them to the member unchanged:
+ `POST /v1/chat/completions`
+ `POST /v1/completions`
+ `POST /v1/embeddings`

The following example uses curl's built-in SigV4 signing.

```bash
curl https://k3x9p2m7q1ab.<...>.us-west-2.on.aws/v1/chat/completions \
  --aws-sigv4 "aws:amz:us-west-2:sagemaker" \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Set `"stream": true` in the body to receive a streamed response. The Global Inference Gateway passes streamed chunks through as the model produces them.

On the OpenAI-compatible paths, errors produced by the Global Inference Gateway are returned with the HTTP status as `{"error": "<message>", "request_id": "<id>"}`. Authentication and authorization errors use `{"error": {"type": "<type>", "message": "<message>", "code": "<code>"}, "request_id": "<id>"}`. Error responses from the member are returned unchanged. The typed exceptions and message prefixes in [Error origin](sagemaker-hyperpod-model-deployment-ts-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-error-origin) and [Invocation errors](sagemaker-hyperpod-model-deployment-ts-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-invocation-errors) apply only to the `InvokeGlobalInferenceGateway` operations.

### Option 2: AWS SDK (InvokeGlobalInferenceGateway)
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-option-2-aws-sdk-invokeglobalinferencegateway"></a>

The SageMaker Gateway Runtime API provides two operations:
+ `InvokeGlobalInferenceGateway` (`POST /global-inference-gateway/{GatewayId}/invocations`) returns the whole response. The response can be up to 10 MiB.
+ `InvokeGlobalInferenceGatewayWithResponseStream` (`POST /global-inference-gateway/{GatewayId}/invocations-response-stream`) returns the response as a stream of `PayloadPart` events.

Both take the gateway ID, a `Content-Type` of `application/json`, and a JSON body in the chat completions format with a `model` field. The service sets `stream` in the body for you to match the operation.

Send both operations to your Global Inference Gateway's `EndpointUrl`: pass it as `--endpoint-url` in the AWS CLI or `endpoint_url` in the AWS SDK for Python (Boto3).

```bash
aws sagemaker-gateway-runtime invoke-global-inference-gateway \
  --region us-west-2 \
  --endpoint-url https://k3x9p2m7q1ab.<...>.us-west-2.on.aws \
  --gateway-id k3x9p2m7q1ab \
  --content-type application/json \
  --body '{"model":"meta-llama/Llama-3.1-8B-Instruct","messages":[{"role":"user","content":"Hello"}]}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

```python
import json
import boto3

client = boto3.client(
    "sagemaker-gateway-runtime",
    region_name="us-west-2",
    endpoint_url="https://k3x9p2m7q1ab.<...>.us-west-2.on.aws",
)

response = client.invoke_global_inference_gateway_with_response_stream(
    GatewayId="k3x9p2m7q1ab",
    ContentType="application/json",
    Body=json.dumps({
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [{"role": "user", "content": "Hello"}],
    }),
)

for event in response["Body"]:
    if "PayloadPart" in event:
        print(event["PayloadPart"]["Bytes"].decode(), end="")
    elif "InternalStreamFailure" in event:
        print(event)
        break
```

The `PayloadPart` bytes, joined in order, are the model server's OpenAI-format server-sent events: `data: {…}` lines with `chat.completion.chunk` objects, ending with `data: [DONE]`. A line can span two parts, so buffer the bytes and split on newlines before you parse each `data:` line as JSON and read `choices[0].delta.content`.

If the stream fails after it has started, the last event is an `InternalStreamFailure` (the connection to the member ended, a time limit was reached, or the member was taken out of service), and the stream ends. `ModelStreamError` is reserved and is not currently sent.

Both operations always send the request to the member's `/v1/chat/completions` path. To call `/v1/completions` or `/v1/embeddings`, use the OpenAI-compatible paths.

### Pass an end-user token to your clusters
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-pass-an-end-user-token-to-your-clusters"></a>

If your in-cluster inference gateways use JWT authentication (`spec.auth.jwt`), send the end user's token in the `X-Amzn-SageMaker-Customer-Identity-Token` header, and include that header in the SigV4 signature. Send the token value only, without a `Bearer` prefix. The Global Inference Gateway uses the `Authorization` header for SigV4 and removes it before forwarding, so the end-user token reaches the cluster only in `X-Amzn-SageMaker-Customer-Identity-Token`. The header can appear only once: a repeated header returns `ValidationException` (400), and a header that isn't in the signature returns `AccessDeniedException` (403). If the cluster rejects the token with 401 or 403, the request is not retried on another member. The SDK operations return `AccessDeniedException` (403) with the member's status in the message. The OpenAI-compatible paths return the member's response unchanged.

### Invoke privately with AWS PrivateLink
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-invoke-privately-with-aws-privatelink"></a>

To call the Global Inference Gateway from your VPC without going over the internet, create an interface VPC endpoint to the service named in `VpcEndpointServiceName`. Create the endpoint in the account that owns the Global Inference Gateway. Endpoints in other accounts can't connect.

```bash
aws ec2 create-vpc-endpoint --region us-west-2 \
  --vpc-endpoint-type Interface \
  --vpc-id <vpc-id> \
  --service-name com.amazonaws.vpce.us-west-2.vpce-svc-0123456789abcdef0 \
  --subnet-ids <subnet-id-1> <subnet-id-2> \
  --security-group-ids <security-group-id>
```

Choose subnets in Availability Zones that the endpoint service supports. To list them, run `aws ec2 describe-vpc-endpoint-services --service-names <service-name>`. The endpoint's security group must allow inbound TCP 443 from every CIDR block your callers use. If your VPC has secondary CIDR blocks, which pods often use, include them, or requests time out.

Keep sending requests to `EndpointUrl`, signed as usual, and resolve its hostname to the endpoint inside your VPC. For example, create a Route 53 private hosted zone named after the full `EndpointUrl` hostname, associate it with your VPC, and add an alias record that points to the endpoint's DNS name. Don't send requests to the endpoint's own DNS name. The TLS certificate is issued for the `EndpointUrl` hostname, so HTTPS clients reject that connection.

**Note**  
After the Global Inference Gateway becomes `ACTIVE`, wait about a minute before you send the first request to `EndpointUrl`. A DNS lookup made before the name was published can be cached as not found for a short time.

## Manage a Global Inference Gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-manage-a-global-inference-gateway"></a>

### Add a member
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-add-a-member"></a>

Add an in-cluster inference gateway from another HyperPod cluster to serve traffic through the Global Inference Gateway. A Global Inference Gateway can have up to 10 members. To add more, remove a member first or create another Global Inference Gateway.

```bash
aws sagemaker add-inference-gateway --region us-west-2 \
  --identifier my-global-gateway \
  --cluster-arn arn:aws:sagemaker:eu-west-1:<account-id>:cluster/<cluster-id-3> \
  --namespace my-namespace \
  --name my-gateway
```

The member starts in `ADDING` and moves to `ACTIVE` or `FAILED`. Check it with `list-inference-gateways`. Before you add a member, complete [Step 1](#sagemaker-hyperpod-model-deployment-global-inference-gateway-step-1-enable-global-routing-on-each-in-cluster-inference-gateway) on its cluster and add its cluster to the execution role (Step 2b and 2c). Adding a member that is already in this Global Inference Gateway succeeds and returns its current status.

### Remove a member
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-remove-a-member"></a>

Remove an in-cluster inference gateway so that the Global Inference Gateway stops sending it traffic.

```bash
aws sagemaker remove-inference-gateway --region us-west-2 \
  --identifier my-global-gateway \
  --cluster-arn arn:aws:sagemaker:eu-west-1:<account-id>:cluster/<cluster-id-3> \
  --namespace my-namespace \
  --name my-gateway
```

The member moves to `REMOVING`. Within about 15 seconds new requests stop going to it. Its private connection is then deleted, so requests still in flight to that member, for example long streaming responses, can be cut off. The member then disappears from `list-inference-gateways`. If the removal can't complete, the member shows `FAILED` with a `FailureReason`; call `remove-inference-gateway` again. You can't remove the last member; a Global Inference Gateway always keeps at least one. A `FAILED` member counts toward this, and a member that is already `REMOVING` doesn't. Removing an in-cluster gateway that isn't a member succeeds and does nothing.

After a member is removed, you can turn off global routing on its `InferenceGatewayConfig`, or add it to another Global Inference Gateway.

**Important**  
Remove the member before you turn off global routing, delete the `InferenceGatewayConfig`, or delete the last model that uses an operator-managed gateway. While a Global Inference Gateway is still connected, the in-cluster gateway can't release its endpoint service: the configuration reports `GlobalRoutingDeleteBlocked` and its deletion waits until the member is removed.

### Change routing weights
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-change-routing-weights"></a>

You can update the routing weights to change how the Global Inference Gateway scores members. There are four weights, each between 0 and 1:
+ `KVHeadroom` (default 0.20): favors members with more free KV cache.
+ `QueueDepth` (default 0.25): favors members with fewer waiting requests.
+ `RegionProximity` (default 0.40): favors members in the same Region as the Global Inference Gateway.
+ `ErrorRate` (default 0.15): favors members with fewer recent errors.

```bash
aws sagemaker update-global-inference-gateway --region us-west-2 \
  --identifier my-global-gateway \
  --routing '{"Weights": {"KVHeadroom": 0.3, "QueueDepth": 0.3, "RegionProximity": 0.2, "ErrorRate": 0.2}}'
```

The Global Inference Gateway moves to `UPDATING` and returns to `ACTIVE` when the new weights are in effect, usually within a few minutes. Requests keep being served during the update. To go back to the default weights, pass `{"Weights": {}}`.

If the update fails, the Global Inference Gateway returns to `ACTIVE`, keeps serving with its previous weights, and `describe-global-inference-gateway` shows a `FailureReason`. Send the same update again to retry. Updating to the weights already in effect returns immediately and changes nothing.

### List Global Inference Gateways
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-list-global-inference-gateways"></a>

To list the Global Inference Gateways in your account and Region, run `list-global-inference-gateways`. To list only those in a given status, add a `Status` filter. The valid values are `CREATING`, `ACTIVE`, `UPDATING`, `DELETING`, and `FAILED`.

```bash
aws sagemaker list-global-inference-gateways --region us-west-2 \
  --filters Name=Status,Value=ACTIVE
```

### Delete a Global Inference Gateway
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-delete-a-global-inference-gateway"></a>

To delete a Global Inference Gateway, use:

```bash
aws sagemaker delete-global-inference-gateway --region us-west-2 --identifier my-global-gateway
```

The Global Inference Gateway moves to `DELETING`, and SageMaker AI removes its endpoint and routing resources. When deletion finishes, its members are released and can join another Global Inference Gateway, its name can be reused, and `describe-global-inference-gateway` returns `ResourceNotFound`. Deleting doesn't change your `InferenceGatewayConfig` resources or your models. SageMaker AI only removes this Global Inference Gateway's entry from the `gig-membership` ConfigMap on each member cluster, which stops that member's metrics publisher. Calling delete again while it is `DELETING` has no effect; if the delete fails, call delete again to retry it.

To stop exposing an in-cluster gateway after you delete the Global Inference Gateway, turn off global routing on its `InferenceGatewayConfig`.

**Note**  
A Global Inference Gateway accepts one change at a time. While a create, update, add, remove, or delete is in progress, other change requests return `ConflictException`. Wait for the current change to finish, then retry.

## Clean up
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-clean-up"></a>

To stop using a Global Inference Gateway and remove the resources you created for it, follow these steps in order.

**Important**  
Delete the Global Inference Gateway before you turn off global routing. While a member is still connected, the in-cluster gateway can't release its endpoint service, and the configuration stays at `GlobalRoutingDeleteBlocked`.

1. Delete the Global Inference Gateway. Its members are released, and SageMaker AI removes the endpoint and routing resources.

   ```bash
   aws sagemaker delete-global-inference-gateway --region us-west-2 --identifier my-global-gateway
   ```

   Wait until `describe-global-inference-gateway` returns `ResourceNotFound`. This usually takes 7 to 8 minutes.

1. On each member cluster, turn off global routing. The controller deletes the metrics publisher and its VPC endpoint, the VPC endpoint service, the internal Network Load Balancer, and the certificates it uploaded to your TLS bucket.

   ```bash
   kubectl -n my-namespace patch inferencegatewayconfig my-gateway --type merge \
     -p '{"spec":{"globalRouting":{"enabled":false}}}'
   ```

   Wait until the `GLOBAL-ROUTING` column of `kubectl get inferencegatewayconfig` is empty.

1. On each member cluster, delete the execution role's access entry.

   ```bash
   aws eks delete-access-entry --cluster-name <eks-cluster-name> --region <cluster-region> \
     --principal-arn arn:aws:iam::<account-id>:role/<execution-role-name>
   ```

1. Delete the execution role. If you used an inline policy in Step 2b, delete it with `aws iam delete-role-policy` instead of detaching the managed policy.

   ```bash
   aws iam detach-role-policy --role-name <execution-role-name> \
     --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerGlobalInferenceGatewayExecutionAccess
   aws iam delete-role --role-name <execution-role-name>
   ```

1. Update the add-on to remove `inferenceGateway.metricsPublisher`, keeping your other values as in Step 1c. Then delete the metrics publisher role.

   ```bash
   aws iam detach-role-policy --role-name AmazonSageMakerInferenceGatewayMetricsPublisherRole \
     --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess
   aws iam delete-role --role-name AmazonSageMakerInferenceGatewayMetricsPublisherRole
   ```

1. Detach the global routing policy from the controller role, and remove any bucket statements that you added in Step 1a.

   ```bash
   aws iam detach-role-policy --role-name <controller-role-name> \
     --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess
   ```

Keep the role itself, because the in-cluster gateway still uses it for TLS certificates. Keep your TLS bucket for the same reason.

## Routing behavior
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-routing-behavior"></a>

This section describes how the Global Inference Gateway decides where each request goes, how often it updates member metrics, and what happens when a member is slow, overloaded, or failing.

### What the Global Inference Gateway knows about each member
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-what-the-global-inference-gateway-knows-about-each-member"></a>

Each member's in-cluster inference gateway runs a metrics publisher that reports, for every model it serves, the following signals to the Global Inference Gateway. The publisher sends a report every 5 seconds by default.


**What the Global Inference Gateway knows about each member**  

| Signal | Source in the cluster | How it is aggregated | 
| --- | --- | --- | 
| Ready pods | Endpoint Picker (EPP) for the model | The highest value reported by any EPP replica | 
| KV cache utilization | Model servers (vLLM, SGLang), through the EPP | Average across the model's serving pods, from 0 to 1 | 
| Queue depth | Model servers, through the EPP | Average number of waiting requests per serving pod | 
| Request count | In-cluster gateway (Envoy) and EPP | Total requests the member received for the model | 
| Error count | In-cluster gateway (Envoy) and EPP | Server errors (5xx) plus requests the EPP rejected because it couldn't serve them | 
| Served models and adapters | InferenceGatewayConfig schedulers and LoRA adapters | The base models and adapter names the member can answer | 
| Component health | EPP and the global routing listener | Whether each component was reachable when the report was taken | 

Request and error counts are used only when every serving pod was scraped successfully.

The Global Inference Gateway reads the latest reports every 15 seconds and computes each member's error rate over the last 5 minutes.

**Important**  
The Global Inference Gateway learns which models a member serves only from these reports. A member that has never sent a report receives no traffic, even if its membership status is `ACTIVE`. If a member's publisher stops after it has reported, the member keeps receiving traffic, scored on its last reported load, for up to 30 minutes.

### Which members can receive a request
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-which-members-can-receive-a-request"></a>

For each request, a member is a candidate only if all of the following are true:
+ It serves the model named in the request's `model` field, either as a base model or as a LoRA adapter.
+ Its membership status is `ACTIVE`.
+ It reports at least one ready pod for that model.
+ Its components are healthy. A member is excluded after two consecutive reports in which its Endpoint Picker or global routing listener was unreachable, and is included again when it reports healthy.
+ It has reported KV cache utilization and queue depth, unless that signal's routing weight is 0. A member that hasn't reported its error rate yet can still receive traffic.
+ It has sent metrics in the last 30 minutes.

**Note**  
KV cache utilization and queue depth come from your model servers' metrics. Use vLLM v0.9.2 or later, or SGLang v0.3.5.post1 or later started with `--enable-metrics`. Earlier versions don't publish these metrics in the form the in-cluster inference gateway reads, so the member doesn't receive traffic from the Global Inference Gateway. For details, see [Inference Gateway for Amazon SageMaker HyperPod Inference](sagemaker-hyperpod-model-deployment-inference-gateway.md). If no member serves the model, the request fails with `ResourceNotFoundException` (404). If members serve the model but none can take traffic right now, it fails with `ServiceUnavailableException` (503).

### How candidates are scored
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-how-candidates-are-scored"></a>

Each candidate gets a score between 0 and 1. The Global Inference Gateway sends the request to the highest score. When several candidates tie, one is picked at random, so equal members share traffic evenly.

The score is a weighted average of four signal values:

```
score = (wKV × KVHeadroom + wQueue × QueueDepth + wRegion × RegionProximity + wError × ErrorRate)
        ÷ (wKV + wQueue + wRegion + wError)
```

The default weights are `KVHeadroom` 0.20, `QueueDepth` 0.25, `RegionProximity` 0.40, and `ErrorRate` 0.15.

If a member hasn't reported its error rate yet, for example because it is new, that signal is left out and the remaining weights are rescaled.

### Choosing routing weights
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-choosing-routing-weights"></a>

Each weight controls how much one signal counts when the Global Inference Gateway picks a member. Raise a weight to make that signal matter more.
+ **`KVHeadroom`:** A higher value favors members with more free KV cache. This helps with long prompts or long responses, which use more cache.
+ **`QueueDepth`:** A higher value favors members with fewer waiting requests. This helps when response time matters most.
+ **`RegionProximity`:** A higher value keeps traffic in the Global Inference Gateway's Region, and uses other Regions only when local members are busy. Set it to 0 to route on spare capacity alone, regardless of Region.
+ **`ErrorRate`:** A higher value steers traffic away from members that have recently returned errors.

Set all four weights, each between 0 and 1, so that they add up to 1.0. A weight of 0 turns that signal off. Weight changes take effect without dropping requests.

**Note**  
`RegionProximity` compares each member's Region with the Region of the Global Inference Gateway, not with the Region of the client.

### Metric freshness
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-metric-freshness"></a>
+ **New members.** A member starts receiving traffic only after its first metrics arrive. Right after a Global Inference Gateway becomes `ACTIVE`, or right after you add a member, it can take a few minutes before requests are routed to it.
+ **Stale metrics.** If a member's latest report is more than 120 seconds old, the Global Inference Gateway keeps routing on the member's last known load. After 30 minutes without a report, the member stops receiving traffic until it reports again. Monitor `MetricsPublisherReady` on your clusters so that stale reports don't go unnoticed.
+ **Removed members.** When you remove a member, it stops receiving new requests within a few minutes.

### Recovery after errors
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-recovery-after-errors"></a>

When a member that was excluded becomes healthy again, it isn't given its full share of traffic at once. It is brought back in steps of 25%, 50%, 75%, and 100% of its normal share, staying at least 5 minutes at each step. The first step starts as soon as the member reports healthy. If the member's error rate is 10% or higher while it is ramping up, it goes back to the start of the ramp and receives requests only when no other member can take them. A member that already has its full share keeps it, even if its error rate rises.If the member reports no ready pods, reports an unhealthy component, or sends no metrics for 30 minutes, it's excluded again, and it restarts the ramp when it recovers.

### What happens when something fails
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-what-happens-when-something-fails"></a>

The following table describes how traffic behaves at each scope of failure, from a single pod to a whole Region.


**What happens when something fails**  

| Failure | What the Global Inference Gateway does | Effect on your clients | 
| --- | --- | --- | 
| A model server pod fails | Nothing. The member's in-cluster gateway stops sending requests to the pod and uses its other pods. | None, as long as the member has other ready pods for the model. | 
| A model is saturated on one member | The member returns 429 or 503, and the request is retried once on the next-best member. The member's growing queue depth and KV cache usage also lower its score, so new requests shift to other members. | Requests are served by other members. If every member is saturated, clients receive ThrottlingException (429) with Retry-After. | 
| A member's Endpoint Picker or global routing listener is down | The member reports the component as unhealthy, and the member is excluded from routing after two consecutive unhealthy reports. | Traffic moves to the other members that serve the model. | 
| A member can't be reached (for example, its cluster or network path is down) | Each request that can't connect within 5 seconds is retried once on the next-best member. | Requests still succeed through other members, with added latency for the failed connection attempt. See the note below. | 
| A member's global routing listener restarts or moves, for example during an add-on update, a node replacement, or an Availability Zone outage in the cluster's VPC | The listener runs as a single Envoy pod, so the member can't take requests from the Global Inference Gateway until the pod is running again. Requests that can't connect are retried once on the next-best member. | Brief failures or added latency for requests to that member, about 15 seconds during an add-on update. Serve each model from at least two members. | 
| A member recovers | The member is brought back gradually, as described in [Recovery after errors](#sagemaker-hyperpod-model-deployment-global-inference-gateway-recovery-after-errors). | None. | 
| All members in one Region fail | Members in other Regions keep their scores and receive the traffic. Region proximity only lowers their score; it never excludes them. | Higher latency for requests that now cross Regions. No configuration change is needed. | 
| A model is served by only one member, and that member fails | There is no other member to send the request to. | Requests for that model fail until the member recovers. Serve each model from at least two members to avoid this. | 
| An Availability Zone fails in the Global Inference Gateway's Region | The routing fleet runs in multiple Availability Zones, and traffic moves to the healthy ones. | Requests in flight in the failed zone, including open streams, fail and must be retried by the client. | 

**Note**  
If a member stops sending metrics entirely, the Global Inference Gateway keeps scoring it on its last reported load, because missing metrics alone are not treated as proof that the member is down. Requests that can't reach it fail over as described in the table. To find members in this state, alarm on `MetricsPublisherReady` on each cluster and on `FAILED` members (see [Recommended alarms](#sagemaker-hyperpod-model-deployment-global-inference-gateway-recommended-alarms)).

### Timeouts
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-timeouts"></a>


**Timeouts**  

| Limit | Value | Result when exceeded | 
| --- | --- | --- | 
| First response byte from the member | 300 seconds | GatewayTimeoutException (504), not retried | 
| Time between streamed chunks | 300 seconds | 504 before the first byte. After it: an InternalStreamFailure event on InvokeGlobalInferenceGatewayWithResponseStream, BadGatewayException (502) on InvokeGlobalInferenceGateway, and a truncated response on the OpenAI-compatible paths | 
| Whole request, including the full stream and any retry | 15 minutes | 504 before the first byte. After it: an InternalStreamFailure event on InvokeGlobalInferenceGatewayWithResponseStream, BadGatewayException (502) on InvokeGlobalInferenceGateway, and a truncated response on the OpenAI-compatible paths | 
| In-flight requests on a member that is removed or withdrawn | 10 minutes to finish | Streams still open after that end with InternalStreamFailure | 

## Status reference
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-status-reference"></a>

### Global Inference Gateway status
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-global-inference-gateway-status"></a>


**Global Inference Gateway status**  

| Status | Meaning | 
| --- | --- | 
| CREATING | SageMaker AI is provisioning the endpoint and connecting to the members. | 
| ACTIVE | The Global Inference Gateway is serving. Some members can still be FAILED; check list-inference-gateways. | 
| UPDATING | A member is being added or removed, or new routing weights are being applied. Traffic is still served. | 
| DELETING | The Global Inference Gateway and its resources are being removed. | 
| FAILED | Creation or deletion failed. FailureReason explains why. If creation failed, delete the Global Inference Gateway and create it again after you fix the cause. If deletion failed, call delete-global-inference-gateway again. | 

`FailureReason` can also be set while the status is `ACTIVE`. It then describes the last add, remove, or routing update that failed; the Global Inference Gateway kept serving.

### Member status
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-member-status"></a>

The member status describes the membership, not the health of the in-cluster gateway itself.


**Member status**  

| Status | Meaning | 
| --- | --- | 
| ADDING | The Global Inference Gateway is connecting to the in-cluster gateway and verifying that it can reach it. | 
| ACTIVE | The member is connected and eligible for traffic. | 
| REMOVING | The member is draining and being disconnected. | 
| FAILED | The member couldn't be added, or couldn't be removed. FailureReason explains why. If it couldn't be added, fix the cause, remove the member, and add it again. If it couldn't be removed, call remove-inference-gateway again. | 

## Monitoring
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-monitoring"></a>

You can monitor a Global Inference Gateway at three levels:
+ **Gateway metrics** in Amazon CloudWatch, which the Global Inference Gateway publishes into your account.
+ **Resource status** from the SageMaker API: the Global Inference Gateway's status and each member's status.
+ **Member health** from Kubernetes, through the `InferenceGatewayConfig` conditions and the in-cluster inference gateway's own metrics.

### Gateway metrics in Amazon CloudWatch
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-gateway-metrics-in-amazon-cloudwatch"></a>

The Global Inference Gateway publishes OpenTelemetry metrics to Amazon CloudWatch in the account that owns it, in the Global Inference Gateway's Region. You don't need to turn anything on: metrics start flowing when the Global Inference Gateway starts serving.
+ **Publishing interval:** every 60 seconds. New data typically becomes queryable within about 6 minutes.
+ **Instrumentation scope:** `cloudwatch.aws/sagemaker/gateway`.
+ **Query language:** PromQL. These metrics are OpenTelemetry metrics, so they don't appear in the classic CloudWatch `ListMetrics` API or in the classic metrics namespace view.
+ **Temporality:** delta. Each data point is the count or distribution for its own 60-second interval, not a running total. See [Query the metrics](#sagemaker-hyperpod-model-deployment-global-inference-gateway-query-the-metrics) for what this means for your queries.

#### Metric reference
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-metric-reference"></a>


**Metric reference**  

| Metric | Type | Unit | Attributes | Description | 
| --- | --- | --- | --- | --- | 
| aws.sagemaker.gateway.invocations | Counter | {invocation} | gateway ID, model name (when resolved), error.type (on failures) | Every inference request that reached the Global Inference Gateway, successful or not. This is the denominator for error rates. Requests rejected before a model was resolved (for example, an oversized body, a missing model, or a failed authorization) are counted without a model name. | 
| aws.sagemaker.gateway.duration | Histogram | s | gateway ID, model name (when resolved), error.type (on failures) | End-to-end time from when the request arrived until the response finished, including the full stream. Recorded for failed requests too, so you can see how long failures take. | 
| aws.sagemaker.gateway.time\_to\_first\_byte | Histogram | s | gateway ID, model name | Time from when the request arrived until the Global Inference Gateway received the first part of the member's response body. For streamed responses this is close to the time to the first streamed chunk. For non-streamed responses, including every InvokeGlobalInferenceGateway call, it includes the whole generation. | 
| aws.sagemaker.gateway.time\_to\_first\_token | Histogram | s | gateway ID, model name | Time from when the request arrived until the first chunk that contains a generated token. Recorded only for streamed responses that contain tokens. | 
| aws.sagemaker.gateway.input\_tokens | Counter | {token} | gateway ID, model name | Prompt tokens, as reported by the model server in the response's usage block. | 
| aws.sagemaker.gateway.output\_tokens | Counter | {token} | gateway ID, model name | Completion tokens, as reported by the model server in the response's usage block. | 
| aws.sagemaker.gateway.global\_router.heartbeat | Gauge | 1 | gateway ID | Reports 1 every interval while the Global Inference Gateway's routing fleet is running. It never reports 0: missing data is the unhealthy signal. | 

#### Attributes
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-attributes"></a>

Each metric includes the following attributes:
+ **aws.sagemaker.gateway.id:** the Global Inference Gateway's ID, for example `k3x9p2m7q1ab`. Every metric has it, so you can use it to separate gateways in the same account.
+ **aws.sagemaker.gateway.model.name:** the base model name. Requests for a LoRA adapter are reported under the base model that the adapter runs on.
+ **error.type:** `4xx`, `5xx`, or `_OTHER`. Only failed requests have it, and only on the invocations and duration metrics. Throttled requests (429) count as `4xx`. A response that fails after streaming has started counts as `5xx`. `_OTHER` means the model server returned a status code outside the standard HTTP error ranges.

Every metric also carries the resource attributes `cloud.provider` (`aws`), `cloud.region`, `cloud.account.id`, and `cloud.resource_id` (the Global Inference Gateway's ARN). In PromQL results these appear with an `@resource.` prefix, for example `@resource.cloud.resource_id`.

**Token metrics for streamed responses** Token counts are published only when the model server returns a `usage` block. For streamed OpenAI-compatible requests, ask for it by setting `"stream_options": {"include_usage": true}` in the request body. The Global Inference Gateway doesn't estimate tokens when the model server doesn't report them.

#### Query the metrics
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-query-the-metrics"></a>

Metric and attribute names contain dots, so quote them inside the PromQL selector:

```
{"aws.sagemaker.gateway.invocations", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}
```

Because the data is delta, don't use `rate()` or `increase()` on these metrics. Those functions assume an ever-increasing counter and give wrong results here. Sum the interval values over a window instead, and divide by the window length if you need a rate. Always query a range (for example `[5m]`), not an instant: an instant query can miss the latest 60-second data point.

The following queries are common starting points. Replace the gateway ID.


**Query the metrics**  

| Question | PromQL | 
| --- | --- | 
| Requests in the last 5 minutes | sum(sum\_over\_time({"aws.sagemaker.gateway.invocations", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m])) | 
| Requests per second, by model | sum by ("aws.sagemaker.gateway.model.name") (sum\_over\_time({"aws.sagemaker.gateway.invocations", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m])) / 300 | 
| Server error rate | sum(sum\_over\_time({"aws.sagemaker.gateway.invocations", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab", "error.type"="5xx"}[5m])) / sum(sum\_over\_time({"aws.sagemaker.gateway.invocations", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m])) | 
| p99 end-to-end latency | histogram\_quantile(0.99, sum by ("aws.sagemaker.gateway.id") (sum\_over\_time({"aws.sagemaker.gateway.duration", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m]))) | 
| p50 time to first token, by model | histogram\_quantile(0.5, sum by ("aws.sagemaker.gateway.model.name") (sum\_over\_time({"aws.sagemaker.gateway.time\_to\_first\_token", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m]))) | 
| Output tokens per minute | sum(sum\_over\_time({"aws.sagemaker.gateway.output\_tokens", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m])) / 5 | 
| Is the routing fleet reporting? | max(max\_over\_time({"aws.sagemaker.gateway.global\_router.heartbeat", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m])) | 

You can run these queries in the CloudWatch console's PromQL query editor, or call the PromQL query API directly. The API request is a SigV4-signed POST to `https://monitoring.<region>.amazonaws.com/api/v1/query`, signed for the service name `monitoring`, with credentials in the account that owns the Global Inference Gateway:

```bash
curl -s https://monitoring.us-west-2.amazonaws.com/api/v1/query \
  --aws-sigv4 "aws:amz:us-west-2:monitoring" \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
  --data-urlencode 'query=sum(sum_over_time({"aws.sagemaker.gateway.invocations", "aws.sagemaker.gateway.id"="k3x9p2m7q1ab"}[5m]))'
```

#### Recommended alarms
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-recommended-alarms"></a>

Create CloudWatch alarms on the gateway metrics to detect issues early.
+ **Heartbeat:** alarm when there's no data for 5 minutes, and treat missing data as breaching. This means the routing fleet isn't running.
+ **Server error rate:** alarm when 5xx invocations divided by all invocations go above your threshold, for example 1% over 5 minutes. This means members are failing, or the Global Inference Gateway can't reach them. To tell which, see Error origin.
+ **Throttling:** alarm when 4xx invocations rise along with 429 responses in your client. This means every member tried was out of capacity. Add capacity or add a member.
+ **Latency:** alarm when p99 `duration` or p50 `time_to_first_token` goes above your target. This means members are queueing. Check KV cache and queue depth on the members.

Also check `list-inference-gateways` for `FAILED` members, and the `MetricsPublisherReady` condition on each member cluster.

### Resource status
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-resource-status"></a>

Poll `describe-global-inference-gateway` for the Global Inference Gateway's `Status` and `FailureReason`, and `list-inference-gateways` for each member's `Status` and `FailureReason`. For what each value means, see [Status reference](#sagemaker-hyperpod-model-deployment-global-inference-gateway-status-reference).

```bash
aws sagemaker list-inference-gateways --region us-west-2 \
  --identifier my-global-gateway \
  --filters Name=Status,Value=FAILED
```

### Member health in Kubernetes
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-member-health-in-kubernetes"></a>

On each member cluster, the `InferenceGatewayConfig` reports two conditions that matter for global routing:

```bash
kubectl -n my-namespace get inferencegatewayconfig my-gateway \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status} {.reason}: {.message}{"\n"}{end}'
```
+ `GlobalRoutingReady`: the private endpoint that the Global Inference Gateway connects to is published and has healthy targets.
+ `MetricsPublisherReady`: the metrics publisher is sending reports to the Global Inference Gateway. While it is `False`, the Global Inference Gateway routes to the member on its last reported load, so it doesn't see load or health changes. After 30 minutes without reports, the member is removed from routing. Direct traffic to the in-cluster gateway is not affected.

The in-cluster inference gateway's own metrics (Endpoint Picker, KV cache, queue depth, model server metrics) are available as described in [Observability](sagemaker-hyperpod-model-deployment-inference-gateway.md#sagemaker-hyperpod-model-deployment-inference-gateway-observability) for the Inference Gateway. They are the same signals the Global Inference Gateway uses to score members, so they are the best place to see why traffic moved between clusters.

## Quotas and limits
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-quotas-and-limits"></a>


**Quotas and limits**  

| Resource | Limit | Notes | 
| --- | --- | --- | 
| Members per Global Inference Gateway | 1–10 | A Global Inference Gateway always keeps at least one member. | 
| Global Inference Gateways per member | 1 | An in-cluster inference gateway can belong to only one Global Inference Gateway at a time. | 
| Models per member with global routing turned on | 10 | Global routing supports up to 10 models (schedulers) on each InferenceGatewayConfig. | 
| Global Inference Gateway name | 1–63 characters | Letters, digits, and hyphens. Must start and end with a letter or digit. Unique per account and Region. Can't be exactly 12 lowercase letters or digits, because that form is reserved for Global Inference Gateway IDs. | 

Global routing creates resources in each cluster's account, and these count against that account's quotas:
+ **Turning on global routing** creates one internal Network Load Balancer, which counts toward **Network Load Balancers per Region** (`L-69A177A2`). If the quota is reached, the `InferenceGatewayConfig` stays at `GlobalRoutingPending`.
+ **Adding the gateway to a Global Inference Gateway** creates one interface VPC endpoint and one security group in the cluster's VPC. These count toward **Interface VPC endpoints per VPC** and **VPC security groups per Region**.

To request an increase, use [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

## Security
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-security"></a>
+ **Authentication and authorization.** Every request is signed with SigV4 and authorized with IAM on the Global Inference Gateway's ARN. Only principals in the owning account can invoke it; requests from other accounts are denied even if their IAM policies allow it.
+ **Encryption in transit.** Clients connect over HTTPS. The Global Inference Gateway connects to each member over a private AWS PrivateLink connection, using TLS. It verifies the member's certificate, which the in-cluster gateway publishes to your TLS bucket, and presents its own client certificate. Each in-cluster gateway accepts only the client certificate of the Global Inference Gateway it belongs to, and refuses all others until it is added. You don't need to configure anything for this.
+ **Certificate rotation.** Each in-cluster gateway's global routing certificate is rotated automatically. Sixty days before it expires, the controller issues a new certificate and publishes it to your TLS bucket alongside the current one. Seven days after that upload, the gateway starts presenting the new certificate. The old certificate stays in the bucket for one more day, and then it's removed. If the current certificate is within one day of expiry, the gateway switches immediately. No action is needed, but don't delete objects under the `gig/` prefix in your TLS bucket.
+ **Private member connectivity.** Members don't need a public endpoint. Each member's VPC endpoint service accepts connections only from the SageMaker Global Inference Gateway service.
+ **Least privilege on your clusters.** The Global Inference Gateway reaches your clusters only through the execution role you provide, protected against the confused deputy problem, and is limited by Kubernetes RBAC to reading `InferenceGatewayConfig` resources and updating a single membership ConfigMap.
+ **Metrics isolation.** Each Global Inference Gateway has its own metrics stream that accepts records only from its owning account.
+ **Logging.** Request and response bodies, credentials, and end-user tokens are never logged.

## Supported Regions
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-supported-regions"></a>

You can create a Global Inference Gateway in the following AWS Regions. Members can be HyperPod clusters in any of these Regions, in the same account as the Global Inference Gateway.
+ US East (N. Virginia) `us-east-1`
+ US East (Ohio) `us-east-2`
+ US West (N. California) `us-west-1`
+ US West (Oregon) `us-west-2`
+ South America (São Paulo) `sa-east-1`
+ Europe (Frankfurt) `eu-central-1`
+ Europe (Ireland) `eu-west-1`
+ Europe (London) `eu-west-2`
+ Europe (Stockholm) `eu-north-1`
+ Asia Pacific (Tokyo) `ap-northeast-1`
+ Asia Pacific (Mumbai) `ap-south-1`
+ Asia Pacific (Singapore) `ap-southeast-1`
+ Asia Pacific (Sydney) `ap-southeast-2`

**Note**  
You can't add an in-cluster gateway as a member if its HyperPod cluster is in a Region that requires opt-in.

## API reference
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-api-reference"></a>

### SageMaker API (control plane)
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-sagemaker-api-control-plane"></a>


**SageMaker API (control plane)**  

| Operation | Description | 
| --- | --- | 
| CreateGlobalInferenceGateway | Creates a Global Inference Gateway with 1–10 members. Asynchronous. Inputs: Name, ExecutionRoleArn, Gateways, optional Routing, ClientToken, Tags. | 
| DescribeGlobalInferenceGateway | Returns the status, EndpointUrl, VpcEndpointServiceName, Routing, CreationTime, and FailureReason. | 
| ListGlobalInferenceGateways | Lists Global Inference Gateways in the account and Region. Filter: Status. | 
| UpdateGlobalInferenceGateway | Changes Routing. Asynchronous. | 
| DeleteGlobalInferenceGateway | Deletes a Global Inference Gateway. Asynchronous. Idempotent. | 
| AddInferenceGateway | Adds one member. Asynchronous. Idempotent. | 
| RemoveInferenceGateway | Removes one member. Asynchronous. Idempotent. | 
| ListInferenceGateways | Lists the members of a Global Inference Gateway, in the order they were added, with each member's status and failure reason. Filters: Status, ClusterArn. | 

All operations that take an `Identifier` accept the Global Inference Gateway's name, ID, or ARN. Names are case-sensitive.

### SageMaker Gateway Runtime API (data plane)
<a name="sagemaker-hyperpod-model-deployment-global-inference-gateway-sagemaker-gateway-runtime-api-data-plane"></a>


**SageMaker Gateway Runtime API (data plane)**  

| Operation | Description | 
| --- | --- | 
| InvokeGlobalInferenceGateway | Sends an inference request and returns the whole response (up to 10 MiB). | 
| InvokeGlobalInferenceGatewayWithResponseStream | Sends an inference request and returns the response as an event stream. | 