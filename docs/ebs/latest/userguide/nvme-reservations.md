# Use NVMe reservations with Multi-Attach enabled Amazon EBS volumes

Multi-Attach enabled `io2` volumes support NVMe reservations, which is a set of
industry-standard storage fencing protocols. These protocols enable you to create
and manage reservations that control and coordinate access from multiple instances
to a shared volume. Reservations are used by shared storage applications to ensure
data consistency.

###### Contents

- [Requirements](#nvme-reservations-reqs "#nvme-reservations-reqs")
- [Enabling support for NVMe reservations](#nvme-reservations-enable "#nvme-reservations-enable")
- [Supported NVMe Reservation commands](#nvme-reservations-commands "#nvme-reservations-commands")
- [Pricing](#nvme-reservations-cost "#nvme-reservations-cost")

## Requirements

NVMe reservations is supported with Multi-Attach enabled `io2` volumes only.
Multi-Attach enabled volumes can be attached only to instances built on the
Nitro system.

NVMe reservations is supported with the following operating systems:

- SUSE Linux Enterprise 12 SP3 and later
- RHEL 8.3 and later
- Amazon Linux 2 and later
- Windows Server 2016 and later

###### Note

For supported Windows Server AMIs dated 2023.09.13 and later, the required
NVMe drivers are included. For earlier AMIs, you must update to NVMe driver
version 1.5.0 or later. For more information, see [AWS NVMe drivers](../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md "../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md").

If you're using EC2Launch v2 to initialize your disks, you must upgrade to version
**2.0.1521** or later. For more information, see
[Use
the EC2Launch v2 agent](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md").

## Enabling support for NVMe reservations

Support for NVMe reservations is enabled by default for all Multi-Attach enabled `io2`
volumes created after **September 18, 2023**.

To enable support for NVMe reservations for existing `io2` volumes created before September
18, 2023, you must detach all instances from the volume and then reattach the required instances.
All attachments made after detaching all of the instances will have NVMe reservations enabled.

## Supported NVMe Reservation commands

Amazon EBS supports the following NVMe Reservation commands:

**Reservation Register**

Registers, unregisters, or replaces a reservation key. A registration key is used to
identify and authenticate an instance. Registering a reservation key
with a volume creates an association between the instance and the
volume. You must register the instance with the volume before that
instance can acquire a reservation.

**Reservation Acquire**

Acquires a reservation on a volume, preempts a reservation held on a
namespace, and aborts a reservation held on a volume. The following reservation
types can be acquired:

- Write Exclusive Reservation
- Exclusive Access Reservation
- Write Exclusive - Registrants Only Reservation
- Exclusive Access - Registrants Only Reservation
- Write Exclusive - All Registrants Reservation
- Exclusive Access - All Registrants Reservation

**Reservation Release**

Releases or clears a reservation held on a volume.

**Reservation Report**

Describes the registration and reservation status of a volume.

## Pricing

There are no additional costs for enabling and using Multi-Attach.
