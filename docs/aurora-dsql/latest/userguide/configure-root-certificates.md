# Configuring SSL/TLS certificates for Aurora DSQL connections

Aurora DSQL requires all connections to use Transport Layer Security (TLS) encryption. To
establish secure connections, your client system must trust the Amazon Root Certificate
Authority (Amazon Root CA 1). This certificate is pre-installed on many operating
systems. This section provides instructions for verifying the pre-installed Amazon Root
CA 1 certificate on various operating systems, and guides you through the process of
manually installing the certificate if it is not already present.

We recommend using PostgreSQL version 17.

###### Important

For production environments, we recommend using `verify-full` SSL mode to ensure the highest level of connection security. This mode verifies that the server certificate is signed by a trusted certificate authority and that the server hostname matches the certificate.

## Verifying pre-installed certificates

In most operating systems, **Amazon Root CA 1** is
already pre-installed. To validate this, you can follow the steps below.

### Linux (RedHat/CentOS/Fedora)

Run the following command in your terminal:

```
trust list | grep "Amazon Root CA 1"
```

If the certificate is installed, you see the following output:

```
label: Amazon Root CA 1
```

### macOS

1. Open Spotlight Search (**Command** +
   **Space**)
2. Search for **Keychain Access**
3. Select **System Roots** under **System Keychains**
4. Look for **Amazon Root CA 1** in the certificate list

### Windows

###### Note

Due to a known issue with the psql Windows client, using system root certificates (`sslrootcert=system`) may return the following error: `SSL error: unregistered scheme`. You can follow the [Connecting from Windows](#connect-windows "#connect-windows") as an alternative way to connect to your cluster using SSL.

If **Amazon Root CA 1** is not installed in your operating
system, follow the steps below.

## Installing certificates

If the `Amazon Root CA 1` certificate is not pre-installed on your operating system, you will need to manually install it in order to establish secure connections to your Aurora DSQL cluster.

### Linux certificate installation

Follow these steps to install the Amazon Root CA certificate on Linux
systems.

1. Download the Root Certificate:

```
wget https://www.amazontrust.com/repository/AmazonRootCA1.pem
```

2. Copy the certificate to the trust store:

```
sudo cp ./AmazonRootCA1.pem /etc/pki/ca-trust/source/anchors/
```

3. Update the CA trust store:

```
sudo update-ca-trust
```

4. Verify the installation:

```
trust list | grep "Amazon Root CA 1"
```

### macOS certificate installation

These certificate installation steps are optional. The [Linux certificate installation](#install-linux "#install-linux") also work for a
macOS.

1. Download the Root Certificate:

```
wget https://www.amazontrust.com/repository/AmazonRootCA1.pem
```

2. Add the certificate to the System keychain:

```
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain AmazonRootCA1.pem
```

3. Verify the installation:

```
security find-certificate -a -c "Amazon Root CA 1" -p /Library/Keychains/System.keychain
```

## Connecting with SSL/TLS verification

Before configuring SSL/TLS certificates for secure connections to your Aurora DSQL cluster, ensure you have the following prerequisites.

- PostgreSQL version 17 installed
- AWS CLI configured with appropriate credentials
- Aurora DSQL cluster endpoint information

### Connecting from Linux

1. Generate and set the authentication token:

```
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token --region=`your-cluster-region` --hostname `your-cluster-endpoint`)
```

2. Connect using system certificates (if pre-installed):

```
PGSSLROOTCERT=system \
PGSSLMODE=verify-full \
psql --dbname postgres \
--username admin \
--host `your-cluster-endpoint`
```

3. Or, connect using a downloaded certificate:

```
PGSSLROOTCERT=/full/path/to/root.pem \
PGSSLMODE=verify-full \
psql --dbname postgres \
--username admin \
--host `your-cluster-endpoint`
```

###### Note

For more on PGSSLMODE settings, see [sslmode](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-SSLMODE "https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-SSLMODE") in the PostgresQL 17 [Database
Connection Control Functions](https://www.postgresql.org/docs/current/libpq-connect.html "https://www.postgresql.org/docs/current/libpq-connect.html") documentation.

### Connecting from macOS

1. Generate and set the authentication token:

```
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token --region=`your-cluster-region` --hostname `your-cluster-endpoint`)
```

2. Connect using system certificates (if pre-installed):

```
PGSSLROOTCERT=system \
PGSSLMODE=verify-full \
psql --dbname postgres \
--username admin \
--host `your-cluster-endpoint`
```

3. Or, download the root certificate and save it as `root.pem` (if
   certificate is not pre-installed)

```
PGSSLROOTCERT=/full/path/to/root.pem \
PGSSLMODE=verify-full \
psql —dbname postgres \
--username admin \
--host your_cluster_endpoint
```

4. Connect using psql:

```
PGSSLROOTCERT=/full/path/to/root.pem \
PGSSLMODE=verify-full \
psql —dbname postgres \
--username admin \
--host your_cluster_endpoint
```

### Connecting from Windows

#### Using Command Prompt

1. Generate the authentication token:

```
aws dsql generate-db-connect-admin-auth-token ^
--region=`your-cluster-region` ^
--expires-in=3600 ^
--hostname=`your-cluster-endpoint`
```

2. Set the password environment variable:

```
set "PGPASSWORD=`token-from-above`"
```

3. Set SSL configuration:

```
set PGSSLROOTCERT=C:\full\path\to\root.pem
set PGSSLMODE=verify-full
```

4. Connect to the database:

```
"C:\Program Files\PostgreSQL\17\bin\psql.exe" --dbname postgres ^
--username admin ^
--host `your-cluster-endpoint`
```

#### Using PowerShell

1. Generate and set the authentication token:

```
$env:PGPASSWORD = (aws dsql generate-db-connect-admin-auth-token --region=`your-cluster-region` --expires-in=3600 --hostname=`your-cluster-endpoint`)
```

2. Set SSL configuration:

```
$env:PGSSLROOTCERT='C:\full\path\to\root.pem'
$env:PGSSLMODE='verify-full'
```

3. Connect to the database:

```
 "C:\Program Files\PostgreSQL\17\bin\psql.exe" --dbname postgres `
--username admin `
--host `your-cluster-endpoint`
```

## Additional resources

- [PostgreSQL SSL documentation](https://www.postgresql.org/docs/current/libpq-ssl.html "https://www.postgresql.org/docs/current/libpq-ssl.html")
- [Amazon Trust Services](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/")
