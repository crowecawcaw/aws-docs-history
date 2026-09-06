NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Installing the AWS Transform MGN vCenter Client for Agentless Replication on vCenter source environments

AWS Transform MGN allows you to perform agentless snapshot replication from your vCenter
source environment into AWS. This is achieved by installing the MGN vCenter Client in your
vCenter environment. MGN recommends using agent-based replication when possible, as it
supports CDP (Continuous Data Protection) and provides the shortest cutover window. Agentless
replication should be used when your company’s policies prevent you from installing the AWS
Replication Agent on each individual server.

###### Topics

- [Agentless replication overview](installing-vcenter-overview-mgn.md "installing-vcenter-overview-mgn.md")
- [VMware limitations](installing-vcenter-reques-mgn.md "installing-vcenter-reques-mgn.md")
- [Generating vCenter Client IAM credentials](vcenter-credentials-mgn.md "vcenter-credentials-mgn.md")
- [Installing the MGN vCenter Client](installing-vcenter-appliance-mgn.md "installing-vcenter-appliance-mgn.md")
- [Replicating servers from vCenter to AWS](replicating-vcenter-aws-mgn.md "replicating-vcenter-aws-mgn.md")
- [Updating the vCenter or AWS Credentials](updating-vcenter-or-aws-credentials.md "updating-vcenter-or-aws-credentials.md")
- [Differentiating agentless and agent-based servers](differences-vcenter-aws.md "differences-vcenter-aws.md")
