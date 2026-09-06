# Creating and managing daemons

After you register a daemon task definition, create a daemon to deploy it across your
Amazon ECS Managed Instances capacity providers. Amazon ECS automatically places one daemon task on every
Amazon EC2 instance in the associated capacity providers and manages the daemon lifecycle.

## Prerequisites

Before you create a daemon, verify that you have the following:

- An Amazon ECS cluster.
- One or more Amazon ECS Managed Instances capacity providers associated with the
  cluster.
- A registered daemon task definition.

## Creating a daemon

### AWS Management Console

1. Open the Amazon ECS console. In the navigation pane, choose
   **Clusters**, then select your cluster.
2. Choose the **Daemons** tab, then choose
   **Create**.
3. For **Daemon task definition family**, select your daemon
   task definition from the dropdown.
4. For **Daemon task definition revision**, select the
   revision to use. Leave blank to use the latest revision.
5. For **Daemon name**, enter a unique name. The name can
   contain up to 255 alphanumeric characters, hyphens, and
   underscores.
6. For **Capacity providers**, select one or more
   Amazon ECS Managed Instances capacity providers. These determine which instances run
   your daemon tasks.
7. (Optional) Configure deployment settings:

   - **Drain percentage** - Percentage of
     instances to drain simultaneously during updates. Default:
     `25`.
   - **Use CloudWatch alarm(s)** - Turn on
     to monitor deployment health and automatically roll back if alarms
     trigger.
   - **Bake time** - The number of
     minutes that Amazon ECS waits after it updates all instances to the new
     daemon revision before it completes the deployment. During this
     period, Amazon ECS monitors CloudWatch alarms and automatically rolls back
     the deployment if any alarm triggers. Default:
     `0`.

8. (Optional) For **Critical**, choose whether the daemon is
   critical to instance health.
9. (Optional) Add tags.
10. (Optional) Turn on **Enable ECS Exec** to run
    interactive commands in your daemon containers for
    troubleshooting.
11. Review your configuration and choose
    **Create**.

### AWS CLI

Create a JSON file with your daemon configuration and run the
`create-daemon` command.

The following is an example JSON file:

```
{
    "clusterArn": "arn:aws:ecs:`us-east-1`:`123456789012`:cluster/`my-daemon-cluster`",
    "daemonName": "`my-monitoring-daemon`",
    "daemonTaskDefinitionArn": "arn:aws:ecs:`us-east-1`:`123456789012`:daemon-task-definition/`my-daemon-task`:1",
    "capacityProviderArns": [
        "arn:aws:ecs:`us-east-1`:`123456789012`:capacity-provider/`my-daemon-capacity-provider`"
    ],
    "critical": true
}
```

Run the following command to create the daemon:

```
aws ecs create-daemon --cli-input-json file://create-daemon.json
```

**Required fields**

- `daemonName` - A unique name for the daemon.
- `clusterArn` - The ARN of the cluster.
- `daemonTaskDefinitionArn` - The ARN of the daemon task
  definition.
- `capacityProviderArns` - An array of Amazon ECS Managed Instances
  capacity provider ARNs.

**Optional fields**

- `deploymentConfiguration` - A
  `DaemonDeploymentConfiguration` object to customize
  deployment behavior.
- `critical` - Whether the daemon is critical to instance
  health.
- `tags` - Key-value pairs for tagging.
- `propagateTags` - Tag propagation setting.
- `clientToken` - An idempotency token.

## Verifying daemon deployment

After you create a daemon, verify its status by using the AWS Management Console or the
AWS CLI.

### AWS Management Console

1. Open the Amazon ECS console. In the navigation pane, choose
   **Clusters**, then select your cluster.
2. Choose the **Daemons** tab.
3. Verify that your daemon shows **Active**
   status.
4. Choose the **Tasks** tab to confirm that one daemon
   task runs on each container instance.

### AWS CLI

Run the following commands to verify daemon status:

```
aws ecs list-daemons \
    --cluster-arn arn:aws:ecs:`us-east-1`:`123456789012`:cluster/`my-daemon-cluster`
```

```
aws ecs describe-daemons \
    --daemon-arn arn:aws:ecs:`us-east-1`:`123456789012`:daemon/`my-daemon-cluster`/`my-monitoring-daemon`
```

## Updating a daemon

To update a daemon with a new task definition revision or to add capacity providers,
use the AWS Management Console or the AWS CLI. This triggers a rolling deployment across all
instances.

### AWS Management Console

1. Open the Amazon ECS console. In the navigation pane, choose
   **Clusters**, then select your cluster.
2. Choose the **Daemons** tab, then select the daemon
   you want to update.
3. Choose **Update**.
4. For **Daemon task definition revision**, select the
   new revision.
5. (Optional) Update the capacity providers or deployment
   settings.
6. Choose **Update** to start the rolling
   deployment.

### AWS CLI

Run the `update-daemon` command:

```
aws ecs update-daemon \
    --daemon-arn arn:aws:ecs:`us-east-1`:`123456789012`:daemon/`my-daemon-cluster`/`my-monitoring-daemon` \
    --daemon-task-definition-arn arn:aws:ecs:`us-east-1`:`123456789012`:daemon-task-definition/`my-daemon-task`:2 \
    --capacity-provider-arns arn:aws:ecs:`us-east-1`:`123456789012`:capacity-provider/`my-daemon-capacity-provider` \
    --no-critical
```

###### Important

When you provide daemon configuration settings in an
`UpdateDaemon` request, Amazon ECS uses your specified settings
instead of the defaults. Daemon configuration settings, including tags and the
enable execute command flag, are not persisted between updates. Each call to
`UpdateDaemon` must include the full set of configuration
settings you want applied. Any settings omitted from the request revert to
their default values. The `critical` parameter defaults to
`true`, so if you omit it from an `UpdateDaemon`
request, the daemon becomes critical.

## Deleting a daemon

To delete a daemon, use the AWS Management Console or the AWS CLI. Wait for all daemon tasks to
stop before you delete the capacity provider or cluster.

### AWS Management Console

1. Open the Amazon ECS console. In the navigation pane, choose
   **Clusters**, then select your cluster.
2. Choose the **Daemons** tab, then select the daemon
   you want to delete.
3. Choose **Delete**.
4. In the confirmation dialog, choose **Delete** to
   confirm.

### AWS CLI

Run the `delete-daemon` command:

```
aws ecs delete-daemon \
    --daemon-arn arn:aws:ecs:`us-east-1`:`123456789012`:daemon/`my-daemon-cluster`/`my-monitoring-daemon`
```
