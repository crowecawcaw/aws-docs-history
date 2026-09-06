

# Step 4 – (Optional) Install additional drivers, libraries, and application software
<a name="working-with_ami_custom_install-software"></a>

Install additional drivers, libraries, and application software on the temporary instance. The installation procedures will vary depending on the specific applications and libraries. If you have not built a custom AMI for AWS PCS before, we recommend you first build and test an AMI with just the AWS PCS software and Slurm installed, then incrementally add your own software and configurations once you have confirmed initial success. 

**Examples**
+  Elastic Fabric Adapter (EFA) software. For more information, see [Get started with EFA and MPI for HPC workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-enable) in the *Amazon Elastic Compute Cloud User Guide*. 
+  Amazon Elastic File System (Amazon EFS) client. For more information, see [Manually installing the Amazon EFS client](https://docs.aws.amazon.com/efs/latest/ug/installing-amazon-efs-utils.html) in the *Amazon Elastic File System User Guide*. 
+  Lustre client, to use Amazon FSx for Lustre and Amazon File Cache. For more information, see [Installing the Lustre client](https://docs.aws.amazon.com/fsx/latest/LustreGuide/install-lustre-client.html) in the *FSx for Lustre User Guide*. 
+  Amazon CloudWatch agent, to use CloudWatch Logs and Metrics. For more information, see [Install the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) in the *Amazon CloudWatch User Guide*. 
+  AWS Neuron, to use **trn\*** and **inf\*** instance types. For more information, see the [AWS Neuron documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/). 
+  NVIDIA Driver, CUDA, and DCGM, to use **p\*** or **g\*** instance types. 