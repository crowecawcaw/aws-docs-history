# EC2 Containment

The `AWSSupport-ContainEC2Instance` containment automation performs a reversible network containment
of an EC2 instance, leaving the instance intact and running, but isolating it from any new network activity
and preventing it from communicating with resources within and outside your VPC.

###### Important

It is important to note that existing tracked connections won't be shut down as a result of changing
security groups – only future traffic will be effectively blocked by the new security group and this SSM document.
More information is available in the [source containment](source-containment.md "source-containment.md") section of the service technical guide.
