# Amazon ECS environment variables

Environment variables control a task's behavior such as the capacity used to run the task.
Amazon ECS sets the following environment variables for your tasks:

- `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` - The full HTTP URL endpoint
  for the SDK to use when making a request for credentials. This includes both the
  scheme and the host. For more information, see [Container
  credential provider](../../../sdkref/latest/guide/feature-container-credentials.md "../../../sdkref/latest/guide/feature-container-credentials.md") in the _AWS SDKs Reference
  Guide_.
- `ECS_CONTAINER_METADATA_URI_V4` - The address of the task metadata
  version 4. For more information, see [Amazon ECS task metadata endpoint version 4](task-metadata-endpoint-v4.md "task-metadata-endpoint-v4.md").
- `ECS_CONTAINER_METADATA_URI` - The address of the task metadata version

3.  For more information, see [Amazon ECS task metadata endpoint version
    3](task-metadata-endpoint-v3.md "task-metadata-endpoint-v3.md").

- `ECS_AGENT_URI` - The base address for different endpoints supported by
  Fargate. For more information, see:
  - [Amazon ECS task scale-in protection
    endpoint](task-scale-in-protection-endpoint.md "task-scale-in-protection-endpoint.md")
  - [Amazon ECS fault injection endpoints](fault-injection-endpoints.md "fault-injection-endpoints.md")

- `AWS_EXECUTION_ENV` - The information about the compute option the task
  runs on.
  - For Fargate, Amazon ECS sets this to `AWS_ECS_FARGATE`.
  - For EC2, Amazon ECS sets this to `AWS_ECS_EC2`.

- `AWS_DEFAULT_REGION` – The default AWS Region for your
  AWS account. This is the default Region where your task
  runs.
- `AWS_REGION` – The Region where the task runs. If
  defined, this value overrides the `AWS_DEFAULT_REGION`.
  You can view the environment variables in the task metadata. For more information, see
  one of the following topics:

- Fargate - [Amazon ECS task metadata available for tasks on
  Fargate](fargate-metadata.md "fargate-metadata.md")
- EC2 - [Task metadata available for Amazon ECS tasks on EC2](ec2-metadata.md "ec2-metadata.md")
