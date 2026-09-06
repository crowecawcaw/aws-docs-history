

# Identify EFA-enabled EC2 instances
<a name="working-with_networking_efa_identify-instances"></a>

To use EFA, all instance types that are allowed for an AWS PCS compute group must support EFA, and must have the same number of vCPUs (and GPUs if appropriate). For a list of EFA-enabled instances, see [Elastic Fabric Adapter for HPC and ML workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon Elastic Compute Cloud User Guide*. You can also use the AWS CLI to view a list of instance types that support EFA. Replace {{region-code}} with the AWS Region where you use AWS PCS, such as `us-east-1`.

```
aws ec2 describe-instance-types \ 
   --region {{region-code}} \ 
   --filters Name=network-info.efa-supported,Values=true \ 
   --query "InstanceTypes[*].[InstanceType]" \
   --output text | sort
```

**Note**  
**Determine how many network interfaces are available** – Some EC2 instances have multiple network cards. This allows them to have multiple EFAs. For more information, see [Multiple network interfaces in AWS PCS](working-with_networking_multi-nic.md).