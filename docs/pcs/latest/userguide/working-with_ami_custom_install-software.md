# Step 4 – (Optional) Install

additional drivers, libraries, and application software

Install additional drivers, libraries, and application software on the temporary instance.
The installation procedures will vary depending on the specific applications and libraries. If
you have not built a custom AMI for AWS PCS before, we recommend you first build and test an
AMI with just the AWS PCS software and Slurm installed, then incrementally add your own
software and configurations once you have confirmed initial success.

###### Examples

- Elastic Fabric Adapter (EFA) software. For more information, see [Get started
  with EFA and MPI for HPC workloads on Amazon EC2](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable") in the _Amazon Elastic Compute Cloud User
  Guide_.
- Amazon Elastic File System (Amazon EFS) client. For more information, see [Manually installing the Amazon EFS
  client](../../../efs/latest/ug/installing-amazon-efs-utils.md "../../../efs/latest/ug/installing-amazon-efs-utils.md") in the _Amazon Elastic File System User Guide_.
- Lustre client, to use Amazon FSx for Lustre and Amazon File Cache. For more information, see [Installing the
  Lustre client](../../../fsx/latest/LustreGuide/install-lustre-client.md "../../../fsx/latest/LustreGuide/install-lustre-client.md") in the _FSx for Lustre User Guide_.
- Amazon CloudWatch agent, to use CloudWatch Logs and Metrics. For more information, see [Install
  the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md") in the _Amazon CloudWatch User Guide_.
- AWS Neuron, to use **trn\*** and **inf\*** instance types. For more information, see the [AWS Neuron
  documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/ "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/").
- NVIDIA Driver, CUDA, and DCGM, to use **p\*** or **g\*** instance types.
