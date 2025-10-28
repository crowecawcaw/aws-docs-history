# Test Amazon MSK TLS encryption

This process describes how to test TLS encryption on Amazon MSK.

###### To test TLS encryption

1. Create a client machine following the guidance in [Step 3: Create a client machine](create-client-machine.md "create-client-machine.md").
2. Install Apache Kafka on the client machine.
3. In this example we use the JVM truststore to talk to the
   MSK cluster. To do this, first create a folder named `/tmp`
   on the client machine. Then, go to the `bin` folder of the
   Apache Kafka installation, and run the following command. (Your JVM path might
   be different.)

```
cp /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-0.amzn2.x86_64/jre/lib/security/cacerts /tmp/kafka.client.truststore.jks
```

4. While still in the `bin` folder of the Apache Kafka
   installation on the client machine, create a text file named
   `client.properties` with the following contents.

```
security.protocol=SSL
ssl.truststore.location=/tmp/kafka.client.truststore.jks
```

5. Run the following command on a machine that has the AWS CLI installed, replacing
   `clusterARN` with the ARN of your cluster.

```
aws kafka get-bootstrap-brokers --cluster-arn `clusterARN`
```

A successful result looks like the following. Save this result because you need it for the next step.

```
{
    "BootstrapBrokerStringTls": "a-1.example.g7oein.c2.kafka.us-east-1.amazonaws.com:0123,a-3.example.g7oein.c2.kafka.us-east-1.amazonaws.com:0123,a-2.example.g7oein.c2.kafka.us-east-1.amazonaws.com:0123"
}
```

6. Run the following command, replacing `BootstrapBrokerStringTls` with one of the broker endpoints that you obtained in the previous step.

```
`<path-to-your-kafka-installation>`/bin/kafka-console-producer.sh --broker-list `BootstrapBrokerStringTls` --producer.config client.properties --topic TLSTestTopic
```

7. Open a new command window and connect to the same client machine. Then, run the following command to create a console consumer.

```
`<path-to-your-kafka-installation>`/bin/kafka-console-consumer.sh --bootstrap-server `BootstrapBrokerStringTls` --consumer.config client.properties --topic TLSTestTopic
```

8. In the producer window, type a text message followed by a return, and look for
   the same message in the consumer window. Amazon MSK encrypted this message in
   transit.
   For more information about configuring Apache Kafka clients to work with encrypted data, see [Configuring
   Kafka Clients](https://kafka.apache.org/documentation/#security_configclients "https://kafka.apache.org/documentation/#security_configclients").
