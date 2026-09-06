

# Using Amazon SageMaker Ground Truth in an Amazon Virtual Private Cloud
<a name="sms-vpc"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

 With [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html) (Amazon VPC) you can launch AWS resources in a logically isolated virtual network that you define. Ground Truth supports running labeling jobs inside an Amazon VPC instead of connecting over the internet. When you launch a labeling job in an Amazon VPC, communication between your VPC and Ground Truth is conducted entirely and securely within the AWS network.

This guide shows how you can use Ground Truth in an Amazon VPC in the following ways:

1. [Run an Amazon SageMaker Ground Truth Labeling Job in an Amazon Virtual Private Cloud](samurai-vpc-labeling-job.md)

1. [Use Amazon VPC Mode from a Private Worker Portal](samurai-vpc-worker-portal.md)