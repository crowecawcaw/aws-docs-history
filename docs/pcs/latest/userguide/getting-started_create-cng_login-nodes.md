

# Create compute node group for login nodes in AWS PCS
<a name="getting-started_create-cng_login-nodes"></a>

 A compute node group is virtual collection of compute nodes (EC2 instances) that AWS PCS launches and manages. When you define a compute node group, you specify common traits such as EC2 instance types, minimum and maximum instance count, target VPC subnets, preferred purchase option, and custom launch configuration. AWS PCS eﬃciently launches, manages, and terminates compute nodes in a compute node group, according to these settings. 

 In this step, you will launch a static compute node group that provides interactive access to the cluster. You can use SSH or Amazon EC2 Systems Manager (SSM) to log in to it, then run shell commands and manage Slurm jobs. 

**To create the compute node group**
+ Open the [AWS PCS console](https://console.aws.amazon.com/pcs) and navigate to **Clusters**.
+ Select the cluster named `get-started`
+ Navigate to **Compute node groups** and choose **Create**.
+ In the **Compute node group setup** section, provide the following:
  + **Compute node group name** – Enter `login`.
+ Under **Computing configuration**, enter or select these values:
  + **EC2 launch template** – Choose the launch template where the name is `login-getstarted-lt`
  + **IAM instance profile** – Choose the instance profile named `AWSPCS-getstarted-role`
  + **Subnets** – Select the subnet where the name starts with `hpc-networking:PublicSubnetA`. Login nodes run in a public subnet so that you can reach them to log in and submit work.
  + **Instances** – Select `c6i.xlarge`.
  + **Scaling configuration** – For **Min. instance count**, enter `1`. For **Max. instance count**, enter `1`. Fixing both counts at `1` keeps a single login node running at all times as a stable entry point to the cluster.
+ Under **Additional settings**, specify the following:
  + **AMI ID** – Select an AMI you want to use, that has a name in the following format:

    ```
    aws-pcs-sample_ami-al2023-{{platform}}-slurm-{{version}}
    ```
**Note**  
Sample AMIs for Slurm 25.05 and previous versions use Amazon Linux 2 (`amzn2`) instead of Amazon Linux 2023 (`al2023`).

    For more information about the sample AMIs, see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md).
+ In the **Node lifecycle actions** section, add scripts that mount shared storage and forward node logs. Choose **Add script** for each of the following actions. Scripts run from top to bottom within a stage, so add them in the order shown. For more information about the scripts that AWS maintains, see [AWS-maintained scripts](cng-node-lifecycle-actions-vetted-scripts.md).

  1. **configure-cloudwatch-logs** – Forwards each node's lifecycle action logs to Amazon CloudWatch Logs. Configure it first so the actions that follow have their output captured from the node's first boot.
     + **Lifecycle stage** – Select `nodeBootstrapped`.
     + **Script location** – Enter `s3://aws-pcs-repo-{{region}}/aws-pcs-node-lifecycle-scripts/configure-cloudwatch-logs-v1-latest.sh`, replacing {{region}} with your cluster's AWS Region.
     + **Name** – Enter `configure-cloudwatch-logs`.
     + **Arguments** – Leave this field empty. The script automatically sends logs to the `/aws/pcs/{{cluster-id}}/lifecycle` log group.
     + **Error handling behavior** – Select `CONTINUE`.
     + **Execution policy** – Select `FIRST_BOOT_ONLY`.

  1. **configure-efs-homes** – Mounts the Amazon EFS file system as the home-directory base at `/home` and configures the node to create each user's home directory on first login.
     + **Lifecycle stage** – Select `nodeBootstrapped`.
     + **Script location** – Enter `s3://aws-pcs-repo-{{region}}/aws-pcs-node-lifecycle-scripts/configure-efs-homes-v1-latest.sh`, replacing {{region}} with your cluster's AWS Region.
     + **Name** – Enter `configure-efs-homes`.
     + **Arguments** – Enter `--efs-id {{efs-file-system-id}} --home-base /home --options tls`, replacing {{efs-file-system-id}} with the ID of the EFS file system you created earlier in the tutorial.
     + **Error handling behavior** – Select `CONTINUE`.
     + **Execution policy** – Select `EVERY_BOOT`.

  1. **mount-fsx-lustre** – Mounts the FSx for Lustre file system at `/shared` for high-performance shared scratch storage.
     + **Lifecycle stage** – Select `nodeBootstrapped`.
     + **Script location** – Enter `s3://aws-pcs-repo-{{region}}/aws-pcs-node-lifecycle-scripts/mount-fsx-lustre-v1-latest.sh`, replacing {{region}} with your cluster's AWS Region (for example, `us-east-1`).
     + **Name** – Enter `mount-fsx-lustre`.
     + **Arguments** – Enter `--fsx-dns-name {{fsx-dns-name}} --mount-name {{mount-name}} --mount-point /shared`, replacing {{fsx-dns-name}} with the **DNS name** and {{mount-name}} with the **Mount name** that you noted when you created the FSx for Lustre file system.
     + **Error handling behavior** – Select `CONTINUE`.
     + **Execution policy** – Select `EVERY_BOOT`.

  1. **set-shared-dir-mode** – Sets `/shared` to world-writable, sticky permissions (mode `1777`) so that any user can create files in it. It runs after `mount-fsx-lustre` so that it applies to the mounted file system.
     + **Lifecycle stage** – Select `nodeBootstrapped`.
     + **Script location** – Enter `https://aws-hpc-recipes.s3.us-east-1.amazonaws.com/main/recipes/pcs-scripts/open_shared_dir/assets/set-shared-dir-mode-v1.0.0.sh`. This community script is published by HPC Recipes for AWS.
     + **Name** – Enter `set-shared-dir-mode`.
     + **Arguments** – Enter `--path /shared --mode 1777`.
     + **Error handling behavior** – Select `CONTINUE`.
     + **Execution policy** – Select `EVERY_BOOT`.
+ Choose **Create compute node group**.

 The **Status** field shows **Creating** while the compute node group is being provisioned. You can proceed to the next step in the tutorial while it is in progress. 