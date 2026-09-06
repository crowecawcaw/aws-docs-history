

# Amazon ECS service deployment hook state change events
<a name="ecs_hook_state_change_events"></a>

Amazon ECS sends hook state change events with the detail type **ECS Hook State Change**. These events are emitted when a deployment lifecycle hook changes status. The following is an event pattern that is used to create an EventBridge rule for Amazon ECS hook state change events.

```
{
    "source": [
        "aws.ecs"
    ],
    "detail-type": [
        "ECS Hook State Change"
    ]
}
```

The following are the hook state change events.

`HOOK_IN_PROGRESS`  
A hook is in progress.

`HOOK_AWAITING_ACTION`  
A pause hook has started and requires action to complete. Call `ContinueServiceDeployment` to continue or roll back the deployment.

`HOOK_SUCCEEDED`  
The hook completed successfully. For pause hooks, this means `ContinueServiceDeployment` was called with the `CONTINUE` action.

`HOOK_FAILED`  
The hook failed. For pause hooks, this means `ContinueServiceDeployment` was called with the `ROLLBACK` action.

`HOOK_TIMED_OUT`  
A hook timed out without completing.

**Example hook awaiting action event**  
The following shows an example event when a pause hook starts and is awaiting action.  

```
{
    "version": "0",
    "id": "3329f79b-3dca-07f8-b1c2-5fe99f0b5e87",
    "detail-type": "ECS Hook State Change",
    "source": "aws.ecs",
    "account": "123456789012",
    "time": "2026-03-05T15:54:41Z",
    "region": "us-west-2",
    "resources": ["arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/0EYSiB0qap8xf0N76FsbE"],
    "detail": {
        "eventType": "INFO",
        "eventName": "HOOK_AWAITING_ACTION",
        "hookId": "ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw",
        "hookType": "PAUSE",
        "expiresAt": "2026-03-05T16:04:41Z",
        "lifecycleStage": "POST_TEST_TRAFFIC_SHIFT",
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/my-service",
        "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/0EYSiB0qap8xf0N76FsbE",
        "updatedAt": "2026-03-05T15:54:41.618059641Z"
    }
}
```