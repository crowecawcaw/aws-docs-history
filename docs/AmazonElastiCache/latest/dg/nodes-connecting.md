# Connecting to nodes

## Connecting to Valkey or Redis OSS nodes

Before attempting to connect to the Valkey or Redis OSS nodes in your cluster, you must have the
endpoints for the nodes. To find the endpoints, see the following:

- [Finding a Valkey or Redis OSS (Cluster Mode Disabled) Cluster's Endpoints (Console)](Endpoints.md#Endpoints.Find.Redis "Endpoints.md#Endpoints.Find.Redis")
- [Finding Endpoints for a Valkey or Redis OSS (Cluster Mode Enabled) Cluster (Console)](Endpoints.md#Endpoints.Find.RedisCluster "Endpoints.md#Endpoints.Find.RedisCluster")
- [Finding Endpoints (AWS CLI)](Endpoints.md#Endpoints.Find.CLI "Endpoints.md#Endpoints.Find.CLI")
- [Finding Endpoints (ElastiCache API)](Endpoints.md#Endpoints.Find.API "Endpoints.md#Endpoints.Find.API")

In the following example, you use the _valkey-cli_ utility to
connect to a cluster that is running Valkey or Redis OSS.

###### Note

For more information about available commands, see the [Commands](http://valkey.io/commands "http://valkey.io/commands") webpage.

###### To connect to a Valkey or Redis OSS cluster using the _valkey-cli_

1. Connect to your Amazon EC2 instance using the connection utility of your choice.

###### Note

For instructions on how to connect to an Amazon EC2 instance, see the
[Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/GettingStartedGuide.md "../../../AWSEC2/latest/GettingStartedGuide.md"). 2. To build `valkey-cli`, download and install the GNU Compiler
Collection (`gcc`). At the command prompt of your EC2 instance, enter
the following command and enter `y` at the confirmation
prompt.

```
sudo yum install gcc
```

Output similar to the following appears.

```
`Loaded plugins: priorities, security, update-motd, upgrade-helper
Setting up Install Process
Resolving Dependencies
--> Running transaction check

...(output omitted)...

Total download size: 27 M
Installed size: 53 M
Is this ok [y/N]: y
Downloading Packages:
(1/11): binutils-2.22.52.0.1-10.36.amzn1.x86_64.rpm | 5.2 MB 00:00
(2/11): cpp46-4.6.3-2.67.amzn1.x86_64.rpm | 4.8 MB 00:00
(3/11): gcc-4.6.3-3.10.amzn1.noarch.rpm | 2.8 kB 00:00

...(output omitted)...

Complete!`

```

3. Download and compile the _valkey-cli_ utility. This utility
   is included in the Valkey software distribution. At the command prompt of your
   EC2 instance, type the following commands:

###### Note

For Ubuntu systems, before running `make`, run `make
 distclean`.

```
wget https://github.com/valkey-io/valkey/archive/refs/tags/8.0.0.tar.gz
tar xvzf valkey-8.0.0.tar.gz
cd valkey-8.0.0
make distclean      # ubuntu systems only
make
```

4. At the command prompt of your EC2 instance, type the following command.

```
src/valkey-cli -c -h `mycachecluster.eaogs8.0001.usw2.cache.amazonaws.com` -p `6379`
```

A Valkey or Redis OSS command prompt similar to the following appears.

```
redis mycachecluster.eaogs8.0001.usw2.cache.amazonaws.com 6379>
```

5. Test the connection by running Valkey or Redis OSS commands.

You are now connected to the cluster and can run Valkey or Redis OSS commands. The
following are some example commands with their Valkey or Redis OSS responses.

```
set a "hello"          // Set key "a" with a string value and no expiration
OK
get a                  // Get value for key "a"
"hello"
get b                  // Get value for key "b" results in miss
(nil)
set b "Good-bye" EX 5  // Set key "b" with a string value and a 5 second expiration
get b
"Good-bye"
                   // wait 5 seconds
get b
(nil)                  // key has expired, nothing returned
quit                   // Exit from valkey-cli
```

For connecting to nodes or clusters which have Secure Sockets Layer
(SSL) encryption (in-transit enabled), see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md "in-transit-encryption.md").

## Connecting to Memcached nodes

Before attempting to connect to your Memcached cluster, you must have the endpoints
for the nodes. To find the endpoints, see the following:

- [Finding a Cluster's Endpoints (Console) (Memcached)](Endpoints.md#Endpoints.Find.Memcached "Endpoints.md#Endpoints.Find.Memcached")
- [Finding Endpoints (AWS CLI)](Endpoints.md#Endpoints.Find.CLI "Endpoints.md#Endpoints.Find.CLI")
- [Finding Endpoints (ElastiCache API)](Endpoints.md#Endpoints.Find.API "Endpoints.md#Endpoints.Find.API")

In the following example, you use the _telnet_ utility to connect
to a node that is running Memcached.

###### Note

For more information about Memcached and available Memcached commands, see the
[Memcached](http://memcached.org/ "http://memcached.org/") website.

###### To connect to a node using _telnet_

1. Connect to your Amazon EC2 instance by using the connection utility of your choice.

###### Note

For instructions on how to connect to an Amazon EC2 instance, see the
[Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/GettingStartedGuide.md "../../../AWSEC2/latest/GettingStartedGuide.md"). 2. Download and install the _telnet_ utility on your Amazon EC2
instance. At the command prompt of your Amazon EC2 instance, type the following
command and type _y_ at the command prompt.

```
sudo yum install telnet
```

Output similar to the following appears.

```
`Loaded plugins: priorities, security, update-motd, upgrade-helper
Setting up Install Process
Resolving Dependencies
--> Running transaction check

...(output omitted)...

Total download size: 63 k
Installed size: 109 k
Is this ok [y/N]: y
Downloading Packages:
telnet-0.17-47.7.amzn1.x86_64.rpm | 63 kB 00:00

...(output omitted)...

Complete!`
```

3. At the command prompt of your Amazon EC2 instance, type the following command,
   substituting the endpoint of your node for the one shown in this example.

```
telnet mycachecluster.eaogs8.0001.usw2.cache.amazonaws.com 11211
```

Output similar to the following appears.

```
Trying 128.0.0.1...
Connected to mycachecluster.eaogs8.0001.usw2.cache.amazonaws.com.
Escape character is '^]'.
>
```

4. Test the connection by running Memcached commands.

You are now connected to a node, and you can run Memcached commands. The
following is an example.

```
set a 0 0 5      // Set key "a" with no expiration and 5 byte value
hello            // Set value as "hello"
STORED
get a            // Get value for key "a"
VALUE a 0 5
hello
END
get b            // Get value for key "b" results in miss
END
>
```
