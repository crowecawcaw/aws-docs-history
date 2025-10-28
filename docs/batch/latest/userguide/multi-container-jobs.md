# Create job definitions using EcsProperties

With AWS Batch job definitions using [`EcsProperties`](../APIReference/API_EcsProperties.md "../APIReference/API_EcsProperties.md"), you
can model hardware, sensors, 3D environments and other simulations in separate containers. You
can use this feature to logically organize your workload components, and separate them from the
main application. This feature can be used with AWS Batch on Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and
AWS Fargate.

## `ContainerProperties`

versus `EcsProperties` job definitions

You can choose to use [`ContainerProperties`](../APIReference/API_ContainerProperties.md "../APIReference/API_ContainerProperties.md") or [`EcsProperties`](../APIReference/API_EcsProperties.md "../APIReference/API_EcsProperties.md")
job definitions as your use case dictates. At a high-level, running AWS Batch jobs with
`EcsProperties` is similar to running jobs with a
`ContainerProperties`.

The legacy job definition structure, using `ContainerProperties`, remains supported. If you
currently have workflows using this structure, you can continue to run them.

The main difference is that there is a new object added to the job definition to
accommodate `EcsProperties`-based definitions.

For example, a job definition that uses `ContainerProperties` on Amazon ECS and
Fargate has the following structure:

```
{
   "containerProperties": {
     ...
     "image": "my_ecr_image1",
     ...
  },
...
}
```

A job definition that uses `EcsProperties` on Amazon ECS and Fargate has the
following structure:

```
{
  "ecsProperties": {
    "taskProperties": [{
      "containers": [
        {
          ...
          "image": "my_ecr_image1",
          ...
        },
        {
          ...
          "image": "my_ecr_image2",
          ...
        },
```

## General changes to the AWS Batch APIs

The following further outlines some of the key differences when using the
`ContainerProperties` and the `EcsProperties` API data types:

- Many of the parameters that are used within `ContainerProperties` appear
  within `TaskContainerProperties`. Some examples include, `command`,
  `image`, `privileged`, `secrets`, and
  `users`. They can all be found within [TaskContainerProperties](../APIReference/API_TaskContainerProperties.md "../APIReference/API_TaskContainerProperties.md").
- Some of the `TaskContainerProperties` parameters don’t have functional
  equivalents in the legacy structure. Some examples include, `dependsOn`,
  `essential`, `name`, `ipcMode`, and
  `pidMode`. For more information, see [EcsTaskDetails](../APIReference/API_EcsTaskDetails.md "../APIReference/API_EcsTaskDetails.md") and
  [TaskContainerProperties](../APIReference/API_TaskContainerProperties.md "../APIReference/API_TaskContainerProperties.md").

