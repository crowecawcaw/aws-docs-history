# Produce and consume data in MSK

Serverless

In this step, you produce and consume data using the topic that you created in the
previous step.

###### To produce and consume messages

1. Run the following command to create a console producer.

```
`<path-to-your-kafka-installation>`/bin/kafka-console-producer.sh --broker-list $BS --producer.config client.properties --topic msk-serverless-tutorial
```

2. Enter any message that you want, and press **Enter**. Repeat
   this step two or three times. Every time you enter a line and press
   **Enter**, that line is sent to your cluster as a separate
   message.
3. Keep the connection to the client machine open, and then open a second,
   separate connection to that machine in a new window.
4. Use your second connection to the client machine to create a console consumer
   with the following command. Replace `my-endpoint` with
   the bootstrap server string that you saved after you created the cluster.

```
`<path-to-your-kafka-installation>`/bin/kafka-console-consumer.sh --bootstrap-server `my-endpoint` --consumer.config client.properties --topic msk-serverless-tutorial --from-beginning
```

You start seeing the messages you entered earlier when you used the console
producer command. 5. Enter more messages in the producer window, and watch them appear in the
consumer window.
If you encounter `classpath` issues while running these commands, make sure that you're running them from the correct directory. Also, make sure that the AWS MSK IAM JAR is in the `libs` directory. Alternatively, you can run Kafka commands using the full Java command with explicit `classpath`, as shown in the following example.

```
java -cp "kafka_2.12-2.8.1/libs/*:kafka_2.12-2.8.1/libs/aws-msk-iam-auth-2.3.0-all.jar" org.apache.kafka.tools.ConsoleProducer —broker-list $BS —producer.config client.properties —topic msk-serverless-tutorial
```

**Next Step**

[Delete resources that you created for MSK
Serverless](delete-resources.md "delete-resources.md")
