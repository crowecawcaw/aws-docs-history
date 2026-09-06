

# Giving Amazon GameLift Streams access to resources in an Amazon VPC
<a name="vpc-connectivity"></a>

By default, Amazon GameLift Streams runs your streaming applications on compute resources that have access to the public internet but not to resources in your private Amazon VPCs. To give your streaming applications access to private resources such as databases, cache servers, or internal APIs, you can configure VPC connectivity when creating a stream group.

Amazon GameLift Streams uses AWS Transit Gateway to establish private network connectivity between the service-managed VPC where your streams run and your own Amazon VPC. This allows your streaming applications to communicate with resources in your Amazon VPC over private IP addresses without exposing traffic to the public internet.