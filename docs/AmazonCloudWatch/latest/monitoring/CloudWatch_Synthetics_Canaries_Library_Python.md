# Library functions available for

Python canary scripts using Selenium

This section lists the Selenium library functions available for Python canary scripts.

###### Topics

- [Python and Selenium library classes and functions
  that apply
  to all canaries](#CloudWatch_Synthetics_Library_allcanaries_Python "#CloudWatch_Synthetics_Library_allcanaries_Python")
- [Python and Selenium library classes and functions
  that apply
  to UI canaries only](#CloudWatch_Synthetics_Library_Python_UIcanaries "#CloudWatch_Synthetics_Library_Python_UIcanaries")

## Python and Selenium library classes and functions

that apply
to all canaries

The following CloudWatch Synthetics Selenium library functions for Python are useful for all canaries.

###### Topics

- [SyntheticsConfiguration class](#CloudWatch_Synthetics_Library_SyntheticsConfiguration_Python "#CloudWatch_Synthetics_Library_SyntheticsConfiguration_Python")
- [SyntheticsLogger class](#CloudWatch_Synthetics_Library_SyntheticsLogger_Python "#CloudWatch_Synthetics_Library_SyntheticsLogger_Python")

### SyntheticsConfiguration class

You can use the SyntheticsConfiguration class to configure the behavior of
Synthetics library functions. For example, you can use this class to configure
the `executeStep()`
function to not capture screenshots.

You can set CloudWatch Synthetics configurations at the global level.

Function definitions:

#### set_config(options)

```
from aws_synthetics.common import synthetics_configuration
```

`options` is an object, which is a set
of configurable options for your canary. The following sections explain the possible
fields in `options`.

- `screenshot_on_step_start` (boolean)—
  Whether to take a screenshot before starting a step.
- `screenshot_on_step_success` (boolean)—
  Whether to take a screenshot after completing a successful step.
- `screenshot_on_step_failure` (boolean)—
  Whether to take a screenshot after a step fails.

**with_screenshot_on_step_start(screenshot_on_step_start)**

Accepts a Boolean argument, which indicates whether to take a screenshot
before starting a step.

**with_screenshot_on_step_success(screenshot_on_step_success)**

Accepts a Boolean argument, which indicates whether to take a screenshot
after completing a step successfully.

**with_screenshot_on_step_failure(screenshot_on_step_failure)**

Accepts a Boolean argument, which indicates whether to take a screenshot
after a step fails.

**get_screenshot_on_step_start()**

Returns whether to take a screenshot before starting a step.

**get_screenshot_on_step_success()**

Returns whether to take a screenshot after completing a step successfully.

**get_screenshot_on_step_failure()**

Returns whether to take a screenshot after a step fails.

**disable_step_screenshots()**

Disables all screenshot options (get_screenshot_on_step_start, get_screenshot_on_step_success,
and get_screenshot_on_step_failure).

**enable_step_screenshots()**

Enables all screenshot options (get_screenshot_on_step_start,
get_screenshot_on_step_success, and get_screenshot_on_step_failure). By default, all
these methods are enabled.

**setConfig(options) regarding CloudWatch metrics**

For canaries using `syn-python-selenium-1.1` or later,
the **(options)** for **setConfig** can
include the following Boolean
parameters that determine which metrics are published by the canary. The default for
each of these options is `true`. The options that start with
`aggregated` determine whether the metric is emitted without the
`CanaryName` dimension. You can use these metrics to see the aggregated
results for all of your canaries. The other options determine whether the metric
is emitted with the `CanaryName` dimension. You can use these metrics to see results
for each individual canary.

For a list of CloudWatch metrics emitted by canaries, see
[CloudWatch metrics published by canaries](CloudWatch_Synthetics_Canaries_metrics.md "CloudWatch_Synthetics_Canaries_metrics.md").

- `failed_canary_metric` (boolean)—
  Whether to emit the `Failed` metric (with the `CanaryName`
  dimension) for this canary. The default is `true`.
- `failed_requests_metric` (boolean)—
  Whether to emit the `Failed requests` metric (with the `CanaryName`
  dimension) for this canary. The default is `true`.
- `2xx_metric` (boolean)—
  Whether to emit the `2xx` metric (with the `CanaryName`
  dimension) for this canary. The default is `true`.
- `4xx_metric` (boolean)—
  Whether to emit the `4xx` metric (with the `CanaryName`
  dimension) for this canary. The default is `true`.
- `5xx_metric` (boolean)—
  Whether to emit the `5xx` metric (with the `CanaryName`
  dimension) for this canary. The default is `true`.
- `step_duration_metric` (boolean)—
  Whether to emit the `Step duration` metric (with the `CanaryName`
  `StepName` dimensions) for this canary. The default is `true`.
- `step_success_metric` (boolean)—
  Whether to emit the `Step success` metric (with the `CanaryName`
  `StepName` dimensions) for this canary. The default is `true`.
- `aggregated_failed_canary_metric` (boolean)—
  Whether to emit the `Failed` metric (without the `CanaryName`
  dimension) for this canary. The default is `true`.
- `aggregated_failed_requests_metric` (boolean)—
  Whether to emit the `Failed Requests` metric (without the `CanaryName`
  dimension) for this canary. The default is `true`.
- `aggregated_2xx_metric` (boolean)—
  Whether to emit the `2xx` metric (without the `CanaryName`
  dimension) for this canary. The default is `true`.
- `aggregated_4xx_metric` (boolean)—
  Whether to emit the `4xx` metric (without the `CanaryName`
  dimension) for this canary. The default is `true`.
- `aggregated_5xx_metric` (boolean)—
  Whether to emit the `5xx` metric (without the `CanaryName`
  dimension) for this canary. The default is `true`.

**with_2xx_metric(2xx_metric)**

Accepts a Boolean argument, which specifies whether to emit a `2xx`
metric with the `CanaryName` dimension for this canary.

**with_4xx_metric(4xx_metric)**

Accepts a Boolean argument, which specifies whether to emit a `4xx`
metric with the `CanaryName` dimension for this canary.

**with_5xx_metric(5xx_metric)**

Accepts a Boolean argument, which specifies whether to emit a `5xx`
metric with the `CanaryName` dimension for this canary.

**withAggregated2xxMetric(aggregated2xxMetric)**

Accepts a Boolean argument, which specifies whether to emit a `2xx`
metric with no dimension for this canary.

**withAggregated4xxMetric(aggregated4xxMetric)**

Accepts a Boolean argument, which specifies whether to emit a `4xx`
metric with no dimension for this canary.

**with_aggregated_5xx_metric(aggregated_5xx_metric)**

Accepts a Boolean argument, which specifies whether to emit a `5xx`
metric with no dimension for this canary.

**with_aggregated_failed_canary_metric(aggregated_failed_canary_metric)**

Accepts a Boolean argument, which specifies whether to emit a `Failed`
metric with no dimension for this canary.

**with_aggregated_failed_requests_metric(aggregated_failed_requests_metric)**

Accepts a Boolean argument, which specifies whether to emit a `Failed 
 requests`
metric with no dimension for this canary.

**with_failed_canary_metric(failed_canary_metric)**

Accepts a Boolean argument, which specifies whether to emit a `Failed`
metric with the `CanaryName` dimension for this canary.

**with_failed_requests_metric(failed_requests_metric)**

Accepts a Boolean argument, which specifies whether to emit a `Failed 
 requests`
metric with the `CanaryName` dimension for this canary.

**with_step_duration_metric(step_duration_metric)**

Accepts a Boolean argument, which specifies whether to emit a `Duration`
metric with the `CanaryName` dimension for this canary.

**with_step_success_metric(step_success_metric)**

Accepts a Boolean argument, which specifies whether to emit a `StepSuccess`
metric with the `CanaryName` dimension for this canary.

##### Methods

to enable or disable metrics

**disable_aggregated_request_metrics()**

Disables the canary from emitting all request metrics that are emitted with no `CanaryName`
dimension.

**disable_request_metrics()**

Disables all request metrics, including both per-canary metrics and
metrics aggregated across all canaries.

**disable_step_metrics()**

Disables all step metrics, including both step success metrics
and step duration metrics.

**enable_aggregated_request_metrics()**

Enables the canary to emit all request metrics that are emitted with no `CanaryName`
dimension.

**enable_request_metrics()**

Enables all request metrics, including both per-canary metrics and
metrics aggregated across all canaries.

**enable_step_metrics()**

Enables all step metrics, including both step success metrics
and step duration metrics.

**Usage in UI canaries**

First, import the synthetics dependency and fetch the configuration.
Then, set the configuration for each option by calling the setConfig method using one
of the following options.

```
from aws_synthetics.common import synthetics_configuration

synthetics_configuration.set_config(
     {
        "screenshot_on_step_start": False,
        "screenshot_on_step_success": False,
        "screenshot_on_step_failure": True
     }
)

or

```

Or

```
synthetics_configuration.with_screenshot_on_step_start(False).with_screenshot_on_step_success(False).with_screenshot_on_step_failure(True)
```

To disable all screenshots, use the disableStepScreenshots() function as in this example.

```
synthetics_configuration.disable_step_screenshots()
```

You can enable and disable screenshots at any point in the code. For
example, to disable screenshots only for one step, disable them before running that step
and then enable them after the step.

##### set_config(options) for UI canaries

Starting with `syn-python-selenium-1.1`, for UI canaries,
`set_config` can include the following Boolean parameters:

- `continue_on_step_failure` (boolean)—
  Whether to continue with running the canary script after a step fails (this
  refers to the **executeStep** function). If any steps
  fail, the canary run will still be marked as failed. The default is `false`.

### SyntheticsLogger class

`synthetics_logger` writes logs out to both the console and to a local log file at the
same log level. This log file is written to both locations only if the log level is at or below the desired logging level of
the log function that was called.

The logging statements in the local log file are prepended with "DEBUG: ", "INFO: ", and so on
to match the log level of the function that was called.

Using `synthetics_logger` is not required to create a log file that is
uploaded to your Amazon S3 results location. You could instead create a different log file in the
`/tmp` folder. Any files created under the `/tmp` folder
are uploaded to the results location in the S3 bucket as artifacts.

To use `synthetics_logger`:

```
from aws_synthetics.common import synthetics_logger
```

Useful function definitions:

Get log level:

```
log_level = synthetics_logger.get_level()
```

Set log level:

```
synthetics_logger.set_level()
```

Log a message with a specified level. The level can be `DEBUG`,
`INFO`, `WARN`, or `ERROR`, as in the following
syntax examples:

```
synthetics_logger.debug(message, *args, **kwargs)
```

```
synthetics_logger.info(message, *args, **kwargs)
```

```
synthetics_logger.log(message, *args, **kwargs)
```

```
synthetics_logger.warning(message, *args, **kwargs)
```

```
synthetics_logger.error(message, *args, **kwargs)
```

For information about debug parameters, see the standard Python documentation at
[logging.debug](https://docs.python.org/3/library/logging.html#logging.debug "https://docs.python.org/3/library/logging.html#logging.debug")

In these logging functions, the `message` is the message format
string. The `args` are the arguments that are merged into `msg`
using the string formatting operator.

There are three keyword arguments in `kwargs`:

- `exc_info`– If not evaluated as false, adds exception information
  to the logging message.
- `stack_info`– defaults to false. If true, adds stack information
  to the logging message, including the actual logging call.
- `extra`– The third optional keyword argument, which you can use to pass in a
  dictionary that is used to populate the `__dict__` of the
  `LogRecord` created for the logging event with user-defined
  attributes.

Examples:

Log a message with the level `DEBUG`:

```
synthetics_logger.debug('Starting step - login.')
```

Log a message with the level `INFO`. `logger.log` is a
synonym for `logger.info`:

```
synthetics_logger.info('Successfully completed step - login.')
```

or

```
synthetics_logger.log('Successfully completed step - login.')
```

Log a message with the level `WARN`:

```
synthetics_logger.warning('Warning encountered trying to publish %s', 'CloudWatch Metric')
```

Log a message with the level `ERROR`:

```
synthetics_logger.error('Error encountered trying to publish %s', 'CloudWatch Metric')
```

Log an exception:

```
synthetics_logger.exception(message, *args, **kwargs)
```

Logs a message with level `ERROR`. Exception information is added to the
logging message. You should call this function only from an exception handler.

For information about exception parameters, see the standard Python documentation at
[logging.exception](https://docs.python.org/3/library/logging.html#logging.exception "https://docs.python.org/3/library/logging.html#logging.exception")

The `message` is the message format string. The `args` are
the arguments, which are merged into `msg` using the string formatting
operator.

There are three keyword arguments in `kwargs`:

- `exc_info`– If not evaluated as false, adds exception information
  to the logging message.
- `stack_info`– defaults to false. If true, adds stack information
  to the logging message, including the actual logging call.
- `extra`– The third optional keyword argument, which you can use to pass in a
  dictionary that is used to populate the `__dict__` of the
  `LogRecord` created for the logging event with user-defined
  attributes.

Example:

```
synthetics_logger.exception('Error encountered trying to publish %s', 'CloudWatch Metric')
```

## Python and Selenium library classes and functions

that apply
to UI canaries only

The following CloudWatch Synthetics Selenium library functions for Python are useful only for UI
canaries.

###### Topics

- [SyntheticsBrowser class](#CloudWatch_Synthetics_Library_Python_SyntheticsBrowser "#CloudWatch_Synthetics_Library_Python_SyntheticsBrowser")
- [SyntheticsWebDriver class](#CloudWatch_Synthetics_Library_Python_SyntheticsWebDriver "#CloudWatch_Synthetics_Library_Python_SyntheticsWebDriver")

### SyntheticsBrowser class

###### Note

`SyntheticsBrowser` is supported only on the Chrome browser.

When you create a browser instance by calling
`synthetics_webdriver.Chrome()`, the returned browser instance is of the
type `SyntheticsBrowser`. The `SyntheticsBrowser` class inherits
the WebDriver class and provides access to all the methods exposed by the [WebDriver](https://www.selenium.dev/documentation/webdriver/ "https://www.selenium.dev/documentation/webdriver/"). It controls the ChromeDriver, and enables the canary script to drive the browser, allowing the Selenium WebDriver to work with Synthetics.

###### Note

Synthetics overrides the WebDriver [quit](https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_firefox/selenium.webdriver.firefox.webdriver.html "https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_firefox/selenium.webdriver.firefox.webdriver.html") method to take no action. You don't need to worry about quitting the browser, as Synthetics handles that for you.

In addition to the standard Selenium methods, it also provides the following
methods.

###### Topics

- [set_viewport_size(width, height)](#CloudWatch_Synthetics_Library_set_viewport_size "#CloudWatch_Synthetics_Library_set_viewport_size")
- [save_screenshot(filename, suffix)](#CloudWatch_Synthetics_Library_save_screenshot "#CloudWatch_Synthetics_Library_save_screenshot")

####

set_viewport_size(width, height)

Sets the viewport of the browser. Example:

```
browser.set_viewport_size(1920, 1080)
```

####

save_screenshot(filename, suffix)

Saves screenshots to the `/tmp` directory. The screenshots
are uploaded from there to the canary artifacts folder in the S3 bucket.

_filename_ is the file name for the screenshot, and
_suffix_ is an optional string to be used for naming the screenshot.

Example:

```
browser.save_screenshot('loaded.png', 'page1')
```

### SyntheticsWebDriver class

To use this class, use the following in your script:

```
from aws_synthetics.selenium import synthetics_webdriver
```

###### Topics

- [add_execution_error(errorMessage, ex);](#CloudWatch_Synthetics_Library_Python_addExecutionError "#CloudWatch_Synthetics_Library_Python_addExecutionError")
- [add_user_agent(user_agent_str)](#CloudWatch_Synthetics_Library_add_user_agent "#CloudWatch_Synthetics_Library_add_user_agent")
- [execute_step(step_name, function_to_execute)](#CloudWatch_Synthetics_Library_Python_execute_step "#CloudWatch_Synthetics_Library_Python_execute_step")
- [get_http_response(url)](#CloudWatch_Synthetics_Library_Python_get_http_response "#CloudWatch_Synthetics_Library_Python_get_http_response")
- [Chrome()](#CloudWatch_Synthetics_Library_Python_Chrome "#CloudWatch_Synthetics_Library_Python_Chrome")

#### add_execution_error(errorMessage, ex);

`errorMessage` describes the error and `ex`
is the exception that is encountered

You can use `add_execution_error` to set execution errors for your canary. It fails
the canary without interrupting the script execution. It also doesn't impact your
`successPercent` metrics.

You should track errors as execution errors only if they are not important to indicate
the success or failure of your canary script.

An example of the use of `add_execution_error` is the following. You are monitoring the
availability of your endpoint and taking screenshots after the page has loaded. Because the failure
of taking a screenshot doesn't determine availability of the endpoint, you can catch any errors
encountered while taking screenshots and add them as execution errors. Your availability metrics will
still indicate that the endpoint is up and running, but your canary status will be marked as failed.
The following sample code block catches such an error and adds it as an execution error.

```
try:
    browser.save_screenshot("loaded.png")
except Exception as ex:
   self.add_execution_error("Unable to take screenshot", ex)

```

####

add_user_agent(user_agent_str)

Appends the value of `user_agent_str` to the browser's
user agent header. You must assign `user_agent_str` before creating
the browser instance.

Example:

```
await synthetics_webdriver.add_user_agent('MyApp-1.0')
```

`add_user_agent` should be used inside an `async` function.

####

execute_step(step_name, function_to_execute)

Processes one function. It also does the following:

- Logs that the step started.
- Takes a screenshot named `<stepName>-starting`.
- Starts a timer.
- Executes the provided function.
- If the function returns normally, it counts as passing. If the function throws, it counts as failing.
- Ends the timer.
- Logs whether the step passed or failed
- Takes a screenshot named `<stepName>-succeeded` or
  `<stepName>-failed`.
- Emits the `stepName` `SuccessPercent` metric,
  100 for pass or 0 for failure.
- Emits the `stepName` `Duration` metric,
  with a value based on the step start and end times.
- Finally, returns what the `functionToExecute` returned or
  re-throws what `functionToExecute` threw.

Example:

```
from selenium.webdriver.common.by import By

def custom_actions():
        #verify contains
        browser.find_element(By.XPATH, "//*[@id=\"id_1\"][contains(text(),'login')]")
        #click a button
        browser.find_element(By.XPATH, '//*[@id="submit"]/a').click()

    await synthetics_webdriver.execute_step("verify_click", custom_actions)

```

####

get_http_response(url)

Makes an HTTP request to the provided URL and returns the response code of the
HTTP request. If an exception occurred during the HTTP request, a string with value
"error" is returned instead.

Example:

```
response_code = syn_webdriver.get_http_response(url)
if not response_code or response_code == "error" or response_code < 200 or response_code > 299:
    raise Exception("Failed to load page!")
```

####

Chrome()

Launches an instance of the Chromium browser and returns the created
instance of the browser.

Example:

```
browser = synthetics_webdriver.Chrome()
browser.get("https://example.com/)
```

To launch a browser in incognito mode, use the following:

```
add_argument('——incognito')
```

To add proxy settings, use the following:

```
add_argument('--proxy-server=%s' % `PROXY`)
```

Example:

```
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("——incognito")
browser = syn_webdriver.Chrome(chrome_options=chrome_options)
```
