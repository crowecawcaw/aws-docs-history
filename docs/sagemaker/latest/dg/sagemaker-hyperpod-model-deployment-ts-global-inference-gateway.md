

# Global Inference Gateway troubleshooting guide

Use this section to diagnose problems with a Global Inference Gateway: an in-cluster gateway that doesn't become ready for global routing, a member that fails, and errors returned when you invoke the Global Inference Gateway or call its control plane API. For setup and concepts, see [Global Inference Gateway for Amazon SageMaker HyperPod Inference](sagemaker-hyperpod-model-deployment-global-inference-gateway.md).

## In-cluster gateway: GLOBAL-ROUTING isn't Ready
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-in-cluster-gateway-global-routing-isnt-ready"></a>

**Problem:** After you turn on global routing, the `InferenceGatewayConfig` doesn't become ready for global routing: its `GLOBAL-ROUTING` column doesn't show `Ready`, or its `READY` column stays `False`.

**Symptoms and resolution:** Check the reason and message on the configuration's conditions, then find the reason below.

```bash
kubectl -n my-namespace get inferencegatewayconfig my-gateway \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status} {.reason}: {.message}{"\n"}{end}'
```

**GlobalRoutingInsufficientAZs:** The load balancer spans fewer than two Availability Zones. Tag a subnet in another Availability Zone of the cluster's VPC with `kubernetes.io/role/internal-elb=1`:

```bash
aws ec2 create-tags --region <region> --resources <subnet-id> \
  --tags Key=kubernetes.io/role/internal-elb,Value=1
```

**GlobalRoutingTargetsUnreachable:** None of the gateway pods run in an Availability Zone that the load balancer uses. Tag a subnet in the pods' Availability Zone as shown for `GlobalRoutingInsufficientAZs`, or schedule the pods in the load balancer's Availability Zones. To find the pods' Availability Zones:

```bash
kubectl -n hyperpod-inference-system get pods -o wide \
  -l gateway.envoyproxy.io/owning-gateway-name=my-gateway-gig
kubectl get nodes -L topology.kubernetes.io/zone
```

**GlobalRoutingTargetsUnhealthy:** No gateway pod is passing the load balancer's health checks, so traffic from the Global Inference Gateway fails. The message lists each target's state. Check the global routing Envoy pods, and the health check of the load balancer's target group:

```bash
kubectl -n hyperpod-inference-system get pods \
  -l gateway.envoyproxy.io/owning-gateway-name=my-gateway-gig
kubectl -n hyperpod-inference-system describe pod <pod-name>
```

**GlobalRoutingUnavailable:** The controller has no AWS credentials. Check that the controller's service account has a role, and if it doesn't, set `inferenceGateway.serviceAccount.roleArn` on the add-on ([Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions)):

```bash
kubectl -n hyperpod-inference-system get sa inference-gateway-controller \
  -o jsonpath='{.metadata.annotations.eks\.amazonaws\.com/role-arn}'
```

The controller reads its role only when it starts, so restart it after you set the role:

```bash
kubectl -n hyperpod-inference-system rollout restart deploy/inference-gateway-controller
```

**GlobalRoutingVPCESError:** An Amazon EC2 or Elastic Load Balancing call failed, or the endpoint service is in a state the controller can't repair. If the message reports an access-denied error, check that the controller role has the `AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess` policy ([Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions)). If it says the endpoint service is `Failed`, remove the member, turn global routing off and on again to replace the endpoint service, and then add the member again. To see the endpoint service's state:

```bash
aws ec2 describe-vpc-endpoint-service-configurations --region <region> \
  --filters Name=tag:CreatedBy,Values=HyperPodInference \
  --query 'ServiceConfigurations[].{Id:ServiceId,State:ServiceState}' --output table
```

**GlobalRoutingCertificateUploadFailed:** The controller couldn't upload its certificate to the TLS bucket. Check that the controller role has the `AmazonSageMakerHyperPodInferenceGatewayGlobalRoutingAccess` policy. If your bucket name doesn't begin with `hyperpod-tls`, add the bucket statements in [Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions) to the controller role.

**GlobalRoutingCertificateBucketNotConfigured:** The controller doesn't have the TLS bucket. Check that the add-on is version `v3.0.0-eksbuild.1` or later and has `tlsCertificateS3Bucket` set ([Step 1c](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1c-update-the-add-on)):

