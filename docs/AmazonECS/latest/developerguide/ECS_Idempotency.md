

# Ensuring idempotency
<a name="ECS_Idempotency"></a>

When you perform a mutating operation, you might see an exception because of timeouts or server issues occurring after the resources are mutated. This can make it difficult to determine whether the mutation occurred, and could lead to multiple retries. However, if the original operation and the subsequent retries actually performed the mutations you might have applied stacking changes or created more resources than you intended to. Idempotency ensures that an operation mutates resources no more than one time. With an idempotent request, if the original request mutated successfully, any subsequent retries complete successfully without performing any further mutation. 

**Topics**
+ [Idempotency in Amazon ECS](#client-tokens)
+ [Idempotency for RunTask](#RunTaskIdempotency)
+ [Examples](#Run_Task_Idempotency_CLI)
+ [Retry recommendations for idempotent requests](#recommended-actions)

## Idempotency in Amazon ECS
<a name="client-tokens"></a>

The following API actions optionally support idempotency using a *client token*. The corresponding AWS CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string. To make an idempotent API request using one of these actions, specify a client token in the request. You should not reuse the same client token for other API requests. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. 

**Idempotent using a client token**
+ CreateService

  The client token can be up to 36 ASCII characters in the range of 33-126 (inclusive).
+ CreateTaskSet

  The client token can be up to 36 ASCII characters in the range of 33-126 (inclusive).
+ RunTask

  The client token can be up to 64 ASCII characters in the range of 33-126 (inclusive).

**Types of idempotency**
+ cluster – Requests with the same token in the same cluster are idempotent. For example, ClientToken A can only be used as a request parameter one time for `RunTask` requests in Cluster X. `RunTask` requests to other clusters are considered a separate request. Therefore, you can use ClientToken A for a `RunTask` request for cluster Y.

## Idempotency for RunTask
<a name="RunTaskIdempotency"></a>

The `RunTask` API supports idempotency using a client token. A client token is a unique string that you specify when you make an API request. If you retry an API request with the same client token and the same request parameters after it has completed successfully, the result of the original request is returned. If you retry a successful request using the same client token, but one or more of the parameters are different, other than the Region or Availability Zone, the retry fails with a `ConflictException`. If you do not specify your own client token, the AWS SDK and AWS Command Line Interface automatically generate a client token for the request to ensure that it is idempotent. A client token can be any string that includes up to 64 ASCII characters in the range of 33-126 (inclusive).

The time to live (TTL) for the `RunTask` client token is 24 hours. You should not reuse the same client token for different requests. The client token maximum TTL is valid for whichever of the following two values is lower:
+ 24 hours
+ The lifetime of the resource plus one hour

  The lifetime of a resource is the timestamp at which the task was created to the timestamp at which the last status (`lastStatus`) transitioned to `STOPPED`. When you use `RunTask` to launch more than one task, the lifetime of the resource equals the lifetime of the last task that transitioned to `STOPPED`.

### RunTask retry rules and responses
<a name="retry-response"></a>

When you retry a request because you received a 5xx exception, the retried successful response normally includes all of the information that the original request would have returned. Tasks that have been stopped for under an hour only include the task ARN, last status, and desired status.

The following is an example snippet of the response from a retry when there is one running task, one stopped task, and one task that failed to launch.

```
{
  "failures": [
    {
      "arn": "arn:aws:ecs:us-east-1:123456789012:container/4df26bb4-f057-467b-a079-961675296e64",
      "reason": "RESOURCE:MEMORY"
    }
  ],
  "tasks": [
    {
      "desiredStatus": "RUNNING",
      "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/fdf2c302-468c-4e55-b884-5331d816e7fb",
      ...
    },
    {
      "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/fdf2c302-468c-4e55-b884-5331d819999",
      "lastStatus": "STOPPED",
      ...
     }
  ]
}
```

Failures that are over an hour old only include the number of failed tasks.

## Examples
<a name="Run_Task_Idempotency_CLI"></a>

### AWS CLI command examples
<a name="cli-example"></a>

To make an AWS CLI command idempotent, add the `--client-token` option. 

**Example: create-service**  
The following [create-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html#examples) command uses idempotency as it includes a client token.

```
aws ecs create-service \
    --cluster MyCluster \
    --service MyService \
    --task-definition MyTaskDefinition:2 \
    --desired-count 2 \
    --launch-type FARGATE \
    --platform-version LATEST \
    --network-configuration "awsvpcConfiguration={subnets=["subnet-12344321"],securityGroups=["sg-12344321"],assignPublicIp="ENABLED"}" \
    --client-token 550e8400-e29b-41d4-a716-44665544
```

**Example: create-task-set**  
The following [create-task-set](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-task-set.html#examples) command uses idempotency as it includes a client token.

```
aws ecs create-task-set \
    --cluster MyCluster \
    --service MyService \
    --task-definition MyTaskDefinition:2 \
    --network-configuration "awsvpcConfiguration={subnets=["subnet-12344321"],securityGroups=["sg-12344321"]}" \
    --client-token 550e8400-e29b-41d4-a716-44665544
```

**Example: run-task**  
The following [run-task](https://docs.aws.amazon.com/cli/latest/reference/ecs/run-task.html#examples) command uses idempotency as it includes a client token.

```
aws ecs run-task \
    --cluster MyCluster \
    --task-definition MyTaskDefinition:2 \
    --client-token 550e8400-e29b-41d4-a716-446655440000
```

### API request examples
<a name="api-example"></a>

To make an API request idempotent, add the `clientToken` parameter.

**Example: CreateService**  
The following [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) API request uses idempotency as it includes a client token.

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 87
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateService
X-Amz-Date: 20150429T170125Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceName": "MyService",
  "taskDefinition": "MyTaskDefinition:2",
  "desiredCount": 10,
   "capacityProviderStrategy": [ 
      { 
         "base": "number",
         "capacityProvider": "FARGATE",
         "weight": 1
      }
   ],
   "capacityProviderStrategy": [ 
      { 
         "base": "number",
         "capacityProvider": "FARGATE_SPOT",
         "weight": 1
      }
   ],
   "clientToken": "550e8400-e29b-41d4-a716-44665544"
}
```

**Example: CreateTaskSet**  
The following [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html) API request uses idempotency as it includes a client token.

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 87
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateTaskSet
X-Amz-Date: 20150429T170125Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceName": "MyService",
  "taskDefinition": "mytask:1",
  "desiredCount": 1,
   "capacityProviderStrategy": [ 
      { 
         "base": "number",
         "capacityProvider": "FARGATE",
         "weight": 1
      }
   ],
   "capacityProviderStrategy": [ 
      { 
         "base": "number",
         "capacityProvider": "FARGATE_SPOT",
         "weight": 1
      }
   ],
    "clientToken": "550e8400-e29b-41d4-a716-44665544" 
}
```

**Example: RunTask**  
The following [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) API request uses idempotency as it includes a client token.

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: AmazonEC2ContainerServiceV20141113.RunTask
X-Amz-Date: 20161121T215740Z
User-Agent: aws-cli/1.11.13 Python/2.7.12 Darwin/16.1.0 botocore/1.4.66
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "count": 1,
  "taskDefinition": "mytask:1",
  "clientToken": "550e8400-e29b-41d4-a716-446655440000" 
}
```

## Retry recommendations for idempotent requests
<a name="recommended-actions"></a>

The following table shows some common responses that you might get for idempotent API requests, and provides retry recommendations.


| Response | Recommendation | Comments | 
| --- | --- | --- | 
| 200 (OK) | Do not retry | The original request completed successfully. Any subsequent retries return successfully. | 
| 400-series response codes ([client errors](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/errors-overview.html#CommonErrors)) | Do not retry | There is a problem with the request, from among the following: +  It includes a parameter or parameter combination that is not valid. <br />+  It uses an action or resource for which you do not have permissions. <br />+  It uses a resource that is in the process of changing states. <br />If the request involves a resource that is in the process of changing states, retrying the request could possibly succeed. | 
| 500-series response codes ([server errors](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/errors-overview.html#api-error-codes-table-server)) | Retry | The error is caused by an AWS server-side issue and is generally transient. Repeat the request with an appropriate back-off strategy. | 