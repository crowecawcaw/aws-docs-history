# Service-managed fleets

A service-managed fleet (SMF) is a fleet of workers that have default settings provided by
Deadline Cloud. These default settings are designed to be efficient and cost-effective.

Some of the default settings limit the amount of time that workers and tasks can run. A
worker can only run for seven days and a task can only run for five days. When the limit is
reached, the task or worker stops. If this happens, you might lose work that worker or task
was running. To avoid this, monitor your workers and tasks to ensure they don't exceed the
maximum duration limits. To learn more about monitoring your workers, see [Using the Deadline Cloud monitor](working-with-deadline-monitor.md "working-with-deadline-monitor.md").

## Create a service-managed fleet

There are 3 types of instance options you can choose for your service-managed fleet; spot,
on-demand, and wait-and-save. Spot instances are unreserved capacity that you can use
at a discounted price, but might be interrupted by on-demand requests. On-demand
instances are priced by the second, have no long-term commitment, and will not be
interrupted. Wait-and-save provides delayed job scheduling for reduced cost
and can be interrupted by on-demand and spot requests.

1. From the [Deadline Cloud
   console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home"), navigate to the farm you want to create the fleet in.
2. Select the **Fleets** tab, and then choose **Create fleet**.
3. Enter a **Name** for your fleet.
4. (Optional) Enter a **Description**. A clear description can
   help you quickly identify your fleet's purpose.
5. Select **Service-managed** fleet type.
6. Choose the **Spot**, **On-demand**, or
   **Wait and Save** instance market option for your fleet.
   By default, fleets use the Spot option.
7. For service access for your fleet, select an existing role or create a new
   role. A service role provides credentials to instances in the fleet, granting
   them permission to process jobs, and to users in the monitor so that they can
   read log information.
8. Choose **Next**.
9. Choose between CPU only instances or GPU accelerated instances. GPU
   accelerated instances may be able to process your jobs faster, but can be more
   expensive.
10. Select the operating system for your workers. You can leave the default,
    **Linux** or choose **Windows**.
11. (Optional) If you selected GPU accelerated instances, set the maximum and
    minimum number of GPUs in each instance. For testing purposes you are limited to
    one GPU. To request more for your production workloads, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
    _Service Quotas User Guide_.
12. Enter the minimum and maximum **vCPUs** that you require for
    you fleet.
13. Enter the minimum and maximum **memory** that you require for
    you fleet.
14. (Optional) You can choose to allow or exclude specific instance types from
    your fleet to ensure only those instance types are used for this fleet.
15. (Optional) Set the maximum number of instances to scale the fleet so that
    capacity is available for the jobs in the queue. We recommend that you leave the
    minimum number of instances at `0` to ensure the fleet
    releases all instances when no jobs are queued.
16. (Optional) You can specify the size of the Amazon Elastic Block Store (Amazon EBS) gp3 volume that
    will be attached to the workers in this fleet. For more information, see the
    [EBS user guide](../../../ebs/latest/userguide/general-purpose.md#gp3-ebs-volume-type "../../../ebs/latest/userguide/general-purpose.md#gp3-ebs-volume-type").
17. Choose **Next**.
18. (Optional) Define custom worker capabilities that define features of this
    fleet that can be combined with custom host capabilities specified on job
    submissions. One example is a particular license type if you plan to connect
    your fleet to your own license server.
19. Choose **Next**.
20. (Optional) To associate your fleet with a queue, select a
    **queue** from the dropdown. If the queue is set up with
    the default conda queue environment, your fleet is automatically
    provided with packages that support partner DCC applications and renderers. For
    a list of provided packages, see [Default conda queue
    environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").
21. Choose **Next**.
22. (Optional) To add a tag to your fleet, choose **Add new
    tag**, and then enter the **key** and
    **value** for that tag.
23. Choose **Next**.
24. Review your fleet settings, and then choose **Create fleet**.
