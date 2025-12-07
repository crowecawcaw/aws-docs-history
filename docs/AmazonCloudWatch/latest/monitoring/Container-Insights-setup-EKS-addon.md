# Quick start with the Amazon CloudWatch

Observability EKS add-on

You can use the Amazon EKS add-on to install Container Insights with enhanced
observability for Amazon EKS. The add-on installs the CloudWatch agent to send infrastructure
metrics from the cluster, installs Fluent Bit to send container logs, and also enables
CloudWatch [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md") to send application
performance telemetry.

When you use the Amazon EKS add-on version 1.5.0 or later, Container Insights is enabled
on both Linux and Windows worker nodes in the cluster. Application Signals is
not supported on Windows in Amazon EKS.

The Amazon EKS add-on is not supported for clusters running Kubernetes instead of
Amazon EKS.

For more information about the Amazon CloudWatch Observability EKS add-on, see [Install the CloudWatch agent with the
Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md").

If you use version 3.1.0 or later of the add-on, you can use EKS Pod Identity to
grant the required permissions to the add-on. EKS Pod Identity is the recommended option
and provides benefits such as least privilege, credential rotation, and auditability.
Additionally, using EKS Pod Identity allows you to install the EKS add-on as part of the
cluster creation itself.

###### To install the Amazon CloudWatch Observability EKS add-on

1. Follow the [EKS
   Pod Identity association](../../../eks/latest/userguide/pod-id-association.md#pod-id-association-create/ "../../../eks/latest/userguide/pod-id-association.md#pod-id-association-create/") steps to create the IAM role and set up the EKS
   Pod Identity agent.
2. Attach an IAM policy that grants the required permissions to your role.
   Replace `my-role` with the name of your IAM role from the
   previous step.

```
aws iam attach-role-policy \
 --role-name `my-role` \
--policy-arn=arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
```

3. Enter the following command, using with the IAM role you created in the
   previous step:

```
aws eks create-addon \
--addon-name amazon-cloudwatch-observability \
--cluster-name `my-cluster-name` \
--pod-identity-associations serviceAccount=cloudwatch-agent,roleArn=arn:aws:iam::`111122223333`:role/`my-role`
```
