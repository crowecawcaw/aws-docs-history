# Create a key pair for your instances

AWS uses public-key cryptography to secure the login information for your instance. A Linux instance, such as
an AWS Batch compute environment container instance, has no password to use for SSH access. You use a key pair to log
in to your instance securely. You specify the name of the key pair when you create your compute environment, then
provide the private key when you log in using SSH.

If you didn't create a key pair already, you can create one using the Amazon EC2 console. Note that, if you plan to
launch instances in multiple AWS Regions, create a key pair in each Region. For more information about Regions, see
[Regions and Availability Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the
_Amazon EC2 User Guide_.

###### To create a key pair

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select an AWS Region for the key pair. You can select any Region that's available
   to you, regardless of your location: however, key pairs are specific to a Region. For example, if you plan to
   launch an instance in the US West (Oregon) Region, create a key pair for the instance in the same Region.
3. In the navigation pane, choose **Key Pairs**, **Create Key Pair**.
4. In the **Create Key Pair** dialog box, for **Key pair name**, enter a name
   for the new key pair , and choose **Create**. Choose a name that you can remember, such as your
   user name, followed by `-key-pair`, plus the Region name. For example,
   _me_-key-pair-_uswest2_.
5. The private key file is automatically downloaded by your browser. The base file name is the name that you
   specified as the name of your key pair, and the file name extension is `.pem`. Save the private
   key file in a safe place.

###### Important

This is the only chance for you to save the private key file. You need to provide the name of your key pair
when you launch an instance and the corresponding private key each time that you connect to the instance. 6. If you use an SSH client on a Mac or Linux computer to connect to your Linux instance, use the following
command to set the permissions of your private key file. That way, only you can read it.

```
$ `chmod 400 `your_user_name`-key-pair-`region_name`.pem`
```

For more information, see [Amazon EC2 Key Pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the
_Amazon EC2 User Guide_.

###### To connect to your instance using your key pair

To connect to your Linux instance from a computer running Mac or Linux, specify the `.pem`
file to your SSH client with the `-i` option and the path to your private key. To connect to your Linux
instance from a computer running Windows, use either MindTerm or PuTTY. If you plan to use PuTTY, install it and
use the following procedure to convert the `.pem` file to a `.ppk`
file.

###### (Optional) To prepare to connect to a Linux instance from Windows using

PuTTY

1. Download and install PuTTY from [http://www.chiark.greenend.org.uk/~sgtatham/putty/](http://www.chiark.greenend.org.uk/~sgtatham/putty/ "http://www.chiark.greenend.org.uk/~sgtatham/putty/"). Be sure to install the entire suite.
2. Start PuTTYgen (for example, from the **Start** menu, choose **All Programs,
   PuTTY, and PuTTYgen**).
3. Under **Type of key to generate**, choose **RSA**. If you're using an
   earlier version of PuTTYgen, choose **SSH-2 RSA**.

![Putty key type](images/puttygen-key-type.png) 4. Choose **Load**. By default, PuTTYgen displays only files with the extension
`.ppk`. To locate your `.pem` file, choose the option to display files of
all types.

![Putty key file type](images/puttygen-load-key.png) 5. Select the private key file that you created in the previous procedure and choose **Open**.
Choose **OK** to dismiss the confirmation dialog box. 6. Choose **Save private key**. PuTTYgen displays a warning about saving the key without a
passphrase. Choose **Yes**. 7. Specify the same name for the key that you used for the key pair. PuTTY automatically adds the
`.ppk` file extension.
