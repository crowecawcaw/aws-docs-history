

# Viewing deployment logs for an Elastic Beanstalk environment
<a name="environments-deployment-logs"></a>

Elastic Beanstalk generates a deployment log for each deployment to your environment. The deployment log provides a consolidated view of what happened during a deployment, so that you can diagnose a failure without collecting several logs yourself. What the log contains, and when it becomes available, depends on whether the environment is a Beanstalk Standard environment or a Beanstalk Cluster environment.

With Beanstalk Standard, deployment logs are written to each instance locally. For deployments triggered through the console, CLI, API, or managed updates, one instance continuously uploads its log to Amazon S3 during the deployment. The Elastic Beanstalk console reads the log from Amazon S3, so you can monitor progress without connecting to the instance.

Standard deployment logs are designed to be concise. On success, the log shows only summary messages (for example, which commands ran and completed). On failure, the log includes up to 50 lines of output from the failed step, so you can see the error without sifting through verbose output.

With Beanstalk Cluster, Elastic Beanstalk collects the deployment log after the operation finishes. It gathers the container logs of every pod in the environment, together with the Kubernetes events for the environment's namespace, and uploads them as a single zip file to your environment's Amazon S3 storage bucket. The Elastic Beanstalk console reads the zip file from Amazon S3 and displays its contents, so you can read it without connecting to your cluster. Availability doesn't depend on a platform version, and Elastic Beanstalk doesn't write a deployment log file to your nodes.

**Note**  
For Beanstalk Standard environments, deployment logs are available on [Amazon Linux 2](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-03-11-al2.html) and [Amazon Linux 2023](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-03-11-al2023.html) platform versions released on or after March 11, 2026, and on [Windows](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-04-22-windows.html) platform versions released on or after April 22, 2026.

## Supported operations
<a name="environments-deployment-logs.supported-operations"></a>

For Beanstalk Standard environments, deployment logs are generated for the following operations:
+ **Application deployments** – Deploying a new application version to your environment.
+ **Configuration updates** – Changing environment configuration settings that are applied to existing instances, and updates that add new instances to the environment.
+ **Environment creation** – The initial deployment when you create a new environment.
+ **Restart app server** – Restarting the application server on your instances.
+ **Managed platform updates** – Platform updates that Elastic Beanstalk applies automatically during a scheduled maintenance window.

Operations that don't modify application or configuration state on instances, such as requesting logs, swapping CNAMEs, or updating tags, do not generate deployment logs.

For Beanstalk Cluster environments, deployment logs are generated for environment creation, application deployments, configuration updates, restart app server, and terminate environment. Terminating an environment produces a deployment log, which it doesn't for Beanstalk Standard. Managed platform updates don't apply, because a Beanstalk Cluster environment runs container images rather than a platform version.

