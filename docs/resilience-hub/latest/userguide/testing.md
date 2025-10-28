# Managing AWS Fault Injection Service experiments

This section describes how to manage AWS Fault Injection Service (AWS FIS) experiments in AWS Resilience Hub. You run
AWS FIS experiments to measure the resiliency of your AWS resources and the amount of time
it takes to recover from application, infrastructure, availability zone, and AWS Region
incidents.

To measure resiliency, these AWS FIS experiments simulate disruptions to your AWS
resources. Examples of disruptions include network unavailable errors, failovers, stopped
processes on Amazon EC2 or AWS ASG, boot recovery in Amazon RDS, and problems with your Availability
Zone. When the AWS FIS experiment concludes, you can estimate whether an application can
recover from the outage types defined in the RTO target of the resiliency policy.

All the experiments in AWS Resilience Hub are built using AWS FIS and they execute AWS FIS actions.
AWS FIS experiments use only AWS FIS automation actions that are customized to specific AWS
services (such as Amazon EKS action). For more information about AWS FIS actions, see [AWS FIS
actions reference](../../../fis/latest/userguide/fis-actions-reference.md "../../../fis/latest/userguide/fis-actions-reference.md").

You can use the AWS FIS experiments in their default state or customize them based on your
requirements. For more information about managing AWS FIS experiments from AWS Resilience Hub console
and AWS FIS console, see the following topics:

- AWS Resilience Hub console
  - [Viewing AWS FIS experiments](view-fis-experiment.md "view-fis-experiment.md")
    - [To view the list of implemented AWS FIS
      experiments from applications](view-fis-experiment.md#view-active-fis-experiments "view-fis-experiment.md#view-active-fis-experiments")
    - [To view the recommended AWS FIS experiments from assessments](view-fis-experiment.md#view-recommended-fis-experiments "view-fis-experiment.md#view-recommended-fis-experiments")

  - [Running AWS FIS experiments](test-assessment-report.md#arh-running-aws-fis-experiments "test-assessment-report.md#arh-running-aws-fis-experiments")
  - [AWS Fault Injection Service experiment failures/status check](test-failures.md "test-failures.md")

- AWS FIS console
  - [Managing your AWS FIS experiments](../../../fis/latest/userguide/experiments.md "../../../fis/latest/userguide/experiments.md")
  - [Working with the AWS FIS scenario library](../../../fis/latest/userguide/scenario-library.md "../../../fis/latest/userguide/scenario-library.md")
  - [Managing AWS FIS experiment templates](../../../fis/latest/userguide/manage-experiment-template.md "../../../fis/latest/userguide/manage-experiment-template.md")
