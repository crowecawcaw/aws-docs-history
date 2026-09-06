

# Using sample Amazon Machine Images (AMIs) with AWS PCS
<a name="working-with_ami_samples"></a>

AWS provides [sample AMIs](ami-release-notes.md) that you can use as a starting point for working with AWS PCS.

**Important**  
Sample AMIs are for demonstration purposes and are not recommended for production workloads.

**Important**  
Compute node groups configured with AWS PCS sample AMIs and multiple network interfaces won't work currently if the subnets are only configured to use IPv6. Use dual-stack subnets (IPv4 and IPv6) or IPv4-only subnets instead.

## Find current AWS PCS sample AMIs
<a name="working-with_ami_samples_find"></a>

------
#### [ AWS Management Console ]

 AWS PCS sample AMIs have the following naming convention: 

```
aws-pcs-sample_ami-{{OS}}-{{architecture}}-{{scheduler}}-{{scheduler-major-version}}
```

**Accepted values**
+  {{OS}} – `al2023` 
+  {{architecture}} – `x86_64` or `arm64` 
+  {{scheduler}} – `slurm` 
+  {{scheduler-major-version}} – `25.11` 

**To find AWS PCS sample AMIs**

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2).

1. Navigate to **AMIs**.

1. Choose **Public images**.

1. In **Find AMI by attribute or tag**, search for an AMI using the templated name.

**Examples**
   + Sample AMI for Slurm 25.11 on Arm64 instances

     ```
     aws-pcs-sample_ami-al2023-arm64-slurm-25.11
     ```
   + Sample AMI for Slurm 25.11 on x86 instances

     ```
     aws-pcs-sample_ami-al2023-x86_64-slurm-25.11
     ```
**Note**  
If there are multiple AMIs, use the AMI with the most recent time stamp.
**Note**  
Sample AMIs for Slurm 25.05 use Amazon Linux 2 (`amzn2`) instead of Amazon Linux 2023 (`al2023`).

1. Use the AMI ID when you create or update a compute node group.

------
#### [ AWS CLI ]

You can find the latest AWS PCS sample AMI with the commands that follow. Replace {{region-code}} with the AWS Region where you use AWS PCS, such as `us-east-1`.
+ **x86\_64**

  ```
  aws ec2 describe-images --region {{region-code}} --owners amazon \
  --filters 'Name=name,Values=aws-pcs-sample_ami-al2023-x86_64-slurm-25.11*' \
              'Name=state,Values=available' \
  --query 'sort_by(Images, &CreationDate)[-1].[Name,ImageId]' --output text
  ```
+ **Arm64**

  ```
  aws ec2 describe-images --region {{region-code}} --owners amazon \
  --filters 'Name=name,Values=aws-pcs-sample_ami-al2023-arm64-slurm-25.11*' \
              'Name=state,Values=available' \
  --query 'sort_by(Images, &CreationDate)[-1].[Name,ImageId]' --output text
  ```

Use the AMI ID when you create or update a compute node group.

------

## Learn more about AWS PCS sample AMIs
<a name="working-with_ami_samples_learn"></a>

To view the contents, configuration details for current and previous releases of the AWS PCS sample AMIs, see [Release notes for AWS PCS sample AMIs](ami-release-notes.md).

## Build your own AMIs compatible with AWS PCS
<a name="working-with_ami_samples_build"></a>

To learn how to build your own AMIs that work with AWS PCS, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md).