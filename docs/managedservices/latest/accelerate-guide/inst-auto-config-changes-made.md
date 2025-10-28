# Automated instance configuration changes

The AMS Accelerate instance configuration automation makes the following changes in your account:

1. IAM permissions

Adds the IAM-managed Policies required to grant the instance permission to use the agents installed by AMS Accelerate. 2. Agents

    1. The Amazon CloudWatch Agent is responsible for emitting OS logs and metrics. The instance configuration automation ensures that the CloudWatch agent is installed and
     running the AMS Accelerate minimum version.
    2. The AWS Systems Manager SSM Agent is responsible for running remote commands on the instance. The instance
     configuration automation ensures that the SSM Agent is running the AMS Accelerate minimum version.

3.  CloudWatch Configuration

        1. To ensure that the required metrics and logs are emitted, AMS Accelerate customizes the
         CloudWatch configuration. For more information, see the following section,
         [CloudWatch configuration change details](inst-auto-config-details-cw.md "inst-auto-config-details-cw.md").

    Automated instance configuration makes changes or additions to your IAM instance profiles
    and CloudWatch configuration.
