# How Amazon EC2 Dedicated Host recovery works

Dedicated Hosts and the host resource groups recovery process use host-level health checks
to assess Dedicated Host availability and to detect underlying system failures. The
type of Dedicated Host failure determines if Dedicated Host auto recovery is possible. Examples of
problems that can cause host-level health checks to fail include:

- Loss of network connectivity
- Loss of system power
- Hardware or software issues on the physical host

###### Important

Dedicated Host auto recovery does not occur when the host is scheduled for
retirement.

## Dedicated Host auto

recovery

When a system power or network connectivity failure is detected on your Dedicated Host,
Dedicated Host auto recovery is initiated and Amazon EC2 **automatically
allocates a replacement Dedicated Host in the same Availability Zone as the original Dedicated Host**.
The replacement Dedicated Host receives a new host ID, but retains the same attributes
as the original Dedicated Host, including:

- Availability Zone
- Instance type
- Tags
- Auto placement settings
- Reservation

When the replacement Dedicated Host is allocated, the **instances
are recovered on to the replacement Dedicated Host**. The recovered instances
retain the same attributes as the original instances, including:

- Instance ID
- Private IP addresses
- Elastic IP addresses
- EBS volume attachments
- All instance metadata

Additionally, the built-in integration with AWS License Manager automates the tracking
and management of your licenses.

###### Note

AWS License Manager integration is supported only in Regions in which AWS License Manager is
available.

If instances have a host affinity relationship with the impaired Dedicated Host, the
recovered instances establish host affinity with the replacement Dedicated Host.

When all of the instances have been recovered on to the replacement Dedicated Host,
**the impaired Dedicated Host is released**, and the
replacement Dedicated Host becomes available for use.

When host recovery is initiated, the AWS account owner is notified by email
and by an AWS Health Dashboard event. A second notification is sent after the host recovery
has been successfully completed.

If you are using AWS License Manager to track your licenses, AWS License Manager allocates new
licenses for the replacement Dedicated Host based on the license configuration limits. If
the license configuration has hard limits that will be breached as a result of
the host recovery, the recovery process is not allowed and you are notified of
the host recovery failure through an Amazon SNS notification (if notification
settings have been configured for AWS License Manager). If the license configuration has
soft limits that will be breached as a result of the host recovery, the recovery
is allowed to continue and you are notified of the limit breach through an Amazon SNS
notification. For more information, see [Using
License Configurations](../../../license-manager/latest/userguide/license-configurations.md "../../../license-manager/latest/userguide/license-configurations.md") and [Settings in
License Manager](../../../license-manager/latest/userguide/settings.md "../../../license-manager/latest/userguide/settings.md") in the _AWS License Manager User Guide_.

## Host recovery states

When a Dedicated Host failure is detected, the impaired Dedicated Host enters the
`under-assessment` state, and all of the instances enter the
`impaired` state. You can't launch instances on to the impaired Dedicated Host
while it is in the `under-assessment` state.

After the replacement Dedicated Host is allocated, it enters the `pending` state.
It remains in this state until the host recovery process is complete. You can't
launch instances on to the replacement Dedicated Host while it is in the `pending`
state. Recovered instances on the replacement Dedicated Host remain in the
`impaired` state during the recovery process.

After the host recovery is complete, the replacement Dedicated Host enters the
`available` state, and the recovered instances return to the
`running` state. You can launch instances on to the replacement Dedicated Host
after it enters the `available` state. The original impaired Dedicated Host is
permanently released and it enters the `released-permanent-failure`
state.

If the impaired Dedicated Host has instances that do not support host recovery, such as instances
with instance store root volumes, the Dedicated Host is not released. Instead, it is
marked for retirement and enters the `permanent-failure`
state.

## Scenarios without

Dedicated Host auto recovery

**Dedicated Host auto recovery does not occur when the host is
scheduled for retirement**. You will receive a retirement
notification in the AWS Health Dashboard, an Amazon CloudWatch event, and the AWS
account owner email address receives a message regarding the Dedicated Host failure.
Follow the remedial steps described in the retirement notification within the
specified time period to manually recover the instances on the retiring
host.

**Stopped instances are not recovered** on to the
replacement Dedicated Host. If you attempt to start a stopped instance that targets the
impaired Dedicated Host, the instance start fails. We recommend that you modify the
stopped instance to either target a different Dedicated Host, or to launch on any
available Dedicated Host with matching configurations and auto-placement enabled.

**Instances with instance storage are not
recovered** on to the replacement Dedicated Host. As a remedial measure, the
impaired Dedicated Host is marked for retirement and you receive a retirement notification
after the host recovery is complete. Follow the remedial steps described in the
retirement notification within the specified time period to manually recover the
remaining instances on the impaired Dedicated Host.
