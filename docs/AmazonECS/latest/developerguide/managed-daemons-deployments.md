

# Daemon deployments
<a name="managed-daemons-deployments"></a>

When you create or update a daemon, Amazon ECS performs a rolling deployment to run daemon tasks on all instances in the associated capacity providers. This section describes how daemon deployments work and how to configure deployment behavior.

## How daemon deployments work
<a name="managed-daemons-deploy-how"></a>

A daemon deployment follows a drain-provision-replace pattern. When you create a daemon on a capacity provider with existing instances, or update a daemon to a new task definition revision, Amazon ECS drains a batch of instances, provisions replacement instances with the updated daemon, and replaces application tasks automatically. This process repeats until all instances run the new daemon revision.

The deployment lifecycle transitions through the following states:

1. `PENDING` - Amazon ECS has created the deployment and is preparing to begin.

1. `IN_PROGRESS` - Amazon ECS is actively draining instances and provisioning replacements.

1. `SUCCESSFUL` - All instances are running the target daemon revision.

1. `STOPPED` - Amazon ECS has stopped the deployment because it failed or was replaced by a new deployment. The daemon may be in a mixed state where some instances run the old revision and others run the new revision.

Amazon ECS automatically rolls back to the previous daemon revision if the deployment circuit breaker detects failures or if a CloudWatch alarm triggers during the deployment.

During a deployment, a non-critical daemon task failure doesn't drain or replace the instance, so the instance stays active and continues to run your application tasks. Daemon task launch failures still count toward the deployment circuit breaker, which can roll back an unstable target revision.

## Deployment configuration parameters
<a name="managed-daemons-deploy-config"></a>

You can customize deployment behavior by using the `deploymentConfiguration` parameter when you create or update a daemon.
+ `drainPercent` (1.0–100.0) - The percentage of instances to drain simultaneously during the deployment. Higher values speed up deployments but may temporarily reduce available capacity. For example, a value of `20.0` drains 20% of instances at a time. If not specified, the default is `25.0`.
+ `alarms` (`DaemonAlarmConfiguration`) - CloudWatch alarms to monitor during the deployment. Amazon ECS evaluates the specified alarms during the deployment and automatically rolls back if any alarm enters the `ALARM` state. Amazon ECS ignores alarms that are already in the `ALARM` state when the deployment begins.
+ `bakeTimeInMinutes` (0–1440) - The number of minutes that Amazon ECS waits after it updates all instances to the new daemon revision before it completes the deployment. During this period, Amazon ECS monitors CloudWatch alarms and automatically rolls back the deployment if any alarm triggers. If not specified, the default is `0`.

**Example with deployment configuration:**

```
aws ecs create-daemon \
    --cluster-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:cluster/{{my-daemon-cluster}} \
    --daemon-name {{my-monitoring-daemon}} \
    --daemon-task-definition-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-task-definition/{{my-daemon-task}}:1 \
    --capacity-provider-arns arn:aws:ecs:{{us-east-1}}:{{123456789012}}:capacity-provider/{{my-daemon-capacity-provider}} \
    --deployment-configuration '{"drainPercent":20.0,"bakeTimeInMinutes":5}'
```

## Monitoring deployments
<a name="managed-daemons-deploy-monitor"></a>

Track deployment progress by using the following commands:

```
aws ecs list-daemon-deployments \
    --daemon-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon/{{my-daemon-cluster}}/{{my-monitoring-daemon}}
```

```
aws ecs describe-daemon-deployments \
    --daemon-deployment-arns arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-deployment/{{my-daemon-cluster}}/{{abc123}}
```

The `describe-daemon-deployments` response includes the deployment status, the target daemon revision, and the `totalRunningInstanceCount` field that indicates how many instances run the target daemon.

## Daemon deployment scenarios
<a name="managed-daemons-deploy-scenarios"></a>

