# How to add related information to

custom telemetry sent to CloudWatch

When you publish your own metrics and logs to CloudWatch, the entity information needed
for related telemetry is not there by default. When you send metrics to CloudWatch or
logs to CloudWatch Logs (with the [PutMetricData](../APIReference/API_PutMetricData.md "../APIReference/API_PutMetricData.md") or [PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md") operations), you can add entity information to those logs or
metrics. The entity information is associated with the telemetry, and used in the
**Explore related** feature to find related telemetry that is
associated with the same entity.

The entity sent with telemetry represents a resource or service that the
telemetry is associated with. For example, a metric about a service, or that comes from
an AWS resource. To identify the entity associated in your code, you create a set of
`KeyAttributes` and optional `Attributes` of the entity.

###### Note

CloudWatch can only find related resources for entities that have had telemetry sent
within the previous three hours. If your resource only emits sparse telemetry
(less than once every 3 hours), you may want to send additional
_heartbeat_ telemetry, to keep the entity active within
CloudWatch.

For information on how to add entity information, see [Entity information in EMF format](CloudWatch_Embedded_Metric_Format_Specification.md#entity-information-emf-format "CloudWatch_Embedded_Metric_Format_Specification.md#entity-information-emf-format").

The following sections describe how to create the `KeyAttributes` and
`Attributes` so that CloudWatch can identify the resources and services associated
with the telemetry.

## Identifying the entity

with the KeyAttributes object

The `KeyAttributes` property of the Entity objects ( [in CloudWatch](../APIReference/API_Entity.md "../APIReference/API_Entity.md") or
[in CloudWatch
logs](../../../AmazonCloudWatchLogs/latest/APIReference/API_Entity.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_Entity.md")) uniquely identifies the entity for CloudWatch. It is a list of
key-value pairs. Entities with the same `KeyAttributes` are considered
to be the same entity. Telemetry associated with the same entity are considered
related, and can be easily found in the **Explore related**
pane.

###### Note

In the CloudWatch API, the property is called `KeyAttributes`. In the
CloudWatch Logs API, the property is called `keyAttributes`. Here they are
treated as the same property.

There are five possible types of object that an `Entity` can
represent.

- **AWS::Resource** – The
  entity represents an AWS resource, such as a DynamoDB table or Amazon EC2
  instance.
- **AWS::Service** – The
  entity represent an AWS service, such as Amazon S3. This might be used, for
  example, when calling the `ListBuckets` operation, which is not
  associated with a specific Amazon S3 resource.
- **Service** – The entity
  represents a workload running in your account. For example, an application
  or service that you manage.
- **Resource** – The
  entity represents a resource that is not managed by AWS, for example,
  operating system resources, such as processes or file volumes.
- **RemoteService** – The
  entity represents an external service in a remote call. For example, a
  remote call to a database, external cache, or an external endpoint.

Depending on which of the above types you are trying to represent, you must
provide the correct key-value pairs for the `KeyAttributes`. The
following describes each type.

AWS::Resource
To specify an AWS Resource, you must include the following three
key value pairs:

- `"Type": "AWS::Resource"` – This key-value
  pair identifies the entity as an AWS resource.
- `"ResourceType": "*<resource-type>*"`
  – The string value of the `ResourceType` is
  the AWS CloudFormation [resource type](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") string. For example,
  `AWS::DynamoDB::Table`.
- `"Identifier": "*<resource-id>*"`
  – The primary identifier for the resource. For more
  information, see [primaryIdentifier](../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-primaryidentifier "../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-primaryidentifier") in the _Extension Development
  for CloudFormation User Guide_.

AWS::Service
To specify an AWS Service, you must include the following two
key value pairs:

- `"Type": "AWS::Service"` – This key-value
  pair identifies the entity as an AWS service.
- `"Name": "*<service-name>*"`
  – The value of the `Name` is the AWS CloudFormation
  [service name](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") string. For example,
  `AWS::DynamoDB`.

Service
To specify a service that is not operated by AWS, you must include
the following three key value pairs:

- `"Type": "Service"` – This key-value
  pair identifies the entity as a service.
- `"Name": "*<service-name>*"`
  – This represents the name of the service that is
  sending the metrics. For example, `my-service-frontend`
  or `api.myservice.com`.
- `"Environment": "*<environment-name>*"`
  – This attribute specifies
  where the service is hosted, or the environment to which it
  belongs. For example `us-west-2`, or
  `myservice.production`.

Resource
To specify a resource that is not provided by AWS, you must include
the following three key value pairs:

- `"Type": "Resource"` – This key-value
  pair identifies the entity as a resource.
- `"ResourceType": "*<resource-type>*"`
  – A string specifying the type of resource. For example,
  `K8s::Pod` for a Kubernetes Pod.
- `"Identifier": "*<resource-id>*"`
  – A string identifier for the resource. Can contain
  multiple names, separated by pipes. For example, a Kubernetes
  Pod might be represented by it's cluster name, namespace, and
  pod name, such as `MyCluster|MyNamespace|MyPod`.

RemoteService
To specify a remote service, you must include the following two
key value pairs:

- `"Type": "RemoteService"` – This key-value
  pair identifies the entity as a remote service.
- `"Name": "*<remote-service-name>*"`
  – Specifies how the application refers to the external
  service in a remote call. For example,
  `api.test.myservice.com`.

## Providing additional details

about the entity with the Attributes object

You can provide additional details about the `Entity` that you
provide with your telemetry. This can include details about the platform,
resource, application, or telemetry provider. The following tables describes
the key words that you can use for each of these types of data.

###### Note

In the CloudWatch API, the property is called `Attributes`. In the
CloudWatch Logs API, the property is called `attributes`. Here they are
treated as the same property.

**Platform details**

| Keyword                | Usage                                                       | Domain of Values                                           | Examples                      |
| ---------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------- |
| `PlatformType`         | Defines the hosted-in platform.                             | AWS::EKS, AWS::ECS, AWS::EC2, AWS::Lambda, K8s, Generic    | `AWS::EC2`                    |
| `EKS.Cluster`          | Name of the Amazon EKS cluster.                             | Alphanumeric string with basic delimiters.                 | `FlyingSquad`                 |
| `K8s.Cluster`          | Name of the self-hosted Kubernetes cluster.                 | Alphanumeric string with basic delimiters.                 | `minicube`                    |
| `K8s.Namespace`        | Name of Kubernetes namespace in Amazon EKS or K8s clusters. | Alphanumeric string with basic delimiters.                 | `default`, `pet-clinic`       |
| `K8s.Workload`         | Name of Kubernetes workload in Amazon EKS and K8s clusters. | Alphanumeric string with basic delimiters.                 | `frontend`                    |
| `K8s.Node`             | Identity of Kubernetes node in Amazon EKS and K8s clusters. | K8s node name (for example, Amazon EC2 instance DNS name). | `ip-11-22-33-44.ec2.internal` |
| `K8s.Pod`              | Identity of Kubernetes pod in Amazon EKS and K8s clusters.  | K8s pod identifier.                                        | `frontend-1234abcd56-ef7890`  |
| `EC2.AutoScalingGroup` | Name of the Amazon EC2 AutoScaling Group.                   | Alphanumeric string with basic delimiters.                 | `my-asg-name-1`               |
| `EC2.InstanceId`       | Identity of the Amazon EC2 instance.                        | Amazon EC2 instance identifier.                            | `i-1234abcd5678ef90`          |
| `ECS.Cluster`          | Identity of the Amazon ECS cluster.                         | Amazon ECS cluster name.                                   | `MyCluster`                   |
| `ECS.Service`          | Identity of the Amazon ECS service.                         | Amazon ECS service name.                                   | `MyService`                   |
| `ECS.Task`             | Identity of the Amazon ECS task.                            | Amazon ECS task ID.                                        | `task-123abc`                 |
| `Lambda.Function`      | Identity of the Lambda function.                            | Lambda function name.                                      | `MyFunction`                  |
| `Host`                 | Name of the host for all platform types.                    | Sub-domain format.                                         | `ip-111-22-33-44.example.com` |

**Resource details**

| Keyword            | Usage                     | Domain of Values                           | Examples                                                        |
| ------------------ | ------------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| `AWS.Resource.ARN` | ARN for the AWS resource. | Alphanumeric string with basic delimiters. | `arn:aws:dynamodb:us-east-1:123456789012:table/myDynamoDBTable` |

**Application details**

| Keyword               | Usage                                   | Domain of Values                           | Examples                                                        |
| --------------------- | --------------------------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| `AWS.Application`     | Name of the application in AppRegistry. | Alphanumeric string with basic delimiters. | `PetClinicApp`                                                  |
| `AWS.Application.ARN` | ARN of the application in AppRegistry.  | Alphanumeric string with basic delimiters. | `arn:aws:servicecatalog:us-east-1:1234567890:/applications/...` |

**Telemetry provider details**

| Keyword            | Usage                                                                                                                      | Domain of Values                                                                | Examples                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------- |
| `Telemetry.SDK`    | The fingerprint of OTEL SDK version for instrumented services.                                                             | Alphanumeric string with basic delimiters.                                      | `opentelemetry,1.32.0-aws-SNAPSHOT,java,Auto` |
| `Telemetry.Agent`  | The fingerprint of the Agent used to collect and send telemetry data.                                                      | Alphanumeric string with basic delimiters.                                      | `CWAgent/1.300026.3, ADOTCollector/1.x`       |
| `Telemetry.Source` | Specifies the point of application where the telemetry was<br>collected or what was used for the source of telemetry data. | ServerSpan, ClientSpan, ProducerSpan, ConsumerSpan, LocalRoot<br>Span, JMX, OS. | `ClientSpan, JMX`                             |
