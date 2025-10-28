# Using `cqlsh` to connect to

Amazon Keyspaces

To connect to Amazon Keyspaces using `cqlsh`, you can use the `cqlsh-expansion`. This is a toolkit that contains
common Apache Cassandra tooling like `cqlsh` and helpers that are preconfigured for Amazon Keyspaces while maintaining
full compatibility with Apache Cassandra. The `cqlsh-expansion` integrates the SigV4 authentication plugin and allows you to connect
using IAM access keys instead of user name and password. You only need to install the
`cqlsh` scripts to make a connection and not the full Apache Cassandra distribution, because Amazon Keyspaces is serverless. This lightweight
install package includes the `cqlsh-expansion` and the classic `cqlsh` scripts that you can install on any platform that supports Python.

###### Note

`Murmur3Partitioner` is the recommended partitioner for Amazon Keyspaces and the
`cqlsh-expansion`. The `cqlsh-expansion` doesn't support the
Amazon Keyspaces `DefaultPartitioner`. For more information, see [Working with partitioners in Amazon Keyspaces](working-with-partitioners.md "working-with-partitioners.md").

For general information about `cqlsh`, see [`cqlsh`: the CQL shell](https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html "https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html").

###### Topics

- [Using the cqlsh-expansion to connect
  to Amazon Keyspaces](#using_cqlsh "#using_cqlsh")
- [How to manually configure
  cqlsh connections for TLS](#encrypt_using_tls "#encrypt_using_tls")

## Using the `cqlsh-expansion` to connect

to Amazon Keyspaces

###### Installing and configuring the `cqlsh-expansion`

1. To install the `cqlsh-expansion` Python package, you can run a `pip` command. This installs
   the `cqlsh-expansion` scripts on your machine using a _pip install_ along with a
   file containing a list of dependencies. The `--user flag` tells `pip` to use the Python user install
   directory for your platform. On a Unix based system, that should be the `~/.local/` directory.

You need Python 3 to install the `cqlsh-expansion`, to find out your Python version, use `Python --version`.
To install, you can run the following command.

```
`python3 -m pip install --user cqlsh-expansion`
```

The output should look similar to this.

```
`Collecting cqlsh-expansion
 Downloading cqlsh_expansion-0.9.6-py3-none-any.whl (153 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 153.7/153.7 KB 3.3 MB/s eta 0:00:00
Collecting cassandra-driver
 Downloading cassandra_driver-3.28.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (19.1 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.1/19.1 MB 44.5 MB/s eta 0:00:00
Requirement already satisfied: six>=1.12.0 in /usr/lib/python3/dist-packages (from cqlsh-expansion) (1.16.0)
Collecting boto3
 Downloading boto3-1.29.2-py3-none-any.whl (135 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.8/135.8 KB 17.2 MB/s eta 0:00:00
Collecting cassandra-sigv4>=4.0.2
 Downloading cassandra_sigv4-4.0.2-py2.py3-none-any.whl (9.8 kB)
Collecting botocore<1.33.0,>=1.32.2
 Downloading botocore-1.32.2-py3-none-any.whl (11.4 MB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.4/11.4 MB 60.9 MB/s eta 0:00:00
Collecting s3transfer<0.8.0,>=0.7.0
 Downloading s3transfer-0.7.0-py3-none-any.whl (79 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.8/79.8 KB 13.1 MB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1
 Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting geomet<0.3,>=0.1
 Downloading geomet-0.2.1.post1-py3-none-any.whl (18 kB)
Collecting python-dateutil<3.0.0,>=2.1
 Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 KB 33.1 MB/s eta 0:00:00
Requirement already satisfied: urllib3<2.1,>=1.25.4 in /usr/lib/python3/dist-packages (from botocore<1.33.0,>=1.32.2->boto3->cqlsh-expansion) (1.26.5)
Requirement already satisfied: click in /usr/lib/python3/dist-packages (from geomet<0.3,>=0.1->cassandra-driver->cqlsh-expansion) (8.0.3)
Installing collected packages: python-dateutil, jmespath, geomet, cassandra-driver, botocore, s3transfer, boto3, cassandra-sigv4, cqlsh-expansion
 WARNING: The script geomet is installed in '/home/ubuntu/.local/bin' which is not on PATH.
 Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
 WARNING: The scripts cqlsh, cqlsh-expansion and cqlsh-expansion.init are installed in '/home/ubuntu/.local/bin' which is not on PATH.
 Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed boto3-1.29.2 botocore-1.32.2 cassandra-driver-3.28.0 cassandra-sigv4-4.0.2 cqlsh-expansion-0.9.6 geomet-0.2.1.post1 jmespath-1.0.1 python-dateutil-2.8.2 s3transfer-0.7.0`
```

If the install directory is not in the `PATH`, you need to add it following the instructions of your
operating system. Below is one example for Ubuntu Linux.

```
export PATH="$PATH:/home/ubuntu/.local/bin"
```

To confirm that the package is installed, you can run the following command.

```
cqlsh-expansion --version
```

The output should look like this.

```
`cqlsh 6.1.0`
```

2.  To configure the `cqlsh-expansion`, you can run a post-install script to
    automatically complete the following steps:

        1. Create the `.cassandra` directory in the user home directory if it
         doesn't already exist.
        2. Copy a preconfigured `cqlshrc` configuration file into the
         `.cassandra` directory.
        3. Copy the combined certificate file into the `.cassandra` directory. Amazon Keyspaces
         uses this certificate to configure the secure connection with Transport
         Layer Security (TLS). Encryption in transit provides an additional layer
         of data protection by encrypting your data as it travels to and from

         Amazon Keyspaces. For more information about certificates, see [How to manually configure
         cqlsh connections for TLS](#encrypt_using_tls "#encrypt_using_tls").

    To review the script first, you can access it in the Github repo at [`post_install.py`](https://github.com/aws-samples/amazon-keyspaces-toolkit/blob/master/cqlsh-expansion/cqlsh_expansion/post_install.py "https://github.com/aws-samples/amazon-keyspaces-toolkit/blob/master/cqlsh-expansion/cqlsh_expansion/post_install.py").

To use the script, you can run the following command.

```
`cqlsh-expansion.init`
```

###### Note

The directory and file created by the post-install script are not removed when you uninstall the `cqlsh-expansion`
using `pip uninstall`, and have to be deleted manually.

###### Connecting to Amazon Keyspaces using the `cqlsh-expansion`

1. Configure your AWS Region and add it as a user environment variable.

To add your default Region as an environment variable on a Unix based system, you can
run the following command. For this example, we use `us-east-1`.

```
export AWS_DEFAULT_REGION=us-east-1
```

For more information about how to set environment variables, including for other platforms, see [How to set environment variables](../../../cli/latest/userguide/cli-configure-envvars.md#envvars-set "../../../cli/latest/userguide/cli-configure-envvars.md#envvars-set"). 2. Find your service endpoint.

Choose the appropriate service endpoint for your Region. To review the available endpoints for Amazon Keyspaces, see
[Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"). For this example, we use the
endpoint `cassandra.us-east-1.amazonaws.com`. 3. Configure the authentication method.

Connecting with IAM access keys (IAM users, roles, and federated identities)
is the recommended method for enhanced security.

Before you can connect with IAM access keys, you need to complete the
following steps:

    1. Create an IAM user, or follow the best practice and create an IAM role that IAM users
     can assume. For more information on how to create IAM access keys, see
     [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").
    2. Create an IAM policy that grants the role (or IAM user) at least read-only access to
     Amazon Keyspaces. For more information about the permissions required for the IAM user
     or role to connect to Amazon Keyspaces, see [Accessing
     Amazon Keyspaces tables](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-one-table "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-one-table").
    3. Add the access keys of the IAM user to the user's environment variables as shown in the
     following example.



    ```
    export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
    export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    ```

    For more information about how to set environment variables, including for other platforms, see [How to set environment variables](../../../cli/latest/userguide/cli-configure-envvars.md#envvars-set "../../../cli/latest/userguide/cli-configure-envvars.md#envvars-set").


    ###### Note

    If you're connecting from an Amazon EC2 instance, you also need to configure an outbound rule in the
     security group that allows traffic from the instance to Amazon Keyspaces. For more information about how to view and edit
     EC2 outbound rules, see [Add
     rules to a security group in the Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#adding-security-group-rule").

4. Connect to Amazon Keyspaces using the `cqlsh-expansion` and SigV4 authentication.

To connect to Amazon Keyspaces with the `cqlsh-expansion`, you can use the following command. Make sure to replace the
service endpoint with the correct endpoint for your Region.

```
`cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl`
```

If the connection is successful, you should see output similar to the following example.

```
`Connected to Amazon Keyspaces at cassandra.us-east-1.amazonaws.com:9142
[cqlsh 6.1.0 | Cassandra 3.11.2 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh current consistency level is ONE.
cqlsh>`
```

If you encounter a connection error, see [I can't connect to Amazon Keyspaces with
cqlsh](troubleshooting.md#troubleshooting.connection.cqlsh "troubleshooting.md#troubleshooting.connection.cqlsh") for troubleshooting
information.

    * Connect to Amazon Keyspaces with service-specific credentials.


    To connect with the traditional username and password combination that
     Cassandra uses for authentication, you must first create
     service-specific credentials for Amazon Keyspaces as described in [Create service-specific
     credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md"). You also have to give that
     user permissions to access Amazon Keyspaces, for more information see [Accessing
     Amazon Keyspaces tables](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-one-table "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-one-table").


    After you have created service-specific credentials and permissions for the user, you
     must update the `cqlshrc` file, typically found in the user directory path `~/.cassandra/`.
     In the `cqlshrc` file, go to the Cassandra `[authentication]` section and comment out the SigV4 module
     and class under `[auth_provider]` using the ";" character as shown in the following example.



    ```
    [auth_provider]

    ; module = cassandra_sigv4.auth

    ; classname = SigV4AuthProvider
    ```

    After you have updated the `cqlshrc` file, you can connect to Amazon Keyspaces with service-specific credentials using the following command.



    ```
    `cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 -u `myUserName` -p `myPassword` --ssl`
    ```

###### Cleanup

- To remove the `cqlsh-expansion` package you can use the `pip uninstall` command.

```
`pip3 uninstall cqlsh-expansion`
```

The `pip3 uninstall` command doesn't remove the directory and related files
created by the post-install script. To remove the folder and files created by the post-install script, you can delete the
`.cassandra` directory.

## How to manually configure

`cqlsh` connections for TLS

Amazon Keyspaces only accepts secure connections using Transport Layer Security (TLS). You can
use the `cqlsh-expansion` utility that automatically downloads the
certificates for you and installs a preconfigured `cqlshrc` configuration file. For more information, see [Using the cqlsh-expansion to connect
to Amazon Keyspaces](#using_cqlsh "#using_cqlsh") on this
page.

If you want to download the certificates and configure the connection manually, you can do so using the
following steps.

1.  Download the following digital certificates and save
    the files locally or in your home directory.

        1. AmazonRootCA1
        2. AmazonRootCA2
        3. AmazonRootCA3
        4. AmazonRootCA4
        5. Starfield Class 2 Root (optional – for backward compatibility)

    To download the certificates, you can use the following commands.

```
curl -O https://www.amazontrust.com/repository/AmazonRootCA1.pem
curl -O https://www.amazontrust.com/repository/AmazonRootCA2.pem
curl -O https://www.amazontrust.com/repository/AmazonRootCA3.pem
curl -O https://www.amazontrust.com/repository/AmazonRootCA4.pem
curl -O https://certs.secureserver.net/repository/sf-class2-root.crt
```

###### Note

Amazon Keyspaces previously used TLS certificates anchored to the Starfield Class 2 CA.
AWS is migrating all AWS Regions to certificates issued under Amazon Trust Services (Amazon Root CAs 1–4).
During this transition, configure clients to trust both Amazon Root CAs 1–4 and the Starfield root to ensure compatibility across all Regions. 2. Combine all downloaded certificates into a single `pem` file with the name
`keyspaces-bundle.pem` in our examples. You can do this by running the following command. Take note of the path to the
file, you need this later.

```
cat AmazonRootCA1.pem \
 AmazonRootCA2.pem \
 AmazonRootCA3.pem \
 AmazonRootCA4.pem \
 sf-class2-root.crt \
 > `keyspaces-bundle.pem`
```

3. Open the `cqlshrc` configuration file in the Cassandra home
   directory, for example `${HOME}/.cassandra/cqlshrc`
   and add the following lines.

```
[connection]
port = 9142
factory = cqlshlib.ssl.ssl_transport_factory

[ssl]
validate = true
certfile =  `path_to_file/keyspaces-bundle.pem`
```
