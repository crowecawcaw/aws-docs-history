# Connecting programmatically to Amazon DocumentDB

This section contains code examples that demonstrate how to connect to
Amazon DocumentDB (with MongoDB compatibility) using several different languages. The examples are
separated into two sections based on whether you are connecting to a
cluster that has Transport Layer Security (TLS) enabled or disabled. By
default, TLS is enabled on Amazon DocumentDB clusters. However, you can turn off
TLS if you want. For more information, see [Encrypting data in transit](security.encryption.md "security.encryption.md").

If you are attempting to connect to your Amazon DocumentDB from
outside the VPC in which your cluster resides, please see [Connecting to an Amazon DocumentDB cluster from outside an Amazon VPC](connect-from-outside-a-vpc.md "connect-from-outside-a-vpc.md").

Before you connect to your cluster, you must know whether TLS is
enabled on the cluster. The next section shows you how to determine the
value of your cluster's `tls` parameter using either the
AWS Management Console or the AWS CLI. Following that, you can continue by finding and
applying the appropriate code example.

###### Topics

- [Determining the value of your tls parameter](#connect_programmatically-determine_tls_value "#connect_programmatically-determine_tls_value")
- [Connecting with TLS enabled](#connect_programmatically-tls_enabled "#connect_programmatically-tls_enabled")
- [Connecting with TLS disabled](#connect_programmatically-tls_disabled "#connect_programmatically-tls_disabled")

## Determining the value of your `tls` parameter

Determining whether your cluster has TLS enabled is a two-step
process that you can perform using either the AWS Management Console or AWS CLI.

1. **Determine which parameter group is
   governing your cluster.**

Using the AWS Management Console

    1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
    2. In the left navigation pane, choose
     **Clusters**.
    3. In the list of clusters, select the name
     of your cluster.
    4. The resulting page shows the details of
     the cluster that you selected. Select the
     **Configuration** tab. In the
     **Configurations and status** section,
     locate the parameter group's name below
     **Cluster parameter group**.

Using the AWS CLI
The following AWS CLI code determines which
parameter is governing your cluster. Make sure you
replace `sample-cluster` with the name
of your cluster.

```
aws docdb describe-db-clusters \
    --db-cluster-identifier `sample-cluster` \
    --query 'DBClusters[*].[DBClusterIdentifier,DBClusterParameterGroup]'
```

Output from this operation looks something
like the following:

```
[
       [
           "sample-cluster",
           **"sample-parameter-group"**
       ]
]
```

2. **Determine the value of the `tls` parameter in
   your cluster's parameter group.**

Using the AWS Management Console

    1. In the navigation pane, choose **Parameter groups**.
    2. In the **Cluster parameter groups**
     window, select your cluster parameter group name from Step
     1d.
    3. The resulting page shows your cluster parameter group's parameters. You can see the value of the `tls` parameter here. For information on modifying this parameter, see [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md "cluster_parameter_groups-modify.md").

Using the AWS CLI
You can use the `describe-db-cluster-parameters`
AWS CLI command to view the details of the parameters
in your cluster parameter group.

    * **`--describe-db-cluster-parameters`**
     — To list all the parameters inside a
     parameter group and their values.




    	+ **`--db-cluster-parameter-group name`**
    	 — Required. The name of your
    	 cluster parameter group.

In the following examples, replace each `user input placeholder` with your cluster's information.

```
aws docdb describe-db-cluster-parameters \
    --db-cluster-parameter-group-name `sample-parameter-group`
```

Output from this operation looks something like
the following:

```
{
        "Parameters": [
            {
                "ParameterName": "profiler_threshold_ms",
                "ParameterValue": "100",
                "Description": "Operations longer than profiler_threshold_ms will be logged",
                "Source": "system",
                "ApplyType": "dynamic",
                "DataType": "integer",
                "AllowedValues": "50-2147483646",
                "IsModifiable": true,
                "ApplyMethod": "pending-reboot"
            },
            {
                "**ParameterName": "tls"**,
                "ParameterValue": "disabled",
                "Description": "Config to enable/disable TLS",
                "Source": "user",
                "ApplyType": "static",
                "DataType": "string",
                "AllowedValues": "disabled,enabled,fips-140-3",
                "IsModifiable": true,
                "ApplyMethod": "pending-reboot"
            }
        ]
}
```

###### Note

Amazon DocumentDB supports FIPS 140-3 endpoints starting with Amazon DocumentDB 5.0 (engine version 3.0.3727) clusters in these regions: ca-central-1, us-west-2, us-east-1, us-east-2, us-gov-east-1, us-gov-west-1.

After determining the value of your `tls` parameter,
continue connecting to your cluster by using one of the code
examples in the following sections.

- [Connecting with TLS enabled](#connect_programmatically-tls_enabled "#connect_programmatically-tls_enabled")
- [Connecting with TLS disabled](#connect_programmatically-tls_disabled "#connect_programmatically-tls_disabled")

## Connecting with TLS enabled

To view a code example for programmatically connecting to a TLS-enabled Amazon DocumentDB cluster, choose the appropriate tab for the
language that you want to use.

To encrypt data in transit, download the public key for Amazon DocumentDB
named `global-bundle.pem` using the following
operation.

```
wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

If your application is on Microsoft Windows and requires a PKCS7 file, you can download the PKCS7 certificate bundle.
This bundle contains both the intermediate and root certificates at [https://truststore.pki.rds.amazonaws.com/global/global-bundle.p7b](https://truststore.pki.rds.amazonaws.com/global/global-bundle.p7b "https://truststore.pki.rds.amazonaws.com/global/global-bundle.p7b").

Python
The following code demonstrates how to connect to
Amazon DocumentDB using Python when TLS is enabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
import pymongo
import sys

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient('mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

##Specify the database to be used
db = client.sample_database

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()
```

Node.js
The following code demonstrates how to connect to Amazon DocumentDB using Node.js when TLS is enabled.

###### Important

There is a known limitation with Node.js drivers older than version 6.13.1, which are currently not supported by IAM identity authentication for Amazon DocumentDB.
Node.js drivers and tools that use Node.js driver (for example, mongosh) must be upgraded to use Node.js driver version 6.13.1 or above.

In the following example, replace each `user input placeholder` with your cluster's information.

```
var MongoClient = require('mongodb').MongoClient

//Create a MongoDB client, open a connection to DocDB; as a replica set,
//  and specify the read preference as secondary preferred

var client = MongoClient.connect(
'mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/sample-database?tls=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false',
{
  tlsCAFile: `global-bundle.pem` //Specify the DocDB; cert
},
function(err, client) {
    if(err)
        throw err;

    //Specify the database to be used
    db = client.db('sample-database');

    //Specify the collection to be used
    col = db.collection('sample-collection');

    //Insert a single document
    col.insertOne({'hello':'Amazon DocumentDB'}, function(err, result){
      //Find the document that was previously written
      col.findOne({'hello':'Amazon DocumentDB'}, function(err, result){
        //Print the result to the screen
        console.log(result);

        //Close the connection
        client.close()
      });
   });
});

```

PHP
The following code demonstrates how to connect to
Amazon DocumentDB using PHP when TLS is enabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
<?php
//Include Composer's autoloader
require 'vendor/autoload.php';

$TLS_DIR = "/home/ubuntu/global-bundle.pem";

//Create a MongoDB client and open connection to Amazon DocumentDB
$client = new MongoDB\Client("mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/?retryWrites=false", ["tls" => "true", "tlsCAFile" => $TLS_DIR ]);

//Specify the database and collection to be used
$col = $client->sampledatabase->samplecollection;

//Insert a single document
$result = $col->insertOne( [ 'hello' => 'Amazon DocumentDB'] );

//Find the document that was previously written
$result = $col->findOne(array('hello' => 'Amazon DocumentDB'));

//Print the result to the screen
print_r($result);
?>
```

Go
The following code demonstrates how to connect to
Amazon DocumentDB using Go when TLS is enabled.

###### Note

As of version 1.2.1, the MongoDB Go Driver will
only use the first CA server certificate found in
`sslcertificateauthorityfile`. The
example code below addresses this limitation by
manually appending all server certificates found in
`sslcertificateauthorityfile` to a custom
TLS configuration used during client creation.

In the following examples, replace each `user input placeholder` with your cluster's information.

```
package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"

	"io/ioutil"
	"crypto/tls"
	"crypto/x509"
	"errors"
)

const (
	// Path to the AWS CA file
	caFilePath = "global-bundle.pem"

	// Timeout operations after N seconds
	connectTimeout  = 5
	queryTimeout    = 30
	username        = "`sample-user`"
	password        = "`password`"
	clusterEndpoint = "`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017"

	// Which instances to read from
	readPreference = "secondaryPreferred"

	connectionStringTemplate = "mongodb://%s:%s@%s/sample-database?tls=true&replicaSet=rs0&readpreference=%s"
)

func main() {

	connectionURI := fmt.Sprintf(connectionStringTemplate, username, password, clusterEndpoint, readPreference)

	tlsConfig, err := getCustomTLSConfig(caFilePath)
	if err != nil {
		log.Fatalf("Failed getting TLS configuration: %v", err)
	}

	client, err := mongo.NewClient(options.Client().ApplyURI(connectionURI).SetTLSConfig(tlsConfig))
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), connectTimeout*time.Second)
	defer cancel()

	err = client.Connect(ctx)
	if err != nil {
		log.Fatalf("Failed to connect to cluster: %v", err)
	}

	// Force a connection to verify our connection string
	err = client.Ping(ctx, nil)
	if err != nil {
		log.Fatalf("Failed to ping cluster: %v", err)
	}

	fmt.Println("Connected to DocumentDB!")

	collection := client.Database("sample-database").Collection("sample-collection")

	ctx, cancel = context.WithTimeout(context.Background(), queryTimeout*time.Second)
	defer cancel()

	res, err := collection.InsertOne(ctx, bson.M{"name": "pi", "value": 3.14159})
	if err != nil {
		log.Fatalf("Failed to insert document: %v", err)
	}

	id := res.InsertedID
	log.Printf("Inserted document ID: %s", id)

	ctx, cancel = context.WithTimeout(context.Background(), queryTimeout*time.Second)
	defer cancel()

	cur, err := collection.Find(ctx, bson.D{})

	if err != nil {
		log.Fatalf("Failed to run find query: %v", err)
	}
	defer cur.Close(ctx)

	for cur.Next(ctx) {
		var result bson.M
		err := cur.Decode(&result)
		log.Printf("Returned: %v", result)

		if err != nil {
			log.Fatal(err)
		}
	}

	if err := cur.Err(); err != nil {
		log.Fatal(err)
	}

}

func getCustomTLSConfig(caFile string) (*tls.Config, error) {
	tlsConfig := new(tls.Config)
	certs, err := ioutil.ReadFile(caFile)

	if err != nil {
		return tlsConfig, err
	}

	tlsConfig.RootCAs = x509.NewCertPool()
	ok := tlsConfig.RootCAs.AppendCertsFromPEM(certs)

	if !ok {
		return tlsConfig, errors.New("Failed parsing pem file")
	}

	return tlsConfig, nil

```

Java
When connecting to a TLS-enabled Amazon DocumentDB cluster from a Java application, your program must use the AWS-provided certificate authority (CA) file to validate the connection. To use the Amazon RDS CA certificate, do the following:

1. Download the Amazon RDS CA file from
   [https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem](https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem")
   .
2. Create a trust store with the CA certificate contained in the file by performing the following commands. Be sure to change the `truststore-password` to something else. If you are accessing a trust store that contains both the old CA certificate (`rds-ca-2015-root.pem`) and the new CA certificate (`rds-ca-2019-root.pem`), you can import the certificate bundle into the trust store.

The following is a sample shell script that imports the certificate bundle into a trust store on a Linux operating system.
In the following examples, replace each `user input placeholder` with your own information.
Most notably, wherever the example directory "`mydir`" is located in the script, replace it with a directory you created for this task.

```
mydir=/tmp/certs
truststore=${`mydir`}/rds-truststore.jks
storepassword=`truststore-password`

curl -sS "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem" > ${`mydir`}/global-bundle.pem
awk 'split_after == 1 {n++;split_after=0} /-----END CERTIFICATE-----/ {split_after=1}{print > "rds-ca-" n ".pem"}' < ${`mydir`}/global-bundle.pem

for CERT in rds-ca-*; do
  alias=$(openssl x509 -noout -text -in $CERT | perl -ne 'next unless /Subject:/; s/.*(CN=|CN = )//; print')
  echo "Importing $alias"
  keytool -import -file ${CERT} -alias "${alias}" -storepass ${storepassword} -keystore ${truststore} -noprompt
  rm $CERT
done

rm ${`mydir`}/global-bundle.pem

echo "Trust store content is: "

keytool -list -v -keystore "$truststore" -storepass ${storepassword} | grep Alias | cut -d " " -f3- | while read alias
do
   expiry=`keytool -list -v -keystore "$truststore" -storepass ${storepassword} -alias "${alias}" | grep Valid | perl -ne 'if(/until: (.*?)\n/) { print "$1\n"; }'`
   echo " Certificate ${alias} expires in '$expiry'"
done

```

The following is a sample shell script that
imports the certificate bundle into a trust store
on macOS.

```
mydir=/tmp/certs
truststore=${`mydir`}/rds-truststore.jks
storepassword=`truststore-password`

curl -sS "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem" > ${`mydir`}/global-bundle.pem
split -p "-----BEGIN CERTIFICATE-----" ${`mydir`}/global-bundle.pem rds-ca-

for CERT in rds-ca-*; do
  alias=$(openssl x509 -noout -text -in $CERT | perl -ne 'next unless /Subject:/; s/.*(CN=|CN = )//; print')
  echo "Importing $alias"
  keytool -import -file ${CERT} -alias "${alias}" -storepass ${storepassword} -keystore ${truststore} -noprompt
  rm $CERT
done

rm ${`mydir`}/global-bundle.pem

echo "Trust store content is: "

keytool -list -v -keystore "$truststore" -storepass ${storepassword} | grep Alias | cut -d " " -f3- | while read alias
do
   expiry=`keytool -list -v -keystore "$truststore" -storepass ${storepassword} -alias "${alias}" | grep Valid | perl -ne 'if(/until: (.*?)\n/) { print "$1\n"; }'`
   echo " Certificate ${alias} expires in '$expiry'"
done
```

3. Use the `keystore` in your program
   by setting the following system properties in
   your application before making a connection to
   the Amazon DocumentDB cluster.

```
javax.net.ssl.trustStore: `truststore`
javax.net.ssl.trustStorePassword: `truststore-password;`
```

4. The following code demonstrates how to connect
   to Amazon DocumentDB using Java when TLS is enabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
package com.example.documentdb;

import com.mongodb.client.*;
import org.bson.Document;

public final class Test {
    private Test() {
    }
    public static void main(String[] args) {

        String template = "mongodb://%s:%s@%s/sample-database?ssl=true&replicaSet=rs0&readpreference=%s";
        String username = "`sample-user`";
        String password = "`password`";
        String clusterEndpoint = "`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017";
        String readPreference = "secondaryPreferred";
        String connectionString = String.format(template, username, password, clusterEndpoint, readPreference);

        String truststore = "`truststore`";
        String truststorePassword = "`truststore-password`";

        System.setProperty("javax.net.ssl.trustStore", truststore);
        System.setProperty("javax.net.ssl.trustStorePassword", truststorePassword);

        MongoClient mongoClient = MongoClients.create(connectionString);

        MongoDatabase testDB = mongoClient.getDatabase("sample-database");
        MongoCollection<Document> numbersCollection = testDB.getCollection("sample-collection");

        Document doc = new Document("name", "pi").append("value", 3.14159);
        numbersCollection.insertOne(doc);

        MongoCursor<Document> cursor = numbersCollection.find().iterator();
        try {
            while (cursor.hasNext()) {
                System.out.println(cursor.next().toJson());
            }
        } finally {
            cursor.close();
        }

    }
}
```

C# / .NET
The following code demonstrates how to connect to Amazon DocumentDB using C# / .NET when TLS is enabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using System.Net.Security;
using MongoDB.Driver;
using MongoDB.Bson;

namespace DocDB
{
    class Program
    {
        static void Main(string[] args)
        {
            string template = "mongodb://{0}:{1}@{2}/sampledatabase?tls=true&replicaSet=rs0&readpreference={3}";
            string username = "`sample-user`";
            string password = "`password`";
            string readPreference = "secondaryPreferred";
            string clusterEndpoint="`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017";
            string connectionString = String.Format(template, username, password, clusterEndpoint, readPreference);

            string pathToCAFile = "<PATH/global-bundle.p7b_file>";

            // ADD CA certificate to local trust store
            // DO this once - Maybe when your service starts
            X509Store localTrustStore = new X509Store(StoreName.Root);
            X509Certificate2Collection certificateCollection = new X509Certificate2Collection();
            certificateCollection.Import(pathToCAFile);
            try
            {
                localTrustStore.Open(OpenFlags.ReadWrite);
                localTrustStore.AddRange(certificateCollection);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Root certificate import failed: " + ex.Message);
                throw;
            }
            finally
            {
                localTrustStore.Close();
            }

            var settings = MongoClientSettings.FromUrl(new MongoUrl(connectionString));
            var client = new MongoClient(settings);

            var database = client.GetDatabase("sampledatabase");
            var collection = database.GetCollection<BsonDocument>("samplecollection");
            var docToInsert = new BsonDocument { { "pi", 3.14159 } };
            collection.InsertOne(docToInsert);
        }
    }
}
```

MongoDB Shell
The following code demonstrates how to connect to and query Amazon DocumentDB using the newest version, mongosh, or the previous mongo shell version, when TLS is enabled.

**Connect to Amazon DocumentDB with mongosh**

###### Important

There is a known limitation with Node.js drivers older than version 6.13.1, which are currently not supported by IAM identity authentication for Amazon DocumentDB.
Node.js drivers and tools that use Node.js driver (for example, mongosh) must be upgraded to use Node.js driver version 6.13.1 or above.

In the following examples, replace each `user input placeholder` with your cluster's information.

```
mongosh --tls --host `cluster-end-point`:27017 --tlsCAFile  global-bundle.pem --username `sample-user` --password `password` --retryWrites false
```

**Connect to Amazon DocumentDB with the previous mongo shell version**

If you use IAM, you must use a previous version of mongo shell.
Enter one of the following command options:

```
mongo --ssl --host `cluster-end-point`:27017 --sslCAFile global-bundle.pem --username `sample-user` --password `password`
```

If you are using a version equal to or greater than 4.2, use the following code to connect.
Retryable writes are not supported in Amazon DocumentDB.
If you are using legacy mongo shell (not mongosh), do not include the `retryWrites=false` command in any code string.
By default, retryable writes are disabled. Including `retryWrites=false` might cause a failure in normal read commands.

```
mongo --tls --host `cluster-end-point`:27017 --tlsCAFile global-bundle.pem --username `sample-user` --password `password`
```

**Test the connection**

1. Insert a single document.

```
db.myTestCollection.insertOne({'hello':'Amazon DocumentDB'})
```

2. Find the document that was previously inserted.

```
db.myTestCollection.find({'hello':'Amazon DocumentDB'})
```

R
The following code demonstrates how to connect to
Amazon DocumentDB with R using mongolite ([https://jeroen.github.io/mongolite/](https://jeroen.github.io/mongolite/ "https://jeroen.github.io/mongolite/"))
when TLS is enabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
#Include the mongolite library.
library(mongolite)

mongourl <- paste("mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/test2?ssl=true&",
          "readPreference=secondaryPreferred&replicaSet=rs0", sep="")

#Create a MongoDB client, open a connection to Amazon DocumentDB as a replica
#   set and specify the read preference as secondary preferred
client <-  mongo(url = mongourl, options = ssl_options(weak_cert_validation = F, ca ="<PATH/global-bundle.pem>"))

#Insert a single document
str <- c('{"hello" : "Amazon DocumentDB"}')
client$insert(str)

#Find the document that was previously written
client$find()
```

