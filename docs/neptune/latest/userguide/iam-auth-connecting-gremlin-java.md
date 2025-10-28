# Connecting to Amazon Neptune databases using IAM with

Gremlin Java

## Using TinkerPop 3.4.11 or higher to connect to Neptune with Sig4 signing

Here is an example of how to connect to Neptune using the Gremlin Java API with
Sig4 signing when using TinkerPop 3.4.11 or higher (it assumes general knowledge about
using Maven). This example uses the [Amazon Neptune SigV4 Signer](https://github.com/aws/amazon-neptune-sigv4-signer "https://github.com/aws/amazon-neptune-sigv4-signer") library to assist in request signing. First, define the dependencies as part
of the `pom.xml` file:

###### Note

The following examples have been updated to include the use of requestInterceptor(). This was added in TinkerPop 3.6.6.
Prior to TinkerPop version 3.6.6, the code examples used handshakeInterceptor(), which was deprecated with that release.

```
<dependency>
  <groupId>com.amazonaws</groupId>
  <artifactId>amazon-neptune-sigv4-signer</artifactId>
  <version>3.1.0</version>
</dependency>
```

The Amazon Neptune SigV4 Signer supports use of both versions 1.x and 2.x of the AWS Java SDK. The following
example uses 2.x where the `DefaultCredentialsProvider` is a
`software.amazon.awssdk.auth.credentials.AwsCredentialsProvider` instance, but you could equally use the
1.x form with any `com.amazonaws.auth.AWSCredentialsProvider`. If you are upgrading from 1.x to 2.x, you can
read more about the changes between 1.x and 2.x in the [Credentials provider changes](../../../sdk-for-java/latest/developer-guide/migration-client-credentials.md "../../../sdk-for-java/latest/developer-guide/migration-client-credentials.md") of
the AWS SDK for Java 2.x documentation.

```
import com.amazonaws.auth.DefaultAWSCredentialsProviderChain;
import com.amazonaws.neptune.auth.NeptuneNettyHttpSigV4Signer;
import com.amazonaws.neptune.auth.NeptuneSigV4SignerException;

 `...`

System.setProperty("aws.accessKeyId","`your-access-key`");
System.setProperty("aws.secretKey","`your-secret-key`");

 `...`

Cluster cluster = Cluster.build(`(your cluster)`)
                 .enableSsl(true)
                 .requestInterceptor( r ->
                  {
                    try {
                      NeptuneNettyHttpSigV4Signer sigV4Signer =
                        new NeptuneNettyHttpSigV4Signer("`(your region)`", DefaultCredentialsProvider.create());
                      sigV4Signer.signRequest(r);
                    } catch (NeptuneSigV4SignerException e) {
                      throw new RuntimeException("Exception occurred while signing the request", e);
                    }
                    return r;
                  }
                 ).create();
try {
  Client client = cluster.connect();
  client.submit("g.V().has('code','IAD')").all().get();
} catch (Exception e) {
  throw new RuntimeException("Exception occurred while connecting to cluster", e);
}
```

###### Note

If you are upgrading from `3.4.11`, remove references to the
`amazon-neptune-gremlin-java-sigv4` library. It is no longer necessary
when using `requestInterceptor()` as shown in the example above.
Do not attempt to use the `requestInterceptor()` in conjunction with
the channelizer (`SigV4WebSocketChannelizer.class`), because it will
produce errors.

### Cross account IAM authentication

Amazon Neptune supports cross account IAM authentication through the use of role assumption, also sometimes referred
to as [role chaining](bulk-load-tutorial-chain-roles.md#bulk-load-tutorial-chain-cross-account "bulk-load-tutorial-chain-roles.md#bulk-load-tutorial-chain-cross-account"). To provide access to a Neptune cluster from an application hosted in a different AWS account:

- Create a new IAM user or role in the application AWS account, with a trust policy that allows the user or role
  to assume another IAM role. Assign this role to the compute hosting the application (EC2 instance, Lambda function,
  ECS Task, etc.).
- Create a new IAM role in the Neptune database AWS account that allows access to the Neptune database and
  allows role assumption from the application account IAM user/role. Use a trust policy of:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "(ARN of application account IAM user or role)"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

- Use the following code example as guidance on how to use these two roles to allow the application to access Neptune.
  In this example, the application account role will be assumed via the [DefaultCredentialProviderChain](../../../sdk-for-java/v1/developer-guide/credentials.md "../../../sdk-for-java/v1/developer-guide/credentials.md") when creating the
  `STSclient`. The `STSclient` is then used via the
  `STSAssumeRoleSessionCredentialsProvider` to assume the role hosted in the Neptune database AWS account.

```
public static void main( String[] args )
  {

    /*
     * Establish an STS client from the application account.
     */
    AWSSecurityTokenService client = AWSSecurityTokenServiceClientBuilder
        .standard()
        .build();

    /*
     * Define the role ARN that you will be assuming in the database account where the Neptune cluster resides.
     */
    String roleArnToAssume = "arn:aws:iam::012345678901:role/CrossAccountNeptuneRole";
    String crossAccountSessionName = "cross-account-session-" + UUID.randomUUID();

    /*
     * Change the Credentials Provider in the SigV4 Signer to use the STSAssumeRole Provider and provide it
     * with both the role to be assumed, the original STS client, and a session name (which can be
     * arbitrary.)
     */
    Cluster cluster = Cluster.build()
                 .addContactPoint("neptune-cluster.us-west-2.neptune.amazonaws.com")
                 .enableSsl(true)
                 .port(8182)
                 .requestInterceptor( r ->
                  {
                    try {
                      NeptuneNettyHttpSigV4Signer sigV4Signer =
                        // new NeptuneNettyHttpSigV4Signer("us-west-2", new DefaultAWSCredentialsProviderChain());
                        new NeptuneNettyHttpSigV4Signer(
                                "us-west-2",
                                 new STSAssumeRoleSessionCredentialsProvider
                                    .Builder(roleArnToAssume, crossAccountSessionName)
                                        .withStsClient(client)
                                        .build());
                      sigV4Signer.signRequest(r);
                    } catch (NeptuneSigV4SignerException e) {
                      throw new RuntimeException("Exception occurred while signing the request", e);
                    }
                    return r;
                  }
                 ).create();

    GraphTraversalSource g = traversal().withRemote(DriverRemoteConnection.using(cluster));

    /* whatever application code is necessary */

    cluster.close();
  }
```

## Using a version of TinkerPop

earlier than 3.4.11 to connect to Neptune with Sig4 signing

TinkerPop versions prior to `3.4.11` did not have support for the
`requestInterceptor()` configuration shown in the [previous section](#iam-auth-connecting-gremlin-java-current "#iam-auth-connecting-gremlin-java-current") and
therefore must rely on the `amazon-neptune-gremlin-java-sigv4` package.
This is a Neptune library that contains the `SigV4WebSocketChannelizer`
class, which replaces the standard TinkerPop Channelizer with one that can automatically
inject a SigV4 signature. Where possible, ugrade to TinkerPop 3.4.11 or higher, because
the `amazon-neptune-gremlin-java-sigv4` library is deprecated.

Here is an example of how to connect to Neptune using the Gremlin Java API with Sig4
signing when using TinkerPop versions prior to 3.4.11 (it assumes general knowledge about
how to use Maven).

First, define the dependencies as part of the `pom.xml` file:

```
<dependency>
  <groupId>com.amazonaws</groupId>
  <artifactId>amazon-neptune-gremlin-java-sigv4</artifactId>
  <version>2.4.0</version>
</dependency>
```

The dependency above will include the Gremlin driver version
`3.4.10`. Although it is possible to use newer Gremlin driver versions
(up through `3.4.13`), an upgrade of the driver past 3.4.10 should
include a change to use the `requestInterceptor()` model described
[above](#iam-auth-connecting-gremlin-java-current "#iam-auth-connecting-gremlin-java-current").

The `gremlin-driver` Cluster object should then be configured as
follows in the Java code:

```
import org.apache.tinkerpop.gremlin.driver.SigV4WebSocketChannelizer;

 `...`

Cluster cluster = Cluster.build(`your cluster`)
                       .enableSsl(true)
                       .channelizer(SigV4WebSocketChannelizer.class)
                       .create();
Client client = cluster.connect();
client.submit("g.V().has('code','IAD')").all().get();
```
