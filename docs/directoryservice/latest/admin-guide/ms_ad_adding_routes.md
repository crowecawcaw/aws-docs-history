# Adding IP routes when using public IP addresses with your AWS Managed Microsoft AD

You can use AWS Directory Service for Microsoft Active Directory to take advantage of many powerful Active Directory
features, including establishing trusts with other directories. However, if the DNS servers for
the networks of the other directories use public (non-RFC 1918) IP addresses, you must specify
those IP addresses as part of configuring the trust. Instructions for doing this can be found in
[Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](ms_ad_setup_trust.md "ms_ad_setup_trust.md").

Similarly, you must also enter the IP address information when routing traffic from
your AWS Managed Microsoft AD on AWS to a peer AWS VPC, if the VPC uses public IP ranges.

When you add the IP addresses as described in [Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](ms_ad_setup_trust.md "ms_ad_setup_trust.md"), you have the option of selecting **Add routes to the
security group for this directory's VPC**. This option should be selected unless you
have previously customized your [security group](../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule") to allow the necessary traffic as
shown below. For more information, see [Understand your directory's AWS security group
configuration and use](ms_ad_best_practices.md#understandsecuritygroup "ms_ad_best_practices.md#understandsecuritygroup").
