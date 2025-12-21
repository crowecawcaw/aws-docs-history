# Instrumenting scripts

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

You can also instrument code that isn't part of your application. When the X-Ray daemon is
running, it will relay any segments that it receives to X-Ray, even if they are not generated
by the X-Ray SDK. Scorekeep uses its own scripts to instrument the build that compiles the
application during deployment.

###### Example [`bin/build.sh`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/build.sh "https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/build.sh") – Instrumented build script

```
SEGMENT=$(python bin/xray_start.py)
gradle build --quiet --stacktrace &> /var/log/gradle.log; GRADLE_RETURN=$?
if (( GRADLE_RETURN != 0 )); then
  echo "Gradle failed with exit status $GRADLE_RETURN" >&2
  python bin/xray_error.py "$SEGMENT" "$(cat /var/log/gradle.log)"
  exit 1
fi
python bin/xray_success.py "$SEGMENT"
```

[`xray_start.py`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/xray_start.py "https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/xray_start.py"), [`xray_error.py`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/xray_error.py "https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/xray_error.py")
and [`xray_success.py`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/xray_success.py "https://github.com/awslabs/eb-java-scorekeep/tree/xray/bin/xray_success.py") are simple Python scripts that construct
segment objects, convert them to JSON documents, and send them to the daemon over UDP. If the
Gradle build fails, you can find the error message by clicking on the
**scorekeep-build** node in the X-Ray console trace map.

![Diagram showing client connection to Scorekeep-build with average time of 14.6s and 0.07/min.](images/scorekeep-servicemap-builderror.png)

![Timeline view showing Scorekeep-build process with 14.6 second duration and warning icon.](images/scorekeep-timeline-builderror.png)

![Error message showing build failure due to missing ElasticBeanstalkPlugin symbol in RdsWebConfig class.](images/scorekeep-exception-builderror.png)
