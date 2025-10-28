NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Instance type right-sizing

AWS Application Migration Service launches a new instance type after every change of configuration on the
source server, for example, added/removed disks, and added/removed RAM. When you use the instance type right-sizing feature Application Migration Service launches a test or cutover
instance type that best matches the OS, CPU, and RAM of your source
server. Set this feature to **On** to enable or to **None** to disable, in which case Application Migration Service launches the
instance type as configured in your Amazon EC2 launch template.

Enable instance type right-sizing if
you want to determine the instance type that is launched in AWS for all your test or cutover
servers.

**Important considerations:**

- The AWS instance type selected by AWS Application Migration Service when this feature is activated overwrites the
  instance type defined in your EC2 launch template.
- Hardware changes and the resulting AWS instance type change may take up to 90 minutes to
  be processed by AWS Application Migration Service.
- The T family instance type is not supported for right-sizing. If you want to use the T
  family, avoid using right-sizing.
- The available capacity for each Amazon EC2 instance type varies by Availability Zone and Region,
  and may be subject to your specific AWS account limits. For mission-critical workloads
  consider using [Reserved Instances](../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md "../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md") to guarantee capacity for specific instance types. Note
  that additional costs apply when reserving capacity.
- The right-sizing instance type selected by AWS Application Migration Service appears on the **Server details** tab.

###### Supported instance families:

The service provides recommendations from these instance families, which are available in
most target Regions:

- c5
- m5
- c4
- m4
- r5
- r4
- i3
- d2

###### Supported instance families for the Thailand and Malaysia Regions:

The _Asia Pacific (Thailand)_ ,
and _Asia Pacific (Malaysia)_ Regions support only these instance families:

- C6i
- m6i
- r6i
