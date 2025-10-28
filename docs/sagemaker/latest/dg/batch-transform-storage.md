# Storage in Batch Transform

When you run a batch transform job, Amazon SageMaker AI attaches an Amazon Elastic Block Store storage volume to
Amazon EC2 instances that process your job. The volume stores your model, and the size of the
storage volume is fixed at 30 GB. You have the option to encrypt your model at rest in
the storage volume.

###### Note

If you have a large model, you may encounter an `InternalServerError`.

For more information about Amazon EBS storage and features, see the following pages:

- [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") in the Amazon EC2 User Guide
- [Amazon EBS volumes](../../../AWSEC2/latest/UserGuide/ebs-volumes.md "../../../AWSEC2/latest/UserGuide/ebs-volumes.md") in the Amazon EC2 User Guide

###### Note

G4dn instances come with their own local SSD storage. To learn more about G4dn instances, see the [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/ "https://aws.amazon.com/ec2/instance-types/g4/") page.
