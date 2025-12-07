# Using SSL/TLS with an Amazon RDS for Db2 DB instance

SSL is an industry-standard protocol for securing network connections between client and
server. After SSL version 3.0, the name was changed to TLS, but we still often refer to the
protocol as SSL. Amazon RDS supports SSL encryption for Amazon RDS for Db2 DB instances. Using SSL/TLS,
you can encrypt a connection between your application client and your RDS for Db2 DB instance.
SSL/TLS support is available in all AWS Regions for RDS for Db2.

To enable SSL/TLS encryption for an RDS for Db2 DB instance, add the Db2 SSL option to the
parameter group associated with the DB instance. Amazon RDS uses a second port, as required by
Db2, for SSL/TLS connections. Doing this allows both clear text and SSL-encrypted
communication to occur at the same time between a DB instance and a Db2 client. For example,
you can use the port with clear text communication to communicate with other resources
inside a VPC while using the port with SSL-encrypted communication to communicate with
resources outside the VPC.

###### Topics

- [Creating an SSL/TLS connection](#db2-creating-ssl-connection "#db2-creating-ssl-connection")
- [Connect to your Db2 database
  server](#db2-connecting-to-server-ssl "#db2-connecting-to-server-ssl")

## Creating an SSL/TLS connection

To create an SSL/TLS connection, choose a certificate authority (CA), download a
certificate bundle for all AWS Regions, and add parameters to a custom parameter
group.

### Step 1: Choose a CA and

download a certificate

Choose a certificate authority (CA) and download a certificate bundle for all
AWS Regions. For more information, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md").

### Step 2: Update parameters in a custom

parameter group

###### Important

If you're using the bring your own license (BYOL) model for RDS for Db2, modify
the custom parameter group that you created for your IBM Customer ID and your
IBM Site ID. If you're using a different licensing model for RDS for Db2, then follow
the procedure to add parameters to a custom parameter group. For more
information, see [Amazon RDS for Db2 licensing options](db2-licensing.md "db2-licensing.md").

You can't modify default parameter groups for RDS for Db2 DB instances. Therefore,
you must create a custom parameter group, modify it, and then attach it to your
RDS for Db2 DB instances. For information about parameter groups, see [DB parameter groups for
Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md").

Use the parameter settings in the following table.

| Parameter      | Value                                                              |
| -------------- | ------------------------------------------------------------------ |
| `DB2COMM`      | `TCPIP,SSL` or `SSL`                                               |
| `SSL_SVCENAME` | `<any port number except the number used for the non-SSL<br>port>` |

###### To update parameters in a custom parameter group

1. Create a custom parameter group by running the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") command.

Include the following required options:

    * `--db-parameter-group-name` – A name for the
     parameter group that you are creating.
    * `--db-parameter-group-family` – The Db2 engine
     edition and major version. Valid values: `db2-se-11-5`,
     `db2-ae-11.5`.
    * `--description` – A description for this
     parameter group.

For more information about creating a DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Modify the parameters in the custom parameter group that you created by
running the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md") command.

Include the following required options:

    * `--db-parameter-group-name` – The name of the
     parameter group that you created.
    * `--parameters` – An array of parameter names,
     values, and the application methods for the parameter update.

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 3. Associate the parameter group with your RDS for Db2 DB instance. For more
information, see [Associating a DB parameter group with a
DB instance in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Connect to your Db2 database

server

Instructions for connecting to your Db2 database server are language-specific.

Java

###### To connect to your Db2 database server using

Java

1. Download the JDBC driver. For more information, see [DB2 JDBC Driver Versions and Downloads](https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads "https://www.ibm.com/support/pages/db2-jdbc-driver-versions-and-downloads")in the
   IBM Support documentation.
2. Create a shell script file with the following content. This script
   adds all certificates from the bundle to a Java
   KeyStore.

###### Important

Verify that `keytool` exists on the path in the
script so that the script can locate it. If you use a Db2
client, you can locate the `keytool` under
`~sqlib/java/jdk64/jre/bin`.

```
#!/bin/bash
PEM_FILE=$1
PASSWORD=$2
KEYSTORE=$3
# number of certs in the PEM file
CERTS=$(grep 'END CERTIFICATE' $PEM_FILE| wc -l)
for N in $(seq 0 $(($CERTS - 1))); do
    ALIAS="${PEM_FILE%.*}-$N"
    cat $PEM_FILE |
    awk "n==$N { print }; /END CERTIFICATE/ { n++ }" |
    keytool -noprompt -import -trustcacerts -alias $ALIAS -keystore $KEYSTORE -storepass $PASSWORD
done
```

3. To run the shell script and import the PEM file
   with the certificate bundle into a Java KeyStore, run
   the following command. Replace
   `shell_file_name.sh` with the name of
   your shell script file and `password` with
   the password for your Java KeyStore.

```
 ./`shell_file_name.sh` global-bundle.pem `password` truststore.jks
```

4. To connect to your Db2 server, run the following command. Replace
   the following placeholders in the example with your RDS for Db2 DB
   instance information.
   - `ip_address` – The IP
     address for your DB instance endpoint.
   - `port` – The port number
     for the SSL connection. This can be any port number except
     the number that's used for the non-SSL port.
   - `database_name` – The name
     of your database in your DB instance.
   - `master_username` – The
     master username for your DB instance.
   - `master_password` – The
     master password for your DB instance.

```
export trustStorePassword=MyPassword
java -cp ~/dsdriver/jdbc_sqlj_driver/linuxamd64/db2jcc4.jar \
com.ibm.db2.jcc.DB2Jcc -url \
"jdbc:db2://`ip_address`:`port`/`database_name`:\
sslConnection=true;sslTrustStoreLocation=\
~/truststore.jks;\
sslTrustStorePassword=${trustStorePassword};\
sslVersion=TLSv1.2;\
encryptionAlgorithm=2;\
securityMechanism=7;" \
-user `master_username` -password `master_password`
```

Node.js

###### To connect to your Db2 database server using

Node.js

1. Install the **node-ibm_db** driver. For more
   information, see [Installing the node-ibm_db driver on Linux and
   UNIX systems](https://www.ibm.com/docs/en/db2/11.5?topic=nodejs-installing-node-db-driver-linux-unix-systems "https://www.ibm.com/docs/en/db2/11.5?topic=nodejs-installing-node-db-driver-linux-unix-systems") in the IBM Db2
   documentation.
2. Create a JavaScript file based on the following
   content. Replace the following placeholders in the example with your
   RDS for Db2 DB instance information.
   - `ip_address` – The IP
     address for your DB instance endpoint.
   - `master_username` – The
     master username for your DB instance.
   - `master_password` – The
     master password for your DB instance.
   - `database_name` – The name
     of your database in your DB instance.
   - `port` – The port number
     for the SSL connection. This can be any port number except
     the number that's used for the non-SSL port.

```
var ibmdb = require("ibm_db");
const hostname = "`ip_address`";
const username = "`master_username`";
const password = "`master_password`";
const database = "`database_name`";
const port = "`port`";
const certPath = "/root/qa-bundle.pem";
ibmdb.open("DRIVER={DB2};DATABASE=" + database + ";HOSTNAME=" + hostname + ";UID=" + username + ";PWD=" + password + ";PORT=" + port + ";PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=" + certPath + ";", function (err, conn){
 if (err) return console.log(err);
 conn.close(function () {
 console.log('done');
 });
});
```

3. To run the JavaScript file, run the following
   command.

```
node ssl-test.js
```

Python

###### To connect to your Db2 database server using

Python

1. Create a Python file with the following content.
   Replace the following placeholders in the example with your RDS for Db2
   DB instance information.
   - `port` – The port number
     for the SSL connection. This can be any port number except
     the number that's used for the non-SSL port.
   - `master_username` – The
     master username for your DB instance.
   - `master_password` – The
     master password for your DB instance.
   - `database_name` – The name
     of your database in your DB instance.
   - `ip_address` – The IP
     address for your DB instance endpoint.

```
import click
import ibm_db
import sys

port = `port`;
master_user_id = "`master_username`" # Master id used to create your DB instance
master_password = "`master_password`" # Master password used to create your DB instance
db_name = "`database_name`" # If not given "db-name'
vpc_customer_private_ip = "`ip_address`" # Hosts end points - Customer private IP Addressicert_path = "/root/ssl/global-bundle.pem" # cert path

@click.command()
@click.option("--path", help="certificate path")
def db2_connect(path):

    try:
        conn = ibm_db.connect(f"DATABASE={db_name};HOSTNAME={vpc_customer_private_ip};PORT={port};
            PROTOCOL=TCPIP;UID={master_user_id};PWD={master_password};SECURITY=ssl;SSLServerCertificate={path};", "", "")
        try:
            ibm_db.exec_immediate(conn, 'create table tablename (a int);')
            print("Query executed successfully")
        except Exception as e:
            print(e)
        finally:
            ibm_db.close(conn)
            sys.exit(1)
    except Exception as ex:
        print("Trying to connect...")

if __name__ == "__main__":
    db2_connect()

```

2. Create the following shell script, which runs the
   Python file you created. Replace
   `python_file_name.py`
   with the name of your Python script file.

```
#!/bin/bash
PEM_FILE=$1
# number of certs in the PEM file
CERTS=$(grep 'END CERTIFICATE' $PEM_FILE| wc -l)

for N in $(seq 0 $(($CERTS - 1))); do
    ALIAS="${PEM_FILE%.*}-$N"
    cert=`cat $PEM_FILE | awk "n==$N { print }; /END CERTIFICATE/ { n++ }"`
    cat $PEM_FILE | awk "n==$N { print }; /END CERTIFICATE/ { n++ }" > $ALIAS.pem
    python3 <`python_file_name.py`> --path $ALIAS.pem
    output=`echo $?`
    if [ $output == 1 ]; then
        break
    fi
done

```

3. To import the PEM file with the certificate bundle
   and run the shell script, run the following command. Replace
   `shell_file_name.sh` with the name of
   your shell script file.

```
./`shell_file_name.sh` global-bundle.pem
```

Db2 CLP

###### To connect to your Db2 database server using Db2 CLP

1. To connect to your Db2 instance using Db2 CLP, you
   need GSKit, which you can download at [IBM Fix Central](https://www.ibm.com/support/fixcentral/swg/selectFixes?parent=Security+Systems&product=ibm/Tivoli/IBM+Global+Security+Kit&release=All&platform=All&function=fixId&fixids=8.0.*&source=fc "https://www.ibm.com/support/fixcentral/swg/selectFixes?parent=Security+Systems&product=ibm/Tivoli/IBM+Global+Security+Kit&release=All&platform=All&function=fixId&fixids=8.0.*&source=fc"). To use Db2 CLP, you
   also need the IBM Db2 client, which you can download from [Download initial Version 11.5 clients and drivers](https://www.ibm.com/support/pages/download-initial-version-115-clients-and-drivers "https://www.ibm.com/support/pages/download-initial-version-115-clients-and-drivers") in IBM Support.
2. Create a keystore.

```
gsk8capicmd_64 -keydb -create -db "`directory`/`keystore-filename`" -pw "`changeThisPassword`" -type pkcs12 -stash
```

3. Import the certificate bundles to the keystore.

```
gsk8capicmd_64 -cert -import -file `global-bundle.pem` -target `directory`/`keystore-filename`> -target_stashed
```

4. Update the Db2 instance configuration.

```
db2 update dbm cfg using SSL_CLNT_KEYDB `keystore-filename` SSL_CLNT_STASH `keystore stash file` immediate
```

5. Catalog the node and database.

```
db2 catalog tcpip node `ssluse1` REMOTE `endpoint` SERVER `ssl_svcename` security ssl

db2 catalog database `testdb` as `ssltest` at node `ssluse1`
```

6. Connect to the database.

```
db2 connect to `ssltest` user `username` using `password`
```
