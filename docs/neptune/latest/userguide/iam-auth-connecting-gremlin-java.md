

# Connecting to Amazon Neptune databases using IAM with Gremlin Java
<a name="iam-auth-connecting-gremlin-java"></a>

Here is an example of how to connect to Neptune using the Gremlin Java API with Sig4 signing (it assumes general knowledge about using Maven). This example uses the [Amazon Neptune SigV4 Signer](https://github.com/aws/amazon-neptune-sigv4-signer) library to assist in request signing. First, define the dependencies as part of the `pom.xml` file:

**Note**  
The following examples use `requestInterceptor()`, which was introduced in TinkerPop 3.6.6. If you are using a TinkerPop version earlier than 3.6.6 (but 3.5.5 or higher), use `handshakeInterceptor()` instead of `requestInterceptor()` in the code examples below.

```
<dependency>
  <groupId>com.amazonaws</groupId>
  <artifactId>amazon-neptune-sigv4-signer</artifactId>
  <version>3.1.0</version>
</dependency>
```

 The Amazon Neptune SigV4 Signer supports both versions 1.x and 2.x of the AWS Java SDK. The following examples use 2.x, where `DefaultCredentialsProvider` is a `software.amazon.awssdk.auth.credentials.AwsCredentialsProvider` instance. If you are upgrading from 1.x to 2.x, see the [Credentials provider changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-credentials.html) in the AWS SDK for Java 2.x documentation. 

```
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import com.amazonaws.neptune.auth.NeptuneNettyHttpSigV4Signer;
import com.amazonaws.neptune.auth.NeptuneSigV4SignerException;

 {{...}}

System.setProperty("aws.accessKeyId","{{your-access-key}}");
System.setProperty("aws.secretKey","{{your-secret-key}}");

 {{...}}

Cluster cluster = Cluster.build({{(your cluster)}})
                 .enableSsl(true)
                 .requestInterceptor( r ->
                  {
                    try {
                      NeptuneNettyHttpSigV4Signer sigV4Signer =
                        new NeptuneNettyHttpSigV4Signer("{{(your region)}}", DefaultCredentialsProvider.create());
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

## Cross account IAM authentication
<a name="iam-auth-connecting-gremlin-java-cross-account"></a>

 Amazon Neptune supports cross account IAM authentication through the use of role assumption, also sometimes referred to as [ role chaining](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-chain-roles.html#bulk-load-tutorial-chain-cross-account). To provide access to a Neptune cluster from an application hosted in a different AWS account: 
+  Create a new IAM user or role in the application AWS account, with a trust policy that allows the user or role to assume another IAM role. Assign this role to the compute hosting the application (EC2 instance, Lambda function, ECS Task, etc.). 

------
#### [ JSON ]

****  

  ```
  {
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Sid": "assumeRolePolicy",
        "Effect": "Allow",
        "Action": "sts:AssumeRole",
        "Resource": "arn:aws:iam::{{111122223333}}:role/{{role-name}}"
      }
    ]
  }
  ```

------
+  Create a new IAM role in the Neptune database AWS account that allows access to the Neptune database and allows role assumption from the application account IAM user/role. Use a trust policy of: 

------
#### [ JSON ]

****  

  ```
  {
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
  }
  ```

------
+  Use the following code example as guidance on how to use these two roles to allow the application to access Neptune. In this example, the application account role will be assumed via the [DefaultCredentialProviderChain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) when creating the `STSclient`. The `STSclient` is then used via the `STSAssumeRoleSessionCredentialsProvider` to assume the role hosted in the Neptune database AWS account. 

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
                          // new NeptuneNettyHttpSigV4Signer("us-west-2", DefaultCredentialsProvider.create());
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