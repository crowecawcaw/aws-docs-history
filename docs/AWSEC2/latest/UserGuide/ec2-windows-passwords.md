# Change the Windows Administrator password for your Amazon EC2 instance

If you launch your instance from an AWS Windows AMI, the launch agents that are pre-installed
set the default password as follows:

- For Windows Server 2022 and later, [EC2Launch v2](ec2launch-v2.md "ec2launch-v2.md") generates the default password.
- For Windows Server 2016 and 2019, the [EC2Launch](ec2launch.md "ec2launch.md") agent generates the default password.
- For Windows Server 2012 R2 and earlier, the [EC2Config service](ec2config-service.md "ec2config-service.md") generates the default password.

###### Note

For Windows Server 2016 and later AMIs, `Password never expires` is disabled
for the local administrator. For AMI versions prior to Windows Server 2016,
`Password never expires` is enabled for the local administrator.

## Change the Administrator password after

connecting

When you connect to an instance the first time, we recommend that you change the
Administrator password from its default value. Use the following procedure to change the
Administrator password for a Windows instance.

###### Important

Store the new password in a safe place. You won't be able to retrieve the new
password using the Amazon EC2 console. The console can only retrieve the default
password. If you attempt to connect to the instance using the default password after
changing it, you'll get a "Your credentials did not work" error.

###### To change the local Administrator password

1. Connect to the instance and open a command prompt.
2. Run the following command. If your new password includes special characters,
   enclose the password in double quotes.

```
`net user Administrator "`new_password`"`
```

3. Store the new password in a safe place.

## Change a lost or expired password

If you lose your password or it expires, you can generate a new password. For password
reset procedures, see [Reset the Windows administrator password for an Amazon EC2 Windows instance](ResettingAdminPassword.md "ResettingAdminPassword.md").
