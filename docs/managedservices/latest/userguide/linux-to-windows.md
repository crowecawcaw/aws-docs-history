# Linux computer to Windows instance

Use an SSH tunnel and an RDP client to connect to a Windows instance from your Linux computer.

MALZ
This procedure requires a Remote Desktop Connection client for Linux; the example uses
Microsoft Remote Desktop (an open source UNIX client for connecting to Windows Remote Desktop Services). Rdesktop is an alternative.

###### Note

How you log in to Windows instances might change based on the remote desktop client being used.

First you establish an SSH tunnel, and then log in.

For more information about the friendly bastion names, see [DNS friendly bastion names](dns-bastions.md "dns-bastions.md").

Before you begin:

- Request access to the instance that you want to connect to; for information, see
  [Access requests](../ctref/ex-access-request.md "../ctref/ex-access-request.md").
- Choose a friendly DNS SSH bastion name to connect to; for example:

```
sshbastion`(1-4)`.`Your_Domain`
```

Which would look like this if your Domain_FQDN is "corp.domain.com", your
AMS-managed Your_Domain is "amazonaws.com", you choose bastion "4", and your user name is "JoeSmith":

```
ssh corp.domain.com\\JoeSmith sshbastion4.amazonaws.com
```

- Find the IP address of the instance that you want to connect to; for information, see
  [Finding an instance ID or IP address](find-instance-id.md "find-instance-id.md").

1.  Set up RDP over an SSH tunnel from a Linux desktop to a Windows instance. In order to
    issue the `ssh` command with the right values, there are a couple of ways to proceed:

        * In the Linux shell, set the variables, and then enter the SSH connection command:



        ```
        BASTION="sshbastion`(1-4)`.`Your_Domain"`"
        WINDOWS="`Windows_Instance_Private_IP`"
        AD="`AD_Account_Number`"
        USER="`AD_Username`"
        ssh -L 3389:$WINDOWS:3389 A$AD\\\\$USER@$BASTION
        ```

        Example, if the following values are used:


        `BASTION="sshbastion4.A123456789123.amazonaws.com"`


        `WINDOWS="172.16.3.254"`


        `AD="ACORP_example"`


        `USER="john.doe"`
        * Add the variable values directly to the `ssh` command.

    In either case, this is what the rendered request would be (assuming the same set of
    variable values):

```
ssh -L 3389:172.16.3.254:3389 ACORP_example\\\\john.doe@myamsadomain.com
```

2. Either: Open your Remote Desktop Client, enter the loopback address and port,
   127.0.0.1:3389, and then open the connection.

Or, log in to the Windows instance from a new Linux desktop shell. If you use
RDesktop, the command looks like this:

```
`rdesktop 127.0.0.1:3389`
```

A remote desktop window for the Windows instance appears on your Linux desktop.

###### Tip

If the remote desktop session fails to start, verify that network connectivity to
the Windows instance from the SSH bastion is allowed on port 3389 from the shell in
step 1 (replace `private_ip_address_of_windows_instance` appropriately):

```
nc private_ip_address_of_windows_instance 3389 -v –z
```

Success:

```
nc 172.16.0.83 3389 -v -z
        Connection to 172.16.0.83 3389 port [tcp/ms-wbt-server] succeeded
        netstat -anvp | grep 3389
        tcp    0     0 172.16.0.253:48079 172.16.3.254:3389 ESTABLISHED
```

SALZ
This procedure for a single-account landing zone requires a Remote Desktop Connection client for Linux; the example uses
Microsoft Remote Desktop (an open source UNIX client for connecting to Windows Remote
Desktop Services). Rdesktop is an alternative.

###### Note

How you log in to Windows instances might change based on the remote desktop client being used.

First you establish an SSH tunnel, and then log in.

For more information about the friendly bastion names, see [DNS friendly bastion names](dns-bastions.md "dns-bastions.md").

Before you begin:

- Request access to the instance that you want to connect to; for information, see
  [Access requests](../ctref/ex-access-request.md "../ctref/ex-access-request.md").
- Choose a friendly DNS SSH bastion name to connect to; for example:

```
sshbastion`(1-4)`.A`AMSAccountNumber`.amazonaws.com
```

Which would look like this if your account number is 123456789123 and you choose
bastion 4:

```
sshbastion4.A123456789123.amazonaws.com
```

- Find the IP address of the instance that you want to connect to; for information, see
  [Finding an instance ID or IP address](find-instance-id.md "find-instance-id.md").

1.  Set up RDP over an SSH tunnel from a Linux desktop to a Windows instance. In order to
    issue the `ssh` command with the right values, there are a couple of ways to proceed:

        * In the Linux shell, set the variables, and then enter the SSH connection command:



        ```
        BASTION="sshbastion`(1-4)`.A`AMSAccountNumber`.amazonaws.com"
        WINDOWS="`WINDOWS_INSTANCE_PRIVATE_IP`"
        AD="`AD_ACCOUNT_NUMBER`"
        USER="`AD_USERNAME`"
        ssh -L 3389:$WINDOWS:3389 A$AD\\\\$USER@$BASTION
        ```

        Example, if the following values are used:


        `BASTION="sshbastion4.A123456789123.amazonaws.com"`


        `WINDOWS="172.16.3.254"`


        `AD="ACORP_example"`


        `USER="john.doe"`
        * Add the variable values directly to the `ssh` command.

    In either case, this is what the rendered request would be (assuming the same set of
    variable values):

```
ssh -L 3389:172.16.3.254:3389 ACORP_example\\\\john.doe@sshbastion4.A123456789123.amazonaws.com
```

2. Either: Open your Remote Desktop Client, enter the loopback address and port,
   127.0.0.1:3389, and then open the connection.

Or, log in to the Windows instance from a new Linux desktop shell. If you use
RDesktop, the command looks like this:

```
`rdesktop 127.0.0.1:3389`
```

A remote desktop window for the Windows instance appears on your Linux desktop.

###### Tip

If the remote desktop session fails to start, verify that network connectivity to
the Windows instance from the SSH bastion is allowed on port 3389 from the shell in
step 1 (replace `private_ip_address_of_windows_instance`
appropriately):

```
nc private_ip_address_of_windows_instance 3389 -v –z
```

Success:

```
nc 172.16.0.83 3389 -v -z
        Connection to 172.16.0.83 3389 port [tcp/ms-wbt-server] succeeded
        netstat -anvp | grep 3389
        tcp    0     0 172.16.0.253:48079 172.16.3.254:3389 ESTABLISHED
```
