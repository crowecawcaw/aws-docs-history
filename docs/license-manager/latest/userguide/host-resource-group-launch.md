

# Launch an instance in a host resource group in License Manager
<a name="host-resource-group-launch"></a>

When you launch an instance, you can specify a host resource group. The launch requirements depend on the host resource group's instance launch option:
+ **License configuration required** – You must associate one or more core- or socket-based self-managed licenses with the AMI that match the license configurations configured in the host resource group, or provide the license configurations in the instance launch request.
+ **License configuration not required** – You can launch with any AMI. You do not need to set up a license configuration.

For example, you can use the following [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command.

```
aws ec2 run-instances --min-count {{2}} --max-count {{2}} \
--instance-type {{c5.2xlarge}} --image-id ami-{{0abcdef1234567890}} \
--placement="Tenancy=host,HostResourceGroupArn={{arn}}"
```

You can also use the Amazon EC2 console. For more information, see [Launching Instances into a host resource group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#launching-hrg-instances) in the *Amazon EC2 User Guide*.