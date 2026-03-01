# Using AWS AppConfig Agent with Amazon ECS and Amazon EKS

You can integrate AWS AppConfig with Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) by using AWS AppConfig Agent.
The agent functions as a sidecar container running alongside your Amazon ECS and Amazon EKS container
applications. The agent enhances containerized application processing and management in the
following ways:

- The agent calls AWS AppConfig on your behalf by using an AWS Identity and Access Management (IAM) role and
  managing a local cache of configuration data. By pulling configuration data from the
  local cache, your application requires fewer code updates to manage configuration data,
  retrieves configuration data in milliseconds, and isn't affected by network issues that
  can disrupt calls for such data.\*
- The agent offers a native experience for retrieving and resolving AWS AppConfig feature
  flags.
- Out of the box, the agent provides best practices for caching strategies, polling
  intervals, and local configuration data availability while tracking the configuration
  tokens needed for subsequent service calls.
- While running in the background, the agent periodically polls the AWS AppConfig data plane
  for configuration data updates. Your containerized application can retrieve the data by
  connecting to localhost on port 2772 (a customizable default port value) and calling
  HTTP GET to retrieve the data.
- AWS AppConfig Agent updates configuration data in your containers without having to restart
  or recycle those containers.
  \*AWS AppConfig Agent caches data the first time the service retrieves your configuration data.
  For this reason, the first call to retrieve data is slower than subsequent calls.

###### Before you begin

To integrate AWS AppConfig with your container applications, you must create AWS AppConfig artifacts
and configuration data, including feature flags or freeform configuration data. For more
information, see [Creating feature flags and free form configuration data in AWS AppConfig](creating-feature-flags-and-configuration-data.md "creating-feature-flags-and-configuration-data.md").

To retrieve configuration data hosted by AWS AppConfig, your container applications must be
configured with access to the AWS AppConfig data plane. To give your applications access, update
the IAM permissions policy that is used by your container service IAM role.
Specifically, you must add the `appconfig:StartConfigurationSession` and
`appconfig:GetLatestConfiguration` actions to the policy. Container service
IAM roles include the following:

- The Amazon ECS task role
- The Amazon EKS node role
- The AWS Fargate pod execution role (if your Amazon EKS containers use Fargate for
  compute processing)
  For more information about adding permissions to a policy, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
  _IAM User Guide_.

###### Topics

- [Starting the AWS AppConfig agent for Amazon ECS integration](appconfig-integration-containers-agent-starting-ecs.md "appconfig-integration-containers-agent-starting-ecs.md")
- [Starting the AWS AppConfig agent for Amazon EKS integration](appconfig-integration-containers-agent-starting-eks.md "appconfig-integration-containers-agent-starting-eks.md")
- [(Optional) Running AWS AppConfig as a DaemonSet in Amazon EKS](appconfig-integration-containers-agent-daemon.md "appconfig-integration-containers-agent-daemon.md")
- [(Optional) Using environment variables to configure AWS AppConfig Agent for Amazon ECS and Amazon EKS](appconfig-integration-containers-agent-configuring.md "appconfig-integration-containers-agent-configuring.md")
- [Retrieving configuration data for applications running in Amazon ECS and Amazon EKS](appconfig-integration-containers-agent-retrieving-data.md "appconfig-integration-containers-agent-retrieving-data.md")
