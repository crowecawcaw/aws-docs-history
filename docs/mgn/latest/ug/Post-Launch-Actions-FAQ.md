NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Post-launch actions related

This section contains answers to questions about post-launch actions.

###### Topics

- [What operating systems
  does the post-launch actions framework support?](#What-OS-Post-Launch-Actions "#What-OS-Post-Launch-Actions")
- [What version of AWS Systems Manager Agent will be installed on my instance?](#What-Version-SSM "#What-Version-SSM")
- [Why is the AWS Systems Manager Agent not executing my post launch actions?](#SSM-Agent-Not-Discovered "#SSM-Agent-Not-Discovered")

## What operating systems

does the post-launch actions framework support?

Verify that your operating systems [are supported by AWS Systems Manager](../../../systems-manager/latest/userguide/prereqs-operating-systems.md "../../../systems-manager/latest/userguide/prereqs-operating-systems.md").

## What version of AWS Systems Manager Agent will be installed on my instance?

AWS Application Migration Service uses the latest [AWS Systems Manager Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md")
version available in your instance's region.

## Why is the AWS Systems Manager Agent not executing my post launch actions?

- By default, [AWS Systems Manager](../../../systems-manager/index.md "../../../systems-manager/index.md") doesn't have permission to perform actions on your
  instances. Grant access by using an AWS Identity and Access Management (IAM) instance
  profile. You can create an instance profile for AWS Systems Manager by attaching one or
  more IAM policies that define the necessary permissions to a new role or to a role you
  already created. You can use the managed policy
  `AmazonSSMManagedInstanceCore` which allows an instance to use AWS Systems
  Manager service core functionality or create a custom policy. For more information, see
  [Create an IAM
  instance profile for AWS Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md").
- The instances you connect to must also allow HTTPS (port 443) outbound traffic to the following endpoints:

```

ec2messages.<REGION>.amazonaws.com
ssm.<REGION>.amazonaws.com
ssmmessages.<REGION>.amazonaws.com

```

You can connect to the required endpoints by using interface endpoints. For more
information, see [Creating VPC endpoints for AWS Systems Manager](../../../systems-manager/latest/userguide/setup-create-vpc.md#sysman-setting-up-vpc-create "../../../systems-manager/latest/userguide/setup-create-vpc.md#sysman-setting-up-vpc-create").

Alternatively, you can use public IP addresses for communication between your
instances and the internet.

- Another reason might be that the managed instance has limited available CPU or memory
  resources. Although your instance might otherwise be functional, if the instance doesn't
  have enough available resources, you can't establish a session. For more information,
  see [Troubleshooting an unreachable instance](../../../AWSEC2/latest/UserGuide/instance-console.md "../../../AWSEC2/latest/UserGuide/instance-console.md").
