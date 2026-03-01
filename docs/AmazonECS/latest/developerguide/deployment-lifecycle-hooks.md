# Lifecycle hooks for Amazon ECS service deployments

When a deployment starts, it goes through lifecycle stages. These stages can be in
states such as IN_PROGRESS or successful. You can use lifecycle hooks, which are Lambda
functions that Amazon ECS runs on your behalf at specified lifecycle stages. The functions
can be either of the following:

- An asynchronous API which validates the health check within 15 minutes.
- A poll API which initiates another asynchronous process which evaluates the
  lifecycle hook completion.
  After the function has finished running, it must return a `hookStatus` for
  the deployment to continue. If a `hookStatus` is not returned, or if the
  function fails, the deployment rolls back. The following are the `hookStatus`
  values:

- `SUCCEEDED` - the deployment continues to the next lifecycle
  stage
- `FAILED` – the deployment rolls back to the last successful
  deployment.
- `IN_PROGRESS` – Amazon ECS runs the function again after a short period
  of time. By default this is a 30 second interval, however this value is customizable by returning a `callBackDelay` alongside the `hookStatus`.
  The following example shows how to return a `hookStatus` with a custom callback delay. In this example, Amazon ECS would retry this hook in 60 seconds instead of the default 30 seconds:

```

{
    "hookStatus": "IN_PROGRESS",
    "callBackDelay": 60
}

```

When a roll back happens, Amazon ECS runs the lifecycle hooks for the following lifecycle
stages:

- PRODUCTION_TRAFFIC_SHIFT
- TEST_TRAFFIC_SHIFT

## Lifecycle payloads

When you configure lifecycle hooks for your ECS service deployments, Amazon ECS invokes these hooks at specific stages of the deployment process. Each lifecycle stage provides a JSON payload with information about the current state of the deployment. This document describes the payload structure for each lifecycle stage.

### Common payload structure

All lifecycle stage payloads include the following common fields:

- `serviceArn` - The Amazon Resource Name (ARN) of the service.
- `targetServiceRevisionArn` - The ARN of the target service revision being deployed.
- `testTrafficWeights` - A map of service revision ARNs to their corresponding test traffic weight percentages.
- `productionTrafficWeights` - A map of service revision ARNs to their corresponding production traffic weight percentages.

### Lifecycle stage payloads

#### RECONCILE_SERVICE

This stage occurs at the beginning of the deployment process when the service is being
reconciled. The following shows an example payload for this lifecycle stage.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892": 100,
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/78652123": 0
  },
  "productionTrafficWeights": {
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892": 100,
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/78652123": 0
  }
}

```

**Expectations at this stage:**

- Primary task set is at 0% scale

#### PRE_SCALE_UP

This stage occurs before the new tasks are scaled up. The following shows an example
payload for this lifecycle stage.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {},
  "productionTrafficWeights": {}
}

```

**Expectations at this stage:**

- The green service revision tasks are at 0% scale

#### POST_SCALE_UP

This stage occurs after the new tasks have been scaled up and are healthy. The
following shows an example payload for this lifecycle stage.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {},
  "productionTrafficWeights": {}
}

```

**Expectations at this stage:**

- The green service revision tasks are at 100% scale
- Tasks in the green service revision are healthy

#### TEST_TRAFFIC_SHIFT

This stage occurs when test traffic is being shifted to the green service revision
tasks.

The following shows an example payload for this lifecycle stage.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892": 100,
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/78652123": 0
  },
  "productionTrafficWeights": {}
}

```

**Expectations at this stage:**

- Test traffic is in the process of moving towards the green service revision
  tasks.

#### POST_TEST_TRAFFIC_SHIFT

This stage occurs after test traffic has been fully shifted to the new tasks.

The following shows an example payload for this lifecycle stage.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {},
  "productionTrafficWeights": {}
}

```

**Expectations at this stage:**

- 100% of test traffic moved towards the green service revision tasks.

#### PRODUCTION_TRAFFIC_SHIFT

This stage occurs when production traffic is being shifted to the green service
revision tasks.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {},
  "productionTrafficWeights": {
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892": 100,
    "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/78652123": 0
  }
}

```

**Expectations at this stage:**

- Production traffic is in the process of moving to the green service revision.

#### POST_PRODUCTION_TRAFFIC_SHIFT

This stage occurs after production traffic has been fully shifted to the green service
revision tasks.

```

{
  "serviceArn": "arn:aws:ecs:us-west-2:1234567890:service/myCluster/myService",
  "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:1234567890:service-revision/myCluster/myService/01275892",
  "testTrafficWeights": {},
  "productionTrafficWeights": {}
}

```

**Expectations at this stage:**

- 100% of production traffic moved towards the green service revision tasks.

### Lifecycle stage categories

Lifecycle stages fall into two categories:

1. **Single invocation stages** - These stages are invoked only once during a service deployment:
   - PRE_SCALE_UP
   - POST_SCALE_UP
   - POST_TEST_TRAFFIC_SHIFT
   - POST_PRODUCTION_TRAFFIC_SHIFT

2. **Recurring invocation stages** - These stages might be
   invoked multiple times during a service deployment, for example when a rollback operation
   happens:
   - TEST_TRAFFIC_SHIFT
   - PRODUCTION_TRAFFIC_SHIFT

### Deployment status during lifecycle hooks

While lifecycle hooks are running, the deployment status will be `IN_PROGRESS` for all lifecycle stages.

| Lifecycle Stage               | Deployment Status |
| ----------------------------- | ----------------- |
| RECONCILE_SERVICE             | IN_PROGRESS       |
| PRE_SCALE_UP                  | IN_PROGRESS       |
| POST_SCALE_UP                 | IN_PROGRESS       |
| TEST_TRAFFIC_SHIFT            | IN_PROGRESS       |
| POST_TEST_TRAFFIC_SHIFT       | IN_PROGRESS       |
| PRODUCTION_TRAFFIC_SHIFT      | IN_PROGRESS       |
| POST_PRODUCTION_TRAFFIC_SHIFT | IN_PROGRESS       |
