# Create compute node group for running compute

jobs in AWS PCS

In this step, you will launch a compute node group that scales elastically to run jobs
submitted to the cluster.

###### To create the compute node group

- Open the [AWS PCS console](https://console.aws.amazon.com/pcs "https://console.aws.amazon.com/pcs") and navigate to
  **Clusters**.
- Select the cluster named `get-started`
- Navigate to **Compute node groups** and choose
  **Create**.
- In the **Compute node group setup** section, provide the following:
  - **Compute node group name** – Enter
    `compute-1`.

- Under **Computing configuration**, enter or select these values:
  - **EC2 launch template** – Choose the launch template where the
    name is `compute-getstarted-lt`
  - **IAM instance profile** – Choose the instance profile named
    `AWSPCS-getstarted-role`
  - **Subnets** – Select the subnet where the name starts with
    `hpc-networking:PrivateSubnetA`.
  - **Instances** – Select `c6i.xlarge`.
  - **Scaling configuration** – For **Min. instance
    count**, enter `0`. For **Max. instance count**, enter
    `4`.

- Under **Additional settings**, specify the following:
  - **AMI ID** – Select an AMI you want to use, that has a name in the following format:

  ```
  aws-pcs-sample_ami-amzn2-`platform`-slurm-`version`
  ```

  For more information about the sample AMIs, see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md "working-with_ami_samples.md").

- Choose **Create compute node group**.
  The **Status** field shows **Creating** while the compute
  node group is being provisioned.

###### Important

Wait for the **Status** field to show **Active** before
proceeding to the next step in this tutorial.
