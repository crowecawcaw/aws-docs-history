# Using a Cassandra Node.js client driver to

access Amazon Keyspaces programmatically

This section shows you how to connect to Amazon Keyspaces by using a Node.js client
driver. To provide users and applications with credentials for programmatic access to
Amazon Keyspaces resources, you can do either of the following:

- Create service-specific credentials that are associated with a specific
  AWS Identity and Access Management (IAM) user.
- For enhanced security, we recommend to create IAM access keys for IAM
  users or roles that are used across all AWS services. The Amazon Keyspaces SigV4
  authentication plugin for Cassandra client drivers enables you to authenticate
  calls to Amazon Keyspaces using IAM access keys instead of user name and password. For
  more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

###### Topics

- [Before you begin](#using_nodejs_driver.BeforeYouBegin "#using_nodejs_driver.BeforeYouBegin")
- [Connect to Amazon Keyspaces using the Node.js DataStax driver for
  Apache Cassandra and service-specific credentials](#nodejs_ssc "#nodejs_ssc")
- [Connect to Amazon Keyspaces using the DataStax Node.js driver
  for Apache Cassandra and the SigV4 authentication plugin](#nodejs_SigV4 "#nodejs_SigV4")

## Before you begin

You need to complete the following task before you can start.

Amazon Keyspaces requires the use of Transport Layer Security (TLS) to help secure
connections with clients. To connect to Amazon Keyspaces using TLS, you need to download an Amazon digital
certificate and configure the Python driver to use TLS.

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

## Connect to Amazon Keyspaces using the Node.js DataStax driver for

Apache Cassandra and service-specific credentials

Configure your driver to use the combined certificate file `keyspaces-bundle.pem` for TLS and
authenticate using service-specific credentials. For example:

```
const cassandra = require('cassandra-driver');
const fs = require('fs');
const auth = new cassandra.auth.PlainTextAuthProvider('`ServiceUserName`', '`ServicePassword`');
const sslOptions1 = {
         ca: [
                    fs.readFileSync('`path_to_file/keyspaces-bundle.pem`', 'utf-8')],
                    host: '`cassandra.us-west-2.amazonaws.com`',
                    rejectUnauthorized: true
        };
const client = new cassandra.Client({
                   contactPoints: ['`cassandra.us-west-2.amazonaws.com`'],
                   localDataCenter: '`us-west-2`',
                   authProvider: auth,
                   sslOptions: sslOptions1,
                   protocolOptions: { port: 9142 }
        });
const query = 'SELECT * FROM system_schema.keyspaces';

client.execute(query)
                    .then( result => console.log('Row from Keyspaces %s', result.rows[0]))
                    .catch( e=> console.log(`${e}`));
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

## Connect to Amazon Keyspaces using the DataStax Node.js driver

for Apache Cassandra and the SigV4 authentication plugin

The following section shows how to use the SigV4 authentication plugin for the
open-source DataStax Node.js driver for Apache Cassandra to access Amazon Keyspaces (for Apache Cassandra).

If you haven't already done so, create credentials for your IAM user or role following the steps at [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

Add the Node.js SigV4 authentication plugin to your application from the [GitHub repository](https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin"). The plugin supports version 4.x of the DataStax
Node.js driver for Cassandra and depends on the AWS SDK for Node.js. It uses
`AWSCredentialsProvider` to obtain credentials.

```
$ npm install aws-sigv4-auth-cassandra-plugin --save
```

This code example shows how to set a Region-specific instance of
`SigV4AuthProvider` as the authentication provider.

```
const cassandra = require('cassandra-driver');
const fs = require('fs');
const sigV4 = require('aws-sigv4-auth-cassandra-plugin');

const auth = new sigV4.SigV4AuthProvider({
    region: '`us-west-2`',
    accessKeyId:'`AKIAIOSFODNN7EXAMPLE`',
    secretAccessKey: '`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`'});

const sslOptions1 = {
  ca: [
      fs.readFileSync('`path_to_file/keyspaces-bundle.pem`', 'utf-8')],
  host: '`cassandra.us-west-2.amazonaws.com`',
  rejectUnauthorized: true
};


const client = new cassandra.Client({
  contactPoints: ['`cassandra.us-west-2.amazonaws.com`'],
  localDataCenter: '`us-west-2`',
  authProvider: auth,
  sslOptions: sslOptions1,
  protocolOptions: { port: 9142 }
});


const query = 'SELECT * FROM system_schema.keyspaces';

client.execute(query).then(
    result => console.log('Row from Keyspaces %s', result.rows[0]))
    .catch( e=> console.log(`${e}`));
```

Usage notes:

1. Replace
   `"`path_to_file/keyspaces-bundle.pem`"`
   with the path to the certificate saved in the first step.
2. Ensure that the `accessKeyId` and
   `secretAccessKey` match the Access Key and
   Secret Access Key you obtained using `AWSCredentialsProvider`. For more
   information, see [Setting Credentials in Node.js](../../../sdk-for-javascript/v2/developer-guide/setting-credentials-node.md "../../../sdk-for-javascript/v2/developer-guide/setting-credentials-node.md") in the _AWS SDK for JavaScript in Node.js_.
3. To store access keys outside of code, see best practices at [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md").
4. For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").
