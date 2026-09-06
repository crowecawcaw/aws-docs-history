

# Troubleshoot the Amazon EFS integration
<a name="sample-efs-troubleshooting"></a>

The following are errors you might encounter when setting up Amazon EFS with CodeBuild.

**Topics**
+ [CLIENT\_ERROR: mounting '127.0.0.1:/' failed. permission denied](#sample-efs-troubleshooting.permission-denied)
+ [CLIENT\_ERROR: mounting '127.0.0.1:/' failed. connection reset by peer](#sample-efs-troubleshooting.connection-reset)
+ [VPC\_CLIENT\_ERROR: Unexpected EC2 error: UnauthorizedOperation](#sample-efs-troubleshooting.unauthorized-operation)

## CLIENT\_ERROR: mounting '127.0.0.1:/' failed. permission denied
<a name="sample-efs-troubleshooting.permission-denied"></a>

IAM authorization is not supported for mounting Amazon EFS with CodeBuild. If you are using a custom Amazon EFS file system policy, you will need to grant read and write access to all IAM principals. For example:

```
"Principal": {
  "AWS": "*"
}
```

## CLIENT\_ERROR: mounting '127.0.0.1:/' failed. connection reset by peer
<a name="sample-efs-troubleshooting.connection-reset"></a>

There are two possible causes for this error:
+ The CodeBuild VPC subnet is in a different availability zone than the Amazon EFS mount target. You can resolve this by adding a VPC subnet in the same availability zone as the Amazon EFS mount target.
+ The security group does not have permissions to communicate with Amazon EFS. You can resolve this by adding an inbound rule to allow all traffic from either the VPC (add the primary CIDR block for your VPC), or the security group itself.

## VPC\_CLIENT\_ERROR: Unexpected EC2 error: UnauthorizedOperation
<a name="sample-efs-troubleshooting.unauthorized-operation"></a>

This error occurs when all of the subnets in your VPC configuration for the CodeBuild project are public subnets. You must have at least one private subnet in the VPC to ensure network connectivity. 