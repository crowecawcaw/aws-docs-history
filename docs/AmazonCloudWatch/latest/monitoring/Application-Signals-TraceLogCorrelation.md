

# Enable trace to log correlation
<a name="Application-Signals-TraceLogCorrelation"></a>

You can enable *trace to log correlation* in Application Signals. This automatically injects trace IDs and span IDs into the relevant application logs. Then, when you open a trace detail page in the Application Signals console, the relevant log entries (if any) that correlate with the current trace automatically appear at the bottom of the page.

For example, suppose you notice a spike in a latency graph. You can choose the point on the graph to load the diagnostics information for that point in time. You then choose the relevant trace to get more information. When you view the trace information, you can scroll down to see the logs associated with the trace. These logs might reveal patterns or error codes associated with the issues causing the latency spike.

**Instrument your application before configuring trace log correlation**  
Your application must already be instrumented for Application Signals before you configure trace log correlation. The Application Signals instrumentation is what populates the `trace_id`, `span_id`, and `trace_flags` MDC values at runtime. Without instrumentation, these values remain empty (for example, `trace_id=`) and correlation does not work.

To achieve trace log correlation, Application Signals relies on the following:
+ [ Logger MDC auto-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/logger-mdc-instrumentation.md) for Java.
+ [ OpenTelemetry Logging Instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html) for Python.
+ The [ Pino](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino), [ Winston](https://www.npmjs.com/package/@opentelemetry/instrumentation-winston), or [ Bunyan](https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan) auto-instrumentations for Node.js.

The OpenTelemetry community provides all of these instrumentations. Application Signals uses them to inject trace contexts such as trace ID and span ID into application logs. To enable this, you must manually change your logging configuration to enable the auto-instrumentation. 

Depending on the architecture that your application runs on, you might have to also set an environment variable to enable trace log correlation, in addition to following the steps in this section.
+ On Amazon EKS, no additional environment variable is needed. You still must configure your logging output as described in the following examples, and your logger must write to stdout so that Container Insights can collect the logs.
+ On Amazon ECS, no additional environment variable is needed. You still must configure your logging output as described in the following examples, and your logger must write to stdout so that Container Insights can collect the logs.
+ On Amazon EC2, see the step 4 in the procedure in [Step 3: Instrument your application and start it](CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument).

**OpenTelemetry Container Insights does not enable trace log correlation automatically**  
Enabling the OpenTelemetry-based Container Insights log collection path (for example, through the [CloudWatch Observability EKS add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-eks-otel-install-addon.html)) collects and ships your container logs to CloudWatch Logs, but it does not instrument your application for Application Signals or inject trace context into those logs. To correlate traces with logs, you must separately enable Application Signals instrumentation *and* configure your logging pattern as described on this page.

After you enable trace log correlation, when you open a trace detail page, any log entries that contain the same trace ID automatically appear at the bottom of the page. With trace log correlation, you can quickly move from a trace to the relevant application logs without manually searching.

## Trace log correlation setup examples
<a name="Application-Signals-TraceLogCorrelation-Examples"></a>

This section contains examples of setting up trace log correlation in several environments.

**Spring Boot for Java**

Suppose you have a Spring Boot application in a folder called `custom-app`. The application configuration is usually a YAML file named `custom-app/src/main/resources/application.yml` that might look like this: 

```
spring:
  application:
    name: custom-app
  config:
    import: optional:configserver:${CONFIG_SERVER_URL:http://localhost:8888/}
    
...
```

To enable trace log correlation, add the following logging configuration.

```
spring:
  application:
    name: custom-app
  config:
    import: optional:configserver:${CONFIG_SERVER_URL:http://localhost:8888/}
    
...    

logging:
  pattern:
    level: trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p
```

**Spring Boot and XML configuration are alternatives**  
The Spring Boot `application.yml` (`logging.pattern.level`) approach and the Logback/Log4j2/Log4j XML configuration approaches shown in the following sections are *alternatives*. Use one or the other, not both. If you set the pattern in `application.yml`, Spring Boot's default Logback configuration picks it up automatically and no separate `logback.xml` is needed.

**EKS and ECS: Write logs to stdout**  
Container Insights collects logs from the container's stdout/stderr, not from files written inside the container. Configure your logger to write to the console (stdout). A FileAppender writing to a file such as `app.log` produces correctly trace-tagged lines, but they are not collected and do not appear correlated on the trace detail page. If you must log to a file, you additionally need to ship that file (for example, a sidecar collector reading a shared volume), which is outside the scope of this page.

**Logback for Java**

In the logging configuration (such as logback.xml), insert the trace context `trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p` into `pattern` of Encoder. For example, the following configuration prepends the trace context before the log message.

```
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
  <encoder> 
    <pattern>trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p - %m%n</pattern> 
  </encoder>
</appender>
```

For more information about encoders in Logback, see [ Encoders](https://logback.qos.ch/manual/encoders.html) in the Logback documentation.

**Log4j2 for Java**

In the logging configuration (such as log4j2.xml), insert the trace context `trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p` into `PatternLayout`. For example, the following configuration prepends the trace context before the log message.

```
<Appenders>
  <Console name="CONSOLE" target="SYSTEM_OUT">
    <PatternLayout pattern="trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p - %m%n"/>
  </Console>
</Appenders>
```

For more information about pattern layouts in Log4j2, see [ Pattern Layout](https://logging.apache.org/log4j/2.x/manual/layouts.html#Pattern_Layout) in the Log4j2 documentation.

**Log4j for Java **

In the logging configuration (such as log4j.xml), insert the trace context `trace_id=%X{trace_id} span_id=%X{span_id} trace_flags=%X{trace_flags} %5p` into `PatternLayout`. For example, the following configuration prepends the trace context before the log message.

```
<appender name="CONSOLE" class="org.apache.log4j.ConsoleAppender">
  <layout class="org.apache.log4j.PatternLayout">
    <param name="ConversionPattern" value="trace_id=%X{trace_id} span_id=%X{span_id} trace_flags=%X{trace_flags} %5p - %m%n"/>
  </layout>
</appender>
```

For more information about pattern layouts in Log4j, see [ Class Pattern Layout](https://logging.apache.org/log4j/1.x/apidocs/org/apache/log4j/PatternLayout.html) in the Log4j documentation.

**Python**

Set the environment variable `OTEL_PYTHON_LOG_CORRELATION` to `true` while running your application. For more information, see [ Enable trace context injection](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html#enable-trace-context-injection)in the Python OpenTelemetry documentation.

**Node.js**

For more information about enabling trace context injection in Node.js for the logging libraries that support it, see the NPM usage documentations of the [ Pino](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino), [ Winston](https://www.npmjs.com/package/@opentelemetry/instrumentation-winston), or [ Bunyan](https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan) auto-instrumentations for Node.js.

### Verify the setup
<a name="Application-Signals-TraceLogCorrelation-Verify"></a>

After redeploying your application, confirm that a log line now shows a populated `trace_id` (for example, by running `kubectl logs {{pod-name}}`). Then open a trace detail page in the Application Signals console and confirm that the correlated log entries appear at the bottom of the page.

On Amazon EKS, logs are written to the Container Insights application log group (`/aws/containerinsights/{{cluster-name}}/application`, or `/aws/otel/containerinsights/{{cluster-name}}/application` when the OpenTelemetry Container Insights log path is enabled).