Elastic Beanstalk collects a Beanstalk Cluster environment's deployment log after the deploy step. If an operation fails before that step, for example while building the container image, creating the cluster, provisioning resources, or generating the Kubernetes specification, there is no deployment log, and the environment's events describe what happened. For more information, see [Viewing an Elastic Beanstalk environment's event stream](using-features.events.md).

## Deployment log contents
<a name="environments-deployment-logs.contents"></a>

For Beanstalk Standard environments, a deployment log captures the following information during a deployment:
+ **Deployment lifecycle** – Start and completion messages for each deployment phase, such as `Starting Application deployment` and `Completed Application deployment`.
+ **.ebextensions output** – On success, the names of commands that ran. On failure, the last 50 lines of `cfn-init` output to help diagnose the issue.
+ **Platform hooks output** – On success, the names of hook scripts that ran. On failure, the last 50 lines of hook output.
+ **Dependency installation** – Output from package managers such as **npm install**, **pip install**, **composer install**, and **bundle install**. On success, only a completion message is logged. On failure, the last 50 lines of output are included.
+ **Build output** – Output from build commands such as **docker build**, **go build**, and Java builds. On failure, the last 50 lines of output are included.
+ **Application startup output** – Initial output from your application after it starts. The source depends on your platform:
  + *Docker* – Container logs from **docker logs** or **docker compose logs**
  + *Java SE, Go, Node.js, Python, Ruby, .NET* – Process stdout logs
  + *Tomcat* – Catalina log output
  + *PHP* – PHP-FPM master and pool error logs
  + *ECS* – Container logs from each task container
**Note**  
Application output is captured starting 2 seconds after the application starts. Only the initial startup messages are included – if your application takes longer to produce output, it won't appear in the deployment log. To see full application logs, request bundle logs or connect to the instance directly. For more information, see [View instance logs](using-features.logging.md).

When a deployment step fails, the log marks it with `[ERROR]` and includes up to 50 lines of output from the failed step. If the deployment log does not contain enough detail, you can retrieve the full instance logs (including `eb-engine.log`, `eb-hooks.log`, and application logs) from the **Logs** tab. For more information, see [Viewing logs from Amazon EC2 instances in your Elastic Beanstalk environment](using-features.logging.md).

### Deployment log contents for Beanstalk Cluster environments
<a name="environments-deployment-logs.contents-cluster"></a>

For a Beanstalk Cluster environment, the deployment log is a zip file. It holds an environment-wide events file and one file per pod, under a `1-environment/` directory:

```
1-environment/
  _k8Events.txt
  {{pod-name}}.txt
```

`_k8Events.txt` holds the Kubernetes events in the environment's namespace that aren't tied to a single pod, such as scheduling, volume, scaling, and load balancer events. The leading underscore sorts it first.

Each `{{pod-name}}.txt` begins with an `=====EVENTS=====` block holding that pod's events, oldest first, followed by a `=====LOGS=====` block holding the logs of each container in the pod. Init containers appear as their own container blocks, so when an init container fails, an empty log for the application container is expected rather than a second problem.

For a container that is restarting, that pod's `=====EVENTS=====` block names the reason (for example, `BackOff`), and the `=====LOGS=====` block holds the container's log as of the time of collection. The log of an earlier instance of the container isn't included.

Each container's log is capped at 5 MiB, with no line limit. A log that reaches the cap is marked as truncated. Apart from that cap, nothing is removed from the log, whether the operation succeeds or fails. If Elastic Beanstalk can't read one container's logs, collection continues and that container's block records the error.

Dependency installation and build output aren't in a Beanstalk Cluster environment's deployment log. Those happen when Elastic Beanstalk builds your container image. For more information, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

## Viewing deployment logs in the console
<a name="environments-deployment-logs.console"></a>

The Elastic Beanstalk console provides a **Deployments** tab on the environment dashboard where you can view your deployment history and logs. The deployment history shows deployments from the last 42 days (6 weeks).

### Viewing deployment history
<a name="environments-deployment-logs.console.history"></a>

**To view deployment history**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the environment dashboard, choose the **Deployments** tab.

   The Deployments tab shows a table of deployments for the environment. Each row includes the following information:
   + **Request ID** – The unique identifier for the deployment.
   + **Status** – *Succeeded*, *Failed*, or *In progress*.
   + **Type** – The deployment type, such as *Environment Creation*, *Application Deployment*, *Configuration Update*, *Managed Platform Update*, *Restart App Server*, *Rebuild Environment*, *Restore Environment*, *Swap Environment Domain*, or *Terminate Environment*.
   + **Policy** – The deployment policy, such as *All at once*, *Rolling*, *Rolling with additional batch*, *Immutable*, or *Traffic splitting*.
   + **Start Time** – When the deployment began.
   + **Duration** – How long the deployment took to complete.

When a deployment is in progress, the tab automatically polls for updates. You can also choose the refresh button to manually reload the list.

### Viewing deployment details and logs
<a name="environments-deployment-logs.console.detail"></a>

**To view deployment details**

1. On the **Deployments** tab, choose the **Request ID** link for the deployment you want to inspect.

1. The deployment detail page shows a summary section with the request ID, status, deployment type, start time, duration, and deployment policy. The deployment policy (for example, *All at once*, *Rolling*, *Rolling with additional batch*, *Immutable*, or *Traffic splitting*) is shown when it can be determined from the deployment events.

1. Below the summary, choose one of the following tabs:
   + **Events** – A timeline of events related to this deployment, filtered to show only events for the selected deployment.
   + **Deployment Logs** – The consolidated deployment log from the instance. You can search, filter by log level, and download the log file.

For in-progress deployments in a Beanstalk Standard environment, the logs tab automatically refreshes to show new log entries as they are written. After a deployment completes, the console fetches the final log state to ensure you see the complete output.

For a Beanstalk Cluster environment, the deployment log appears after the operation completes, so the logs tab doesn't refresh while the operation runs. The environment-wide events file is shown first, followed by the per-pod files. If the compressed zip file is larger than 5 MiB, the console asks you to download it from Amazon S3 rather than displaying it. That limit applies to the archive as a whole, not to any single container's log.

**Important**  
Viewing deployment logs in the console requires `s3:GetObject` permission on the environment's Amazon S3 storage bucket (`elasticbeanstalk-{{region}}-{{account-id}}`). If your IAM policy does not include this permission, the deployment history and events will still be available, but the logs tab will show an error.

## Where deployment logs are stored
<a name="environments-deployment-logs.instance"></a>

### Deployment log files on Beanstalk Standard instances
<a name="environments-deployment-logs.instance.standard"></a>

Deployment logs are written to the `/var/log/deployments/` directory on each instance. The log filename depends on how the deployment was triggered:
+ **Workflow-controlled deployments** (triggered through the console, CLI, or API) – `eb-deployment-{{request-id}}.log`, where {{request-id}} is the unique deployment request ID.
+ **Self-startup deployments** (instance launch) – `eb-deployment-{{timestamp}}-{{instance-id}}.log`, where {{timestamp}} is in UTC format (for example, `20260317T151315Z`) and {{instance-id}} is the Amazon EC2 instance ID.

Elastic Beanstalk automatically rotates these files, keeping the 50 most recent deployment logs on each instance.

For workflow-controlled deployments, the log is uploaded to Amazon S3 at the following path:

```
s3://{{elasticbeanstalk-region-account-id}}/resources/environments/logs/deployments/{{environment-id}}/{{log-filename}}
```

For self-startup deployments, the log is uploaded to Amazon S3 under a `selfstartup/` subdirectory:

```
s3://{{elasticbeanstalk-region-account-id}}/resources/environments/logs/deployments/{{environment-id}}/selfstartup/{{log-filename}}
```

For workflow-controlled deployments, the first instance to begin uploading claims the role for the entire deployment. That instance uploads its log to Amazon S3 for the duration of the deployment. For self-startup deployments, each instance uploads its own log independently. All instances still write deployment logs locally.

**Important**  
Uploading deployment logs to Amazon S3 requires `s3:PutObject` permission on the environment's Amazon S3 storage bucket in the instance profile, and the VPC configuration must allow connectivity to Amazon S3.

Deployment log uploads are capped at 1 MB per file. If a deployment log exceeds this size, the uploaded version is truncated with a message indicating that the full log is available on the instance.

#### Disabling S3 log uploads
<a name="environments-deployment-logs.disable"></a>

For Beanstalk Standard environments, to prevent deployment logs from being uploaded to Amazon S3, set the following environment property on your environment:

```
option_settings:
  - namespace:  aws:elasticbeanstalk:application:environment
    option_name:  EB_DEPLOYMENT_LOG_S3_DISABLED
    value:  true
```

When this environment property is set, deployment logs are still written locally to `/var/log/deployments/` on each instance, but they are not uploaded to Amazon S3 and will not be available in the console **Deployments** tab. You can also set this property in the **Configuration** page under **Software**, or by using the EB CLI or AWS CLI.

The `EB_DEPLOYMENT_LOG_S3_DISABLED` property is read on your instances, so it has no effect on a Beanstalk Cluster environment. There is currently no way to prevent Elastic Beanstalk from uploading a Beanstalk Cluster environment's deployment log.

### Deployment log files for Beanstalk Cluster environments
<a name="environments-deployment-logs.cluster-storage"></a>

For a Beanstalk Cluster environment, Elastic Beanstalk uploads the deployment log to your environment's Amazon S3 storage bucket at the following path:

```
s3://{{elasticbeanstalk-region-account-id}}/resources/environments/logs/deployments/{{environment-id}}/deployment-{{environment-name}}-{{request-id}}.zip
```

Elastic Beanstalk performs the upload itself, using the environment's operation role, so no instance profile permission is involved and nothing needs to reach Amazon S3 from your nodes.

The upload is best effort. If it doesn't succeed, the operation still completes, no environment event is generated, and the console reports the deployment log as unavailable.