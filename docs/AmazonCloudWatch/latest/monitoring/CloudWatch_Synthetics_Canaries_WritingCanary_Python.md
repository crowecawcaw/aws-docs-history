# Writing a Python canary script

This script passes as a successful run, and returns a string.
To see what a failing canary looks like, change fail = False to fail = True

```
def basic_custom_script():
    # Insert your code here
    # Perform multi-step pass/fail check
    # Log decisions made and results to /tmp
    # Be sure to wait for all your code paths to complete
    # before returning control back to Synthetics.
    # In that way, your canary will not finish and report success
    # before your code has finished executing
    fail = False
    if fail:
        raise Exception("Failed basicCanary check.")
    return "Successfully completed basicCanary checks."
def handler(event, context):
    return basic_custom_script()
```

## Packaging your Python canary files

If you have more than one .py file or your script has a dependency, you can bundle them
all into a single ZIP file. If you use the `syn-python-selenium-1.1` runtime, the
ZIP file must contain your main canary
.py file within a `python` folder, such as
`python/my_canary_filename.py`. If you use
`syn-python-selenium-1.1` or later, you can optionally use a different folder
, such as `python/myFolder/my_canary_filename.py`.

This ZIP file
should contain all necessary folders and files, but the other files do not need
to be in the `python` folder.

Be sure to set your canary’s script entry point as
`my_canary_filename.functionName` to match the file name and function name of your script’s entry
point. If you are using the `syn-python-selenium-1.0` runtime, then `functionName`
must be `handler`. If you are using `syn-python-selenium-1.1` or later, this handler
name restriction
doesn't apply, and you can also optionally store the canary in a separate folder such as
`python/myFolder/my_canary_filename.py`. If you store it in a separate folder,
specify that path in your script entry point, such as `myFolder/my_canary_filename.functionName`.

## Changing an existing Selenium script to use a Synthetics canary

You can quickly modify an existing script for Python and Selenium to be used as a canary.
For more information about Selenium, see
[www.selenium.dev/](https://www.selenium.dev/ "https://www.selenium.dev/").

For this example, we'll start with the following Selenium script:

```
from selenium import webdriver

def basic_selenium_script():
    browser = webdriver.Chrome()
    browser.get('https://example.com')
    browser.save_screenshot('loaded.png')

basic_selenium_script()
```

The conversion steps are as follows.

###### To convert a Selenium script to be used as a canary

1. Change the `import` statement to use Selenium
   from the `aws_synthetics` module:

```
from aws_synthetics.selenium import synthetics_webdriver as webdriver
```

The Selenium module from `aws_synthetics` ensures that the canary
can emit metrics and logs, generate a HAR file, and work with other
CloudWatch Synthetics features. 2. Create a handler function and call your Selenium method. The handler
is the entry point function for the script.

If you are using `syn-python-selenium-1.0`,
the handler function must be named `handler`. If you are using `syn-python-selenium-1.1`
or later, the function can have any name, but it must be the same name that is
used in the script. Also, if you are using `syn-python-selenium-1.1`
or later, you can store your scripts under any folder and specify that folder as part of the handler name.

```
def handler(event, context):
    basic_selenium_script()
```

The script is now updated to be a CloudWatch Synthetics canary. Here is
the updated script:

The `webdriver` is an instance of the class [SyntheticsWebDriver](CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_SyntheticsWebDriver "CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_SyntheticsWebDriver") and the browser returned by `webdriver.Chrome()` is an instance of [SyntheticsBrowser](CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_SyntheticsBrowser "CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_SyntheticsBrowser").

```
from aws_synthetics.selenium import synthetics_webdriver as webdriver

def basic_selenium_script():
    browser = webdriver.Chrome()
    browser.get('https://example.com')
    browser.save_screenshot('loaded.png')

def handler(event, context):
    basic_selenium_script()
```

## Changing an existing Puppeteer Synthetics script to authenticate non-standard certificates

One important use case for Synthetics canaries is for you to monitor your own endpoints. If you want to monitor an endpoint that isn't ready for external
traffic, this monitoring can sometimes mean that you don't have a proper
certificate signed by a trusted third-party certificate authority.

Two possible solutions to this scenario are as follows:

- To authenticate a client certificate, see [How to validate authentication using Amazon CloudWatch Synthetics – Part 2](https://aws.amazon.com/blogs/mt/how-to-validate-authentication-using-amazon-cloudwatch-synthetics-part-2/ "https://aws.amazon.com/blogs/mt/how-to-validate-authentication-using-amazon-cloudwatch-synthetics-part-2/").
- To authenticate a self-signed certificate, see [How to validate authentication with self-signed certificates in Amazon CloudWatch Synthetics](https://aws.amazon.com/blogs/mt/how-to-validate-authentication-with-self-signed-certificates-in-amazon-cloudwatch-synthetics/ "https://aws.amazon.com/blogs/mt/how-to-validate-authentication-with-self-signed-certificates-in-amazon-cloudwatch-synthetics/")

You are not limited to these two options when you use CloudWatch Synthetics canaries. You can extend these features and add your business logic by extending the canary code.

###### Note

Synthetics canaries running on Python runtimes innately have the `--ignore-certificate-errors` flag enabled, so those canaries shouldn't have any issues reaching sites with non-standard certificate
configurations.
