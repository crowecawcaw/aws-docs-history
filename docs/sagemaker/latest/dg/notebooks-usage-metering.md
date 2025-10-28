# Usage Metering for Amazon SageMaker Studio Classic Notebooks

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

There is no additional charge for using Amazon SageMaker Studio Classic. The costs incurred for running
Amazon SageMaker Studio Classic notebooks, interactive shells, consoles, and terminals are based on Amazon Elastic Compute Cloud
(Amazon EC2) instance usage.

When you run the following resources, you must choose a SageMaker image and kernel:

###### From the Studio Classic Launcher

- Notebook
- Interactive Shell
- Image Terminal

###### From the **File** menu

- Notebook
- Console
  When launched, the resource is run on an Amazon EC2 instance of the chosen instance type. If an
  instance of that type was previously launched and is available, the resource is run on that
  instance.

For CPU based images, the default suggested instance type is `ml.t3.medium`.
For GPU based images, the default suggested instance type is
`ml.g4dn.xlarge`.

The costs incurred are based on the instance type. You are billed separately for each
instance.

Metering starts when an instance is created. Metering ends when all the apps on the
instance are shut down, or the instance is shut down. For information about how to shut down
an instance, see [Shut Down Resources from
Amazon SageMaker Studio Classic](notebooks-run-and-manage-shut-down.md "notebooks-run-and-manage-shut-down.md").

###### Important

You must shut down the instance to stop incurring charges. If you shut down the notebook
running on the instance but don't shut down the instance, you will still incur charges. When
you shut down the Studio Classic notebook instances, any additional resources, such as SageMaker AI
endpoints, Amazon EMR clusters, and Amazon S3 buckets created from Studio Classic are not deleted. Delete
those resources to stop accrual of charges.

When you open multiple notebooks on the same instance type, the notebooks run on the same
instance even if they are using different kernels. You are billed only for the time that one
instance is running.

You can change the instance type from within the notebook after you open it. For more
information, see [Change the Instance
Type for an Amazon SageMaker Studio Classic Notebook](notebooks-run-and-manage-switch-instance-type.md "notebooks-run-and-manage-switch-instance-type.md").

For information about billing along with pricing examples, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
