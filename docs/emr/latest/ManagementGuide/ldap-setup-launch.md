# Launch an EMR cluster that authenticates with

LDAP

Use the following steps to launch an EMR cluster with LDAP or Active Directory.

1. Set up your environment:
   - Make sure that the nodes on your EMR cluster can communicate
     with Amazon S3 and AWS Secrets Manager. For more information on how to modify your
     EC2 instance profile role to communicate with these services, see
     [Add AWS Secrets Manager permissions to the Amazon EMR instance
     role](ldap-setup-asm.md "ldap-setup-asm.md").
   - If you plan to run your EMR cluster in a private subnet, you
     should use AWS PrivateLink and Amazon VPC endpoints, or use network address
     transalation (NAT) to configure the VPC to communicate with S3 and
     Secrets Manager. For more information, see [AWS PrivateLink and VPC endpoints](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") and [NAT
     instances](../../../vpc/latest/userguide/VPC_NAT_Instance.md "../../../vpc/latest/userguide/VPC_NAT_Instance.md") in the
     _Amazon VPC Getting Started Guide_.
   - Make sure that there is network connectivity between your
     EMR cluster and the LDAP server. Your EMR clusters must access
     your LDAP server over the network. The primary, core, and task nodes
     for the cluster communicate with the LDAP server to sync user data.
     If your LDAP server runs on Amazon EC2, update the EC2 security group to
     accept traffic from the EMR cluster. For more information, see
     [Add AWS Secrets Manager permissions to the Amazon EMR instance
     role](ldap-setup-asm.md "ldap-setup-asm.md").

2. Create an Amazon EMR security configuration for the LDAP integration. For more
   information, see [Create the Amazon EMR security configuration for
   LDAP integration](ldap-setup-security.md "ldap-setup-security.md").
3. Now that you're set up, use the steps in [Launch an Amazon EMR
   cluster](emr-gs.md#emr-getting-started-launch-sample-cluster "emr-gs.md#emr-getting-started-launch-sample-cluster") to launch
   your cluster with the following configurations:
   - Select Amazon EMR release 6.12 or higher. We recommend that you use the
     latest Amazon EMR release.
   - Only specify or select applications for your cluster that support
     LDAP. For a list of LDAP-supported applications with Amazon EMR, see
     [Application support and considerations with LDAP
     for Amazon EMR](ldap-considerations.md "ldap-considerations.md").
   - Apply the security configuration that you created in the previous
     step.
