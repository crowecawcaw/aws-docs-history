

# Reduce costs with Basic Ingest in AWS IoT SiteWise
<a name="basic-ingest-rules"></a>

AWS IoT Core provides a feature called Basic Ingest that you can use to send data through AWS IoT Core without incurring [AWS IoT messaging costs](https://aws.amazon.com/iot-core/pricing/). Basic Ingest optimizes data flow for high volume data ingestion workloads by removing the publish/subscribe message broker from the ingestion path. You can use Basic Ingest if you know which rules your messages should be routed to.

To use Basic Ingest, you send messages directly to a specific rule using a special topic, `$aws/rules/{{rule-name}}`. For example, to send a message to a rule named `SiteWiseWindFarmRule`, you send a message to the topic `$aws/rules/SiteWiseWindFarmRule`.

If your rule action uses substitution templates that contain [topic(Decimal)](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-function-topic), you can pass the original topic at the end of the Basic Ingest special topic, such as `$aws/rules/{{rule-name}}/{{original-topic}}`. For example, to use Basic Ingest with the wind farm property alias example from the previous section, you can send messages to the following topic.

```
$aws/rules/SiteWiseWindFarmRule//company/windfarm/3/turbine/7/temperature
```

**Note**  
The above example includes a second slash (`//`) because AWS IoT removes the Basic Ingest prefix (`$aws/rules/{{rule-name}}/`) from the topic that's visible to the rule action. In this example, the rule receives the topic `/company/windfarm/3/turbine/7/temperature`.

For more information, see [Reducing messaging costs with basic ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html) in the *AWS IoT Developer Guide*.