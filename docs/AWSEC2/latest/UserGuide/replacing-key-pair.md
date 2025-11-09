# Add or replace a public key on your Linux

instance

|                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| If you lose a private key, you lose access to any instances that use the key<br>pair. For more information about connecting to an instance using a different key pair<br>than the one that you specified at launch, see [I've lost my private key](TroubleshootingInstancesConnecting.md#replacing-lost-key-pair "TroubleshootingInstancesConnecting.md#replacing-lost-key-pair"). |

When you launch an instance, you can [specify a key
pair](ec2-instance-launch-parameters.md#liw-key-pair "ec2-instance-launch-parameters.md#liw-key-pair"). If you specify a key pair at launch, when your instance boots for the first
time, the public key material is placed on your Linux instance in an entry within
`~/.ssh/authorized_keys`. When you first connect to your Linux instance using SSH,
you specify the default user and the private key that corresponds to the public key that is
stored on your Linux instance.

After you connect to your instance, you can change the key pair that is used to access
the default system account of your instance by adding a new public key on the instance, or by
replacing the public key (deleting the existing public key and adding a new one) on the instance.
You can also remove all public keys from an instance.

You might add or replace a key pair for the following reasons:

- If a user in your organization requires access to the system user using a separate key
  pair, you can add the public key to your instance.
- If someone has a copy of the private key (`.pem` file) and you want
  to prevent them from connecting to your instance (for example, if they've left your
  organization), you can delete the public key on the instance and replace it with a new
  one.
- If you create a Linux AMI from an instance, the public key material is copied from the
  instance to the AMI. If you launch an instance from the AMI, the new instance includes the
  public key from the original instance. To prevent someone who has the private key from
  connecting to the new instance, you can remove the public key from the original instance
  _before_ creating the AMI.
  Use the following procedures to modify the key pair for the default user, such as
  `ec2-user`. For information about adding users to your instance, see the
  documentation for the operating system on your instance.

###### To add or replace a key pair

1. Create a new key pair using the [Amazon EC2
   console](create-key-pairs.md#having-ec2-create-your-key-pair "create-key-pairs.md#having-ec2-create-your-key-pair") or a [third-party tool](create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws "create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws").
2. Retrieve the public key from your new key pair. For more information, see [Retrieve the public key material](describe-keys.md#retrieving-the-public-key "describe-keys.md#retrieving-the-public-key").
3. [Connect to your instance](connect-to-linux-instance.md "connect-to-linux-instance.md").
4. On the instance, using the text editor of your choice, open the `.ssh/authorized_keys`
   file. Paste the public key information from your new key pair underneath the existing
   public key information and then save the file.
5. Disconnect from your instance. Test that you can connect to your instance using
   the private key file from the new key pair.
6. If you're using Auto Scaling, EC2 fleet, or a launch template to launch your instances,
   check whether the key pair that you're replacing is specified in your launch template
   or launch configuration. Otherwise, instance launches will fail.
7. (Optional) If you're replacing an existing key pair, connect to your instance and
   delete the public key information for the original key pair from the
   `.ssh/authorized_keys` file.

###### To remove a public key from an instance

1. [Connect to your instance](connect-to-linux-instance.md "connect-to-linux-instance.md").
2. Using a text editor of your choice, open the `.ssh/authorized_keys`
   file on the instance. Delete the public key information, and then save the file.

###### Warning

If you remove all the public keys from an instance and disconnect from the instance,
you can't connect to the instance again unless you've configured an alternate way to
log in.
