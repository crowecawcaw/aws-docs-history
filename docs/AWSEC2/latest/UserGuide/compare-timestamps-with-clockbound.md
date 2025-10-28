# Compare timestamps for your Linux

instances

If you're using the Amazon Time Sync Service, you can compare the timestamps on your Amazon EC2 Linux
instances with ClockBound to determine the true time of an event. ClockBound measures
the clock accuracy of your EC2 instance, and allows you to check if a given timestamp is
in the past or future with respect to your instance's current clock. This information is
valuable for determining the order and consistency of events and transactions across EC2
instances, independent of each instance's geographic location.

ClockBound is an open source daemon and library. To learn more about ClockBound,
including installation instructions, see [ClockBound](https://github.com/aws/clock-bound "https://github.com/aws/clock-bound") on _GitHub_.

ClockBound is only supported for Linux instances.

If you're using the direct PTP connection to the PTP hardware clock, your time daemon,
such as chrony, will underestimate the clock error bound. This is because
a PTP hardware clock does not pass the correct error bound information to
chrony, the way that NTP does. As a result, your clock
synchronization daemon assumes the clock is accurate to UTC and thus has an error bound
of `0`. To measure the full error bound, the Nitro System calculates the
error bound of the PTP hardware clock, and makes it available to your EC2 instance over
the ENA driver `sysfs` filesystem. You can read this directly as a value, in
nanoseconds.

###### To retrieve the PTP hardware clock error bound

1.  First get the correct location of the PTP hardware clock device by using one
    of the following commands. The path in the command is different depending on the
    AMI used to launch the instance.

        * For Amazon Linux 2:



        ```
        cat /sys/class/net/eth0/device/uevent | grep PCI_SLOT_NAME
        ```
        * For Amazon Linux 2023:



        ```
        cat /sys/class/net/ens5/device/uevent | grep PCI_SLOT_NAME
        ```

    The output is the PCI slot name, which is the location of the PTP hardware
    clock device. In this example, the location is `0000:00:03.0`.

```
PCI_SLOT_NAME=`0000:00:03.0`
```

2. To retrieve the PTP hardware clock error bound, run the following command.
   Include the PCI slot name from the previous step.

```
cat /sys/bus/pci/devices/`0000:00:03.0`/phc_error_bound
```

The output is the clock error bound of the PTP hardware clock, in
nanoseconds.
To calculate the correct clock error bound at a specific point in time when using the
direct PTP connection to the PTP hardware clock, you must add the clock error bound from
chrony or ClockBound at the time that chrony polls the
PTP hardware clock. For more information about measuring and monitoring clock accuracy,
see [Manage Amazon EC2 instance clock accuracy using Amazon Time Sync Service and Amazon
CloudWatch – Part 1](https://aws.amazon.com/blogs/mt/manage-amazon-ec2-instance-clock-accuracy-using-amazon-time-sync-service-and-amazon-cloudwatch-part-1/ "https://aws.amazon.com/blogs/mt/manage-amazon-ec2-instance-clock-accuracy-using-amazon-time-sync-service-and-amazon-cloudwatch-part-1/").
