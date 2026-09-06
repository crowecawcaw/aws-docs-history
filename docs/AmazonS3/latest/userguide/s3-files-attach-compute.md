

# Mounting your S3 buckets on compute resources
<a name="s3-files-attach-compute"></a>

You can mount an S3 file system on compute resources to access your S3 data as files. Your compute resource must run in the same Amazon Virtual Private Cloud (Amazon VPC) as the S3 file system. All compute resources communicate with the file system through mount targets on NFS port 2049.

S3 Files supports the following compute environments:
+ [Amazon Elastic Compute Cloud (Amazon EC2) instances](s3-files-mounting.md)
+ [AWS Lambda functions](s3-files-mounting-lambda.md)
+ [Amazon Elastic Kubernetes Service (Amazon EKS) clusters](s3-files-mounting-eks.md)
+ [Amazon Elastic Container Service (Amazon ECS) clusters](s3-files-mounting-ecs.md)