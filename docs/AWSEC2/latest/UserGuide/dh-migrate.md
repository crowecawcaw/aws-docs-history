# Migrate to Nitro-based Amazon EC2 Dedicated Hosts

The Nitro System is a collection of hardware and software components built by AWS
that enable high performance, high availability, and high security. Nitro-based Dedicated Hosts
offer improved price performance compared to Xen-based Dedicated Hosts. If you have any Xen-based
Dedicated Hosts in your account, we recommend that you migrate your workloads to Nitro-based
Dedicated Hosts. For more information, see [AWS Nitro
System](https://aws.amazon.com/ec2/nitro/ "https://aws.amazon.com/ec2/nitro/").

To migrate from a Xen-based Dedicated Host to a Nitro-based Dedicated Host, you need to migrate the
Xen-based instances on your Dedicated Host to Nitro-based instance types, allocate a new
Nitro-based Dedicated Host, and then move your migrated Nitro-based instances to your new
Nitro-based Dedicated Host.

This topic provides detailed steps for migrating from Xen-based Dedicated Hosts to Nitro-based
Dedicated Hosts.

###### Migration steps

- [Step 1: Identify your Xen-based Dedicated Hosts](#identify-xen-hosts "#identify-xen-hosts")
- [Step 2: Migrate Xen-based instances to Nitro-based
  instance types](#migrate-dh-instances "#migrate-dh-instances")
- [Step 3: Allocate a Nitro-based Dedicated Host](#allocate-nitro-host "#allocate-nitro-host")
- [Step 4: Move migrated instances to new Nitro-based Dedicated Host](#move-instances "#move-instances")
- [Step 5: Release unused Xen-based Dedicated Host](#release-xen-instances "#release-xen-instances")

## Step 1: Identify your Xen-based Dedicated Hosts

The following Dedicated Hosts are Xen-based and are eligible to be migrated to
Nitro-based Dedicated Hosts.

- **General purpose:** M3 | M4
- **Compute optimized:** C3 | C4
- **Memory optimized:** R3 | R4 | X1 | X1e
- **Storage optimized:** D2 | H1 | I2 | I3
- **Accelerated computing:** F1 | G3 | P2 | P3

###### To check if you have Xen-based Dedicated Hosts in your account

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Dedicated Hosts**.
3. In the **Search field**, use the **Instance family**
   filter to search for the Xen-based Dedicated Hosts above. For example, _Instance family = m3_.

## Step 2: Migrate Xen-based instances to Nitro-based

instance types

Instances that run on Xen-based Dedicated Hosts are also Xen-based. You must migrate these
instances to Nitro-based instance types before you can move them to Nitro-based
Dedicated Hosts.

###### Important

Before you begin migrating your instances, we recommend that you back up
your data. For more information, see [Create multi-volume
Amazon EBS snapshots from an Amazon EC2 instance](../../../ebs/latest/userguide/ebs-create-snapshots.md "../../../ebs/latest/userguide/ebs-create-snapshots.md").

###### To find instances running on your Xen-based Dedicated Hosts

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Dedicated Hosts**.
3. Select the Xen-based host you intend to migrate and then select the
   **Running instances** tab. The tab lists all of the
   instances running of the selected host.

To migrate **Linux instances**, see
[Amazon EC2 instance type changes](ec2-instance-resize.md "ec2-instance-resize.md").

To migrate **Windows instances**, see
[Migrate an EC2 Windows instance to a Nitro-based instance type](migrating-latest-types.md "migrating-latest-types.md").

###### Note

Ensure that you migrate your instances to an instance type that matches the
Nitro-based Dedicated Host that you intend to migrate to. For example, if you intend to
migrate to a M7i Dedicated Host, ensure that you migrate your instances to an M7i
instance type.

## Step 3: Allocate a Nitro-based Dedicated Host

###### To find supported Nitro-based Dedicated Hosts

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, select **Instance Types**.
3. Apply the following filters:
   - _Hypervisor = nitro_
   - _Dedicated Host support = true_

After you've found a suitable Nitro-based instance type, [allocate a new Dedicated Host](dedicated-hosts-allocating.md "dedicated-hosts-allocating.md").

## Step 4: Move migrated instances to new Nitro-based Dedicated Host

After you have allocated the Nitro-based Dedicated Host and it reaches the `available` state,
you can move the instances that you previously migrated to Nitro-based instance types to the
new Dedicated Host.

###### To move your instances to your new Nitro-based Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, **Instances**.
3. Select the instance that you migrated and choose **Actions**,
   **Instance settings**, **Modify instance placement**.
4. For **Target dedicated host**, select the new
   Nitro-based Dedicated Host, and then choose **Save**.
5. Restart the instance. Select the instance and choose **Instance state**,
   **Start instance**.

## Step 5: Release unused Xen-based Dedicated Host

After you have migrated your workloads from the Xen-based Dedicated Host to the new Nitro-based Dedicated Host,
you can [release the Xen-based Dedicated Host](dedicated-hosts-releasing.md "dedicated-hosts-releasing.md") if you no
longer need it.
