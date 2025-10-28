# Linux computer to Linux instance

Use SSH to connect to the SSH bastion and then to the Linux instance.

MALZ
For more information about the friendly bastion names, see
[DNS bastions](dns-bastions.md "dns-bastions.md").

In order to connect to the Linux instance, you must first connect to an SSH bastion.

1. Open a shell window and enter:

```
ssh `Domain_FQDN`\\`Username`@`SSH_bastion_name`
    or `SSH_bastion_IP`
```

Which would look like this if your Domain_FQDN is "corp.domain.com", your account number is "123456789123",
Your_Domain is "amazonaws.com", you choose bastion "4", and your user name is "JoeSmith":

```
ssh corp.domain.com\\JoeSmith sshbastion4.A123456789123.amazonaws.com
```

2. Log in with your corporate Active Directory credentials.
3. When presented with a Bash prompt, SSH in to the instance, and then enter:

```
ssh `Domain_FQDN`\\`Username`@`Instance_IP`
```

Or, you can use the Login flag (-l):

```
ssh -l `Domain_FQDN`\\`Username`@`Instance_IP`
```

SALZ
For more information about the friendly bastion names, see
[DNS bastions](dns-bastions.md "dns-bastions.md").

In order to connect to the Linux instance, you must first connect to an SSH bastion.

1. Open a shell window and enter:

```
ssh `DOMAIN_FQDN`\\`USERNAME`@`SSH_BASTION_name`
    or `SSH_BASTION_IP`
```

Which would look like this if your account number is 123456789123, you
choose bastion 4, and your user name is JoeSmith:

```
ssh corp.domain.com\\JoeSmith sshbastion1.A123456789123.amazonaws.com
```

2. Log in with your corporate Active Directory credentials.
3. When presented with a Bash prompt, SSH in to the instance, and then enter:

```
ssh `DOMAIN_FQDN`\\`USERNAME`@`INSTANCE_IP`
```

Or, you can use the Login flag (-l):

```
ssh -l `DOMAIN_FQDN`\\`USERNAME`@`INSTANCE_IP`
```
