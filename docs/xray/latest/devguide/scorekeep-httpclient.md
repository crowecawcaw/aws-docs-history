

# Instrumenting outgoing HTTP calls
<a name="scorekeep-httpclient"></a>

**Note**  
X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see [X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation ](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html).

The user factory class shows how the application uses the X-Ray SDK for Java's version of `HTTPClientBuilder` to instrument outgoing HTTP calls.

**Example [`src/main/java/scorekeep/UserFactory.java`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/UserFactory.java) – HTTPClient instrumentation**  

```
import [com.amazonaws.xray.proxies.apache.http.HttpClientBuilder](https://docs.aws.amazon.com/xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/proxies/apache/http/HttpClientBuilder.html);

  public String randomName() throws IOException {
    CloseableHttpClient httpclient = HttpClientBuilder.create().build();
    HttpGet httpGet = new HttpGet("http://uinames.com/api/");
    CloseableHttpResponse response = httpclient.execute(httpGet);
    try {
      HttpEntity entity = response.getEntity();
      InputStream inputStream = entity.getContent();
      ObjectMapper mapper = new ObjectMapper();
      Map<String, String> jsonMap = mapper.readValue(inputStream, Map.class);
      String name = jsonMap.get("name");
      EntityUtils.consume(entity);
      return name;
    } finally {
      response.close();
    }
  }
```

If you currently use `org.apache.http.impl.client.HttpClientBuilder`, you can simply swap out the import statement for that class with one for `com.amazonaws.xray.proxies.apache.http.HttpClientBuilder`.