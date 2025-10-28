# Amazon SageMaker Studio Classic Pricing

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

When the first member of your team onboards to Amazon SageMaker Studio Classic, Amazon SageMaker AI creates an
Amazon Elastic File System (Amazon EFS) volume for the team. When this member, or any member of the team, opens Studio Classic, a home directory is created in
the volume for the member. A storage charge is incurred for this directory. Subsequently,
additional storage charges are incurred for the notebooks and data files stored in the member's
home directory. For pricing information on Amazon EFS, see [Amazon EFS Pricing](https://aws.amazon.com/efs/pricing/ "https://aws.amazon.com/efs/pricing/").

Additional costs are incurred when other operations are run inside Studio Classic, for example,
running a notebook, running training jobs, and hosting a model.

For information on the costs associated with using Studio Classic notebooks, see [Usage Metering for Amazon SageMaker Studio Classic Notebooks](notebooks-usage-metering.md "notebooks-usage-metering.md").

For information about billing along with pricing examples, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

If Amazon SageMaker Studio is your default experience, see [Amazon SageMaker Studio pricing](studio-updated-cost.md "studio-updated-cost.md") for more pricing information.
