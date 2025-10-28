# Network traffic rules for integrating with Amazon EMR

When Apache Ranger is integrated with your EMR cluster, the cluster needs to
communicate with additional servers and AWS.

All Amazon EMR nodes, including core and task nodes, must be able to communicate
with the Apache Ranger Admin servers to download policies. If your Apache Ranger
Admin is running on Amazon EC2, you need to update the security group to be able to
take traffic from the EMR cluster.

In addition to communicating with the Ranger Admin server, all nodes need to
be able to communicate with the following AWS services:

- Amazon S3
- AWS KMS (if using EMRFS SSE-KMS)
- Amazon CloudWatch
- AWS STS
  If you are planning to run your EMR cluster within a private subnet, configure
  the VPC to be able to communicate with these services using either [AWS PrivateLink and
  VPC endpoints](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") in the _Amazon VPC User Guide_ or using
  [network address translation (NAT) instance](../../../vpc/latest/userguide/VPC_NAT_Instance.md "../../../vpc/latest/userguide/VPC_NAT_Instance.md") in the
  _Amazon VPC User Guide_.
