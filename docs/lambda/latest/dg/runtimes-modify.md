# Modifying the runtime environment

You can use [internal extensions](lambda-extensions.md "lambda-extensions.md") to modify the runtime process. Internal
extensions are not separate processes—they run as part of the runtime process.

Lambda provides language-specific [environment variables](configuration-envvars.md "configuration-envvars.md") that you can
set to add options and tools to the runtime. Lambda also provides [wrapper
scripts](#runtime-wrapper "#runtime-wrapper"), which allow Lambda to delegate the runtime startup to your script. You can create a wrapper script
to customize the runtime startup behavior.

## Language-specific environment variables

Lambda supports configuration-only ways to enable code to be pre-loaded during function initialization through
the following language-specific environment variables:

- `JAVA_TOOL_OPTIONS` – On Java, Lambda supports this
  environment variable to set additional command-line variables in Lambda. This environment variable allows you
  to specify the initialization of tools, specifically the launching of native or Java programming language
  agents using the `agentlib` or `javaagent` options. For more information, see
  [`JAVA_TOOL_OPTIONS` environment variable](java-customization.md#java-tool-options "java-customization.md#java-tool-options").
- `NODE_OPTIONS` – Available in [Node.js runtimes](lambda-nodejs.md "lambda-nodejs.md").
- `DOTNET_STARTUP_HOOKS` – On .NET Core 3.1 and above, this environment variable specifies
  a path to an assembly (dll) that Lambda can use.

Using language-specific environment variables is the preferred way to set startup properties.

## Wrapper scripts

You can create a _wrapper script_ to customize the runtime startup behavior of your Lambda
function. A wrapper script enables you to set configuration parameters that cannot be set through
language-specific environment variables.

###### Note

Invocations may fail if the wrapper script does not successfully start the runtime process.

Wrapper scripts are supported on all native [Lambda runtimes](lambda-runtimes.md "lambda-runtimes.md"). Wrapper scripts are not supported on [OS-only runtimes](runtimes-provided.md "runtimes-provided.md") (the `provided` runtime family).

When you use a wrapper script for your function, Lambda starts the runtime using your script. Lambda sends to
your script the path to the interpreter and all of the original arguments for the standard runtime startup. Your
script can extend or transform the startup behavior of the program. For example, the script can inject and alter
arguments, set environment variables, or capture metrics, errors, and other diagnostic information.

You specify the script by setting the value of the `AWS_LAMBDA_EXEC_WRAPPER` environment variable
as the file system path of an executable binary or script.

### Example: Create and use a wrapper script as a Lambda layer

In the following example, you create a wrapper script to start the Python interpreter with the `-X
 importtime` option. When you run the function, Lambda generates a log entry to show the duration of the
import time for each import.

###### To create and use a wrapper script as a layer

1. Create a directory for the layer:

```
mkdir -p `python-wrapper-layer/bin`
cd `python-wrapper-layer/bin`
```

2. In the `bin` directory, paste the following code into a new file named
   `importtime_wrapper`. This is the wrapper script.

```
#!/bin/bash

# the path to the interpreter and all of the originally intended arguments
args=("$@")

# the extra options to pass to the interpreter
extra_args=("-X" "importtime")

# insert the extra options
args=("${args[@]:0:$#-1}" "${extra_args[@]}" "${args[@]: -1}")

# start the runtime with the extra options
exec "${args[@]}"
```

3. Give the script executable permissions:

```
chmod +x `importtime_wrapper`
```

4. Create a .zip file for the layer:

```
cd ..
zip -r ../`python-wrapper-layer.zip` .
```

5. Confirm that your .zip file has the following directory structure:

```
python-wrapper-layer.zip
└ bin
    └ importtime_wrapper
```

6. [Create a layer](creating-deleting-layers.md#layers-create "creating-deleting-layers.md#layers-create") using the .zip package.
7. Create a function using the Lambda console.
   1. Open the [Lambda console](https://console.aws.amazon.com/lambda "https://console.aws.amazon.com/lambda").
   2. Choose **Create function**.
   3. Enter a **Function name**.
   4. For **Runtime**, choose the **Latest supported** Python runtime.
   5. Choose **Create function**.

8. Add the layer to your function.
   1. Choose your function, and then choose the **Code** tab if it's not already selected.
   2. Scroll down to the **Layers** section, and then choose **Add a layer**.
   3. For **Layer source**, select **Custom layers**, and then choose your layer from the **Custom layers** dropdown list.
   4. For **Version**, choose **1**.
   5. Choose **Add**.

9. Add the wrapper environment variable.
   1. Choose the **Configuration** tab, then choose **Environment variables**.
   2. Under **Environment variables**, choose **Edit**.
   3. Choose **Add environment variable**.
   4. For **Key**, enter `AWS_LAMBDA_EXEC_WRAPPER`.
   5. For **Value**, enter `/opt/bin/importtime_wrapper` (`/opt/` + your .zip layer's folder structure).
   6. Choose **Save**.

10. Test the wrapper script.
    1. Choose the **Test** tab.
    2. Under **Test event**, choose **Test**. You don't need to create a test event—the default event will work.
    3. Scroll down to **Log output**. Because your wrapper script started the Python interpreter with the `-X importtime` option,
       the logs show the time required for each import. For example:

    ```
    532 |           collections
    import time:        63 |         63 |           _functools
    import time:      1053 |       3646 |         functools
    import time:      2163 |       7499 |       enum
    import time:       100 |        100 |         _sre
    import time:       446 |        446 |           re._constants
    import time:       691 |       1136 |         re._parser
    import time:       378 |        378 |         re._casefix
    import time:       670 |       2283 |       re._compiler
    import time:       416 |        416 |       copyreg
    ```
