

# Amazon S3 Files volumes
<a name="s3files-volumes"></a>

S3 Files provides direct file system access to data stored in Amazon Simple Storage Service (Amazon S3) buckets. With AWS Batch, you can define S3 Files volumes in your job definitions so that your containers can read and write Amazon S3 data using standard file operations.

To use S3 Files volumes, you need an S3 file system and mount target configured in the same VPC as your AWS Batch compute environment. For complete setup instructions including bucket configuration, IAM roles, file system creation, and mount targets, see [S3 Files prerequisites](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html) in the *Amazon S3 User Guide* and [Configuring S3 Files for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/s3files-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

## Amazon S3 Files volume considerations
<a name="s3files-volume-considerations"></a>

Consider the following when using S3 Files volumes:
+ 
**Important**  
S3 Files are not supported on the Amazon EC2 launch type at this time. If you configure an S3 file system in a job definition and attempt to run it on the Amazon EC2 launch type, the job will fail at launch. Amazon EC2 launch type support is planned for a future release.
+ Transit encryption is always enabled for S3 Files volumes. You can optionally specify the port using the `transitEncryptionPort` parameter. The default port is `2049`.
+ The job role (equivalent to the Amazon ECS task role) must have `s3files:ClientMount` and `s3files:ClientWrite` permissions on the file system. For direct reads from Amazon S3, the role also needs `s3:GetObject`, `s3:GetObjectVersion`, and `s3:ListBucket` permissions on the bucket.
+ The S3 file system mount target must be in the same VPC and reachable from the subnets of your AWS Batch compute environment. The mount target security group must allow inbound NFS traffic (TCP port 2049) from the compute environment security group.

## Use Amazon S3 Files access points
<a name="s3files-volume-accesspoints"></a>

S3 Files access points are application-specific entry points into a file system that enforce a POSIX user identity and root directory for all file system requests. You can use access points to isolate tenants so that each job can only access its own directory within a shared file system.

**Note**  
When you specify an access point using the `accessPointArn` parameter, the `rootDirectory` must either be omitted or set to `/`. The access point enforces its own root directory path.

For more information about creating and managing access points, see [Creating access points for an S3 file system](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html) in the *Amazon S3 User Guide*. For more information about using file system policies to enforce access point isolation, see [How S3 Files works with IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-security-iam.html) in the *Amazon S3 User Guide*.

## Specify an Amazon S3 Files file system in your job definition
<a name="specify-s3files-config"></a>

To use S3 Files volumes for your containers, you must specify the volume and mount point configurations in your job definition. The following job definition JSON snippet shows the syntax for the `volumes` and `mountPoints` objects for a container:

```
{
    "ecsProperties": {
        "taskProperties": [
            {
                ...,
                "taskRoleArn": "arn:aws:iam::{{<account>}}:role/{{<job-role-name>}}",
                "containers": [
                    {
                        ...,
                        "mountPoints": [
                            {
                                "sourceVolume": "{{myS3FilesVolume}}",
                                "containerPath": "{{/mnt/s3data}}",
                                "readOnly": {{false}}
                            }
                        ]
                    }
                ],
                "volumes": [
                    {
                        "name": "{{myS3FilesVolume}}",
                        "s3filesVolumeConfiguration": {
                            "fileSystemArn": "arn:aws:s3files:{{<region>}}:{{<account>}}:file-system/{{<fs-id>}}",
                            "rootDirectory": "{{/keypath/in/s3}}"
                        }
                    }
                ]
            }
        ]
    }
}
```

`s3filesVolumeConfiguration`  
Type: Object  
Required: No  
This parameter is specified when using S3 Files volumes.    
`fileSystemArn`  
Type: String  
Required: Yes  
The full ARN of the S3 file system to use.  
`rootDirectory`  
Type: String  
Required: No  
The directory within the S3 file system to mount as the root directory inside the host. If this parameter is omitted, the root of the file system is used. Specifying `/` has the same effect as omitting this parameter. It can be up to 4,096 characters in length.  
If an S3 Files access point is specified in the `accessPointArn`, the root directory parameter must either be omitted or set to `/`. This enforces the path that's set on the access point.  
`transitEncryptionPort`  
Type: Integer  
Required: No  
The port to use when sending encrypted data between the AWS Batch host and the S3 Files server. If you don't specify a transit encryption port, the default value of `2049` is used. The value must be between 0 and 65,535. Transit encryption is always enabled for S3 Files volumes.  
`accessPointArn`  
Type: String  
Required: No  
The ARN of the S3 Files access point to use. If an access point is specified, the root directory value in the `s3filesVolumeConfiguration` must either be omitted or set to `/`. This enforces the path that's set on the access point. Access points enforce a POSIX user identity and can restrict access to specific directories within the file system. For more information, see [Creating access points for an S3 file system](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html) in the *Amazon S3 User Guide*.

## Use S3 Files volumes with AWS Batch and Amazon EKS
<a name="s3files-eks-volumes"></a>

For jobs that use Amazon EKS resources, AWS Batch supports S3 Files volumes through a `persistentVolumeClaim` in the EKS job definition volume configuration. You must pre-create the persistent volume and persistent volume claim in your Amazon EKS cluster before referencing it in your job definition.

The following job definition snippet shows how to reference an S3 Files persistent volume claim:

```
{
    "eksProperties": {
        "podProperties": {
            ...,
            "containers": [
                {
                    ...,
                    "volumeMounts": [
                        {
                            "name": "{{s3files-vol}}",
                            "mountPath": "{{/mnt/s3data}}"
                        }
                    ]
                }
            ],
            "volumes": [
                {
                    "name": "{{s3files-vol}}",
                    "persistentVolumeClaim": {
                        "claimName": "{{<s3files-pvc-name>}}"
                    }
                }
            ]
        }
    }
}
```

For more information about setting up S3 Files with Amazon EKS, see [Mounting S3 file systems in Amazon EKS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-mounting-eks.html) in the *Amazon S3 User Guide*. For the full volume parameter reference, see [EksVolume](https://docs.aws.amazon.com/batch/latest/APIReference/API_EksVolume.html) in the *AWS Batch API Reference*.