# Updating a cluster with new or updated lifecycle scripts

There are three ways to update the HyperPod cluster software.

- The `UpdateClusterSoftware` API for patching the HyperPod
  software re-runs the lifecycle scripts on the entire instance group.
- The `UpdateCluster` API only runs the lifecycle scripts for new
  instance groups.
- You can also run lifecycle scripts directly in the HyperPod
  instances.

###### Note

HyperPod runs [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami") on
each instance of a cluster, and the AMI has pre-installed software packages
complying compatibilities between them and HyperPod functionalities. Note
that if you reinstall any of the pre-installed packages, you are responsible for
installing compatible packages and note that some HyperPod functionalities
might not work as expected.