```bash
aws eks describe-addon --cluster-name <eks-cluster-name> --region <region> \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --query '{version:addon.addonVersion,config:addon.configurationValues}' --output json
```

Then restart the controller:

```bash
kubectl -n hyperpod-inference-system rollout restart deploy/inference-gateway-controller
```

**GlobalRoutingCertificatePending:** This appears on the `Ready` condition (the `READY` column is `False`), not in the `GLOBAL-ROUTING` column. The global routing listener's certificate hasn't been issued yet. Wait. If it persists, check that [cert-manager](https://docs.aws.amazon.com/eks/latest/userguide/community-addons.html#addon-cert-manager) is running and that the certificate is issued:

```bash
kubectl get pods -n cert-manager
kubectl -n hyperpod-inference-system get certificate
```

**GlobalRoutingCertificateConflict:** This appears on the `Ready` condition (the `READY` column is `False`), not in the `GLOBAL-ROUTING` column. A certificate Secret that this gateway needs belongs to another `InferenceGatewayConfig`. The message names the Secret, so you can see which configuration owns it.

**GlobalRoutingGetError or GlobalRoutingNotProgrammed:** These appear on the `Ready` condition (the `READY` column is `False`), not in the `GLOBAL-ROUTING` column. The controller couldn't read a Kubernetes object, or the gateway's global routing listener isn't set up yet. Both usually clear on their own. If they persist, check the global routing Gateway and the controller logs:

```bash
kubectl -n hyperpod-inference-system get gateway my-gateway-gig
kubectl -n hyperpod-inference-system logs deploy/inference-gateway-controller --since=15m
```

**GlobalRoutingDeleteBlocked:** Global routing is being turned off, but a Global Inference Gateway is still connected. Remove the member from the Global Inference Gateway first. If deletion stays blocked after you remove the member, another interface VPC endpoint is still connected to the endpoint service. Reject it:

```bash
aws ec2 describe-vpc-endpoint-connections --region <region> \
  --filters Name=service-id,Values=<vpce-svc-id> \
  --query 'VpcEndpointConnections[].{Endpoint:VpcEndpointId,State:VpcEndpointState}' --output table
aws ec2 reject-vpc-endpoint-connections --region <region> \
  --service-id <vpce-svc-id> --vpc-endpoint-ids <vpce-id>
```

Teardown then completes on its own, usually within 30 seconds. Don't remove the finalizer from the `InferenceGatewayConfig` by hand; that leaves the endpoint service and the load balancer behind in your account.

**GlobalRoutingEnvoyServiceStuck:** The gateway's global routing Envoy Service was deleted, and the deletion can't finish while the endpoint service uses its load balancer. Traffic keeps flowing, and the endpoint service and the member aren't affected. To recover, remove the load balancer finalizer from the Service that the message names:

```bash
kubectl -n hyperpod-inference-system patch service <envoy-service-name> --type json -p \
  '[{"op":"test","path":"/metadata/finalizers","value":["service.k8s.aws/resources"]},
    {"op":"remove","path":"/metadata/finalizers"}]'
```

Envoy Gateway re-creates the Service within a minute. If its target group stays empty, remove the checkpoint annotations from its `TargetGroupBinding`:

```bash
kubectl -n hyperpod-inference-system get targetgroupbinding
kubectl -n hyperpod-inference-system annotate targetgroupbinding <binding-name> \
  elbv2.k8s.aws/checkpoint- elbv2.k8s.aws/checkpoint-timestamp-
```

**GlobalRoutingPrincipalsNotConfigured:** The controller can't name the service principals that are allowed to connect. Update the add-on to the latest version.

**GlobalRoutingDeleting:** The endpoint service is being deleted. Wait.

If `ec2:DescribeRegions` is missing from the controller role, the condition stays `Ready`, but the endpoint service accepts connections only from Global Inference Gateways in Regions that are enabled by default, and the condition message says so. Attach the policy in [Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions) to support Global Inference Gateways in [opt-in Regions](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-supported-regions).

**GlobalRoutingPending:** The load balancer or the endpoint service is still being created. This usually takes about 3 minutes. If it persists, your account may have reached the **Network Load Balancers per Region** quota (see [Quotas and limits](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-quotas-and-limits)). Check the events on the gateway's global routing Envoy Service, and check the quota:

```bash
kubectl -n hyperpod-inference-system get svc | grep my-gateway-gig
kubectl -n hyperpod-inference-system describe svc <envoy-service-name>
aws service-quotas get-service-quota --region <region> \
  --service-code elasticloadbalancing --quota-code L-69A177A2
```

## In-cluster gateway: MetricsPublisherReady is False
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-in-cluster-gateway-metricspublisherready-is-false"></a>

**Problem:** The gateway is added to a Global Inference Gateway, but its `MetricsPublisherReady` condition is `False`. The Global Inference Gateway doesn't route to a member until its metrics publisher is running.

**Symptoms and resolution:** Check the reason and message on the `MetricsPublisherReady` condition, then find the reason below.

```bash
kubectl -n my-namespace get inferencegatewayconfig my-gateway \
  -o jsonpath='{.status.conditions[?(@.type=="MetricsPublisherReady")].reason}: {.status.conditions[?(@.type=="MetricsPublisherReady")].message}{"\n"}'
```

**ServiceAccountMissing or ServiceAccountRoleNotConfigured:** The metrics publisher has no IAM role. Check the publisher's service account, and if it has no role, create the role and set `inferenceGateway.metricsPublisher.serviceAccount.roleArn` on the add-on (Steps [1b](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1b-create-the-metrics-publisher-role) and [1c](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1c-update-the-add-on)):

```bash
kubectl -n hyperpod-inference-system get sa inference-gateway-metrics-publisher \
  -o jsonpath='{.metadata.annotations.eks\.amazonaws\.com/role-arn}'
```

**AWSUnavailable:** The controller has no AWS credentials. Set `inferenceGateway.serviceAccount.roleArn` on the add-on ([Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions)), and then restart the controller, because it reads its role only when it starts:

```bash
kubectl -n hyperpod-inference-system rollout restart deploy/inference-gateway-controller
```

**ClusterARNUnresolved:** The controller couldn't look up the HyperPod cluster, usually because the controller role is missing `sagemaker:DescribeCluster`. Attach the policy in [Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions).

**KinesisEndpointPending or KinesisEndpointError:** The private endpoint for metrics is being created, or Amazon EC2 refused it, and the message has the error. If none of the cluster's subnets is in an Availability Zone that supports the endpoint, or none has a free IP address, the message says so and lists the zones. A failed endpoint is replaced automatically. During removal, the message starts with `delete Kinesis endpoint:` and usually names a missing permission ([Step 1a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1a-grant-the-gateway-controller-the-global-routing-permissions)). To see the endpoint and the free IP addresses in the cluster's subnets:

```bash
# Describe the metrics VPC endpoint
aws ec2 describe-vpc-endpoints --region <region> \
  --filters Name=tag:HyperPodInferenceComponent,Values=metrics-publisher-kinesis-endpoint \
  --query 'VpcEndpoints[].{Id:VpcEndpointId,State:State,Subnets:SubnetIds}' --output json

# Describe the cluster's subnets
aws ec2 describe-subnets --region <region> --subnet-ids <subnet-id-1> <subnet-id-2> \
  --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,ZoneId:AvailabilityZoneId,FreeIPs:AvailableIpAddressCount}' --output table
```

If no subnet in a supported Availability Zone has a free IP address, that Availability Zone is left out of the metrics endpoint and the condition message names it. The endpoint keeps working from the other Availability Zones.

**PublisherProgressing:** The metrics publisher is rolling out. Wait for the rollout:

```bash
kubectl -n hyperpod-inference-system rollout status deploy/my-gateway-metrics-publisher --timeout=150s
```

**GIGMembershipInvalid:** The membership settings that the Global Inference Gateway wrote for this gateway can't be used, and the message names the field. The Global Inference Gateway rewrites them when it retries. If the condition persists, remove the member and add it again. To see the settings:

```bash
kubectl -n hyperpod-inference-system get configmap gig-membership -o yaml
```

**NoModels:** The `InferenceGatewayConfig` has no schedulers. Add at least one scheduler.

**ApplyFailed:** The controller couldn't create or update one of the metrics publisher's Kubernetes objects. The message names the object and the error. Check for an admission webhook or policy that rejects it:

```bash
kubectl -n hyperpod-inference-system get events --sort-by=.lastTimestamp | grep metrics-publisher
```

**ResourceGenerationFailed:** The controller couldn't build the metrics publisher's Kubernetes resources. The message has the error. Contact AWS Support.

**MetricsPublisherDeleting:** The metrics publisher and its endpoint are being deleted. Wait.

If the condition is `True` but writes fail with `KMSAccessDeniedException` in the publisher's logs, check that the publisher role has the `AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess` policy ([Step 1b](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1b-create-the-metrics-publisher-role)):

```bash
kubectl -n hyperpod-inference-system logs deploy/my-gateway-metrics-publisher --since=15m | grep -i kms
```

## Member is FAILED
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-member-is-failed"></a>

Run `list-inference-gateways` and read `FailureReason`. Common causes:
+ **Role trust:** The execution role can't be assumed. Check the trust policy in [Step 2a](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-2a-create-the-role), including the `aws:SourceAccount` and `aws:SourceArn` conditions.
+ **Cluster access:** The execution role can't reach the cluster. Check the permissions in [Step 2b](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-2b-attach-the-permissions-policy) and the [EKS access entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in [Step 2c](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-2c-grant-the-role-access-to-each-members-kubernetes-api).
+ **Global routing off:** Global routing isn't turned on for the `InferenceGatewayConfig`. Set `spec.globalRouting.enabled` to `true` ([Step 1d](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1d-turn-on-global-routing)).
+ **Not ready in time:** The member didn't become reachable in time. Check that its `InferenceGatewayConfig` is `Ready` and `GLOBAL-ROUTING` is `Ready` ([Step 1e](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-1e-verify)), and that the add-on is the version in [Prerequisites](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-prerequisites), which publishes the certificates global routing needs.
+ **Cluster not found:** The HyperPod cluster wasn't found, or isn't orchestrated by Amazon EKS. Check the `ClusterArn`.
+ **Gateway not found:** The `InferenceGatewayConfig` wasn't found. Check the namespace and name.
+ **Certificate access:** The execution role can't read the gateway's certificate from the TLS bucket. Check the policy in [Step 2b](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-2b-attach-the-permissions-policy). If your bucket name doesn't begin with `hyperpod-tls`, use the inline policy in Step 2b.
+ **Connectivity:** The Global Inference Gateway couldn't reach the member over its endpoint. Check that the in-cluster gateway pods are healthy.
+ **Membership ConfigMap:** The cluster has no `gig-membership` ConfigMap in `hyperpod-inference-system`. The add-on creates it; update the add-on to a version that supports global routing.

A cluster in another account or in an [opt-in Region](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-supported-regions), or an in-cluster gateway that already belongs to another Global Inference Gateway, is rejected when you call create or add (`ValidationException` or `ResourceInUse`), so it never becomes a `FAILED` member.

After you fix the cause, remove the member, wait until it no longer appears in `list-inference-gateways`, and then add it again. If it's the only member, add another member first.

## Invocation errors
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-invocation-errors"></a>

### Error origin
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-error-origin"></a>

For the `InvokeGlobalInferenceGateway` and `InvokeGlobalInferenceGatewayWithResponseStream` operations, the start of each error message tells you where the error came from. This includes `InternalStreamFailure` events. Errors on the OpenAI-compatible paths don't use these prefixes.
+ **Global Inference Gateway:** The Global Inference Gateway produced the error, for example `Global Inference Gateway: timed out waiting for the inference gateway`.
+ **inference gateway:** A member cluster produced the error, for example `inference gateway: 500 ...`.
+ **inference gateway (component name):** A specific component in the member cluster produced the error: `config`, `scheduler`, `model selector`, or `model server`. For example, `inference gateway (model server): 400 ...`.

For errors from a member, the message includes the member's HTTP status code and up to 256 bytes of its error message.

### Request IDs
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-request-ids"></a>

Every response includes the request ID in the `x-amzn-requestid` and `x-request-id` headers. The Global Inference Gateway also forwards `x-request-id` to the member, so you can use it to find the request in your in-cluster gateway and model server logs.

To use your own request ID, send it in `x-request-id`. It can be up to 128 characters, using letters, digits, and `- _ . : ; = + /`. If you don't send one, or yours isn't valid, the Global Inference Gateway generates one.

If you contact AWS Support about a request, include its request ID.

### Exceptions
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-exceptions"></a>

These exceptions are returned by the SDK operations. The OpenAI-compatible paths return the same HTTP status with an `{"error": ...}` body, or the member's own response.


**Exceptions**  

| HTTP status | Error | Common cause | 
| --- | --- | --- | 
| 400 | ValidationException | Invalid JSON, missing or duplicate model, or the member rejected the request. | 
| 403 | AccessDeniedException | The request isn't signed, the signature is invalid, the caller is in another account, IAM denies the action, or the member's JWT check rejected the end-user token. | 
| 404 | ResourceNotFoundException | The gateway ID is wrong, the model name doesn't match any model your members serve (Global Inference Gateway: model not found on any target), or the member returned 404. | 
| 413 | PayloadTooLargeException | The request body is larger than 10 MiB. | 
| 429 | ThrottlingException | The request was throttled, or every member tried was throttled. Retry after the time in the Retry-After header. | 
| 502 | BadGatewayException | The member couldn't be reached or returned a server error, or a buffered response was larger than 10 MiB. | 
| 503 | ServiceUnavailableException | One of the following messages:+ `Global Inference Gateway: no target available for model`. No member can take the model yet: members haven't reported metrics (right after create or add), or have stopped reporting for 30 minutes and were removed (check [`MetricsPublisherReady`](#sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-in-cluster-gateway-metricspublisherready-is-false) on each member). Retry after the time in the `Retry-After` header.<br />+ `Global Inference Gateway: all targets unavailable`. Members serve the model, but none is healthy (for example, none has a ready model pod). No `Retry-After` is sent. Check each member's status.<br />+ `Global Inference Gateway: no servable target`. Every member that serves the model is being removed or is disabled.<br />+ `Global Inference Gateway: authorization is temporarily unavailable`. Retry with backoff. | 
| 504 | GatewayTimeoutException | The member didn't send the first byte of its response body within 300 seconds (for non-streamed requests, the whole generation must finish within that time), the member returned 408 or 504, or the 15-minute limit was reached before the first byte. | 

## Removing a member returns ValidationException
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-removing-a-member-returns-validationexception"></a>

**Problem:** `remove-inference-gateway` returns `ValidationException` with a message that the Global Inference Gateway needs at least one member.

**Symptoms and resolution:** You can't remove the last member, because a Global Inference Gateway always keeps at least one. A `FAILED` member counts toward this, and a member that is already `REMOVING` doesn't. To check the members:

```bash
aws sagemaker list-inference-gateways --region us-west-2 --identifier my-global-gateway
```

To remove every member, delete the Global Inference Gateway instead. For the steps, see [Clean up](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-clean-up).

## A routing weight change doesn't take effect
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-a-routing-weight-change-doesnt-take-effect"></a>

**Problem:** After you update the routing weights, traffic is still distributed as before.

**Symptoms and resolution:** The Global Inference Gateway applies new weights within about 15 seconds after the update completes. Check that its status is `ACTIVE`, not `UPDATING`, and check `FailureReason`. `Routing` shows the weights you requested even if the update failed.

```bash
aws sagemaker describe-global-inference-gateway --region us-west-2 \
  --identifier my-global-gateway --query '{Status:Status,Routing:Routing,FailureReason:FailureReason}'
```

If `FailureReason` is set, the update failed and the previous weights are still in effect. Send the same update again to retry.

## Control plane errors
<a name="sagemaker-hyperpod-model-deployment-ts-global-inference-gateway-control-plane-errors"></a>


**Control plane errors**  

| Error | Common cause | 
| --- | --- | 
| ValidationException | Invalid input, for example routing weights that don't add up to 1.0 or that set only some of the four weights, a name that is exactly 12 lowercase letters and digits, an execution role or cluster in another account, a cluster in an [opt-in Region](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-supported-regions), or removing the last member. | 
| ResourceInUse | The name is already used in this account and Region, or an in-cluster gateway already belongs to another Global Inference Gateway. | 
| ResourceLimitExceeded | More than 10 members, or the account quota for Global Inference Gateways is reached (see [Quotas and limits](sagemaker-hyperpod-model-deployment-global-inference-gateway.md#sagemaker-hyperpod-model-deployment-global-inference-gateway-quotas-and-limits)). | 
| ConflictException | Another change is in progress, or the Global Inference Gateway failed to create and only accepts delete. One membership change runs at a time per Global Inference Gateway. Wait until no member is ADDING or REMOVING, then retry. | 
| ResourceNotFound | No Global Inference Gateway has that name, ID, or ARN. | 
| ThrottlingException | Too many requests in a short time. Retry with exponential backoff. AddInferenceGateway and RemoveInferenceGateway are rate limited, so send membership changes one at a time rather than in parallel. | 