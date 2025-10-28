# Verifying your agent's network

connections

Once you activate your AWS DataSync agent, make sure that the agent has network
connectivity to your storage system and the DataSync service.

## Accessing your agent's local

console

How you access your agent's local console depends on the type of agent you're
using.

For
security reasons, you can't remotely connect to the local
console of the DataSync agent virtual machine (VM).

- If this is your first time using the local
  console, log in with the default credentials. The default user name
  is `admin` and the password is
  `password`.

###### Note

We recommend changing the default password. To do this, on the
console main menu enter `5` (or
`6` for VMware VMs), then run the
`passwd` command to change the password.
To connect to an Amazon EC2 agent's local console, you must use SSH.

**Before you begin**: Make sure that your EC2
instance's security group allows access with SSH (TCP port 22).

1. Open a terminal and copy the following `ssh`
   command:

```
ssh -i `/path/key-pair-name`.pem `instance-user-name`@`instance-public-ip-address`
```

    * For `/path/key-pair-name`,
     specify the path and file name (`.pem`) of the
     private key required to connect to your instance.
    * For `instance-user-name`, specify
     `admin`.
    * For `instance-public-ip-address`,
     specify the public IP address of your instance.

2. Run the `ssh` command to connect to the
   instance.
   Once connected, the main menu of the agent's local console
   displays.

## Verifying your agent's

connection to your storage system

Test whether your DataSync agent can connect to your storage system. For more
information, see [1. Network connection between your
storage system and agent](networking-datasync.md#1-network-between-storage-agent "networking-datasync.md#1-network-between-storage-agent").

1. [Access your
   agent's local console](#local-console-login-getting-started "#local-console-login-getting-started").
2. On the **AWS DataSync Activation - Configuration** main
   menu, enter `3`.
3. Enter one of the following options:
   1. Enter `1` to test an NFS server
      connection.
   2. Enter `2` to test an SMB server
      connection.
   3. Enter `3` to test an object storage server
      connection.
   4. Enter `4` to test an HDFS connection.
   5. Enter `5` to test a Microsoft Azure
      Blob Storage connection.

4. Enter the storage server's IP address or domain name.

Remember the following when entering the IP address or domain name:

    * Don't include a protocol. For example, enter
     `mystorage.com` instead of
     `https://mystorage.com`.
    * For HDFS, enter the IP address or domain name of the NameNode or
     DataNode in the Hadoop cluster.

5. If requested, enter the TCP port for connecting to the storage server (for
   example, `443`).

See if the connectivity test **PASSED** or
**FAILED**.

## Verifying your agent's connection to the DataSync

service

Test whether your DataSync agent can connect to the DataSync service. For more
information, see [2. Network connection between your
agent and DataSync service](networking-datasync.md#2-network-between-agent-service "networking-datasync.md#2-network-between-agent-service").

1. [Access your
   agent's local console](#local-console-login-getting-started "#local-console-login-getting-started").
2. On the **AWS DataSync Activation - Configuration** main
   menu, enter `2` to begin testing network
   connectivity.

If your agent is activated, the **Test Network
Connectivity** option can be initiated without any additional
user input, because the Region and endpoint type are taken from the
activated agent information. 3. Enter the type of DataSync service endpoint that your agent uses:

    1. For public service endpoints, enter `1` and
     the AWS Region where your agent is activated.
    2. For FIPS service endpoints, enter `2` and the
     Region where your agent is activated.
    3. For VPC service endpoints, enter `3`.
    4. For FIPS VPC service endpoints, enter `4`.You see a **PASSED** or **FAILED**

message. 4. If you see a **FAILED** message, check your network
configuration. For more information, see [AWS DataSync network requirements](datasync-network.md "datasync-network.md").

## Next steps

Create the DataSync location that you want to use with your agent. This might be an
[on-premises](transferring-on-premises-storage.md "transferring-on-premises-storage.md") or [other cloud](transferring-other-cloud-storage.md "transferring-other-cloud-storage.md") location.
