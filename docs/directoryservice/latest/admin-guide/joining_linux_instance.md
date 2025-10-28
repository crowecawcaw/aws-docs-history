# Joining an Amazon EC2 Linux instance to your AWS Managed Microsoft AD

Active Directory

You can launch and join an EC2 Linux instance to your AWS Managed Microsoft AD in the AWS Management Console. You
can also manually join EC2 Linux instance to your AWS Managed Microsoft AD. Tools like Winbind can also be
used so you can domain join an EC2 Linux instance to your AWS Managed Microsoft AD.

The following Linux instance distributions and versions are supported:

- Amazon Linux AMI 2018.03.0
- Amazon Linux 2 (64-bit x86)
- Red Hat Enterprise Linux 8 (HVM) (64-bit x86)
- Ubuntu Server 18.04 LTS & Ubuntu Server 16.04 LTS
- CentOS 7 x86-64
- SUSE Linux Enterprise Server 15 SP1

###### Note

Distributions prior to Ubuntu 14 and Red Hat Enterprise Linux 7 and 8 do not support the
seamless domain join feature.

###### Ways to domain join a EC2 Linux instance:

- [Seamlessly joining an Amazon EC2 Linux instance
  to your AWS Managed Microsoft AD Active Directory](seamlessly_join_linux_instance.md "seamlessly_join_linux_instance.md")
- [Seamlessly joining an Amazon EC2 Linux
  instance to a shared AWS Managed Microsoft AD](seamlessly_join_linux_to_shared_MAD.md "seamlessly_join_linux_to_shared_MAD.md")
- [Manually joining an Amazon EC2 Linux instance to your
  AWS Managed Microsoft AD Active Directory](join_linux_instance.md "join_linux_instance.md")
- [Manually joining an Amazon EC2 Linux instance to
  your AWS Managed Microsoft AD Active Directory using Winbind](join_linux_instance_winbind.md "join_linux_instance_winbind.md")
