

# Scaling Beanstalk Cluster environments
<a name="configuring-cluster-scaling"></a>

A Beanstalk Cluster environment scales by changing the number of *replicas* of your application that it runs. A replica is one running copy of your container image. Amazon EKS supplies the node capacity that those replicas need and adds or removes nodes to fit them, so you size the application rather than a fleet of instances.

This is the main difference from Beanstalk Standard, which scales an Auto Scaling group of Amazon EC2 instances. The `aws:autoscaling:*` namespaces do not apply to a Beanstalk Cluster environment. Scaling is configured through the `aws:elasticbeanstalk:eks:environment:autoscaling` namespace and its child namespaces instead. For every option and its accepted values, see [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).

## Setting the replica bounds
<a name="configuring-cluster-scaling-replicas"></a>

Two options bound the replica count: `min-replica` and `max-replica`, both in the `aws:elasticbeanstalk:eks:environment:autoscaling` namespace. Elastic Beanstalk keeps the replica count between them.

Set both options to the same value to run a fixed number of replicas. Set `max-replica` higher than `min-replica` to let the environment scale between the two. An environment always runs at least one replica, because `min-replica` accepts `1` as its lowest value.

```
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-cluster-env}} \
    --option-settings \
        Namespace=aws:elasticbeanstalk:eks:environment:autoscaling,OptionName=min-replica,Value=2 \
        Namespace=aws:elasticbeanstalk:eks:environment:autoscaling,OptionName=max-replica,Value=20
```

## How Elastic Beanstalk decides when to scale
<a name="configuring-cluster-scaling-triggers"></a>

Within those bounds, one or more *triggers* decide the replica count. Elastic Beanstalk evaluates the triggers on the interval that `polling-interval` sets. When the triggers stop reporting activity, Elastic Beanstalk waits for the period that `cooldown-period` sets before it scales the environment back down, which keeps a brief lull from removing replicas that are about to be needed again.

If you configure no trigger at all, the environment scales on the CPU utilization of its replicas. The remaining sections describe the triggers you can configure instead.

## Scaling on CPU or memory
<a name="configuring-cluster-scaling-cpu-memory"></a>

To scale on the resources that your replicas consume, set a metric type and a target value in the `aws:elasticbeanstalk:eks:environment:autoscaling:trigger` namespace. Elastic Beanstalk adds or removes replicas to hold the environment near the target that you set.
+ For CPU, set `cpu-metric-type` and `cpu-value`.
+ For memory, set `memory-metric-type` and `memory-value`.

A metric type of `Utilization` treats the value as a percentage of what the replica reserves through the `cpu` and `memory` options, so a `cpu-value` of `75` targets 75 percent of the reserved CPU. A metric type of `AverageValue` treats the value as an absolute amount per replica.

You can set both the CPU and the memory trigger on one environment.

```
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-cluster-env}} \
    --option-settings \
        Namespace=aws:elasticbeanstalk:eks:environment:autoscaling:trigger,OptionName=cpu-metric-type,Value=Utilization \
        Namespace=aws:elasticbeanstalk:eks:environment:autoscaling:trigger,OptionName=cpu-value,Value=75
```

## Scaling on a schedule
<a name="configuring-cluster-scaling-schedule"></a>

To run a chosen number of replicas during a recurring time window, set `scaler-type` to `cron` and describe the window in `scaler-metadata`, which takes a JSON object with four fields.


| Field | Description | 
| --- | --- | 
| timezone | The time zone that the window is expressed in, as an IANA time zone name such as UTC, America/New\_York, or Asia/Tokyo. | 
| start | When the window opens, as a five field cron expression (minute, hour, day of month, month, day of week). | 
| end | When the window closes, in the same format. | 
| desiredReplicas | The number of replicas to run while the window is open. Choose a value within your min-replica and max-replica bounds. | 

Outside the window, the environment returns to `min-replica`. The following example runs five replicas during weekday working hours in UTC:

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

