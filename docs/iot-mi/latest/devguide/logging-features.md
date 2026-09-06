

# Logging features
<a name="logging-features"></a>

Use these methods to implement logging features that managed integrations provides.

## Logger initialization
<a name="logging-initialization"></a>

```
void iotmi_devicesdk_log_init(const char* logger_name)
```

You must initialize the logger before you use any logging functionality.

Parameters  
`logger_name` - The logger name you specify. Default value is: `MyApplication`

## Logging macros
<a name="logging-macros"></a>

`LOGGER_LOGD(...)`  
Use this macro in your application for DEBUG level logging.

`LOGGER_LOGI(...)`  
Use this macro in your application for INFO level logging.

`LOGGER_LOGW(...)`  
Use this macro in your application for WARN level logging.

`LOGGER_LOGE(...)`  
Use this macro in your application for ERROR level logging.

**Note**  
For more information about logging features, see [Hub logging documentation](https://docs.aws.amazon.com/iot-mi/latest/devguide/hub-log.html). Custom protocol plugins fully support all logging features that managed integrations offers.