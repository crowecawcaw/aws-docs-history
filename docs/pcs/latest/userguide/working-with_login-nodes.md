# AWS PCS login nodes

An AWS PCS cluster usually needs at least 1 login node to support interactive access and
job management. A way to accomplish this is with a static AWS PCS compute node group configured
for login node capability. You can also configure a standalone EC2 instance to act as a
login node.

###### Topics

- [Using an AWS PCS
  compute node group to provide login nodes](working-with_login-nodes_compute-node-group-for-login.md "working-with_login-nodes_compute-node-group-for-login.md")
- [Using standalone instances as AWS PCS
  login nodes](working-with_login-nodes_standalone.md "working-with_login-nodes_standalone.md")
- [Connecting a standalone login node to multiple
  clusters in AWS PCS](multi-cluster-login-script.md "multi-cluster-login-script.md")