As well, some `ContainerProperties` parameters don’t have equivalents, or
application, in the `EcsProperties` structure. In [`taskProperties`](../APIReference/API_EcsProperties.md#Batch-Type-EcsProperties-taskProperties "../APIReference/API_EcsProperties.md#Batch-Type-EcsProperties-taskProperties"), `container` has been replaced with
`containers` so that the new object can accept up to ten elements. For more
information see [RegisterJobDefinition:containerProperties](../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-containerProperties "../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-containerProperties") and [EcsTaskProperties:containers](../APIReference/API_EcsTaskProperties.md "../APIReference/API_EcsTaskProperties.md").

- `taskRoleArn` is functionally equivalent to `jobRoleArn`. For
  more information see [EcsTaskProperties:taskRoleArn](../APIReference/API_EcsTaskProperties.md "../APIReference/API_EcsTaskProperties.md") and [ContainerProperties:jobRoleArn](../APIReference/API_ContainerProperties.md "../APIReference/API_ContainerProperties.md").
- You can include from one (1) to ten (10) containers in the `EcsProperties`
  structure. For more information see [EcsTaskProperties:containers](../APIReference/API_EcsTaskProperties.md "../APIReference/API_EcsTaskProperties.md").
- The `taskProperties` and instanceTypes objects are arrays, but currently
  accept only one element. For example, [EcsProperties:taskProperties](../APIReference/API_EcsProperties.md "../APIReference/API_EcsProperties.md") and [NodeRangeProperty:instanceTypes](../APIReference/API_NodeRangeProperty.md "../APIReference/API_NodeRangeProperty.md").

## Multi-container job definitions for Amazon ECS

To accommodate the multi-container structure for Amazon ECS, some of the API data types are
different. For example,

- [`ecsProperties`](../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-ecsProperties "../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-ecsProperties") is the same level as
  `containerProperties` in the single-container definition. For more
  information, see [EcsProperties](../APIReference/API_EcsProperties.md "../APIReference/API_EcsProperties.md") in the
  _AWS Batch API Reference Guide_.
- [`taskProperties`](../APIReference/API_EcsProperties.md#Batch-Type-EcsProperties-taskProperties "../APIReference/API_EcsProperties.md#Batch-Type-EcsProperties-taskProperties") contains the properties defined for the Amazon ECS
  task. For more information, see [EcsProperties](../APIReference/API_EcsProperties.md "../APIReference/API_EcsProperties.md") in the
  _AWS Batch API Reference Guide_.
- [`containers`](../APIReference/API_EcsTaskProperties.md#Batch-Type-EcsTaskProperties-containers "../APIReference/API_EcsTaskProperties.md#Batch-Type-EcsTaskProperties-containers") includes similar information to
  `containerProperties` in the single-container definition. The main difference
  is that `containers` allows you to define up to ten containers. For more
  information, see [ECSTaskProperties:containers](../APIReference/API_EcsTaskProperties.md "../APIReference/API_EcsTaskProperties.md") in the _AWS Batch API Reference
  Guide_.
- [`essential`](../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-essential "../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-essential") parameter indicates how the container affects the job.
  All essential containers must complete successfully (exit as 0) in order for the job to
  progress. If a container that is marked as essential fails (exits as non-0), then the job
  fails.

The default value is `true` and at least one container must be marked as
`essential`. For more information, see [`essential`](../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-essential "../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-essential") in the _AWS Batch API Reference
Guide_.

- With the [`dependsOn`](../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-dependsOn "../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-dependsOn") parameter, you can define a list of container
  dependencies. For more information, see [`dependsOn`](../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-dependsOn "../APIReference/API_TaskContainerProperties.md#Batch-Type-TaskContainerProperties-dependsOn") in the _AWS Batch API Reference
  Guide_.

###### Note

The complexity of the `dependsOn` list and the associated container
runtime can affect the start time for your job. If the dependencies take a long time to
run, the job will remain in a `STARTING` state until they complete.

For more information about the `ecsProperties` and structure, see [RegisterJobDefinition](../APIReference/API_RegisterJobDefinition.md#API_RegisterJobDefinition_RequestBody "../APIReference/API_RegisterJobDefinition.md#API_RegisterJobDefinition_RequestBody") request syntax for [ecsProperties](../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-ecsProperties "../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-ecsProperties").

## Multi-container job definitions for Amazon EKS

To accommodate the multi-container structure for Amazon EKS, some of the API data types are
different. For example,

- [`name`](../APIReference/API_EksContainer.md#Batch-Type-EksContainer-name "../APIReference/API_EksContainer.md#Batch-Type-EksContainer-name") is a unique identifier for the container. This object isn't
  required for a single container, but is required when defining multiple containers in a
  pod. When `name` isn't defined for single containers, the default name,
  `default`, is applied.
- [`initContainers`](../APIReference/API_EksPodProperties.md#Batch-Type-EksPodProperties-initContainers "../APIReference/API_EksPodProperties.md#Batch-Type-EksPodProperties-initContainers") are defined within the [eksPodProperties](../APIReference/API_EksPodProperties.md "../APIReference/API_EksPodProperties.md") data type. They run before application containers, always
  runs to completion, and must complete successfully before the next container
  starts.

These containers are registered with the Amazon EKS Connector agent and persists the
registration information in the Amazon Elastic Kubernetes Service backend data store. The
`initContainers` object can accept up to ten (10) elements. For more
information, see [Init
Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/") in the _Kubernetes documentation_.

###### Note

The `initContainers` object can affect the start time for your job. If
the `initContainers` take a long time to run, the job will remain in a
`STARTING` state until they complete.

- [`shareProcessNamespace`](../APIReference/API_EksPodProperties.md#Batch-Type-EksPodProperties-shareProcessNamespace "../APIReference/API_EksPodProperties.md#Batch-Type-EksPodProperties-shareProcessNamespace") indicates if the containers in the pod can
  share the same process namespace. The default values is `false`. Setting this
  to `true` to enable containers see and signal processes in other containers
  that located in the same pod.
- Every container has importance. All containers must complete successfully (exit as 0)
  for the job to succeed. If one container fails (exits as other than 0), then the job
  fails.

For more information about the `eksProperties` and structure, see [RegisterJobDefinition](../APIReference/API_RegisterJobDefinition.md#API_RegisterJobDefinition_RequestBody "../APIReference/API_RegisterJobDefinition.md#API_RegisterJobDefinition_RequestBody") request syntax for [eksProperties](../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-eksProperties "../APIReference/API_RegisterJobDefinition.md#Batch-RegisterJobDefinition-request-eksProperties").
