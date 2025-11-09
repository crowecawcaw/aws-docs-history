# Client.UnsupportedOperation: Instances can only be launched within Amazon VPC in this region

**Service:**
Amazon EC2

**Issue:** When I attempt to launch an instance by using the CLI or API, I get a "Client.UnsupportedOperation: Instances can only be launched within Amazon VPC in this region" error.

**Cause:** Your account might not have a VPC.

**Recommended Action:** Verify that your account has a VPC. If not, create a VPC and then use it to launch instances.

In some cases, your account might have a default VPC. For more information, see [Determining if your account has a default VPC](govcloud-ec2.md#govcloud-ec2-vpc "govcloud-ec2.md#govcloud-ec2-vpc"). If you still receive this error when you run the `ec2-run-instances` command (or the `RunInstances` action) to launch an Amazon EC2 instance, you must specify the `subnet` parameter. Although the `subnet` parameter is optional in other regions, if you omit it in the AWS GovCloud (US-West) Region, you receive an error.
