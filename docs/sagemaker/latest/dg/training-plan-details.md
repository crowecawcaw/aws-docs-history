# View training plan details

From the training plans list, follow a plan's name to view its details. Specifically,
you can check your current capacity usage, and list your workloads in your plan's details
page.

The details page shows:

- The training plan overview: Status, target, instance type, and duration.
- Expandable sections for segment details, pricing, plan name, and tags.
- Capacity utilization:

      + Total: The total number of instances reserved in this training plan.
      + In-use: The number of instances currently in use from this training plan.
      + Available instances: The number of instances currently available for use in this
       training plan.

  At the bottom of the page, a link allows you to view either the training jobs or the
  list of SageMaker HyperPod cluster instance groups associated with this plan, depending on its
  target resource.

![SageMaker AI console page displaying details of a training plan. The page shows basic plan information, status, and instance details. Below are expandable sections for additional details. At the bottom, a capacity utilization section shows total, in-use, and available instances for the plan.](images/training-plans/tp-view-training-plan.png)
