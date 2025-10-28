# Launch an instance in a host resource group in License Manager

When you launch an instance, you can specify a host resource group. For example, you can
use the following [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command. You must associate a core- or socket-based self-managed license with the AMI.

```
`aws ec2 run-instances --min-count `2` --max-count `2` \
--instance-type `c5.2xlarge` --image-id ami-`0abcdef1234567890` \
--placement="Tenancy=host,HostResourceGroupArn=`arn`"`
```

You can also use the Amazon EC2 console. For more information, see [Launching
Instances into a host resource group](../../../AWSEC2/latest/UserGuide/how-dedicated-hosts-work.md#launching-hrg-instances "../../../AWSEC2/latest/UserGuide/how-dedicated-hosts-work.md#launching-hrg-instances") in the _Amazon EC2 User
Guide_.
