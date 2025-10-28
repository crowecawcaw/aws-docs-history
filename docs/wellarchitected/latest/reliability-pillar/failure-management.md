# Failure management

######

Failures are a given and everything will eventually fail over time: from routers to hard
disks, from operating systems to memory units corrupting TCP packets, from transient errors to
permanent failures. This is a given, whether you are using the highest-quality hardware or
lowest cost components - [**Werner Vogels, CTO - Amazon.com**](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html "https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html")

Low-level hardware component failures are something to be dealt with
every day in in an on-premises data center. In the cloud, however,
you should be protected against most of these types of failures. For
example, Amazon EBS volumes are placed in a specific Availability
Zone where they are automatically replicated to protect you from the
failure of a single component. All EBS volumes are designed for
99.999% availability. Amazon S3 objects are stored across a minimum
of three Availability Zones providing 99.999999999% durability of
objects over a given year. Regardless of your cloud provider, there
is the potential for failures to impact your workload. Therefore,
you must take steps to implement resiliency if you need your
workload to be reliable.

A prerequisite to applying the best practices discussed here is that
you must ensure that the people designing, implementing, and
operating your workloads are aware of business objectives and the
reliability goals to achieve these. These people must be aware of
and trained for these reliability requirements.

The following sections explain the best practices for managing failures to prevent impact
on your workload.

###### Topics

- [Back up data](back-up-data.md "back-up-data.md")
- [Use fault isolation to protect
  your workload](use-fault-isolation-to-protect-your-workload.md "use-fault-isolation-to-protect-your-workload.md")
- [Design your workload to withstand component failures](design-your-workload-to-withstand-component-failures.md "design-your-workload-to-withstand-component-failures.md")
- [Test reliability](test-reliability.md "test-reliability.md")
- [Plan for Disaster Recovery (DR)](plan-for-disaster-recovery-dr.md "plan-for-disaster-recovery-dr.md")
