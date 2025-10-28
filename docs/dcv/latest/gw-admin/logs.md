# Understanding Connection Gateway activity logs

The Amazon DCV Connection Gateway logs its activities to a log file. Log files are useful for monitoring the state of the Connection Gateway and can be
used to troubleshoot problems. This section introduces the log file used by the Amazon DCV Connection Gateway and describes how to configure
all the aspects related to logging, such as location, verbosity, size, and rotation.

By default, log files produced by the Amazon DCV Connection Gateway are located in `/var/log/dcv-connection-gateway/` folder. Logs are rotated by default.
The most recent log is named `gateway.log`, while older logs are named `gateway.log.N`,
where `N` is a number. A bigger number indicates an older file log.

Every line in the log files uses the following format.

```
[Timestamp] [Level] [Context]: [Message]
```

Timestamps refer to the UTC time. Log level is one of `error`, `warn`, `info`, `debug`, `trace`
and it is an indication of the importance of the message. By default, `debug` and `trace` messages are not included in the logs
to reduce the verbosity, but while troubleshooting it is recommended to turn them on by changing the `level` parameter in the configuration.
Consult the [configuration file reference](config-reference.md#config-log "config-reference.md#config-log") for a list of parameters that affect the logging behavior.
