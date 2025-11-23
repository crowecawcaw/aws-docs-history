# Connecting to Amazon Neptune databases using IAM authentication with Gremlin console

How you connect to Amazon Neptune using the Gremlin console with Signature Version 4
authentication depends on whether you are using TinkerPop version `3.4.11` or
higher, or an earlier version. In either case, the following prerequisites are
necessary:

- You must have the IAM credentials needed to sign the requests. See [Using the default credential
  provider chain](../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default "../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default") in the AWS SDK for Java Developer Guide.
- You must have installed a Gremlin console version that is compatible with
  the version of the Neptune engine being used by your DB cluster.
  If you are using temporary credentials, they expire after a specified interval,
  as does the session token, so you must update your session token when you request new
  credentials. See [Using
  temporary security credentials to request access to AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the
  IAM User Guide.

For help connecting using SSL/TLS, see [SSL/TLS configuration](access-graph-gremlin-java.md#access-graph-gremlin-java-ssl "access-graph-gremlin-java.md#access-graph-gremlin-java-ssl").

## Using TinkerPop 3.4.11 or higher to connect to Neptune with Sig4 signing

With TinkerPop 3.6.6 or higher, you will use `requestInterceptor()`,
which provides a way to plug in a Sigv4 signer to the connection established by the
`:remote` command. As with the approach used for Java, it requires you to
configure the `Cluster` object manually and then pass it to the
`:remote` command.

Note that this is quite different from the typical situation where the
`:remote` command takes a configuration file to form the connection.
The configuration file approach won't work because `requestInterceptor()`
must be set programmatically, and can't load its configuration from a file.

###### Connect the Gremlin console (TinkerPop 3.4.11 and higher) with Sig4 signing

1. Start the Gremlin console:

```
$ bin/gremlin.sh
```

2. At the `gremlin>` prompt, install the
   `amazon-neptune-sigv4-signer` library (this only needs to be done
   once for the console):

```
:install com.amazonaws amazon-neptune-sigv4-signer 2.4.0
```

If you encounter problems with this step, it may help to consult the [TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-applications "https://tinkerpop.apache.org/docs/current/reference/#gremlin-applications")
about [Grape](http://docs.groovy-lang.org/latest/html/documentation/grape.html "http://docs.groovy-lang.org/latest/html/documentation/grape.html") configuration.

###### Note

If you are using an HTTP proxy, you may encounter errors with this step where the
`:install` command does not complete. To solve this problem, run the following
commands to tell the console about the proxy:

```
System.setProperty("https.proxyHost", "`(the proxy IP address)`")
System.setProperty("https.proxyPort", "`(the proxy port)`")
```

3. Import the class required to handle the signing into `requestInterceptor()`:

```
:import com.amazonaws.auth.DefaultAWSCredentialsProviderChain
:import com.amazonaws.neptune.auth.NeptuneNettyHttpSigV4Signer
```

4. If you are using temporary credentials, you will also need to supply your Session Token
   as follows:

```
System.setProperty("aws.sessionToken","(your session token)")
```

5. If you haven't otherwise established your account credentials, you can assign
   them as follows:

```
System.setProperty("aws.accessKeyId","``(your access key)``")
System.setProperty("aws.secretKey","`(your secret key)`")
```

6. Manually construct the `Cluster` object to connect to Neptune:

###### Note

The following example has been updated to include the use of requestInterceptor(). This was added in TinkerPop 3.6.6.
Prior to TinkerPop version 3.6.6, the code example used handshakeInterceptor(), which was deprecated with that release.

```

cluster = Cluster.build("`(host name)`")  \
                 .enableSsl(true) \
                 .requestInterceptor { r ->  \
                   def sigV4Signer = new NeptuneNettyHttpSigV4Signer("`(Amazon region)`", \
                                     new DefaultAWSCredentialsProviderChain()); \
                   sigV4Signer.signRequest(r); \
                   return r; } \
                 .create()
```

For help finding the host name of a Neptune DB instance, see [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md"). 7. Establish the `:remote` connection using the variable name of the
`Cluster` object in the previous step:

```
:remote connect tinkerpop.server cluster
```

8. Enter the following command to switch to remote mode. This sends all Gremlin
   queries to the remote connection:

```
:remote console
```

## Using a version of TinkerPop

earlier than 3.4.11 to connect to Neptune with Sig4 signing

With TinkerPop 3.4.10 or lower, use the `amazon-neptune-gremlin-java-sigv4`
library provided by Neptune to connect the console to Neptune with Sigv4 signing, as
described below:

###### Connect the Gremlin console (TinkerPop versions earlier than 3.4.11) with Sig4 signing

1. Start the Gremlin console:

```
$ bin/gremlin.sh
```

2. At the `gremlin>` prompt, install the
   `amazon-neptune-sigv4-signer` library (this only needs to be done
   once for the console):

```
:install com.amazonaws amazon-neptune-sigv4-signer 2.4.0
```

###### Note

If you are using an HTTP proxy, you may encounter errors with this step where the
`:install` command does not complete. To solve this problem, run the following
commands to tell the console about the proxy:

```
System.setProperty("https.proxyHost", "`(the proxy IP address)`")
System.setProperty("https.proxyPort", "`(the proxy port)`")
```

It may also help to consult the [TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-applications "https://tinkerpop.apache.org/docs/current/reference/#gremlin-applications")
about [Grape](http://docs.groovy-lang.org/latest/html/documentation/grape.html "http://docs.groovy-lang.org/latest/html/documentation/grape.html") configuration. 3. In the `conf` subdirectory of the extracted directory, create a file
named `neptune-remote.yaml`.

If you used the CloudFormation template to create your Neptune DB cluster, a
`neptune-remote.yaml` file will already exist. In that case, all you
have to do is edit the existing file to include the channelizer setting shown
below.

Otherwise, copy the following text into the file, replacing `(host name)`
with the host name or IP address of your Neptune DB instance. Note that the square brackets ([ ])
enclosing the host name are required.

```
hosts: [`(host name)`]
port: `8182`
connectionPool: {
  channelizer: org.apache.tinkerpop.gremlin.driver.SigV4WebSocketChannelizer,
  enableSsl: true
}
serializer: { className: org.apache.tinkerpop.gremlin.driver.ser.GraphBinaryMessageSerializerV1,
              config: { serializeResultToString: true }}
```

4. ###### Important

You must provide IAM credentials to sign the requests. Enter the following
commands to set your credentials as environment variables, replacing the relevant items
with your credentials.

```
export AWS_ACCESS_KEY_ID=`access_key_id`
export AWS_SECRET_ACCESS_KEY=`secret_access_key`
export SERVICE_REGION=`us-east-1 or us-east-2 or us-west-1 or us-west-2 or ca-central-1 or
 sa-east-1 or eu-north-1 or eu-west-1 or eu-west-2 or eu-west-3 or eu-central-1 or me-south-1 or
 me-central-1 or il-central-1 or af-south-1 or ap-east-1 or ap-northeast-1 or ap-northeast-2 or ap-southeast-1 or ap-southeast-2 or ap-south-1 or
 cn-north-1 or cn-northwest-1 or
 us-gov-east-1 or us-gov-west-1`
```

The Neptune Version 4 Signer uses the default credential provider chain. For
additional methods of providing credentials, see [Using the Default Credential Provider Chain](../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default "../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default") in the
_AWS SDK for Java Developer Guide_.

The `SERVICE_REGION` variable is required, even when using a credentials
file. 5. Establish the `:remote` connection using the `.yaml` file:

```
:remote connect tinkerpop.server conf/neptune-remote.yaml
```

6. Enter the following command to switch to remote mode, which sends
   all Gremlin queries to the remote connection:

```
:remote console
```
