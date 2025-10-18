# Library functions available for
 Node.js canary

This section describes the library functions that are available for canary scripts using the Node.js runtime.

###### Topics

* [addExecutionError(errorMessage, ex);](#Library_function_Nodejs_addExecutionError_Nodecanary "#Library_function_Nodejs_addExecutionError_Nodecanary")
* [getCanaryName();](#Library_function_Nodejs_getCanaryName "#Library_function_Nodejs_getCanaryName")
* [getCanaryArn();](#Library_function_Nodejs_Nodecanary "#Library_function_Nodejs_Nodecanary")
* [getCanaryUserAgentString();](#Library_function_Nodejs_getCanaryUserAgentString_Nodecanary "#Library_function_Nodejs_getCanaryUserAgentString_Nodecanary")
* [getRuntimeVersion();](#Library_function_Nodejs_getRuntimeVersion_Nodecanary "#Library_function_Nodejs_getRuntimeVersion_Nodecanary")
* [getLogLevel();](#Library_function_Nodejs_getLogLevel_Nodecanary "#Library_function_Nodejs_getLogLevel_Nodecanary")
* [setLogLevel();](#Library_function_Nodejs_setLogLevel_Nodecanary "#Library_function_Nodejs_setLogLevel_Nodecanary")
* [executeStep(stepName, functionToExecute, [stepConfig])](#Library_function_Nodejs_executestep_Nodecanary "#Library_function_Nodejs_executestep_Nodecanary")
* [executeHttpStep(stepName, requestOptions, [callback], [stepConfig])](#Library_function_Nodejs_executeHttpStep "#Library_function_Nodejs_executeHttpStep")

## addExecutionError(errorMessage, ex);


`errorMessage` describes the error and `ex`
 is the exception that is encountered


You can use `addExecutionError` to set execution errors for your canary. It fails
 the canary without interrupting the script execution. It also doesn't impact your
 `successPercent` metrics.


You should track errors as execution errors only if they are not important to indicate
 the success or failure of your canary script.


An example of the use of `addExecutionError` is the following. You are monitoring the 
 availability of your endpoint and taking screenshots after the page has loaded. Because the failure
 of taking a screenshot doesn't determine availability of the endpoint, you can catch any errors 
 encountered while taking screenshots and add them as execution errors. Your availability metrics will
 still indicate that the endpoint is up and running, but your canary status will be marked as failed.
 The following sample code block catches such an error and adds it as an execution error.



```
try {await synthetics.executeStep(stepName, callbackFunc);} catch(ex) {synthetics.addExecutionError('Unable to take screenshot ', ex);}
```

## getCanaryName();


Returns the name of the canary.


## getCanaryArn();


Returns the ARN of the canary.


## getCanaryUserAgentString();


Returns the custom user agent of the canary.


## getRuntimeVersion();


This function is available on runtime version `syn-nodejs-3.0` and later. It returns the Synthetics runtime version of the canary. For example, the return value could be `syn-nodejs-3.0`.


## getLogLevel();


Retrieves the current log level for the Synthetics library. Possible values are the following:



* `0` – Debug
* `1` – Info
* `2` – Warn
* `3` – Error

Example:



```
let logLevel = synthetics.getLogLevel();
```

## setLogLevel();


Sets the log level for the Synthetics library. Possible values are the following:



* `0` – Debug
* `1` – Info
* `2` – Warn
* `3` – Error

Example:



```
synthetics.setLogLevel(0);
```

## executeStep(stepName, functionToExecute, [stepConfig])


Executes the provided step, wrapping it with start/pass/fail logging and pass/fail and duration metrics.


The `executeStep` function also does the following:



* Logs that the step started
* Starts a timer
* Executes the provided function
* When the function returns normally, it counts as passing. If the function throws, it counts as failing
* Ends the timer
* Logs whether the step passed or failed
* Emits the `stepName SuccessPercent` metric, 100 for pass or 0 for failure
* Emits the `stepName Duration metric`, with a value based on the step start and end times
* Returns what the functionToExecute returned or re-throws what `functionToExecute` threw
* Adds a step execution summary to the canary's report

**Example**



```
await synthetics.executeStep(stepName, async function () {
    return new Promise((resolve, reject) => {
        const req = https.request(url, (res) => {
            console.log(`Status: ${res.statusCode}`);
            if (res.statusCode >= 400) {
                reject(new Error(`Request failed with status ${res.statusCode} for ${url}`));
            } else {
                resolve();
            }
        });

        req.on('error', (err) => {
            reject(new Error(`Request failed for ${url}: ${err.message}`));
        });

        req.end();
    });
});
```

## executeHttpStep(stepName, requestOptions, [callback], [stepConfig])


Executes the provided HTTP request as a step, and publishes `SuccessPercent` (pass/fail) and 
 `Duration` metrics.


**executeHttpStep** uses either HTTP or HTTPS native functions under the hood,
 depending upon the protocol specified in the request.


This function also adds a step execution summary to the canary's report. The 
 summary includes details about each HTTP request, such as the following:



* Start time
* End time
* Status (PASSED/FAILED)
* Failure reason, if it failed
* HTTP call details such as request/response headers, body, status code, 
 status message, and performance timings.

###### Topics

* [Parameters](#Library_function_Nodejs_executeHttpStep_parameters_Nodecanary "#Library_function_Nodejs_executeHttpStep_parameters_Nodecanary")
* [Examples
 of using executeHttpStep](#Library_function_Nodejs_executeHttpStep_examples_Nodecanary "#Library_function_Nodejs_executeHttpStep_examples_Nodecanary")

### Parameters


**stepName(`String`)**


Specifies the name of the step. This name is also used for publishing
 CloudWatch metrics for this step.


**requestOptions(`Object or String`)**


The value of this parameter can be a URL, a URL string, or an object. If it is 
 an object, then it must be a set of configurable options to make an HTTP request. It 
 supports all options in 
 [http.request(options[, callback])](https://nodejs.org/api/http.html#http_http_request_options_callback "https://nodejs.org/api/http.html#http_http_request_options_callback") in the Node.js documentation.


In addition to these Node.js options, **requestOptions**
 supports the additional parameter `body`. You can use the `body`
 parameter to pass data as a request body.


**callback(`response`)**


(Optional) This is a user function which is invoked with the HTTP response. The response
 is of the type [Class: http.IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage "https://nodejs.org/api/http.html#http_class_http_incomingmessage").


**stepConfig(`object`)**


(Optional) Use this parameter to override global synthetics configurations with a 
 different configuration for this step.


### Examples
 of using executeHttpStep


The following series of examples build on each other to illustrate the various uses 
 of this option.


This first example configures request parameters. You can pass a URL as **requestOptions**:



```
let requestOptions = 'https://www.amazon.com';
```

Or you can pass a set of options:



```
let requestOptions = {
        'hostname': 'myproductsEndpoint.com',
        'method': 'GET',
        'path': '/test/product/validProductName',
        'port': 443,
        'protocol': 'https:'
    };
```

The next example creates a callback function which accepts a response. By 
 default, if you do not specify **callback**, CloudWatch Synthetics validates that the status is between 200 and 299 inclusive.



```
// Handle validation for positive scenario
    const callback = async function(res) {
        return new Promise((resolve, reject) => {
            if (res.statusCode < 200 || res.statusCode > 299) {
                throw res.statusCode + ' ' + res.statusMessage;
            }
     
            let responseBody = '';
            res.on('data', (d) => {
                responseBody += d;
            });
     
            res.on('end', () => {
                // Add validation on 'responseBody' here if required. For ex, your status code is 200 but data might be empty
                resolve();
            });
        });
    };
```

The next example creates a configuration for this step that overrides
 the global CloudWatch Synthetics configuration. The step configuration in this example
 allows request headers, response headers, request body (post data), and response body 
 in your report and restrict 'X-Amz-Security-Token' and 'Authorization' header values. 
 By default, these values are not included in the report for security reasons. 
 If you choose to include them, the data is only stored in your S3 bucket.



```
// By default headers, post data, and response body are not included in the report for security reasons. 
// Change the configuration at global level or add as step configuration for individual steps
let stepConfig = {
    includeRequestHeaders: true, 
    includeResponseHeaders: true,
    restrictedHeaders: ['X-Amz-Security-Token', 'Authorization'], // Restricted header values do not appear in report generated.
    includeRequestBody: true,
    includeResponseBody: true
};
```

This final example passes your request to **executeHttpStep** and names the step.



```
await synthetics.executeHttpStep('Verify GET products API', requestOptions, callback, stepConfig);
```

With this set of examples, CloudWatch Synthetics adds the details from each step in your report and
 produces metrics for each step using **stepName**.



 You will see `successPercent` and `duration` metrics for 
 the `Verify GET products API` step. You can monitor your API 
 performance by monitoring the metrics for your API call steps. 
 


For a sample complete script that uses these functions, see [Multi-step API canary](CloudWatch_Synthetics_Canaries_Samples.md#CloudWatch_Synthetics_Canaries_Samples_APIsteps "CloudWatch_Synthetics_Canaries_Samples.md#CloudWatch_Synthetics_Canaries_Samples_APIsteps").
