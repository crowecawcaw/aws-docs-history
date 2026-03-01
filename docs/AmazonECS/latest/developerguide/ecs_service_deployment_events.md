# Amazon ECS service deployment state change events

Amazon ECS sends service deployment change state events with the detail type
**ECS Deployment State Change**. The following is an event
pattern that is used to create an EventBridge rule for Amazon ECS service deployment state
change events. For more information about creating an EventBridge rule, see [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User Guide_.

```
{
    "source": [
        "aws.ecs"
    ],
    "detail-type": [
        "ECS Deployment State Change"
    ]
}
```

Amazon ECS sends events with `INFO` and `ERROR` event types. For
more information, see [Amazon ECS service action events](ecs_service_events.md "ecs_service_events.md")

The following are the service deployment state change events.

`SERVICE_DEPLOYMENT_IN_PROGRESS`

The service deployment is in progress. This event is sent for both
initial deployments and rollback deployments.

`SERVICE_DEPLOYMENT_COMPLETED`

The service deployment has completed. This event is sent once a
service reaches a steady state after a deployment.

`SERVICE_DEPLOYMENT_FAILED`

The service deployment has failed. This event is sent for services
with deployment circuit breaker logic turned on.

###### Example service deployment in progress event

Service deployment in progress events are delivered when both an initial and a
rollback deployment is started. The difference between the two is in the
`reason` field. For more information about EventBridge parameters, see
[AWS service event metadata;](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the
_Amazon EventBridge User Guide_.

The following shows an example output for an initial deployment
starting.

```
{
   "version": "0",
   "id": "ddca6449-b258-46c0-8653-e0e3a6EXAMPLE",
   "detail-type": "ECS Deployment State Change",
   "source": "aws.ecs",
   "account": "111122223333",
   "time": "2020-05-23T12:31:14Z",
   "region": "us-west-2",
   "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
   ],
   "detail": {
        "eventType": "INFO",
        "eventName": "SERVICE_DEPLOYMENT_IN_PROGRESS",
        "deploymentId": "ecs-svc/`123`",
        "updatedAt": "2020-05-23T11:11:11Z",
        "reason": "ECS deployment `deploymentId` in progress."
   }
}
```

The following shows an example output for a rollback deployment starting. The
`reason` field provides the ID of the deployment the service is
rolling back to.

```
{
   "version": "0",
   "id": "ddca6449-b258-46c0-8653-e0e3aEXAMPLE",
   "detail-type": "ECS Deployment State Change",
   "source": "aws.ecs",
   "account": "111122223333",
   "time": "2020-05-23T12:31:14Z",
   "region": "us-west-2",
   "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
   ],
   "detail": {
        "eventType": "INFO",
        "eventName": "SERVICE_DEPLOYMENT_IN_PROGRESS",
        "deploymentId": "ecs-svc/123",
        "updatedAt": "2020-05-23T11:11:11Z",
        "reason": "ECS deployment circuit breaker: rolling back to deploymentId `deploymentID`."
   }
}
```

###### Example service deployment completed event

Service deployment completed state events are delivered in the following
format. For more information, see [Deploy Amazon ECS services by replacing tasks](deployment-type-ecs.md "deployment-type-ecs.md").

```
{
   "version": "0",
   "id": "ddca6449-b258-46c0-8653-e0e3aEXAMPLE",
   "detail-type": "ECS Deployment State Change",
   "source": "aws.ecs",
   "account": "111122223333",
   "time": "2020-05-23T12:31:14Z",
   "region": "us-west-2",
   "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
   ],
   "detail": {
        "eventType": "INFO",
        "eventName": "SERVICE_DEPLOYMENT_COMPLETED",
        "deploymentId": "ecs-svc/123",
        "updatedAt": "2020-05-23T11:11:11Z",
        "reason": "ECS deployment `deploymentID` completed."
   }
}
```

###### Example service deployment failed event

Service deployment failed state events are delivered in the following format.
A service deployment failed state event will only be sent for services that have
deployment circuit breaker logic turned on. For more information, see [Deploy Amazon ECS services by replacing tasks](deployment-type-ecs.md "deployment-type-ecs.md").

```
{
   "version": "0",
   "id": "ddca6449-b258-46c0-8653-e0e3aEXAMPLE",
   "detail-type": "ECS Deployment State Change",
   "source": "aws.ecs",
   "account": "111122223333",
   "time": "2020-05-23T12:31:14Z",
   "region": "us-west-2",
   "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
   ],
   "detail": {
        "eventType": "ERROR",
        "eventName": "SERVICE_DEPLOYMENT_FAILED",
        "deploymentId": "ecs-svc/123",
        "updatedAt": "2020-05-23T11:11:11Z",
        "reason": "ECS deployment circuit breaker: task failed to start."
   }
}
```
