

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Linux computer to Linux instance
<a name="linux-to-linux"></a>

Use SSH to connect to the SSH bastion and then to the Linux instance.

------
#### [ MALZ ]<a name="lin-to-lin-malz-procedure"></a>

For more information about the friendly bastion names, see [DNS bastions](https://docs.aws.amazon.com/managedservices/latest/userguide/dns-bastions.html).

In order to connect to the Linux instance, you must first connect to an SSH bastion.

1. Open a shell window and enter:

   ```
   ssh {{Domain_FQDN}}\\{{Username}}@{{SSH_bastion_name}} 
       or {{SSH_bastion_IP}}
   ```

   Which would look like this if your Domain\_FQDN is "corp.domain.com", your account number is "123456789123", Your\_Domain is "amazonaws.com", you choose bastion "4", and your user name is "JoeSmith":

   ```
   ssh corp.domain.com\\JoeSmith sshbastion4.A123456789123.amazonaws.com
   ```

1. Log in with your corporate Active Directory credentials.

1. When presented with a Bash prompt, SSH in to the instance, and then enter:

   ```
   ssh {{Domain_FQDN}}\\{{Username}}@{{Instance_IP}}
   ```

   Or, you can use the Login flag (-l):

   ```
   ssh -l {{Domain_FQDN}}\\{{Username}}@{{Instance_IP}}
   ```

------
#### [ SALZ ]<a name="lin-to-lin-salz-procedure"></a>

For more information about the friendly bastion names, see [DNS bastions](https://docs.aws.amazon.com/managedservices/latest/userguide/dns-bastions.html).

In order to connect to the Linux instance, you must first connect to an SSH bastion.

1. Open a shell window and enter:

   ```
   ssh {{DOMAIN_FQDN}}\\{{USERNAME}}@{{SSH_BASTION_name}} 
       or {{SSH_BASTION_IP}}
   ```

   Which would look like this if your account number is 123456789123, you choose bastion 4, and your user name is JoeSmith:

   ```
   ssh corp.domain.com\\JoeSmith sshbastion1.A123456789123.amazonaws.com
   ```

1. Log in with your corporate Active Directory credentials.

1. When presented with a Bash prompt, SSH in to the instance, and then enter:

   ```
   ssh {{DOMAIN_FQDN}}\\{{USERNAME}}@{{INSTANCE_IP}}
   ```

   Or, you can use the Login flag (-l):

   ```
   ssh -l {{DOMAIN_FQDN}}\\{{USERNAME}}@{{INSTANCE_IP}}
   ```

------