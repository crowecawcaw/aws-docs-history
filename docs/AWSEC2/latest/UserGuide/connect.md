# Connect to your EC2 instance

Your Amazon EC2 instance is a virtual server in the AWS Cloud. To log on to your instance,
you must establish a connection to the instance. How you connect to your instance depends on
the operating system of the instance and the operating system on the computer that you use
to connect to the instance. The following table details the requirements for each connection method.

| Connection option             | Instance operating system | Inbound traffic rule | IAM permissions | Instance profile role | Software on instance | Software on connecting system | Key pair |
| ----------------------------- | ------------------------- | -------------------- | --------------- | --------------------- | -------------------- | ----------------------------- | -------- |
| SSH client                    | Linux                     | Yes                  | No              | No                    | No                   | Yes                           | Yes      |
| EC2 Instance Connect          | Linux                     | Yes                  | Yes             | No                    | Yes ¹                | No                            | No       |
| PuTTY                         | Linux                     | Yes                  | No              | No                    | No                   | Yes                           | Yes      |
| RDP client                    | Windows                   | Yes                  | No              | No                    | No                   | Yes                           | Yes ²    |
| Fleet Manager                 | Windows                   | No                   | Yes             | Yes                   | Yes ¹                | No                            | Yes      |
| Session Manager               | Linux, Windows            | No                   | Yes             | Yes                   | Yes ¹                | No                            | No       |
| EC2 Instance Connect Endpoint | Linux, Windows            | Yes                  | Yes             | No                    | No                   | No                            | No ³     |

¹ The required software is only pre-installed on certain AMIs. You can manually install
the required software as needed on supported operating systems.

² The key pair is only required if you are using the randomly generated password for
the local Administrator user account.

³ A key pair is required if you use the SSH connection method.

For more information, see the documentation for the connection option that you intend to
use.

###### Connection options

- [Connect to your Linux instance using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md")
- [Connect to your Linux instance using PuTTY](connect-linux-inst-from-windows.md "connect-linux-inst-from-windows.md")
- [Connect to your Windows instance using an RDP client](connect-rdp.md "connect-rdp.md")
- [Connect to your Windows instance using Fleet Manager](connect-rdp-fleet-manager.md "connect-rdp-fleet-manager.md")
- [Connect using Session Manager](connect-with-systems-manager-session-manager.md "connect-with-systems-manager-session-manager.md")
- [Connect using a public IP and
  EC2 Instance Connect](connect-linux-inst-eic.md "connect-linux-inst-eic.md")
- [Connect using a
  private IP and EC2 Instance Connect Endpoint](connect-with-ec2-instance-connect-endpoint.md "connect-with-ec2-instance-connect-endpoint.md")
