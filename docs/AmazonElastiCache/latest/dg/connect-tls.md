# Connecting to ElastiCache (Valkey) or Amazon ElastiCache for Redis OSS with in-transit encryption using valkey-cli

To access data from ElastiCache for Redis OSS caches enabled with in-transit encryption, you use clients that work with Secure Socket Layer (SSL). You can also use valkey-cli with TLS on Amazon Linux 2023.
If your client does not support TLS, you can use the `stunnel` command on your client host to create an SSL tunnel to the Redis OSS nodes.

## Encrypted connection with Linux

To use valkey-cli to connect to a Valkey or Redis OSS cluster that has in-transit encryption enabled on Amazon Linux 2023, follow these steps.

1. At the command prompt of your EC2 instance, install the Valkey package. The valkey-cli utility included in this package is built with TLS support.

```
sudo dnf install valkey -y
```

2. Confirm that the utility is installed.

```
valkey-cli --version
```

3. To connect to a cluster with encryption and authentication enabled, enter this command. The `--askpass` option prompts you for the password instead of taking it on the command line, which keeps it out of your shell history and out of the process list.

```
valkey-cli -h `Primary or Configuration Endpoint` --tls --askpass -p 6379
```

###### Note

If you are connecting to a cluster-mode enabled cache using the Configuration Endpoint, add the `-c` flag to enable cluster mode in the client. This allows the client to follow `MOVED` and `ASK` redirections automatically:

```
valkey-cli -c -h `Configuration Endpoint` --tls --askpass -p 6379
```

###### Note

If you install the redis6 package on Amazon Linux 2023 instead, use the command `redis6-cli` in place of `valkey-cli`:

```
redis6-cli -h `Primary or Configuration Endpoint` --tls -p 6379
```

###### Note

If your Linux distribution doesn't provide a Valkey package, you can build the utility from source instead. Install `gcc`, `make`, and the OpenSSL development package, download a current source release as described in [Install Valkey](https://valkey.io/topics/installation/ "https://valkey.io/topics/installation/") on the Valkey website, and then run `make valkey-cli BUILD_TLS=yes`. A client that you build from source doesn't receive package updates, so you must update it yourself as new releases become available.

## Encrypted connection with stunnel

To use valkey-cli to connect to a Redis OSS cluster enabled with in-transit encryption using stunnel, follow these steps.

1. Use SSH to connect to your client and install `stunnel`.

```
sudo yum install stunnel
```

2. Run the following command to create and edit file `'/etc/stunnel/valkey-cli.conf'` simultaneously to add a ElastiCache for Redis OSS cluster endpoint to one or more connection parameters, using the provided output below as template.

```
vi /etc/stunnel/valkey-cli.conf


fips = no
setuid = root
setgid = root
pid = /var/run/stunnel.pid
debug = 7
delay = yes
options = NO_SSLv2
options = NO_SSLv3
[valkey-cli]
   client = yes
   accept = 127.0.0.1:6379
   connect = primary.ssltest.wif01h.use1.cache.amazonaws.com:6379
[valkey-cli-replica]
   client = yes
   accept = 127.0.0.1:6380
   connect = ssltest-02.ssltest.wif01h.use1.cache.amazonaws.com:6379
```

In this example, the config file has two connections, the `valkey-cli` and the `valkey-cli-replica`.
The parameters are set as follows:

    * **client** is set to yes to specify this stunnel instance is a client.
    * **accept** is set to the client IP. In this example, the
     primary is set to the Redis OSS default 127.0.0.1 on port 6379. The replica must
     call a different port and set to 6380. You can use ephemeral ports
     1024–65535. For more information, see [Ephemeral ports](../../../AmazonVPC/latest/UserGuide/VPC_ACLs.md#VPC_ACLs_Ephemeral_Ports "../../../AmazonVPC/latest/UserGuide/VPC_ACLs.md#VPC_ACLs_Ephemeral_Ports") in the *Amazon VPC User Guide.*
    * **connect** is set to the Redis OSS server endpoint. For more information, see
     [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md").

3. Start `stunnel`.

```
sudo stunnel /etc/stunnel/valkey-cli.conf
```

Use the `netstat` command to confirm that the tunnels started.

```
sudo netstat -tulnp | grep -i stunnel

tcp        0      0 127.0.0.1:6379              0.0.0.0:*                   LISTEN      3189/stunnel
tcp        0      0 127.0.0.1:6380              0.0.0.0:*                   LISTEN      3189/stunnel
```

4. Connect to the encrypted Redis OSS node using the local endpoint of the tunnel.

   - If no AUTH password was used during ElastiCache for Redis OSS cluster creation, this example uses the valkey-cli to connect to the ElastiCache for Redis OSS server using complete path for valkey-cli, on Amazon Linux:

   ```
   /home/ec2-user/redis-7.2.5/src/valkey-cli -h localhost -p 6379
   ```

   If AUTH password was used during Redis OSS cluster creation, this example uses valkey-cli to connect to the Redis OSS server using complete path for valkey-cli, on Amazon Linux:

   ```
    /home/ec2-user/redis-7.2.5/src/valkey-cli -h localhost -p 6379 -a `my-secret-password`
   ```

OR

    * Change directory to redis-7.2.5 and do the following:


    If no AUTH password was used during ElastiCache for Redis OSS cluster creation, this example uses the valkey-cli to connect to the ElastiCache for Redis OSS server using complete path for valkey-cli, on Amazon Linux:



    ```
    src/valkey-cli -h localhost -p 6379
    ```

    If AUTH password was used during Redis OSS cluster creation, this example uses valkey-cli to connect to the Valkey or Redis OSS server using complete path for valkey-cli, on Amazon Linux:



    ```
    src/valkey-cli -h localhost -p 6379 -a `my-secret-password`
    ```

This example uses Telnet to connect to the Valkey Redis OSS server.

```
telnet localhost 6379

Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
auth MySecretPassword
+OK
get foo
$3
bar
```

5. To stop and close the SSL tunnels, `pkill` the stunnel process.

```
sudo pkill stunnel
```
