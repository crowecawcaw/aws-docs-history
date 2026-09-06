

# Developing lifecycle scripts interactively on a HyperPod cluster node
<a name="sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-develop-lifecycle-scripts"></a>

This section explains how you can interactively develop lifecycle scripts without repeatedly creating and deleting a HyperPod cluster.

1. Create a HyperPod cluster with the base lifecycle scripts.

1. Log in to a cluster node.

1. Develop a script (`configure_xyz.sh`) by editing and running it repeatedly on the node.

   1. HyperPod runs the lifecycle scripts as the root user, so we recommend that you run the `configure_xyz.sh` as the root user while developing to make sure that the script is tested under the same condition while run by HyperPod.

1. Integrate the script into `lifecycle_script.py` by adding a code line similar to the following.

   ```
   ExecuteBashScript("./utils/{{configure_xyz.sh}}").run()
   ```

1. Upload the updated lifecycle scripts to the S3 bucket that you initially used for uploading the base lifecycle scripts.

1. Test the integrated version of `lifecycle_script.py` by creating a new HyperPod cluster. You can also use manual instance replacement to test the updated lifecycle scripts by creating new instances. For detailed instructions, see [Manually replace a node](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance.html#sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance-replace). Note that only worker nodes are replaceable.