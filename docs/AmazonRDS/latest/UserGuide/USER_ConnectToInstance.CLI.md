

# Connecting from the MySQL command-line client (unencrypted)
<a name="USER_ConnectToInstance.CLI"></a>

**Important**  
Only use an unencrypted MySQL connection when the client and server are in the same VPC and the network is trusted. For information about using encrypted connections, see [Connecting to your MySQL DB instance on Amazon RDS with SSL/TLS from the MySQL command-line client (encrypted)](USER_ConnectToInstanceSSL.CLI.md).

To connect to a DB instance using the MySQL command-line client, enter the following command at the command prompt. For the -h parameter, substitute the DNS name (endpoint) for your DB instance. For the -P parameter, substitute the port for your DB instance. For the -u parameter, substitute the user name of a valid database user, such as the master user. Enter the master user password when prompted. 

```
mysql -h {{mysql–instance1.123456789012.us-east-1.rds.amazonaws.com}} -P 3306 -u {{mymasteruser}} -p
```

After you enter the password for the user, you should see output similar to the following.

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9738
Server version: 8.0.28 Source distribution

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>
```