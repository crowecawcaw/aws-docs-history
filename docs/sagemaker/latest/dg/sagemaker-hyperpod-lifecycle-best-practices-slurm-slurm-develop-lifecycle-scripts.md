# Developing lifecycle scripts interactively on a HyperPod cluster node

This section explains how you can interactively develop lifecycle scripts without
repeatedly creating and deleting a HyperPod cluster.

1. Create a HyperPod cluster with the base lifecycle scripts.
2. Log in to a cluster node.
3. Develop a script (`configure_xyz.sh`) by editing and running it
   repeatedly on the node.
   1. HyperPod runs the lifecycle scripts as the root user, so we
      recommend that you run the `configure_xyz.sh` as the root
      user while developing to make sure that the script is tested under the
      same condition while run by HyperPod.

4. Integrate the script into `lifecycle_script.py` by adding a code
   line similar to the following.

```
ExecuteBashScript("./utils/`configure_xyz.sh`").run()
```

5. Upload the updated lifecycle scripts to the S3 bucket that you initially used
   for uploading the base lifecycle scripts.
6. Test the integrated version of `lifecycle_script.py` by creating a
   new HyperPod cluster. You can also use manual instance replacement to
   test the updated lifecycle scripts by creating new instances. For detailed
   instructions, see [Manually replace a node](sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance.md#sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance-replace "sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance.md#sagemaker-hyperpod-resiliency-slurm-replace-faulty-instance-replace"). Note that only worker nodes are
   replaceable.
