# Manually instrumenting AWS SDK clients

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

The X-Ray SDK for Java automatically instruments all AWS SDK clients when you [include the AWS SDK Instrumentor submodule in your
build dependencies](xray-sdk-java.md#xray-sdk-java-dependencies "xray-sdk-java.md#xray-sdk-java-dependencies").

You can disable automatic client instrumentation by removing the Instrumentor submodule.
This enables you to instrument some clients manually while ignoring others, or use different
tracing handlers on different clients.

To illustrate support for instrumenting specific AWS SDK clients, the application passes a
tracing handler to `AmazonDynamoDBClientBuilder` as a request handler in the user,
game, and session model. This code change tells the SDK to instrument all calls to DynamoDB using
those clients.

###### Example [`src/main/java/scorekeep/SessionModel.java`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/SessionModel.java "https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/SessionModel.java") – Manual AWS

SDK client instrumentation

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.handlers.TracingHandler;

public class SessionModel {
  private AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
        .withRegion(Constants.REGION)
        `.withRequestHandlers(new TracingHandler(AWSXRay.getGlobalRecorder()))`
        .build();
  private DynamoDBMapper mapper = new DynamoDBMapper(client);
```

If you remove the AWS SDK Instrumentor submodule from project dependencies, only the
manually instrumented AWS SDK clients appear in the trace map.
