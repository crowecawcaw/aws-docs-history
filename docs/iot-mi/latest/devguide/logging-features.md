# Logging features

Use these methods to implement logging features that managed integrations provides.

## Logger initialization

```
void iotmi_devicesdk_log_init(const char* logger_name)
```

You must initialize the logger before you use any logging functionality.

Parameters

`logger_name` - The logger name you specify. Default value is: `MyApplication`

## Logging macros

`LOGGER_LOGD(...)`

Use this macro in your application for DEBUG level logging.

`LOGGER_LOGI(...)`

Use this macro in your application for INFO level logging.

`LOGGER_LOGW(...)`

Use this macro in your application for WARN level logging.

`LOGGER_LOGE(...)`

Use this macro in your application for ERROR level logging.

###### Note

For more information about logging features, see [Hub logging documentation](hub-log.md "hub-log.md").
Custom protocol plugins fully support all logging features that managed integrations offers.
