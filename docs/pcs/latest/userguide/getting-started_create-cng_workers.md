# Create compute node group for running compute jobs in AWS PCS

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
    `hpc-networking:PrivateSubnetA`. Compute nodes run in a private subnet because
    they process jobs and do not need to be reachable from the internet.
  - **Instances** – Select `c6i.xlarge`.
  - **Scaling configuration** – For **Min. instance
    count**, enter `0`. For **Max. instance count**, enter
    `4`. A minimum of `0` lets AWS PCS scale the group down to no
    instances when there are no jobs to run, so you pay for compute only when work is queued.

- Under **Additional settings**, specify the following:

  - **AMI ID** – Select an AMI you want to use, that has a name in the following format:

  ```
  aws-pcs-sample_ami-al2023-`platform`-slurm-`version`
  ```

  ###### Note

  Sample AMIs for Slurm 25.05 and previous versions use Amazon Linux 2 (`amzn2`) instead of Amazon Linux 2023 (`al2023`).

  For more information about the sample AMIs, see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md "working-with_ami_samples.md").

- In the **Node lifecycle actions** section, add scripts that mount
  shared storage and forward node logs. Choose **Add script** for each
  of the following actions. Scripts run from top to bottom within a stage, so add them in
  the order shown. For more information about the scripts that AWS maintains, see
  [AWS-maintained
  scripts](cng-node-lifecycle-actions-vetted-scripts.md "cng-node-lifecycle-actions-vetted-scripts.md").

  1.  **configure-cloudwatch-logs** – Forwards each node's lifecycle action logs to Amazon CloudWatch Logs. Configure it first so the actions that follow have their output captured from the node's first boot.

      - **Lifecycle stage** – Select
        `nodeBootstrapped`.
      - **Script location** – Enter
        `s3://aws-pcs-repo-`region`/aws-pcs-node-lifecycle-scripts/configure-cloudwatch-logs-v1-latest.sh`,
        replacing `region` with your cluster's AWS Region.
      - **Name** – Enter
        `configure-cloudwatch-logs`.
      - **Arguments** – Leave this field empty. The script
        automatically sends logs to the
        `/aws/pcs/`cluster-id`/lifecycle` log group.
      - **Error handling behavior** – Select
        `CONTINUE`.
      - **Execution policy** – Select
        `FIRST_BOOT_ONLY`.

  2.  **configure-efs-homes** – Mounts the Amazon EFS file system as the home-directory base at `/home` and configures the node to create each user's home directory on first login.

      - **Lifecycle stage** – Select
        `nodeBootstrapped`.
      - **Script location** – Enter
        `s3://aws-pcs-repo-`region`/aws-pcs-node-lifecycle-scripts/configure-efs-homes-v1-latest.sh`,
        replacing `region` with your cluster's AWS Region.
      - **Name** – Enter
        `configure-efs-homes`.
      - **Arguments** – Enter
        `--efs-id `efs-file-system-id` --home-base /home --options tls`,
        replacing `efs-file-system-id` with the ID of the EFS file
        system you created earlier in the tutorial.
      - **Error handling behavior** – Select
        `CONTINUE`.
      - **Execution policy** – Select
        `EVERY_BOOT`.

  3.  **mount-fsx-lustre** – Mounts the FSx for Lustre file system at `/shared` for high-performance shared scratch storage.

      - **Lifecycle stage** – Select
        `nodeBootstrapped`.
      - **Script location** – Enter
        `s3://aws-pcs-repo-`region`/aws-pcs-node-lifecycle-scripts/mount-fsx-lustre-v1-latest.sh`,
        replacing `region` with your cluster's AWS Region (for
        example, `us-east-1`).
      - **Name** – Enter
        `mount-fsx-lustre`.
      - **Arguments** – Enter
        `--fsx-dns-name `fsx-dns-name`--mount-name`mount-name` --mount-point /shared`,
        replacing `fsx-dns-name` with the **DNS name**
        and `mount-name` with the **Mount name** that you
        noted when you created the FSx for Lustre file system.
      - **Error handling behavior** – Select
        `CONTINUE`.
      - **Execution policy** – Select
        `EVERY_BOOT`.

  4.  **set-shared-dir-mode** – Sets `/shared` to world-writable, sticky permissions (mode `1777`) so that any user can create files in it. It runs after `mount-fsx-lustre` so that it applies to the mounted file system.

      - **Lifecycle stage** – Select
        `nodeBootstrapped`.
      - **Script location** – Enter
        `https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/pcs-scripts/open_shared_dir/assets/set-shared-dir-mode-v1.0.0.sh`.
        This community script is published by HPC Recipes for AWS.
      - **Name** – Enter
        `set-shared-dir-mode`.
      - **Arguments** – Enter
        `--path /shared --mode 1777`.
      - **Error handling behavior** – Select
        `CONTINUE`.
      - **Execution policy** – Select
        `EVERY_BOOT`.

- Choose **Create compute node group**.
  The **Status** field shows **Creating** while the compute
  node group is being provisioned.

###### Important

Wait for the **Status** field to show **Active** before
proceeding to the next step in this tutorial.