Ruby
The following code demonstrates how to connect to
Amazon DocumentDB with Ruby when TLS is enabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
require 'mongo'
require 'neatjson'
require 'json'
client_host = 'mongodb://`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017'
client_options = {
   database: 'test',
   replica_set: 'rs0',
   read: {:secondary_preferred => 1},
   user: '`sample-user`',
   password: '`password`',
   ssl: true,
   ssl_verify: true,
   ssl_ca_cert: `'PATH/global-bundle.pem'`,
   retry_writes: false
}


begin
   ##Create a MongoDB client, open a connection to Amazon DocumentDB as a
   ##   replica set and specify the read preference as secondary preferred
   client = Mongo::Client.new(client_host, client_options)

   ##Insert a single document
   x = client[:test].insert_one({"hello":"Amazon DocumentDB"})

   ##Find the document that was previously written
   result = client[:test].find()

   #Print the document
   result.each do |document|
      puts JSON.neat_generate(document)
   end
end

#Close the connection
client.close
```

## Connecting with TLS disabled

To view a code example for programmatically connecting to a TLS-disabled Amazon DocumentDB cluster, choose the tab for language that you want to use.

Python
The following code demonstrates how to connect to
Amazon DocumentDB using Python when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
## Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred

import pymongo
import sys

client = pymongo.MongoClient('mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

##Specify the database to be used
db = client.sample_database

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()
```

