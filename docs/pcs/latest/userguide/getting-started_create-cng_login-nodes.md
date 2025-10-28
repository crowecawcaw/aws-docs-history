# Create compute node group for login

nodes in AWS PCS

A compute node group is virtual collection of compute nodes (EC2 instances) that AWS PCS
launches and manages. When you define a compute node group, you specify common traits such as EC2
instance types, minimum and maximum instance count, target VPC subnets, preferred purchase option,
and custom launch configuration. AWS PCS eﬃciently launches, manages, and terminates compute nodes
in a compute node group, according to these settings.

In this step, you will launch a static compute node group that provides interactive access
to the cluster. You can use SSH or Amazon EC2 Systems Manager (SSM) to log in to it, then run
shell commands and manage Slurm jobs.

###### To create the compute node group

- Open the [AWS PCS console](https://console.aws.amazon.com/pcs "https://console.aws.amazon.com/pcs") and navigate to
  **Clusters**.
- Select the cluster named `get-started`
- Navigate to **Compute node groups** and choose
  **Create**.
- In the **Compute node group setup** section, provide the following:
  - **Compute node group name** – Enter `login`.

- Under **Computing configuration**, enter or select these values:
  - **EC2 launch template** – Choose the launch template where the
    name is `login-getstarted-lt`
  - **IAM instance profile** – Choose the instance profile named
    `AWSPCS-getstarted-role`
  - **Subnets** – Select the subnet where the name starts with
    `hpc-networking:PublicSubnetA`.
  - **Instances** – Select `c6i.xlarge`.
  - **Scaling configuration** – For **Min. instance
    count**, enter `1`. For **Max. instance count**, enter
    `1`.

- Under **Additional settings**, specify the following:
  - **AMI ID** – Select an AMI you want to use, that has a name in the following format:

  ```
  aws-pcs-sample_ami-amzn2-`platform`-slurm-`version`
  ```

  For more information about the sample AMIs, see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md "working-with_ami_samples.md").

- Choose **Create compute node group**.
  The **Status** field shows **Creating** while the compute
  node group is being provisioned. You can proceed to the next step in the tutorial while it is in
  progress.
