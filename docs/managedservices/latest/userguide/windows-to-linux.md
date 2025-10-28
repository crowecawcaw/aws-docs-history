# Windows computer to Linux instance

To RDP to an SSH bastion from a Windows environment, follow these steps.

MALZ
Before you begin:

- Request access to the instance that you want to connect to; for information, see
  [Access requests](../ctref/ex-access-request.md "../ctref/ex-access-request.md").
- Choose a friendly DNS SSH bastion name to connect to; for example:

```
sshbastion`(1-4)`.`YOUR_DOMAIN`
```

Which would look like this if YOUR_DOMAIN is myamsaddomain.com" and you choose bastion 4:

```
sshbastion4.myamsaddomain.com
```

- Find the IP address of the instance that you want to connect to; for information, see
  [Finding an instance ID or IP address](find-instance-id.md "find-instance-id.md").
  In order to connect to the Linux instance from your Windows machine, you must first connect to an SSH bastion.

Use the native Windows
[OpenSSH client](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse "https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse") or install
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html "http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html")
on your local machine. To learn more about OpenSSH, see
[OpenSSH in Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview "https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview").

1. Use the native Windows or open PuTTY and enter the SSH bastion hostname or the IP address of the SSH bastion.
   For example, 10.65.2.214 (22 is the port used for SSH; it will be set by default).
2. OpenSSH or PuTTY attempts an SSH connection to the bastion and open a shell window.
3. Use your corporate Active Directory credentials as you would with the RDP hosts to gain access.
4. When presented with a Bash prompt, SSH into the instance. Enter:

```
ssh `DOMAIN_FQDN`\`USERNAME`@`INSTANCE_IP`
```

SALZ
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
  In order to connect to the Linux instance from your Windows machine, you must first connect to an SSH bastion.

Use the native Windows
[OpenSSH client](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse "https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse") or install
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html "http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html")
on your local machine. To learn more about OpenSSH, see
[OpenSSH in Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview "https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview").

1. Use the native Windows or open PuTTY and enter the SSH bastion hostname or the IP address of the SSH bastion.
   For example, 10.65.2.214 (22 is the port used for SSH; it will be set by default).
2. OpenSSH or PuTTY attempts an SSH connection to the bastion and open a shell window.
3. Use your corporate Active Directory credentials as you would with the RDP hosts to gain access.
4. When presented with a Bash prompt, SSH into the instance. Enter:

```
ssh `DOMAIN_FQDN`\`USERNAME`@`INSTANCE_IP`
```
