NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Copy Private IP

Choose whether you want AWS Application Migration Service to ensure that the private IP used by the test or
cutover instance matches the private IP used by the source server.

AWS Application Migration Service monitors the source server on an hourly basis to identify the
private IP. Application Migration Service uses the private IP of the primary network interface.

The **No** option is chosen by default. Click **No** if you do not want the private IP of the test or cutover instance
to match that of the source machine.

Click **Yes** if you want to use a private IP. The IP is shown in brackets next to the option.

###### Note

- Private IP is not supported for IPv6.
- Removing a private IP from a specific server's settings does not remove it from the launch template.
- If you chose **Yes**, ensure that the IP range of the
  subnet you set in the EC2 launch template includes the private IP address.
- If the both the source server and the test or cutover instance shares the same subnet
  though a VPN, then the source private IP is already in use, and the **Copy private IP** option should not be used.
