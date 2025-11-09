AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up AWS Blu Age Runtime (on Amazon EC2) Amazon CloudWatch alarms

You can set up CloudWatch to receive your application log and add an alarm to warn you of
possible errors. This allows you to have more visible notifications whenever your deployed
applications encounter exceptions. The following sections help you understand and learn
about the configuration of CloudWatch logging and alarm setup.

## Deployment of CloudWatch logging

By default, the AWS Blu Age Runtime contains a logging file named
`logback-cloudwatch.yml`. This file is referenced in the
`application-main.yml` file, but this reference is commented
out.

```
# logging:
#  config: classpath:logback-cloudwatch.xml
```

Both files are in the config folder, and by uncommenting the above lines, the feature
can be activated. CloudWatch logging can be configured, as explained in the following
sections.

## Configuration of CloudWatch logging

The default `logback-cloudwatch.xml` file has the following
contents.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration>
<configuration>

    <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%date{yyyy-MM-dd HH:mm:ss.SSS,UTC}  %level --- [%thread{15}] %logger{40} : %msg%n%xThrowable</pattern>
        </encoder>
    </appender>

    <appender name="cloudwatch" class="com.netfective.bluage.runtime.cloudwatchlogger.CloudWatchAppender">
        <logGroup>BluAgeRuntimeOnEC2-Logs</logGroup>
        <logStream>%date{yyyy-MM-dd,UTC}.%instanceId.%uuid</logStream>
        <layout>
            <pattern>%date{yyyy-MM-dd HH:mm:ss.SSS,UTC}  %level --- [%thread{15}] %logger{40} : %msg%n%xThrowable</pattern>
        </layout>
        <appender-ref ref="console" />
    </appender>

    <root level="INFO">
        <appender-ref ref="cloudwatch" />
    </root>
</configuration>
```

Everything outside the <appender name="cloudwatch"/> element is standard logback
configuration. There are two appenders in this file: a console appender to send logs to
the console and a CloudWatch appender to send logs to CloudWatch.

The `level` attribute in the `root` element specifies the
logging level of the entire application.

The required values inside the tag <appender name="cloudwatch"/> are:

- <logGroup/>:Sets the name of the log group in CloudWatch. If the value is not
  specified it defaults to `BluAgeRuntimeOnEC2-Logs`. If the log group
  doesn’t exist it will be created automatically. This behavior can be changed
  through configuration, which is covered below.
- <logStream/>: Sets the name of the logStream (inside of the log group)
  in CloudWatch.

Optional values:

- <region/>: Overrides the Region that the log stream will be written to.
  By default, logs go to the same Region as the EC2 instance.
- <layout/>: The pattern the log messages will use.
- <maxbatchsize/>: The maximum number of log messages to send to CloudWatch per
  operation.
- <maxbatchtimemillis/>: The time in milliseconds to allow for CloudWatch logs
  to be written.
- <maxqueuewaittimemillis/>: The time in milliseconds to try to insert
  requests in the internal log queue.
- <internalqueuesize/>: The maximum size of the internal queue.
- <createlogdests/>: Create log group and log stream if they don't
  exist.
- <initialwaittimemillis/>: The amount of time that you want the thread to
  sleep on startup. This initial wait allows for an initial accrual of
  logs.
- <maxeventmessagesize/>: The maximum size of a log event. Logs that
  exceed this size won’t be sent.
- <truncateeventmessages/>: Truncate messages that are too long.
- <printrejectedevents/>: Enable the emergency appender.

## CloudWatch setup

In order for the above configuration to correctly push logs to CloudWatch, update your Amazon EC2
IAM instance profile role to grant it additional permissions for the
`BluAgeRuntimeOnEC2-Logs` log group and its log streams:

- `logs:CreateLogStream`
- `logs:DescribeLogStreams`
- `logs:CreateLogGroup`
- `logs:PutLogEvents`
- `logs:DescribeLogGroups`

## Alarm setup

Thanks to CloudWatch logs, you can then configure different metrics and alarms, depending on
your application and your needs. Specifically, you can set up proactive alarms for usage
alerts, in order to be warned in the case of errors that might put your application in a
grace period (and in the end, prevent it from working at all). To achieve this, you can
add a metric concerning the "Error C5001" string in the logs, which highlights errors in
the connection to the AWS Blu Age control system. You can then define an alarm that reacts to
this metric.
