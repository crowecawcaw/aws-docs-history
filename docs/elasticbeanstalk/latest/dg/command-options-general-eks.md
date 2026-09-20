

# Configuration options for Beanstalk Cluster environments
<a name="command-options-general-eks"></a>

A Beanstalk Cluster environment is configured through the twelve namespaces on this page. They are the only namespaces that a Beanstalk Cluster environment accepts. The classic namespaces in [Configuration options for Beanstalk Standard environments](command-options-general.md) configure Beanstalk Standard environments and do not apply, and passing one of them to a Beanstalk Cluster environment returns an `InvalidParameterValueException` rather than being ignored.

For the ways to set these options, and for how Elastic Beanstalk resolves them, see [Configuration options](command-options.md).

**Note**  
The **Default** column gives the value that `DescribeConfigurationOptions` advertises for the option. Where Elastic Beanstalk applies a value even though it advertises no default, the description says so.

**Topics**
+ [aws:elasticbeanstalk:eks](#command-options-eks-base)
+ [aws:elasticbeanstalk:eks:environment](#command-options-eks-environment)
+ [aws:elasticbeanstalk:eks:environment:deployment](#command-options-eks-deployment)
+ [aws:elasticbeanstalk:eks:environment:deployment:strategy:rolling](#command-options-eks-deployment-rolling)
+ [aws:elasticbeanstalk:eks:environment:autoscaling](#command-options-eks-autoscaling)
+ [aws:elasticbeanstalk:eks:environment:autoscaling:trigger](#command-options-eks-autoscaling-trigger)
+ [aws:elasticbeanstalk:eks:environment:autoscaling:behavior](#command-options-eks-autoscaling-behavior)
+ [The container probe namespaces](#command-options-eks-probes)
+ [aws:elasticbeanstalk:eks:alb](#command-options-eks-alb)
+ [aws:elasticbeanstalk:eks:observability](#command-options-eks-observability)

## aws:elasticbeanstalk:eks
<a name="command-options-eks-base"></a>

Configure the IAM roles for the Amazon EKS cluster that runs your environment. You supply both roles, and Elastic Beanstalk requires them when you create the environment. The subnets that you select determine which cluster the environment joins, and Elastic Beanstalk rejects the request if these roles don't match the roles registered for that cluster. For the role names that the console creates, their trusted services, and their policies, see [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md).

The environment also requires an observability role, and it can take an optional application role. Both of those settings are in the `aws:elasticbeanstalk:eks:environment` namespace rather than this one. See [aws:elasticbeanstalk:eks:environment](#command-options-eks-environment).


**Namespace: `aws:elasticbeanstalk:eks`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `cluster-role` | The ARN of the IAM role that Amazon EKS assumes for the cluster. | None. You must supply a value. | An IAM role ARN | 
| `node-role` | The ARN of the IAM role that the cluster's Amazon EC2 nodes assume. | None. You must supply a value. | An IAM role ARN | 

## aws:elasticbeanstalk:eks:environment
<a name="command-options-eks-environment"></a>

Configure the application container, the compute it reserves, its network placement, and the roles it uses.


**Namespace: `aws:elasticbeanstalk:eks:environment`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `application-role` | The ARN of an optional IAM role that your application assumes to call AWS services. See [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md). | None | An IAM role ARN | 
| `arch` | The CPU architecture that your application runs on. | `amd64` | `amd64` \| `arm64` | 
| `cpu` | The CPU that each replica of your application reserves. Uses Kubernetes quantity notation, so `500m` is half of a virtual CPU and `2` is two virtual CPUs. | `250m` | `0.01` to `128`, or `10m` to `128000m` | 
| `cpu-limit` | The most CPU that each replica of your application can use. Uses the same notation as `cpu`. | None | `0.01` to `128`, or `10m` to `128000m` | 
| `env-variables` | The environment variables for the container, as a JSON object that maps each variable name to its value. This is one option that holds every variable, not one option per variable. Elastic Beanstalk sets `PORT` from `service-port` and overrides any value that you supply for it. | `{"PORT" : 8080}` | A JSON object | 
| `ingress-allowlist-environments` | The names of the environments that may send traffic to this environment. See [Multi-tenancy for Beanstalk Cluster environments](beanstalk-cluster-multi-tenancy.md). | None | A comma-separated list of environment names | 
| `ingress-allowlist-groups` | The ingress groups whose environments may send traffic to this environment. Every environment in a listed group is allowed. | None | A comma-separated list of ingress group names | 
| `ingress-groups` | The ingress groups that this environment belongs to. Environments in the same group can reach each other. | None | A comma-separated list of ingress group names | 
| `instance-category` | The Amazon EC2 instance category that the cluster's nodes are selected from. | None | `c` \| `d` \| `g` \| `gr` \| `hpc` \| `i` \| `im` \| `is` \| `m` \| `p` \| `r` \| `t` \| `x` \| `z` | 
| `language` | The runtime language of your application, which selects the OpenTelemetry auto-instrumentation that Elastic Beanstalk adds to your container, so that your application emits metrics, logs, and traces to the observability backends that you select without application changes. This option chooses auto-instrumentation only. It doesn't limit the languages your application can use. Omit it if your runtime isn't listed, or if your application emits OpenTelemetry data on its own. | None | `python` \| `java` \| `dotnet` \| `nodejs` | 
| `load-balancer-type` | How traffic reaches your application. With `None`, Elastic Beanstalk doesn't create a load balancer. See [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md). | `ALB` | `ALB` \| `None` | 
| `memory` | The memory that each replica of your application reserves. Uses Kubernetes quantity notation, such as `512Mi` or `1.5Gi`. Fractional values are accepted. | `512Mi` | A Kubernetes memory quantity | 
| `memory-limit` | The most memory that each replica of your application can use. Uses the same notation as `memory`. | `1Gi` | A Kubernetes memory quantity | 
| `node-pool` | The name of the node pool that runs this environment's replicas. A unique value gives the environment its own nodes, and a shared value groups environments onto shared nodes. See [Multi-tenancy for Beanstalk Cluster environments](beanstalk-cluster-multi-tenancy.md). | None | A DNS-1123 label | 
| `observability-role` | The ARN of the IAM role that publishes the environment's metrics, logs, and traces. Elastic Beanstalk requires it, and it must match the role registered for the cluster that your subnets select. There is no default, so supply it explicitly. See [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md). | None. You must supply a value. | An IAM role ARN | 
| `secrets` | The secrets to expose to the container, as a JSON object that maps each name to the ARN of a secret in Secrets Manager or a parameter in Systems Manager Parameter Store. Like `env-variables`, this is one option that holds every secret. Requires `application-role`: Elastic Beanstalk reads each secret through the pod's identity, which exists only when you set that option. Without it, the volume mount fails and your replicas never start. | None | A JSON object | 
| `service-port` | The port that your application listens on. Elastic Beanstalk requires it, injects it into the container as the `PORT` environment variable, and uses it as the port that other environments and the container probes reach. | `8080` | `1` to `65535` | 
| `subnets` | The subnets for the environment. They determine where the cluster's nodes run and which cluster the environment joins. If you omit them, Elastic Beanstalk uses the public subnets of the default VPC. You can't change them after you create the environment. See [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md). | None | A comma-separated list of subnet IDs | 

## aws:elasticbeanstalk:eks:environment:deployment
<a name="command-options-eks-deployment"></a>

Choose how Elastic Beanstalk replaces the running replicas of your application when you deploy a new application version.


**Namespace: `aws:elasticbeanstalk:eks:environment:deployment`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `strategy` | The deployment strategy. `RollingUpdate` replaces replicas gradually, and `Recreate` takes all of them down and starts the new version, which is the strategy that the console calls all at once. See [Choosing a deployment policy](using-features.deploy-existing-version.md#deployments-scenarios). | `RollingUpdate` | `RollingUpdate` \| `Recreate` | 

## aws:elasticbeanstalk:eks:environment:deployment:strategy:rolling
<a name="command-options-eks-deployment-rolling"></a>

Bound how far a rolling deployment may run ahead of, or behind, the number of replicas that the environment is running. These options apply when `strategy` is `RollingUpdate`.


**Namespace: `aws:elasticbeanstalk:eks:environment:deployment:strategy:rolling`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `max-surge` | How many replicas Elastic Beanstalk may start beyond the environment's current replica count while it deploys. | `1` | A count, such as `2`, or a percentage, such as `25%` | 
| `max-unavailable` | How many of the environment's replicas may be unavailable at one time while it deploys. | `0` | A count, such as `1`, or a percentage, such as `25%` | 

## aws:elasticbeanstalk:eks:environment:autoscaling
<a name="command-options-eks-autoscaling"></a>

Set the number of replicas that Elastic Beanstalk runs for your application, and how often it evaluates whether to change that number.

If you configure no trigger, Elastic Beanstalk scales the environment on CPU utilization with a target of 80 percent, between `min-replica` and `max-replica`. To scale on something else, set a trigger. See [aws:elasticbeanstalk:eks:environment:autoscaling:trigger](#command-options-eks-autoscaling-trigger).


**Namespace: `aws:elasticbeanstalk:eks:environment:autoscaling`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `min-replica` | The fewest replicas of your application that the environment runs. | `1` | `1` to `100` | 
| `max-replica` | The most replicas of your application that the environment runs. | `10` | `1` to `100` | 
| `polling-interval` | How often, in seconds, Elastic Beanstalk evaluates the scaling triggers. | `30` | `1` to `1000` | 
| `cooldown-period` | How long, in seconds, Elastic Beanstalk waits after the last trigger stops reporting activity before it scales the environment back down. | `300` | An integer of `1` or greater | 

## aws:elasticbeanstalk:eks:environment:autoscaling:trigger
<a name="command-options-eks-autoscaling-trigger"></a>

Choose what makes the environment scale. You can scale on the CPU or memory that your replicas use, and you can scale on a schedule or on a metric that your own endpoint reports. These options have no advertised defaults. When you set none of them, Elastic Beanstalk supplies a CPU trigger with `cpu-metric-type` set to `Utilization` and `cpu-value` set to `80`.


**Namespace: `aws:elasticbeanstalk:eks:environment:autoscaling:trigger`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `cpu-metric-type` | Whether the CPU trigger compares a percentage of the reserved CPU (`Utilization`) or an absolute amount (`AverageValue`). | None. Elastic Beanstalk applies `Utilization` if you set `cpu-value` alone, or if you set no trigger at all. | `Utilization` \| `AverageValue` | 
| `cpu-value` | The CPU target that the environment scales to hold. With `Utilization`, a value of `60` means 60 percent of the reserved CPU. | None. Elastic Beanstalk applies `80` if you set no trigger at all. | An integer | 
| `memory-metric-type` | Whether the memory trigger compares a percentage of the reserved memory (`Utilization`) or an absolute amount (`AverageValue`). | None. Elastic Beanstalk applies `Utilization` if you set `memory-value` alone. | `Utilization` \| `AverageValue` | 
| `memory-value` | The memory target that the environment scales to hold. | None | An integer | 
| `scaler-type` | The kind of event-driven trigger. `cron` scales on a schedule, and `metrics-api` scales on a value that Elastic Beanstalk reads from an HTTP endpoint that you supply. | None | `cron` \| `metrics-api` | 
| `scaler-metadata` | The settings for the trigger, as a JSON object. With `cron`, supply `timezone`, `start`, `end`, and `desiredReplicas`. With `metrics-api`, supply `url`, `valueLocation`, and `targetValue`. | None | A JSON object | 
| `scaler-auth-mode` | How Elastic Beanstalk authenticates to the endpoint that a `metrics-api` trigger reads. | `bearer` | `bearer` \| `basic` \| `apiKey` \| `tls` | 
| `scaler-auth-secret` | The ARN of the Secrets Manager secret that holds the credentials for the endpoint. You can set it only when `scaler-type` is `metrics-api`. Requires `application-role`: Elastic Beanstalk reads the secret through the pod's identity, which exists only when you set that option. Without it, the mount fails and your replicas never start. | None | An Secrets Manager secret ARN | 

The following example scales the environment to five replicas during weekday working hours in UTC:

```
$ cat schedule.json
[
  {
    "Namespace": "aws:elasticbeanstalk:eks:environment:autoscaling:trigger",
    "OptionName": "scaler-type",
    "Value": "cron"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:environment:autoscaling:trigger",
    "OptionName": "scaler-metadata",
    "Value": "{\"timezone\":\"UTC\",\"start\":\"0 8 * * 1-5\",\"end\":\"0 18 * * 1-5\",\"desiredReplicas\":\"5\"}"
  }
]
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-cluster-env}} \
    --option-settings file://schedule.json
```

A `scaler-metadata` value is itself a JSON document, so the settings go in a file rather than on the command line.

## aws:elasticbeanstalk:eks:environment:autoscaling:behavior
<a name="command-options-eks-autoscaling-behavior"></a>

Limit how quickly the environment adds or removes replicas once a trigger fires. Each direction takes a period, a unit, and an amount: within each period, the environment changes the replica count by at most the amount that you set.


**Namespace: `aws:elasticbeanstalk:eks:environment:autoscaling:behavior`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `scaleup-period` | The period, in seconds, that `scaleup-value` applies to. | None | An integer of `1` or greater | 
| `scaleup-type` | Whether `scaleup-value` is a number of replicas (`Pods`) or a percentage of the current count (`Percent`). | None | `Pods` \| `Percent` | 
| `scaleup-value` | The most that the environment adds within one `scaleup-period`. | None | An integer | 
| `scaledown-period` | The period, in seconds, that `scaledown-value` applies to. | None | An integer of `1` or greater | 
| `scaledown-type` | Whether `scaledown-value` is a number of replicas (`Pods`) or a percentage of the current count (`Percent`). | None | `Pods` \| `Percent` | 
| `scaledown-value` | The most that the environment removes within one `scaledown-period`. | None | An integer | 

## The container probe namespaces
<a name="command-options-eks-probes"></a>

Three namespaces configure container probes, and each one takes the same nine options:
+ `aws:elasticbeanstalk:eks:environment:readiness-probe` decides when a replica is ready to receive traffic. A replica that fails it is taken out of service without being restarted.
+ `aws:elasticbeanstalk:eks:environment:liveness-probe` decides when a replica is unhealthy. A replica that fails it is restarted.
+ `aws:elasticbeanstalk:eks:environment:startup-probe` gives a slow-starting replica time to initialize before the other two probes begin.

Every probe is off until you enable it. For how probes relate to environment health, see [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md).


**Namespaces: `aws:elasticbeanstalk:eks:environment:readiness-probe`, `aws:elasticbeanstalk:eks:environment:liveness-probe`, and `aws:elasticbeanstalk:eks:environment:startup-probe`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `enabled` | Whether the probe runs. | `false` | `true` \| `false` | 
| `http-path` | The path that the probe requests. | `/` | A URL path | 
| `http-port` | The port that the probe requests. If you omit it, the probe uses `service-port`. | None. The probe uses `service-port`. | `1` to `65535` | 
| `initial-delay-seconds` | How long the probe waits after a replica starts before its first request. | `0` | An integer number of seconds | 
| `period-seconds` | How often the probe runs. | `30` | `1` to `3600` | 
| `timeout-seconds` | How long the probe waits for a response before the request counts as a failure. | `5` | An integer number of seconds | 
| `success-threshold` | How many consecutive successes make the probe pass. | `1` | An integer | 
| `failure-threshold` | How many consecutive failures make the probe fail. | `3` | An integer | 

## aws:elasticbeanstalk:eks:alb
<a name="command-options-eks-alb"></a>

Configure the Application Load Balancer in front of your application, its listeners and TLS, and the health check on its target group. These options apply when `load-balancer-type` is `ALB`. For the network settings, for supplying a load balancer that you already own, and for the rules that govern the HTTPS listener, see [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md).


**Namespace: `aws:elasticbeanstalk:eks:alb`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `arn` | The ARN of an Application Load Balancer that you already own, used instead of one that Elastic Beanstalk creates. Elastic Beanstalk rejects the ARN of a Network Load Balancer. | None. Elastic Beanstalk creates a load balancer. | An Application Load Balancer ARN | 
| `scheme` | Whether the load balancer is reachable from the internet. If you omit it, Elastic Beanstalk derives it from your subnets: public subnets give an internet-facing load balancer, and private subnets give an internal one. | None. Derived from your subnets. | `internet-facing` \| `internal` | 
| `subnets` | The subnets to place the load balancer in. If you omit them, it uses the environment's subnets. | None. The environment's subnets. | A comma-separated list of subnet IDs | 
| `security-groups` | The security groups to attach to the load balancer. | None | A comma-separated list of security group IDs | 
| `manage-backend-security-group-rules` | Whether Elastic Beanstalk adds and removes the security group rules between the load balancer and your application. | `true` | `true` \| `false` | 
| `ip-address-type` | Whether the load balancer serves IPv4 only or both IPv4 and IPv6. Elastic Beanstalk advertises no default and applies `ipv4`. | `ipv4`, applied by Elastic Beanstalk | `ipv4` \| `dualstack` | 
| `target-type` | Whether the load balancer sends traffic to the replicas' IP addresses or to the nodes that run them. Elastic Beanstalk advertises no default and applies `ip`. | `ip`, applied by Elastic Beanstalk | `ip` \| `instance` | 
| `listen-ports` | The listeners to open, as a JSON array with one object per listener, such as `[{"HTTPS":443},{"HTTP":80}]`. Each port must be unique. Elastic Beanstalk makes sure that an HTTPS listener exists, and supplies the certificate for it. An HTTP listener redirects to HTTPS rather than serving application traffic. | None. Elastic Beanstalk configures HTTPS on port 443. | A JSON array of protocol-to-port objects | 
| `certificate-arn` | The ARN of your own ACM certificate to attach to the HTTPS listeners, for example when you serve the environment from a custom domain. You don't need this option for HTTPS to work: Elastic Beanstalk creates and attaches a certificate for the environment's own domain either way. If you set it, the load balancer carries both certificates. | None | An ACM certificate ARN | 
| `ssl-policy` | The security policy for the HTTPS listeners. | None | An Elastic Load Balancing security policy name | 
| `ssl-redirect` | Selects which HTTPS port Elastic Beanstalk redirects HTTP requests to. The value must be a port that a configured HTTPS listener uses. Elastic Beanstalk redirects requests that arrive on an HTTP listener whether or not you set this option, so it only changes the target port. | None. Elastic Beanstalk redirects to your HTTPS listener's port. | `1` to `65535` | 
| `backend-protocol` | The protocol that the load balancer uses to reach your application. | None | `HTTP` \| `HTTPS` | 
| `backend-protocol-version` | The protocol version that the load balancer uses to reach your application. Applies only when `backend-protocol` is set. | None | `HTTP2` \| `GRPC` | 
| `healthcheck-path` | The path that the target group health check requests. | `/` | A URL path | 
| `healthcheck-protocol` | The protocol that the target group health check uses. | `HTTP` | `HTTP` \| `HTTPS` | 
| `healthcheck-interval-seconds` | How often the target group health check runs. | `15` | `5` to `300` | 
| `healthcheck-timeout-seconds` | How long the health check waits for a response. | `5` | `2` to `120` | 
| `success-codes` | The HTTP status codes that count as a successful health check. | `200` | A status code, a list, or a range | 
| `healthy-threshold-count` | How many consecutive successful checks make a target healthy. | `2` | `2` to `10` | 
| `unhealthy-threshold-count` | How many consecutive failed checks make a target unhealthy. | `2` | `2` to `10` | 
| `wafv2-acl-arn` | The ARN of the AWS WAF web ACL to associate with the load balancer. | None | An AWS WAF web ACL ARN | 
| `tags` | The tags to apply to the load balancer. | None | A JSON object of tag keys and values | 
| `load-balancer-attributes` | Load balancer attributes to apply to the load balancer, passed through to Elastic Load Balancing without interpretation. | None | A comma-separated list of `key=value` pairs, such as `idle_timeout.timeout_seconds=300,routing.http2.enabled=false` | 
| `listener-attributes` | Listener attributes to apply to a specific listener, passed through to Elastic Load Balancing without interpretation. Supply only listener attributes here, not load balancer attributes. | None | A JSON array of objects, each mapping a listener to a comma-separated list of `key=value` pairs, such as `[{"HTTPS-8443":"routing.http.response.server.enabled=false"}]` | 
| `raw-annotation` | Annotations to apply directly to the Kubernetes ingress that Elastic Beanstalk generates for your environment. Use this for load balancer behavior that the other options in this namespace don't cover. | None | A JSON array of objects, each mapping an ingress annotation key to its value. Each comma-separated segment of a value must contain exactly one `=` | 

**Note**  
`load-balancer-attributes`, `listener-attributes`, and `raw-annotation` pass their values through to the load balancer without interpreting them, so Elastic Beanstalk doesn't validate what an individual attribute or annotation means. When you create an environment, an invalid value prevents the load balancer from being created, so the failure is visible. When you update an environment, Elastic Beanstalk doesn't wait for the load balancer to reconcile, so the operation can succeed before your change takes effect. Confirm the change on the load balancer itself.

## aws:elasticbeanstalk:eks:observability
<a name="command-options-eks-observability"></a>

Choose where your application's metrics, logs, and traces go. Elastic Beanstalk provisions and operates the collection components, and you are responsible for instrumenting your application and for access to any destination that you select. See [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md).


**Namespace: `aws:elasticbeanstalk:eks:observability`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| `metrics-backend` | Where your application's metrics go. `amp` sends them to Amazon Managed Service for Prometheus and requires `metrics-endpoint`. | `cloudwatch` | `cloudwatch` \| `amp` \| `custom` \| `none` | 
| `metrics-endpoint` | The Amazon Managed Service for Prometheus remote-write endpoint. Set it only when `metrics-backend` is `amp`. | None | A remote-write endpoint URL | 
| `logs-backend` | Where your application's logs go. | `cloudwatch` | `cloudwatch` \| `s3` \| `custom` \| `none` | 
| `traces-backend` | Where your application's traces go. Unlike metrics and logs, traces have no backend until you select one. | None | `xray` \| `custom` \| `none` | 
| `custom-config` | The OpenTelemetry collector pipeline configuration to use for the signals that you set to `custom`. Reference each credential as a `${{{NAME}}}` placeholder that `custom-credentials` supplies. See [Sending observability data to a third-party backend](monitoring-cluster-environments.md#monitoring-cluster-environments-custom-backend). | None | A collector pipeline configuration, as JSON | 
| `custom-credentials` | The ARN of an Secrets Manager secret holding the credentials that the collector needs to reach a `custom` backend. The secret value must be a JSON object whose keys match the placeholders in `custom-config`. Requires `application-role`: the collector reads the secret through the pod's identity, which exists only when you set that option, and that role must also be allowed to read the secret. | None | An Secrets Manager secret ARN | 