An environment takes one schedule. To vary the replica count across several windows, such as a different weekend schedule, combine the schedule with another trigger as described in [Combining triggers](#configuring-cluster-scaling-combining).

**Note**  
The settings go in a file because a `scaler-metadata` value is itself a JSON document. For the forms that the AWS CLI accepts for `--option-settings`, see [Using shorthand syntax in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html).

## Scaling on a metric from your own endpoint
<a name="configuring-cluster-scaling-metrics-api"></a>

To scale on a value that your own service reports, such as a queue depth or a count of in-flight jobs, set `scaler-type` to `metrics-api`. Elastic Beanstalk reads an HTTP endpoint that you supply and scales on the number it finds there. Describe the endpoint in `scaler-metadata`.


| Field | Description | 
| --- | --- | 
| url | The endpoint that Elastic Beanstalk reads. | 
| valueLocation | Where the number sits in the JSON response, as a dotted path. For a response body of {"data":{"result":[{"value":"500"}]}}, the location is data.result.0.value. | 
| targetValue | The amount that one replica is expected to handle. | 

Elastic Beanstalk divides the reported value by `targetValue` and rounds up to get the replica count, then holds that count within your replica bounds. With a `targetValue` of `100`, a reported value of `500` asks for five replicas.

You can point the trigger at your own environment. Because the environment's URL is only known after it launches, set `url` in an update rather than at create time.

The following example scales on a depth that the application reports, with one replica for every 100 units of reported work:

```
$ cat trigger.json
[
  {
    "Namespace": "aws:elasticbeanstalk:eks:environment:autoscaling:trigger",
    "OptionName": "scaler-type",
    "Value": "metrics-api"
  },
  {
    "Namespace": "aws:elasticbeanstalk:eks:environment:autoscaling:trigger",
    "OptionName": "scaler-metadata",
    "Value": "{\"url\":\"https://{{my-service.example.com}}/queue-depth\",\"valueLocation\":\"data.result.0.value\",\"targetValue\":\"100\"}"
  }
]
$ aws elasticbeanstalk update-environment \
    --environment-name {{my-cluster-env}} \
    --option-settings file://trigger.json
```

### Authenticating to the endpoint
<a name="configuring-cluster-scaling-metrics-api-auth"></a>

If your endpoint requires credentials, store them in an AWS Secrets Manager secret and set `scaler-auth-secret` to the secret's ARN. You can set it only when `scaler-type` is `metrics-api`. Set `scaler-auth-mode` to the scheme that your endpoint expects. The secret's value is a JSON object whose keys depend on that scheme.


| Authentication mode | Required keys in the secret | 
| --- | --- | 
| bearer, the default | token | 
| basic | username and password | 
| apiKey | apiKey | 
| tls | ca, cert, and key | 

Set the environment's `application-role` option as well. Elastic Beanstalk mounts the credentials into your replicas through the environment's Pod Identity, which exists only when `application-role` is set. Without it, the mount fails and the replicas don't start. A schedule trigger doesn't require it, and neither does a metrics endpoint that needs no credentials.

The environment's *application role* reads the secret, so grant it both `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` on the secret's ARN. Elastic Beanstalk refreshes the credentials on a schedule and the refresh checks the secret's current version, so an environment that is granted only `GetSecretValue` starts normally and then fails on every later refresh. For the roles that a Beanstalk Cluster environment uses, see [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md).

This secret is separate from the `secrets` option that supplies secrets to your application. Changing the value of `scaler-auth-secret` replaces the environment's replicas, because the credentials are mounted when a replica starts.

## Combining triggers
<a name="configuring-cluster-scaling-combining"></a>

An environment takes one event-driven trigger, either a schedule or an endpoint metric, because `scaler-type` and `scaler-metadata` describe a single trigger. It can carry the CPU and memory triggers alongside that one.

Two behaviors are worth knowing before you combine them:
+ Setting `scaler-type` replaces the default CPU scaling described in [How Elastic Beanstalk decides when to scale](#configuring-cluster-scaling-triggers). To keep scaling on CPU as well, set `cpu-metric-type` and `cpu-value` explicitly.
+ When more than one trigger applies, the highest replica count wins. A schedule that asks for five replicas and a CPU trigger that asks for three produce five.

Pairing a schedule with a CPU trigger is a common combination: the schedule carries the replica count you expect during busy hours, and the CPU trigger stays available the rest of the time.

## Watching the environment scale
<a name="configuring-cluster-scaling-watching"></a>

The environment's monitoring page in the Elastic Beanstalk console shows an **Application replica count** graph, which reports the replicas that the environment is running over time. Comparing it with the **CPU (cores)** and **Memory (bytes)** graphs shows whether a trigger is holding its target. For the health and metrics that a Beanstalk Cluster environment reports, see [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md).

Elastic Beanstalk records an environment event when it changes a scaling setting, so the environment's event stream shows when a scaling change took effect.