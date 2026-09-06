

# Reviewing environment variables reference
<a name="sagemaker-hyperpod-multihead-slurm-variables-reference"></a>

The following environment variables are defined and used in the tutorial of [Setting up multiple controller nodes for a SageMaker HyperPod Slurm cluster](sagemaker-hyperpod-multihead-slurm-setup.md). These environment variables are only available in the current session unless explicitly preserved. They are defined using the `$variable_name` syntax. Variables with key/value pairs represent AWS-created resources, while variables without keys are user-defined.


**Environment variables reference**  

| Variable | Description | 
| --- | --- | 
| $BACKUP\_SUBNET |  +  Example key: `BackupPrivateSubnet` <br />+  Example value: `{{subnet-04a8ab51748510a51}}` <br />+  Description: The backup private subnet ID used for HyperPod Slurm cluster creation.   | 
| $COMPUTE\_IG\_NAME |  +  Example value: `{{compute-nodes}}` <br />+  Description: The name of the compute instance group used for cluster creation.   | 
| $COMPUTE\_NODE\_ROLE |  +  Example key: `AmazonSagemakerClusterExecutionRoleArn` <br />+  Example value: `{{arn:aws:iam::111122223333:role/sagemaker-hyperpod-AmazonSagemakerClusterExecutionR-123OTacPcKk1}}` <br />+  Description: The Amazon Resource Name (ARN) of the IAM role for the compute instance group.   | 
| $CONTOLLER\_IG\_NAME |  +  Example value: `{{controller-machine}}` <br />+  Description: The name of the controller instance group for cluster creation.   | 
| $DB\_USER\_NAME |  +  Example value: `{{mydbuser}}` <br />+  Description: The database username for Slurm accounting database access, used in [Provision additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead).   | 
| $EMAIL |  +  Example value: `{{123abc@email.com}}` <br />+  Description: The email address for Amazon SNS notifications, used in [Provision additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead).   | 
| $PRIMARY\_SUBNET |  +  Example key: `PrimaryPrivateSubnet` <br />+  Example value: `{{subnet-01a56ebc42df102a7}}` <br />+  Description: The primary private subnet ID used for HyperPod Slurm cluster creation.   | 
| $POLICY |  +  Example value: `{{arn:aws:iam::111122223333:policy/AmazonSagemakerExecutionPolicy}}` <br />+  Description: The IAM policy ARN you create and attach to the Slurm execution role for the controller instance group.   | 
| $REGION |  +  Example value: `{{us-east-1}}` <br />+  Description: The AWS Region where you create all the resources.   | 
| $ROOT\_BUCKET\_NAME |  +  Example key: `SecurityGroup` <br />+  Example value: `{{sagemaker-lifecycle-ab214000}}` <br />+  Description: The name of the Amazon S3 bucket where lifecycle scripts are uploaded.   | 
| $SECURITY\_GROUP |  +  Example key: `AmazonS3BucketName` <br />+  Example value: `{{sg-006a5d175cb35675a}}` <br />+  Description: The security group ID used for [Provision additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead).   | 
| $SLURM\_DB\_ENDPOINT\_ADDRESS |  +  Example key: `SlurmDBEndpointAddress` <br />+  Example value: `{{sagemaker-hyperpod-mh-slurmdbinstance-sxcmatjv0ei0.clplgxt06ysb.us-east-1.rds.amazonaws.com}}` <br />+  Description: The Amazon RDS database endpoint used in cluster creation.   | 
| $SLURM\_DB\_SECRET\_ARN |  +  Example key: `SlurmDBSecretArn` <br />+  Example value: `{{arn:aws:secretsmanager:us-east-1:111122223333:secret:sagemaker-hyperpod-mh-db-secret-us-east-1-dmz72K}}` <br />+  Description: The database secret ARN used in cluster creation.   | 
| $SLURM\_EXECUTION\_ROLE\_ARN |  +  Example key: `SlurmExecutionRoleArn` <br />+  Example value: `{{arn:aws:iam::111122223333:role/sagemaker-hyperpod-mhSlurmExecutionRole-us-east-1}}` <br />+  Description: The IAM role ARN for the controller instance group, used in cluster creation.   | 
| $SLURM\_FSX\_DNS\_NAME |  +  Example key: `FSxLustreFilesystemDNSname` <br />+  Example value: `{{fs-0662da327f9326017.fsx.us-east-1.amazonaws.com}}` <br />+  Description: The Domain Name System (DNS) of the FSx for Lustre filesystem, used in [Provision additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead) and [Create configuration file](sagemaker-hyperpod-multihead-slurm-scripts.md#sagemaker-hyperpod-multihead-slurm-update-config-file).   | 
| $SLURM\_FSX\_MOUNT\_NAME |  +  Example key: `FSxLustreFilesystemMountname` <br />+  Example value: `{{lbajka4v}}` <br />+  Description: The mount ID of the FSx for Lustre filesystem, used in [Provision additional resources to support multiple controller nodes](sagemaker-hyperpod-multihead-slurm-cfn.md#sagemaker-hyperpod-multihead-slurm-cfn-multihead) and [Create configuration file](sagemaker-hyperpod-multihead-slurm-scripts.md#sagemaker-hyperpod-multihead-slurm-update-config-file).   | 
| $SLURM\_SNS\_FAILOVER\_TOPIC\_ARN |  +  Example key: `SlurmFailOverSNSTopicArn` <br />+  Example value: `{{arn:aws:sns:us-east-1:111122223333:sagemaker-hyperpod-mhSlurmFailOverTopic-us-east-1}}` <br />+  Description: The Amazon SNS topic ARN, used in [Create configuration file](sagemaker-hyperpod-multihead-slurm-scripts.md#sagemaker-hyperpod-multihead-slurm-update-config-file).   | 