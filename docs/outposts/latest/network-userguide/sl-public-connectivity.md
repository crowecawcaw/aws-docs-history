

# Service link public connectivity options
<a name="sl-public-connectivity"></a>

You can configure the service link with a public connection for the traffic between the Outposts and home AWS Region. You can choose to use the public internet or Direct Connect public VIFs.

If you plan on allow-listing only AWS Region public IPs (instead of 0.0.0.0/0) on your firewalls, you must ensure that your firewall rules are up-to-date with the current IP address ranges. For more information, see [AWS IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html) in the *Amazon VPC User Guide*.

The following image shows both options to establish a service link public connection between your Outposts and the AWS Region:

![The service link public connection options.](http://docs.aws.amazon.com/outposts/latest/network-userguide/images/outpost-rack2ndgen-sl-public-connection-options.PNG)


**Note**  
Second-generation Outposts racks require a /24 or larger subnet for the service link infrastructure. This subnet is customer-provided IP address space used by Outpost networking devices to establish connectivity to AWS Region endpoints.

## Option 1. Public connectivity through the internet
<a name="sl-public-internet-option"></a>

This option requires the AWS Outposts [service link infrastructure subnet IPs](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#service-link-subnet) to have access to the public IP ranges of your AWS Region or home Region. You must allow-list AWS Region public IPs or 0.0.0.0/0 on networking devices such as your firewall.

## Option 2. Public connectivity through Direct Connect public VIFs
<a name="sl-dx-public-vif-option"></a>

This option requires the AWS Outposts [service link infrastructure subnet IPs](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#service-link-subnet) to have access to the public IP ranges of your AWS Region or home Region over DX service. You must allow-list AWS Region public IPs or 0.0.0.0/0 on networking devices such as your firewall.