# Step 2: Configure your

Amazon EC2 instance

When your Amazon EC2 instance is available, you can log into it and prepare it for first
use.

###### Note

The following steps assume that you're connecting to your Amazon EC2 instance from a
computer running Linux. For other ways to connect, see [Connect to your Linux
instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_.

###### To configure your Amazon EC2 instance

1.  You need to authorize inbound SSH traffic to your Amazon EC2 instance. To do this,
    create a new EC2 security group, and then assign the security group to your EC2
    instance.
    1.  In the navigation pane, choose **Security
        Groups**.
    2.  Choose **Create Security Group**. In the
        **Create Security Group** window, do the
        following:

            * **Security group name** – Enter a name
             for your security group. For example:
             `my-ssh-access`
            * **Description** – Enter a short
             description for the security group.
            * **VPC** – Choose your default
             VPC.
            * In the **Inbound rules** section, choose
             **Add Rule** and do the following:




            	+ **Type** – Choose
            	 **SSH**.
            	+ **Source** – Choose
            	 **My IP**.
            	+ Choose **Add rule**.

        On the bottom of the page, confirm the configuration settings and
        choose **Create Security Group**.

    3.  In the navigation pane, choose **Instances**.
    4.  Choose the Amazon EC2 instance that you launched in [Step 1: Launch an Amazon EC2
        instance](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md").
    5.  Choose **Actions**, choose
        **Security**, and then choose **Change
        Security Groups**.
    6.  In **Change Security Groups**, go to **Associated security groups**
        and enter the security
        group that you created earlier in this procedure (for example,
        `my-ssh-access`). The existing `default`
        security group should also be selected. Confirm the configuration
        settings and choose **Save**.

2.  Use the following command to protect your private key file from access. If you
    skip this step, the connection fails.

```
chmod 400 `path_to_file`/`my-keypair.pem`
```

3. Use the `ssh` command to log in to your Amazon EC2 instance, as in the
   following example.

```
ssh -i `path_to_file`/`my-keypair.pem` ubuntu@`public-dns-name`
```

You need to specify your private key file (_.pem_ file) and
the public DNS name of your instance. (See [Step 1: Launch an Amazon EC2
instance](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md")).

The login ID is `ubuntu`. No password is required.

For more information about allowing connections to your Amazon EC2 instance and for
AWS CLI instructions, see [Authorize inbound
traffic for your Linux instances](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md") in the _Amazon EC2 User Guide_. 4. Download and install the latest version of the AWS Command Line Interface.

    1. Install `unzip`.



    ```
    sudo apt install unzip
    ```
    2. Download the `zip` file with the AWS CLI.



    ```
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    ```
    3. Unzip the file.



    ```
    unzip awscliv2.zip
    ```
    4. Install the AWS CLI.



    ```
    sudo ./aws/install
    ```
    5. Confirm the version of the AWS CLI installation.



    ```
    aws --version
    ```

    The output should look like this:



    ```
    `aws-cli/2.9.19 Python/3.9.11 Linux/5.15.0-1028-aws exe/x86_64.ubuntu.22 prompt/off`
    ```

5. Configure your AWS credentials, as shown in the following example. Enter
   your AWS access key ID, secret key, and default Region name when
   prompted.

```
`aws configure`

AWS Access Key ID [None]: `AKIAIOSFODNN7EXAMPLE`
AWS Secret Access Key [None]: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
Default region name [None]: `us-east-1`
Default output format [None]:
```

6. Add rules to your VPCs security group that allow inbound HTTP, HTTPS, and SSH access from IPv6 addresses.
7. To confirm that your VPC endpoint has been configured correctly, you have to use a `cqlsh`
   connection to Amazon Keyspaces. If you use your local environment or
   the Amazon Keyspaces CQL editor in the AWS Management Console, the connection automatically goes through
   the public endpoint instead of your VPC endpoint. To use `cqlsh` to
   test your VPC endpoint connection in this tutorial, complete the setup
   instructions in [Using cqlsh to connect to
   Amazon Keyspaces](programmatic.md "programmatic.md").
   You are now ready to create a dual-stack VPC endpoint for Amazon Keyspaces.
