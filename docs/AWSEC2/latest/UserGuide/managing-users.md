# Manage system users on your Amazon EC2 Linux instance

Each Linux instance launches with a default Linux system user. You can add users to your
instance and delete users.

For the default user, the [default username](#ami-default-user-names "#ami-default-user-names") is
determined by the AMI that was specified when you launched the instance.

###### Note

By default, password authentication and root login are disabled, and sudo is enabled. To
log in to your instance, you must use a key pair. For more information about logging
in, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").

You can allow password authentication and root login for your instance. For more
information, see the documentation for your operating system.

###### Note

Linux system users should not be confused with IAM users. For more
information, see [IAM
users](../../../IAM/latest/UserGuide/id.md#id_iam-users "../../../IAM/latest/UserGuide/id.md#id_iam-users") in the _IAM User Guide_.

###### Contents

- [Default usernames](#ami-default-user-names "#ami-default-user-names")
- [Considerations](#add-user-best-practice "#add-user-best-practice")
- [Create a user](#create-user-account "#create-user-account")
- [Remove a user](#delete-user-account "#delete-user-account")

## Default usernames

The default username for your EC2 instance is determined by the AMI that was specified when
you launched the instance.

The default usernames are:

- For an Amazon Linux AMI, the username is
  `ec2-user`.
- For a CentOS AMI, the username is `centos` or
  `ec2-user`.
- For a Debian AMI, the username is `admin`.
- For a Fedora AMI, the username is `fedora` or
  `ec2-user`.
- For a FreeBSD AMI, the username is `ec2-user`.
- For a RHEL AMI, the username is `ec2-user` or
  `root`.
- For a SUSE AMI, the username is `ec2-user` or
  `root`.
- For an Ubuntu AMI, the username is `ubuntu`.
- For an Oracle AMI, the username is `ec2-user`.
- For a Bitnami AMI, the username is `bitnami`.

###### Note

To find the default username for other Linux distributions, check with the AMI provider.

## Considerations

Using the default user is adequate for many applications. However, you may choose to add
users so that individuals can have their own files and workspaces. Furthermore,
creating users for new users is much more secure than granting multiple (possibly
inexperienced) users access to the default user, because the default user can cause
a lot of damage to a system when used improperly. For more information, see [Tips for
Securing Your EC2 Instance](https://aws.amazon.com/articles/tips-for-securing-your-ec2-instance/ "https://aws.amazon.com/articles/tips-for-securing-your-ec2-instance/").

To enable users SSH access to your EC2 instance using a Linux system user, you must share
the SSH key with the user. Alternatively, you can use EC2 Instance Connect to
provide access to users without the need to share and manage SSH keys. For more
information, see [Connect to your Linux instance using a public IP address
and EC2 Instance Connect](connect-linux-inst-eic.md "connect-linux-inst-eic.md").

## Create a user

First create the user, and then add the SSH public key that allows the user to connect
to and log into the instance.

###### Important

In Step 1 of this procedure, you create a new key pair. Because a key pair functions like
a password, it's crucial to handle it securely. If you create a key pair for a user,
you must ensure that the private key is sent to them securely. Alternatively, the
user can complete Steps 1 and 2 by creating their own key pair, keeping the private
key secure on their machine, and then sending you the public key to complete the
procedure from Step 3.

###### To create a user

1. [Create a new key pair](create-key-pairs.md#having-ec2-create-your-key-pair "create-key-pairs.md#having-ec2-create-your-key-pair"). You must
   provide the `.pem` file to the user for whom you are creating the
   user. They must use this file to connect to the instance.
2. Retrieve the public key from the key pair that you created in the previous step.

```
`$` ssh-keygen -y -f /`path_to_key_pair`/`key-pair-name`.pem
```

The command returns the public key, as shown in the following example.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6Vhz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXrlsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZqaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3RbBQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
```

3. Connect to the instance.
4. Use the **adduser** command to create the user and add it to the system
   (with an entry in the `/etc/passwd` file). The command
   also creates a group and a home directory for the user. In this example, the
   user is named `newuser`.
   - AL2023 and Amazon Linux 2

   With AL2023 and Amazon Linux 2, the user is created with password authentication disabled by
   default.

   ```
   `[ec2-user ~]$` `sudo adduser `newuser``
   ```

   - Ubuntu

   Include the `--disabled-password` parameter to create the user with password
   authentication disabled.

   ```
   `[ubuntu ~]$` `sudo adduser `newuser`` --disabled-password
   ```

5. Switch to the new user so that the directory and file that you create will have the proper
   ownership.

```
`[ec2-user ~]$` `sudo su - `newuser``
```

The prompt changes from `ec2-user` to
`newuser` to indicate that you
have switched the shell session to the new user. 6. Add the SSH public key to the user. First create a directory in the user's home directory
for the SSH key file, then create the key file, and finally paste the public
key into the key file, as described in the following sub-steps.

    1. Create a `.ssh` directory in the
     ``newuser`` home
     directory and change its file permissions to `700` (only
     the owner can read, write, or open the directory).



    ```
    `[newuser ~]$` `mkdir .ssh`
    ```


    ```
    `[newuser ~]$` `chmod 700 .ssh`
    ```

    ###### Important

    Without these exact file permissions, the user will not be able to log in.
    2. Create a file named `authorized_keys` in the `.ssh`
     directory and change its file permissions to `600` (only the owner can read
     or write to the file).



    ```
    `[newuser ~]$` `touch .ssh/authorized_keys`
    ```


    ```
    `[newuser ~]$` `chmod 600 .ssh/authorized_keys`
    ```

    ###### Important

    Without these exact file permissions, the user will not be able to log in.
    3. Open the `authorized_keys` file using your favorite text editor (such
     as **vim** or **nano**).



    ```
    `[newuser ~]$` `nano .ssh/authorized_keys`
    ```

    Paste the public key that you retrieved in **Step 2** into the
     file and save the changes.


    ###### Important

    Ensure that you paste the public key in one continuous line. The public key must not be split over multiple lines.


    The user should now be able to log into the
     ``newuser`` user on your
     instance, using the private key that corresponds to the public key
     that you added to the `authorized_keys` file. For
     more information about the different methods of connecting to a
     Linux instance, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").

## Remove a user

If a user is no longer needed, you can remove that user so that it can no longer be
used.

Use the **userdel** command to remove the user from the system. When you
specify the `-r` parameter, the user's home directory and mail spool are
deleted. To keep the user's home directory and mail spool, omit the `-r`
parameter.

```
`[ec2-user ~]$` `sudo userdel -r `olduser``
```
