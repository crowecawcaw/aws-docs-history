

# Connecting to Amazon Neptune databases using IAM authentication with Gremlin console
<a name="iam-auth-connecting-gremlin-console"></a>

To connect to Amazon Neptune using the Gremlin console with Signature Version 4 authentication, you use `requestInterceptor()` to plug in a SigV4 signer to the connection established by the `:remote` command. This requires you to configure the `Cluster` object manually and then pass it to the `:remote` command.

Note that this is quite different from the typical situation where the `:remote` command takes a configuration file to form the connection. The configuration file approach won't work because `requestInterceptor()` must be set programmatically, and can't load its configuration from a file.

**Note**  
The following examples use `requestInterceptor()`, which was introduced in TinkerPop 3.6.6. If you are using a TinkerPop version earlier than 3.6.6 (but 3.5.5 or higher), use `handshakeInterceptor()` instead of `requestInterceptor()` in the code examples below.

The following prerequisites are necessary:
+ You must have the IAM credentials needed to sign the requests. See [Using the default credential provider chain](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-chain.html) in the AWS SDK for Java Developer Guide.
+ You must have installed a Gremlin console version that is compatible with the version of the Neptune engine being used by your DB cluster.

If you are using temporary credentials, they expire after a specified interval, as does the session token, so you must update your session token when you request new credentials. See [Using temporary security credentials to request access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide.

For help connecting using SSL/TLS, see [SSL/TLS configuration](access-graph-gremlin-java.md#access-graph-gremlin-java-ssl).

**Connect the Gremlin console with Sig4 signing**

1. Start the Gremlin console:

   ```
   $ bin/gremlin.sh
   ```

1. At the `gremlin>` prompt, install the `amazon-neptune-sigv4-signer` library (this only needs to be done once for the console):

   ```
   :install com.amazonaws amazon-neptune-sigv4-signer 2.4.0
   ```

   If you encounter problems with this step, it may help to consult the [TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-applications) about [Grape](http://docs.groovy-lang.org/latest/html/documentation/grape.html) configuration.
**Note**  
If you are using an HTTP proxy, you may encounter errors with this step where the `:install` command does not complete. To solve this problem, run the following commands to tell the console about the proxy:  

   ```
   System.setProperty("https.proxyHost", "{{(the proxy IP address)}}")
   System.setProperty("https.proxyPort", "{{(the proxy port)}}")
   ```

1. Import the class required to handle the signing into `requestInterceptor()`:

   ```
   :import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider
   :import com.amazonaws.neptune.auth.NeptuneNettyHttpSigV4Signer
   ```

1. If you are using temporary credentials, you will also need to supply your Session Token as follows:

   ```
   System.setProperty("aws.sessionToken","(your session token)")
   ```

1. If you haven't otherwise established your account credentials, you can assign them as follows:

   ```
   System.setProperty("aws.accessKeyId","{{{{(your access key)}}}}")
   System.setProperty("aws.secretKey","{{(your secret key)}}")
   ```

1. Manually construct the `Cluster` object to connect to Neptune:

   ```
   cluster = Cluster.build("{{(host name)}}")  \
                    .enableSsl(true) \
                    .requestInterceptor { r ->  \
                      def sigV4Signer = new NeptuneNettyHttpSigV4Signer("{{(Amazon region)}}", \
                                        DefaultCredentialsProvider.create()); \
                      sigV4Signer.signRequest(r); \
                      return r; } \
                    .create()
   ```

   For help finding the host name of a Neptune DB instance, see [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md).

1. Establish the `:remote` connection using the variable name of the `Cluster` object in the previous step:

   ```
   :remote connect tinkerpop.server cluster
   ```

1. Enter the following command to switch to remote mode. This sends all Gremlin queries to the remote connection:

   ```
   :remote console
   ```