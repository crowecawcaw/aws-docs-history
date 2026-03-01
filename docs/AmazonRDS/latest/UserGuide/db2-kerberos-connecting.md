# Connecting to Amazon RDS for Db2 with Kerberos authentication

Use the following procedure to connect to your Amazon RDS for Db2 DB instance with Kerberos authentication.

###### To connect to RDS for Db2 with Kerberos authentication

1. At a command prompt, run the following command. In the following example, replace
   `username` with your Microsoft Active
   Directory username.

```
kinit `username`
```

2. If the RDS for Db2 DB instance is using a publicly accessible VPC, add the IP address for your DB instance endpoint to your `/etc/hosts` file on the Amazon EC2 client. The following example obtains the IP address and then adds it to the `/etc/hosts` file.

```
% dig +short Db2-endpoint.AWS-Region.rds.amazonaws.com
;; Truncated, retrying in TCP mode.
ec2-34-210-197-118.AWS-Region.compute.amazonaws.com.
34.210.197.118

% echo "34.210.197.118  Db2-endpoint.AWS-Region.rds.amazonaws.com" >> /etc/hosts
```

3. Use the following command to log in to an RDS for Db2 DB instance that is associated
   with Active Directory. Replace `database_name` with the
   name of your RDS for Db2 database.

```
db2 connect to `database_name`
```
