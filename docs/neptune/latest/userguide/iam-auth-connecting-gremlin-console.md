# Connecting to Amazon Neptune databases using IAM authentication with Gremlin console

There are two prerequisites to connecting Amazon Neptune using Gremlin Console with Signature Version 4 authentication:

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

The `:remote` command is used to create a connection from the Gremlin
Console to Neptune. You will use the `requestInterceptor()` to plug-in a Sigv4
signer to that connection to authenticate it over IAM.

Note that this is quite different from the typical situation where the
`:remote` command takes a configuration file to form the connection.
The configuration file approach won't work because `requestInterceptor()`
must be set programmatically, and can't load its configuration from a file.

###### Connect the Gremlin console with Sigv4 signing

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
