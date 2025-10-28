# Using a Cassandra Go client driver to

access Amazon Keyspaces programmatically

This section shows you how to connect to Amazon Keyspaces by using a Go Cassandra client
driver. To provide users and applications with credentials for programmatic access to
Amazon Keyspaces resources, you can do either of the following:

- Create service-specific credentials that are associated with a specific
  AWS Identity and Access Management (IAM) user.
- For enhanced security, we recommend to create IAM access keys
  for IAM principals that are used across all AWS services. The Amazon Keyspaces
  SigV4 authentication plugin for Cassandra client drivers enables you to
  authenticate calls to Amazon Keyspaces using IAM access keys instead of user name and
  password. For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

###### Topics

- [Before you begin](#using_go_driver.BeforeYouBegin "#using_go_driver.BeforeYouBegin")
- [Connect to Amazon Keyspaces using the
  Gocql driver for Apache Cassandra and service-specific credentials](#go_ssc "#go_ssc")
- [Connect to Amazon Keyspaces using the
  Go driver for Apache Cassandra and the SigV4 authentication plugin](#go_SigV4 "#go_SigV4")

## Before you begin

You need to complete the following task before you can start.

Amazon Keyspaces requires the use of Transport Layer Security (TLS) to help secure
connections with clients. To connect to Amazon Keyspaces using TLS, you need to download an Amazon digital
certificate and configure the Go driver to use TLS.

Download the following digital certificates and save
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
During this transition, configure clients to trust both Amazon Root CAs 1–4 and the Starfield root to ensure compatibility across all Regions.

Combine all downloaded certificates into a single `pem` file with the name
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

## Connect to Amazon Keyspaces using the

Gocql driver for Apache Cassandra and service-specific credentials

1. Create a directory for your application.

```
mkdir ./gocqlexample
```

2. Navigate to the new directory.

```
cd gocqlexample
```

3. Create a file for your application.

```
touch cqlapp.go
```

4. Download the Go driver.

```
go get github.com/gocql/gocql
```

5. Add the following sample code to the cqlapp.go file.

```
package main

import (
	    "fmt"
	    "github.com/gocql/gocql"
	    "log"
)

func main() {

    // add the Amazon Keyspaces service endpoint
    cluster := gocql.NewCluster("`cassandra.us-east-2.amazonaws.com`")
    cluster.Port=9142
    // add your service specific credentials
    cluster.Authenticator = gocql.PasswordAuthenticator{
            Username: "`ServiceUserName`",
            Password: "`ServicePassword`"}

    // provide the path to the `keyspaces-bundle.pem`
    cluster.SslOpts = &gocql.SslOptions{
            CaPath: "`path_to_file/keyspaces-bundle.pem`",
            EnableHostVerification: false,
     }

     // Override default Consistency to LocalQuorum
     cluster.Consistency = gocql.LocalQuorum
     cluster.DisableInitialHostLookup = false

     session, err := cluster.CreateSession()
     if err != nil {
            fmt.Println("err>", err)
     }
     defer session.Close()

     // run a sample query from the system keyspace
     var text string
     iter := session.Query("SELECT keyspace_name FROM system_schema.tables;").Iter()
     for iter.Scan(&text) {
            fmt.Println("keyspace_name:", text)
     }
     if err := iter.Close(); err != nil {
            log.Fatal(err)
     }
     session.Close()
}
```

Usage notes:

    1. Replace
     `"`path_to_file/keyspaces-bundle.pem`"`
     with the path to the combined certificate file saved in the first step.
    2. Ensure that the `ServiceUserName` and
     `ServicePassword` match the user
     name and password you obtained when you generated the
     service-specific credentials by following the steps to [Create service-specific
     credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md").
    3. For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").

6. Build the program.

```
go build cqlapp.go
```

7. Run the program.

```
./cqlapp
```

## Connect to Amazon Keyspaces using the

Go driver for Apache Cassandra and the SigV4 authentication plugin

The following code sample shows how to use the SigV4 authentication plugin for the open-source Go driver to
access Amazon Keyspaces (for Apache Cassandra).

If you haven't already done so, create credentials for your IAM principal following the steps at [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md"). If an application is running on Lambda or an Amazon EC2 instance, your application
is automatically using the credentials of the instance. To run this tutorial locally, you can store the credentials
as local environment variables.

Add the Go SigV4 authentication plugin to your application from the [GitHub
repository](https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin"). The plugin supports version 1.2.x of the open-source Go
driver for Cassandra and depends on the AWS SDK for Go.

```
$ go mod init
$ go get github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin
```

In this code example, the Amazon Keyspaces endpoint is represented by the `Cluster`
class. It uses the `AwsAuthenticator` for the authenticator property of the
cluster to obtain credentials.

```
package main

import (
        "fmt"
        "github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin/sigv4"
        "github.com/gocql/gocql"
        "log"
)

func main() {
    // configuring the cluster options
    cluster := gocql.NewCluster("`cassandra.us-west-2.amazonaws.com`")
    cluster.Port=9142

    // the authenticator uses the default credential chain to find AWS credentials
    cluster.Authenticator = sigv4.NewAwsAuthenticator()

    cluster.SslOpts = &gocql.SslOptions{

            CaPath: "`path_to_file/keyspaces-bundle.pem`",
            EnableHostVerification: false,
    }
    cluster.Consistency = gocql.LocalQuorum
    cluster.DisableInitialHostLookup = false

    session, err := cluster.CreateSession()
    if err != nil {
	    fmt.Println("err>", err)
	    return
    }
    defer session.Close()

    // doing the query
    var text string
    iter := session.Query("SELECT keyspace_name FROM system_schema.tables;").Iter()
    for iter.Scan(&text) {
	    fmt.Println("keyspace_name:", text)
    }
    if err := iter.Close(); err != nil {
	    log.Fatal(err)
    }
}
```

Usage notes:

1. Replace
   `"`path_to_file/keyspaces-bundle.pem`"`
   with the path to the certificate file saved in the first step.
2. For this example to run locally, you need to define the following variables as environment variables:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`

3. To store access keys outside of code, see best practices at [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md").
4. For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").
