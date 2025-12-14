# Configuring SQL\*Plus to

use SSL with an RDS for Oracle DB instance

Before you can connect to an RDS for Oracle DB instance that uses the Oracle SSL option, you
must configure SQL\*Plus before connecting.

###### Note

To allow access to the DB instance from the appropriate clients, ensure that your security groups are configured correctly. For more information,
see [Controlling access with security
groups](Overview.md "Overview.md"). Also, these instructions are for SQL\*Plus and other
clients that directly use an Oracle home. For JDBC connections, see [Setting up an SSL connection over JDBC](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md").

###### To configure SQL\*Plus to use SSL to connect to an RDS for Oracle DB instance

1. Set the `ORACLE_HOME` environment variable to the location of
   your Oracle home directory.

The path to your Oracle home directory depends on your installation. The
following example sets the `ORACLE_HOME` environment
variable.

```
prompt>export ORACLE_HOME=/home/user/app/user/product/19.0.0/dbhome_1
```

For information about setting Oracle environment variables, see [SQL\*Plus environment variables](http://docs.oracle.com/database/121/SQPUG/ch_two.htm#SQPUG331 "http://docs.oracle.com/database/121/SQPUG/ch_two.htm#SQPUG331") in the Oracle documentation, and
also see the Oracle installation guide for your operating system. 2. Append `$ORACLE_HOME/lib` to the
`LD_LIBRARY_PATH` environment variable.

The following is an example that sets the LD_LIBRARY_PATH environment
variable.

```
prompt>export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
```

3. Create a directory for the Oracle wallet at
   `$ORACLE_HOME/ssl_wallet`.

The following is an example that creates the Oracle wallet
directory.

```
prompt>mkdir $ORACLE_HOME/ssl_wallet
```

4. Download the certificate bundle .pem file that works for all AWS Regions and
   put the file in the ssl_wallet directory. For information, see [Using SSL/TLS to encrypt a connection to a DB
   instance or cluster](UsingWithRDS.md "UsingWithRDS.md").
5. In the `$ORACLE_HOME/network/admin` directory, modify
   or create the `tnsnames.ora` file and include the following
   entry.

```
`net_service_name` =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS =
        (PROTOCOL = TCPS)
        (HOST = `endpoint`)
        (PORT = `ssl_port_number`)
      )
    )
    (CONNECT_DATA =
      (SID = `database_name`)
    )
    (SECURITY =
      (SSL_SERVER_CERT_DN = "C=US,ST=Washington,L=Seattle,O=Amazon.com,OU=RDS,CN=`endpoint`")
    )
  )
```

6. In the same directory, modify or create the
   sqlnet.ora file and include the following
   parameters.

###### Note

To communicate with entities over a TLS secured connection, Oracle requires a wallet with the necessary certificates for authentication.
You can use Oracle's ORAPKI utility to create and maintain Oracle wallets, as shown in step 7. For more information, see
[Setting up Oracle wallet using ORAPKI](https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tsvt/task_SettingUpOracleWalletUsingORAPKI.html "https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tsvt/task_SettingUpOracleWalletUsingORAPKI.html") in the Oracle documentation.

```
WALLET_LOCATION = (SOURCE = (METHOD = FILE) (METHOD_DATA = (DIRECTORY = $ORACLE_HOME/ssl_wallet)))
SSL_CLIENT_AUTHENTICATION = FALSE
SSL_VERSION = 1.0
SSL_CIPHER_SUITES = (SSL_RSA_WITH_AES_256_CBC_SHA)
SSL_SERVER_DN_MATCH = ON
```

###### Note

You can set `SSL_VERSION` to a higher value if your DB instance supports it. 7. Run the following command to create the Oracle wallet.

```
prompt>orapki wallet create -wallet $ORACLE_HOME/ssl_wallet -auto_login_only
```

8. Extract each certificate in the .pem bundle file into a separate .pem file
   using an OS utility.
9. Add each certificate to your wallet using separate `orapki`
   commands, replacing `certificate-pem-file`
   with the absolute file name of the .pem file.

```
prompt>orapki wallet add -wallet $ORACLE_HOME/ssl_wallet -trusted_cert -cert
      `certificate-pem-file` -auto_login_only
```

For more information, see [Rotating your SSL/TLS
certificate](UsingWithRDS.md "UsingWithRDS.md").
