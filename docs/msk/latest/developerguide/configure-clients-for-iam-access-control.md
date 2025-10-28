# Configure clients for IAM access control

To enable clients to communicate with an MSK cluster that uses IAM access control, you can use either of these mechanisms:

- Non-Java client configuration using SASL_OAUTHBEARER mechanism
- Java client configuration using SASL_OAUTHBEARER mechanism or AWS_MSK_IAM mechanism

## Use the SASL_OAUTHBEARER mechanism to configure IAM

1. Edit your client.properties configuration file using the following Python Kafka client example. Configuration changes are similar in other languages.

```
from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka.sasl.oauth import AbstractTokenProvider
import socket
import time
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token('<my AWS Region>')
        return token

tp = MSKTokenProvider()

producer = KafkaProducer(
    bootstrap_servers='<myBootstrapString>',
    security_protocol='SASL_SSL',
    sasl_mechanism='OAUTHBEARER',
    sasl_oauth_token_provider=tp,
    client_id=socket.gethostname(),
)

topic = "<my-topic>"
while True:
    try:
        inp=input(">")
        producer.send(topic, inp.encode())
        producer.flush()
        print("Produced!")
    except Exception:
        print("Failed to send message:", e)

producer.close()
```

2. Download the helper library for your chosen configuration language and follow the instructions in the _Getting started_ section of that language library’s homepage.
   - JavaScript: [https://github.com/aws/aws-msk-iam-sasl-signer-js#getting-started](https://github.com/aws/aws-msk-iam-sasl-signer-js#getting-started "https://github.com/aws/aws-msk-iam-sasl-signer-js#getting-started")
   - Python: [https://github.com/aws/aws-msk-iam-sasl-signer-python#get-started](https://github.com/aws/aws-msk-iam-sasl-signer-python#get-started "https://github.com/aws/aws-msk-iam-sasl-signer-python#get-started")
   - Go: [https://github.com/aws/aws-msk-iam-sasl-signer-go#getting-started](https://github.com/aws/aws-msk-iam-sasl-signer-go#getting-started "https://github.com/aws/aws-msk-iam-sasl-signer-go#getting-started")
   - .NET: [https://github.com/aws/aws-msk-iam-sasl-signer-net#getting-started](https://github.com/aws/aws-msk-iam-sasl-signer-net#getting-started "https://github.com/aws/aws-msk-iam-sasl-signer-net#getting-started")
   - JAVA: SASL_OAUTHBEARER support for Java is available through the [`aws-msk-iam-auth`](https://github.com/aws/aws-msk-iam-auth/releases "https://github.com/aws/aws-msk-iam-auth/releases") jar file

## Use the MSK custom AWS_MSK_IAM mechanism to configure IAM

1. Add the following to the `client.properties` file. Replace
   `<PATH_TO_TRUST_STORE_FILE>` with the
   fully-qualified path to the trust store file on the client.

###### Note

If you don't want to use a specific certificate, you can remove
`ssl.truststore.location=`<PATH_TO_TRUST_STORE_FILE>`` from your`client.properties`file. When you don't specify a
 value for`ssl.truststore.location`, the Java process uses
the default certificate.

```
ssl.truststore.location=`<PATH_TO_TRUST_STORE_FILE>`
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

To use a named profile that you created for AWS credentials, include
`awsProfileName="`your profile
name`";` in your client configuration file. For
information about named profiles, see [Named profiles](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md") in the AWS CLI documentation. 2. Download the latest stable [aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth/releases "https://github.com/aws/aws-msk-iam-auth/releases") JAR file, and place it in the class path. If
you use Maven, add the following dependency, adjusting the version number as
needed:

```
<dependency>
    <groupId>software.amazon.msk</groupId>
    <artifactId>aws-msk-iam-auth</artifactId>
    <version>1.0.0</version>
</dependency>
```

The Amazon MSK client plugin is open-sourced under the Apache 2.0 license.