This section walks through common deployment scenarios for Managed Daemons.
+ [Deploy a daemon on an empty capacity provider](#managed-daemons-scenario-empty)
+ [Deploy a daemon on a capacity provider with existing instances](#managed-daemons-scenario-existing)
+ [Add a capacity provider to an existing daemon](#managed-daemons-scenario-add-cp)
+ [Update a daemon to a new revision](#managed-daemons-scenario-update)

### Deploy a daemon on an empty capacity provider
<a name="managed-daemons-scenario-empty"></a>

In this scenario, you deploy a daemon on a capacity provider with no existing instances. Instances launch when you schedule application tasks.

**Prerequisites:** A cluster and a Amazon ECS Managed Instances capacity provider with no running instances.

1. Register your daemon task definition.

1. Create the daemon. Amazon ECS completes the creation immediately even though no instances exist yet.

   ```
   aws ecs create-daemon \
       --cluster-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:cluster/{{my-daemon-cluster}} \
       --daemon-name {{my-monitoring-daemon}} \
       --daemon-task-definition-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-task-definition/{{my-daemon-task}}:1 \
       --capacity-provider-arns arn:aws:ecs:{{us-east-1}}:{{123456789012}}:capacity-provider/{{my-daemon-capacity-provider}}
   ```

1. Create a service that uses the same capacity provider. When Amazon ECS provisions an instance for the service, it starts the daemon task first, then transitions the application task to `RUNNING`.

   ```
   aws ecs create-service \
       --cluster {{my-daemon-cluster}} \
       --service-name {{my-app-service}} \
       --task-definition {{my-app-task}} \
       --desired-count 2 \
       --capacity-provider-strategy capacityProvider={{my-daemon-capacity-provider}},weight=1
   ```

1. Verify that the daemon task is running on each instance by using the `describe-daemons` command or by checking the **Daemons** tab in the console.

**Note**  
The daemon deployment may remain in `PENDING` state briefly while Amazon ECS provisions instances and starts daemon tasks. Wait for the deployment to reach `SUCCESSFUL` before verifying daemon task placement.

### Deploy a daemon on a capacity provider with existing instances
<a name="managed-daemons-scenario-existing"></a>

In this scenario, you deploy a daemon on a capacity provider that already has running instances and application tasks.

**Prerequisites:** A cluster with a Amazon ECS Managed Instances capacity provider that has running instances.

1. Register your daemon task definition.

1. Create the daemon. Amazon ECS starts a rolling deployment to place daemon tasks on all existing instances.

   ```
   aws ecs create-daemon \
       --cluster-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:cluster/{{my-daemon-cluster}} \
       --daemon-name {{my-monitoring-daemon}} \
       --daemon-task-definition-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-task-definition/{{my-daemon-task}}:1 \
       --capacity-provider-arns arn:aws:ecs:{{us-east-1}}:{{123456789012}}:capacity-provider/{{my-daemon-capacity-provider}} \
       --deployment-configuration '{"drainPercent":25.0,"bakeTimeInMinutes":3}'
   ```

   Amazon ECS drains a batch of existing instances (based on the `drainPercent`), provisions replacement instances with the daemon, and replaces application tasks. This process repeats until all instances run the daemon.

1. Monitor the deployment progress:

   ```
   aws ecs list-daemon-deployments \
       --daemon-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon/{{my-daemon-cluster}}/{{my-monitoring-daemon}}
   ```

### Add a capacity provider to an existing daemon
<a name="managed-daemons-scenario-add-cp"></a>

In this scenario, you add a second capacity provider to an existing daemon. The daemon automatically deploys to instances in the new capacity provider.

**Prerequisites:** A daemon running on a first capacity provider, and a second capacity provider created and associated with the cluster.

1. Update the daemon to include both capacity providers:

   ```
   aws ecs update-daemon \
       --daemon-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon/{{my-daemon-cluster}}/{{my-monitoring-daemon}} \
       --daemon-task-definition-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-task-definition/{{my-daemon-task}}:1 \
       --capacity-provider-arns \
           arn:aws:ecs:{{us-east-1}}:{{123456789012}}:capacity-provider/{{my-daemon-capacity-provider}} \
           arn:aws:ecs:{{us-east-1}}:{{123456789012}}:capacity-provider/{{my-daemon-capacity-provider-2}}
   ```

1. Monitor the deployment and verify that daemon tasks run on instances in both capacity providers.

### Update a daemon to a new revision
<a name="managed-daemons-scenario-update"></a>

In this scenario, you update an existing daemon to use a new task definition revision.

1. Register a new revision of your daemon task definition with the updated container image or configuration.

1. Update the daemon to use the new revision:

   ```
   aws ecs update-daemon \
       --daemon-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon/{{my-daemon-cluster}}/{{my-monitoring-daemon}} \
       --daemon-task-definition-arn arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-task-definition/{{my-daemon-task}}:2
   ```

   Amazon ECS performs a rolling deployment. It drains instances running the old revision, provisions replacement instances with the new revision, and replaces application tasks automatically. If the circuit breaker detects failures, Amazon ECS rolls back to the previous revision.

1. Monitor the deployment and verify that all instances run the new revision:

   ```
   aws ecs describe-daemon-deployments \
       --daemon-deployment-arns arn:aws:ecs:{{us-east-1}}:{{123456789012}}:daemon-deployment/{{my-daemon-cluster}}/{{deployment-id}}
   ```