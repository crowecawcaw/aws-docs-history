# Enable trace to log correlation

You can enable *trace to log correlation* in Application Signals. This automatically injects trace IDs and span IDs into the relevant application logs. Then, when you open a trace detail page in the Application Signals console, 
 the relevant log entries (if any) that correlate 
 with the current trace automatically appear at the bottom of the page.

For example, suppose you notice a spike in a latency graph. You can choose the point on the graph to load the diagnostics information for that point in time. You then choose the relevant trace to get more information. When you view the trace 
 information, you can scroll down to see the logs associated with the trace. These logs might reveal patterns or error codes associated with the issues causing the latency spike.

To achieve trace log correlation, Application Signals relies on the following:


* [Logger MDC auto-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/logger-mdc-instrumentation.md "https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/logger-mdc-instrumentation.md") for Java.
* [OpenTelemetry Logging Instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html") for Python.
* The [Pino](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino "https://www.npmjs.com/package/@opentelemetry/instrumentation-pino"), [Winston](https://www.npmjs.com/package/@opentelemetry/instrumentation-winston "https://www.npmjs.com/package/@opentelemetry/instrumentation-winston"), or [Bunyan](https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan "https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan") auto-instrumentations for Node.js.
All of these isntrumentations are provided by OpenTelemetry community. Application Signals uses them to inject trace contexts such as trace ID and span ID into application logs. 
 To enable this, you must manually change your logging configuration to enable the auto-instrumentation. 

Depending on the architecture that your application runs on, you might have to also set an environment variable to enable trace log correlation, in addition to following the 
 steps in this section.


* On Amazon EKS, no further steps are needed.
* On Amazon ECS, no further steps are needed.
* On Amazon EC2, see the step 4 in the procedure in [Step 3: Instrument your application and start it](CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument "CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument").
After you enable trace log correlation, 


## Trace log correlation setup examples


This section contains examples of setting up trace log correlation in several environments.


**Spring Boot for Java**


Suppose you have a Spring Boot application in a folder called `custom-app`. The application configuration is usually a YAML file 
 named `custom-app/src/main/resources/application.yml` that might look like this: 



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

**logging:
 pattern:
 level: trace\_id=%mdc{trace\_id} span\_id=%mdc{span\_id} trace\_flags=%mdc{trace\_flags} %5p**
```

**Logback for Java**


In the logging configuration (such as logback.xml), insert the trace context `trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p` into `pattern` 
 of Encoder. For example, the following configuration prepends the trace context before the log message.



```
<appender name="FILE" class="ch.qos.logback.core.FileAppender">
  <file>app.log</file>
  <append>true</append>
  <encoder> 
    <pattern>trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p - %m%n</pattern> 
  </encoder>
</appender>
```

For more information about encoders in Logback, see [Encoders](https://logback.qos.ch/manual/encoders.html "https://logback.qos.ch/manual/encoders.html") in the Logback documentation.


**Log4j2 for Java**


In the logging configuration (such as log4j2.xml), insert the trace context `trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p` 
 into `PatternLayout`.
 For example, the following configuration prepends the trace context before the log message.



```
<Appenders>
  <File name="FILE" fileName="app.log">
    <PatternLayout pattern="trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p - %m%n"/>
  </File>
</Appenders>
```

For more information about pattern layouts in Log4j2, see [Pattern Layout](https://logging.apache.org/log4j/2.x/manual/layouts.html#Pattern_Layout "https://logging.apache.org/log4j/2.x/manual/layouts.html#Pattern_Layout") in the Log4j2 documentation.


**Log4j for Java** 


In the logging configuration (such as log4j.xml), insert the trace context `trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p` 
 into `PatternLayout`.
 For example, the following configuration prepends the trace context before the log message.



```
<appender name="FILE" class="org.apache.log4j.FileAppender">;
  <param name="File" value="app.log"/>;
  <param name="Append" value="true"/>;
  <layout class="org.apache.log4j.PatternLayout">;
    <param name="ConversionPattern" value="trace_id=%mdc{trace_id} span_id=%mdc{span_id} trace_flags=%mdc{trace_flags} %5p - %m%n"/>;
  </layout>;
</appender>;
```

For more information about pattern layouts in Log4j, see [Class Pattern Layout](https://logging.apache.org/log4j/1.x/apidocs/org/apache/log4j/PatternLayout.html "https://logging.apache.org/log4j/1.x/apidocs/org/apache/log4j/PatternLayout.html") in the Log4j documentation.


**Python**


Set the environment variable `OTEL_PYTHON_LOG_CORRELATION` to `true` while running your application. For more information, see 
 [Enable trace context injection](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html#enable-trace-context-injection "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html#enable-trace-context-injection")in the Python OpenTelemetry documentation.


**Node.js**


For more information about enabling trace context injection in Node.js for the logging libraries that support it, 
 see the NPM usage documentations of the [Pino](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino "https://www.npmjs.com/package/@opentelemetry/instrumentation-pino"), [Winston](https://www.npmjs.com/package/@opentelemetry/instrumentation-winston "https://www.npmjs.com/package/@opentelemetry/instrumentation-winston"), or [Bunyan](https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan "https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan") auto-instrumentations for Node.js.
