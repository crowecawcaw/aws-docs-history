

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Using bastion IP addresses
<a name="find-bastions"></a>

AMS customers can use SSH and RDP bastions, either the [DNS friendly bastion names](dns-bastions.md) described previously, or bastion IP addresses.

To find bastion IP addresses, SSH and RDP, for your account:

1. For multi-account landing zone only: Log in to the Shared Services account.

1. Open the EC2 Console and choose **Running Instances**.

   The **Instances** page opens.

1. In the filter box at the top, enter either **ssh-bastion** or **rdp-bastion**.

   In the filter box at the top, enter either **customer-ssh** or **customer-rdp**.

   The SSH and/or RDP bastions for your account display.

   Note that in addition to your SSH bastions, you may see AMS perimeter network bastions in the list, which are unavailable for this.

1. Select an SSH or RDP bastion. If you're using a Windows computer and want to log in to a Linux instance, you use an SSH bastion. If you want to log in to a Windows instance, you use an RDP bastion. If you're on a Linux OS and want to log in to a Windows instance, you use an SSH bastion through an RDP tunnel (this is so you can access the Windows desktop). To access a Linux instance from a Linux OS, you use an SSH bastion.