Node.js
The following code demonstrates how to connect to
Amazon DocumentDB using Node.js when TLS is disabled.

###### Important

There is a known limitation with Node.js drivers older than version 6.13.1, which are currently not supported by IAM identity authentication for Amazon DocumentDB.
Node.js drivers and tools that use Node.js driver (for example, mongosh) must be upgraded to use Node.js driver version 6.13.1 or above.

In the following example, replace each `user input placeholder` with your cluster's information.

```
var MongoClient = require('mongodb').MongoClient;

//Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set,
//  and specify the read preference as secondary preferred
var client = MongoClient.connect(
'mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/sample-database?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false',
{
  useNewUrlParser: true
},

function(err, client) {
    if(err)
        throw err;
    //Specify the database to be used
    db = client.db('sample-database');

    //Specify the collection to be used
    col = db.collection('sample-collection');

    //Insert a single document
    col.insertOne({'hello':'Amazon DocumentDB'}, function(err, result){
      //Find the document that was previously written
      col.findOne({'hello':'Amazon DocumentDB'}, function(err, result){
        //Print the result to the screen
        console.log(result);

        //Close the connection
        client.close()
      });
   });
});
```

PHP
The following code demonstrates how to connect to
Amazon DocumentDB using PHP when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
<?php
//Include Composer's autoloader
require 'vendor/autoload.php';

