# Inferred workload type

Inferred workload type is a feature that's included with AWS Compute Optimizer that infers the applications that
might be running on your AWS resources, such as EC2 instances and EC2 Amazon EC2 Auto Scaling groups. Inferred workload type does
this by analyzing the attributes of your resources. These resources include resource names,
tags, and configuration. Compute Optimizer currently can infer if your instances are running Amazon EMR, Apache
Cassandra, Apache Hadoop, Memcached, NGINX, PostgreSQL, Redis, Kafka, or SQL Server. By inferring the
applications that are running on your instances, Compute Optimizer can identify the effort to migrate your
workloads from x86-based instance types to Arm-based AWS Graviton instances types. By
default, the inferred workload type feature is activated. But, you can create a recommendation preference to
deactivate the feature.

###### Note

You can't infer the SQL Server application in the Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hong Kong), Europe (Milan), and
Asia Pacific (Jakarta) Regions.

The inferred workload types and migration effort are listed in the **Inferred
workload types** and **Migration effort** columns of the EC2
instances and EC2 Amazon EC2 Auto Scaling groups recommendations pages. For more information, see [Viewing EC2 instance recommendations](view-ec2-recommendations.md "view-ec2-recommendations.md") and [Viewing EC2 Amazon EC2 Auto Scaling group recommendations](view-asg-recommendations.md "view-asg-recommendations.md").

## Required permissions

You must have the appropriate permissions to activate the inferred workload type feature.
For more information, see [Policies to grant
access to manage Compute Optimizer recommendation preferences](security-iam.md#enhanced-infrastructure-metrics-permissions "security-iam.md#enhanced-infrastructure-metrics-permissions").

## Organization and account level

By default, inferred workload type is activated. However, you can create a recommendation
preference to deactivate the feature. You can deactivate inferred workload type using the Compute Optimizer
console, AWS Command Line Interface (AWS CLI), or AWS SDKs. In the console, you can deactivate the feature in
the following areas. Deactivating in each area provides a different level of
deactivation.

- For an individual AWS account holder, you can deactivate the
  inferred workload type feature for all AWS resources in the account that meet your AWS Region
  criteria. For more information, see [Activating inferred workload type](activating-inferred-workload-type-steps.md "activating-inferred-workload-type-steps.md")
- The account manager or the delegated administrator of an AWS Organization
  can deactivate the inferred workload type feature for all resources in all member accounts of the
  organization that meet your AWS Region criteria. For more information, see [Activating inferred workload type](activating-inferred-workload-type-steps.md "activating-inferred-workload-type-steps.md").

After you deactivate the inferred workload type feature, Compute Optimizer stops inferring workload types the next
time that recommendations are refreshed. This can take up to 24 hours to take effect.

## Next steps

For instructions on how to activate inferred workload type, see [Activating inferred workload type](activating-inferred-workload-type-steps.md "activating-inferred-workload-type-steps.md").
