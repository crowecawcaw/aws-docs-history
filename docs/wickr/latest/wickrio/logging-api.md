This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Logging API

This section describes the logging module that can be imported from the WickrIOAPI. This logging module allows for different log levels and log file rotations in the bot integrations. Winston logger is used as the logging library and the default log levels are those predefined by NPM and in order of importance are: error, warn, info, verbose, debug, and silly.

## Getting Started with the Logger

To get started with the logger first import WickrLogger from the wickrio-bot-api library. Then you can access a new logger like so:

```
const logger = new WickrLogger().getLogger()
```

If you are currently using console.log as your default logger all instances of console.log can be piped through the logger with this block of code:

```
console.log = function () {
  logger.info(util.format.apply(null, arguments))
}
```

Similarly console.error can be piped through the logger like so:

```
console.error = function () {
  logger.error(util.format.apply(null, arguments))
}
```

## Logger Configuration

The logger will look to the processes.json for the log level, max log file size, and max number of log files. These values can be changed by updating the values of LOG_LEVEL, LOG_FILE_SIZE, and LOG_MAX_FILES in the env section of processes.json.

Without modifying the log_tokens the log level will be set to info, the max file size will be set to 10MB and the max number of log files will be set to 5.

```
{
  "apps": [
    {
      "name": "WickrIO-Broadcast-Bot",
      "args": [],
      "script": "./build/index.js",
      "exec_interpreter": "node",
      "autorestart": false,
      "watch": ["package.json"],
      "ignore_watch": [".git"],
      "env": {
        "tokens": {},
        "log_tokens":
        {
          "LOG_LEVEL": "debug",
          "LOG_FILE_SIZE": "10m",
          "LOG_MAX_FILES": "5"
        }
      }
    }
  ]
}
```