//Create a MongoDB client and open connection to Amazon DocumentDB
$client = new MongoDB\Client("mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/?retryWrites=false");

//Specify the database and collection to be used
$col = $client->sampledatabase->samplecollection;

//Insert a single document
$result = $col->insertOne( [ 'hello' => 'Amazon DocumentDB'] );

//Find the document that was previously written
$result = $col->findOne(array('hello' => 'Amazon DocumentDB'));

//Print the result to the screen
print_r($result);
?>
```

Go
The following code demonstrates how to connect to
Amazon DocumentDB using Go when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const (
	// Timeout operations after N seconds
	connectTimeout  = 5
	queryTimeout    = 30
	username        = "`sample-user`"
	password        = "`password`"
	clusterEndpoint = "`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017"

	// Which instances to read from
	readPreference           = "secondaryPreferred"
	connectionStringTemplate = "mongodb://%s:%s@%s/sample-database?replicaSet=rs0&readpreference=%s"
)

func main() {

	connectionURI := fmt.Sprintf(connectionStringTemplate, username, password, clusterEndpoint, readPreference)

	client, err := mongo.NewClient(options.Client().ApplyURI(connectionURI))
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), connectTimeout*time.Second)
	defer cancel()

	err = client.Connect(ctx)
	if err != nil {
		log.Fatalf("Failed to connect to cluster: %v", err)
	}

	// Force a connection to verify our connection string
	err = client.Ping(ctx, nil)
	if err != nil {
		log.Fatalf("Failed to ping cluster: %v", err)
	}

	fmt.Println("Connected to DocumentDB!")

	collection := client.Database("sample-database").Collection("sample-collection")

	ctx, cancel = context.WithTimeout(context.Background(), queryTimeout*time.Second)
	defer cancel()

	res, err := collection.InsertOne(ctx, bson.M{"name": "pi", "value": 3.14159})
	if err != nil {
		log.Fatalf("Failed to insert document: %v", err)
	}

	id := res.InsertedID
	log.Printf("Inserted document ID: %s", id)

	ctx, cancel = context.WithTimeout(context.Background(), queryTimeout*time.Second)
	defer cancel()

	cur, err := collection.Find(ctx, bson.D{})

	if err != nil {
		log.Fatalf("Failed to run find query: %v", err)
	}
	defer cur.Close(ctx)

	for cur.Next(ctx) {
		var result bson.M
		err := cur.Decode(&result)
		log.Printf("Returned: %v", result)

		if err != nil {
			log.Fatal(err)
		}
	}

	if err := cur.Err(); err != nil {
		log.Fatal(err)
	}

}
```

Java
The following code demonstrates how to connect to
Amazon DocumentDB using Java when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
package com.example.documentdb;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.ServerAddress;
import com.mongodb.MongoException;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;
import org.bson.Document;


public final class Main {
    private Main() {
    }
    public static void main(String[] args) {

        String template = "mongodb://%s:%s@%s/sample-database?replicaSet=rs0&readpreference=%s";
        String username = "`sample-user`";
        String password = "`password`";
        String clusterEndpoint = "`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017";
        String readPreference = "secondaryPreferred";
        String connectionString = String.format(template, username, password, clusterEndpoint, readPreference);

        MongoClientURI clientURI = new MongoClientURI(connectionString);
        MongoClient mongoClient = new MongoClient(clientURI);

        MongoDatabase testDB = mongoClient.getDatabase("sample-database");
        MongoCollection<Document> numbersCollection = testDB.getCollection("sample-collection");

        Document doc = new Document("name", "pi").append("value", 3.14159);
        numbersCollection.insertOne(doc);

        MongoCursor<Document> cursor = numbersCollection.find().iterator();
        try {
            while (cursor.hasNext()) {
                System.out.println(cursor.next().toJson());
            }
        } finally {
            cursor.close();
        }

    }
}
```

C# / .NET
The following code demonstrates how to connect to
Amazon DocumentDB using C# / .NET when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using System.Net.Security;
using MongoDB.Driver;
using MongoDB.Bson;

namespace CSharpSample
{
   class Program
    {
       static void Main(string[] args)
        {
           string template = "mongodb://{0}:{1}@{2}/sampledatabase?replicaSet=rs0&readpreference={3}";
           string username = "`sample-user`";
           string password = "`password`";
           string clusterEndpoint = "`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017";
           string readPreference = "secondaryPreferred";
           string connectionString = String.Format(template, username, password, clusterEndpoint, readPreference);

           var settings = MongoClientSettings.FromUrl(new MongoUrl(connectionString));
           var client = new MongoClient(settings);

           var database = client.GetDatabase("sampledatabase");
           var collection = database.GetCollection<BsonDocument>("samplecollection");
           var docToInsert = new BsonDocument { { "pi", 3.14159 } };
            collection.InsertOne(docToInsert);
        }
    }
}
```

MongoDB Shell
The following code demonstrates how to connect to and query Amazon DocumentDB using the newest version, mongosh, or the previous mongo shell version, when TLS is disabled.

**Connect to Amazon DocumentDB with mongosh**

###### Important

There is a known limitation with Node.js drivers older than version 6.13.1, which are currently not supported by IAM identity authentication for Amazon DocumentDB.
Node.js drivers and tools that use Node.js driver (for example, mongosh) must be upgraded to use Node.js driver version 6.13.1 or above.

In the following examples, replace each `user input placeholder` with your cluster's information.

```
mongosh --host `cluster-end-point`:27017 --username `sample-user` --password `password` --retryWrites false
```

**Connect to Amazon DocumentDB with the previous mongo shell version**

If you use IAM, you must use a previous version of mongo shell.
Enter one of the following command options:

```
mongo --host `cluster-end-point`:27017 --username `sample-user` --password `password`
```

If you are using a version equal to or greater than 4.2, use the following code to connect.
Retryable writes are not supported in Amazon DocumentDB.
If you are using legacy mongo shell (not mongosh), do not include the `retryWrites=false` command in any code string.
By default, retryable writes are disabled. Including `retryWrites=false` might cause a failure in normal read commands.

```
mongo --host `cluster-end-point`:27017 --username `sample-user` --password `password`
```

**Test the connection**

1. Insert a single document.

```
db.myTestCollection.insertOne({'hello':'Amazon DocumentDB'})
```

2. Find the document that was previously inserted.

```
db.myTestCollection.find({'hello':'Amazon DocumentDB'})
```

R
The following code demonstrates how to connect to
Amazon DocumentDB with R using mongolite ([https://jeroen.github.io/mongolite/](https://jeroen.github.io/mongolite/ "https://jeroen.github.io/mongolite/"))
when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
#Include the mongolite library.
library(mongolite)

#Create a MongoDB client, open a connection to Amazon DocumentDB as a replica
#   set and specify the read preference as secondary preferred
client <- mongo(url = "mongodb://`sample-user`:`password`@`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017/sample-database?readPreference=secondaryPreferred&replicaSet=rs0")

##Insert a single document
str <- c('{"hello" : "Amazon DocumentDB"}')
client$insert(str)

##Find the document that was previously written
client$find()
```

Ruby
The following code demonstrates how to connect to
Amazon DocumentDB with Ruby when TLS is disabled.

In the following example, replace each `user input placeholder` with your cluster's information.

```
require 'mongo'
require 'neatjson'
require 'json'
client_host = 'mongodb://`sample-cluster.node`.us-east-1.docdb.amazonaws.com:27017'
client_options = {
   database: 'test',
   replica_set: 'rs0',
   read: {:secondary_preferred => 1},
   user: '`sample-user`',
   password: '`password`',
   retry_writes: false
}

begin
   ##Create a MongoDB client, open a connection to Amazon DocumentDB as a
   ##   replica set and specify the read preference as secondary preferred
   client = Mongo::Client.new(client_host, client_options)

   ##Insert a single document
   x = client[:test].insert_one({"hello":"Amazon DocumentDB"})

   ##Find the document that was previously written
   result = client[:test].find()

   #Print the document
   result.each do |document|
      puts JSON.neat_generate(document)
   end
end

#Close the connection
client.close
```
