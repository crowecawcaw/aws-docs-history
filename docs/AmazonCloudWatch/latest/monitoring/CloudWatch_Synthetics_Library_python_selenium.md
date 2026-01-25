# Runtime versions using Python

and Selenium Webdriver

The following sections contain information about the CloudWatch Synthetics runtime versions
for Python and Selenium Webdriver. Selenium is
an open-source browser automation tool. For more information about Selenium, see
[www.selenium.dev/](https://www.selenium.dev "https://www.selenium.dev")

For features and methods supported by Synthetics runtime on Selenium framework, see [Python and Selenium library classes and functions that apply to UI canaries only](CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_UIcanaries "CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_UIcanaries") and [Selenium API reference](https://www.selenium.dev/selenium/docs/api/py/api.html "https://www.selenium.dev/selenium/docs/api/py/api.html").

The naming convention for these runtime versions is
`syn-`language`-`framework`-`majorversion`.`minorversion``.

##

syn-python-selenium-8.0

Version 8.0 is the newest CloudWatch Synthetics runtime for Python and Selenium.

**Major dependencies**:

- Python 3.11
- Selenium 4.32.0
- Chromium version 142.0.7444.175

**Changes in syn-python-selenium-8.0**

- Applied security patches and updated Selenium and browser versions.
- Modified failed HAR network request log level from ERROR to INFO.

For more information, see the following:

- [Selenium Change log](https://www.selenium.dev/blog/2025/selenium-4-32-released "https://www.selenium.dev/blog/2025/selenium-4-32-released")
- [Selenium documentation](https://www.selenium.dev/selenium/docs/api/py/api.html "https://www.selenium.dev/selenium/docs/api/py/api.html")

The following earlier runtime versions for Python and Selenium are still supported.

###

syn-python-selenium-7.0

**Major dependencies**:

- Python 3.11
- Selenium 4.32.0
- Chromium version 138.0.7204.168

**Changes in syn-python-selenium-7.0**

- Applied security patches and updated Selenium and browser versions.

For more information, see the following:

- [Selenium Change log](https://www.selenium.dev/blog/2025/selenium-4-32-released "https://www.selenium.dev/blog/2025/selenium-4-32-released")
- [Selenium documentation](https://www.selenium.dev/selenium/docs/api/py/api.html "https://www.selenium.dev/selenium/docs/api/py/api.html")

###

syn-python-selenium-6.0

**Major dependencies**:

- Python 3.11
- Selenium 4.21.0
- Chromium version 131.0.6778.264

**Changes in syn-python-selenium-6.0**

- Upgrade from Python 3.9 to Python 3.11.

For more information, see the following:

- [Selenium Change log](https://www.selenium.dev/blog/2024/selenium-4-21-released/ "https://www.selenium.dev/blog/2024/selenium-4-21-released/")
- [Selenium documentation](https://www.selenium.dev/selenium/docs/api/py/api.html "https://www.selenium.dev/selenium/docs/api/py/api.html")

###

syn-python-selenium-5.1

**Major dependencies**:

- Python 3.9
- Selenium 4.21.0
- Chromium version 131.0.6778.264

**Changes in syn-python-selenium-5.1**

- Minor updates on metric emission.
- Supports dry runs for the canary which allows for adhoc executions or performing a safe canary update.

###

syn-python-selenium-5.0

**Major dependencies**:

- Python 3.9
- Selenium 4.21.0
- Chromium version 131.0.6778.264

**Changes in syn-python-selenium-5.0**:

- Automatic retry if the browser fails to launch.

###

syn-python-selenium-4.1

**Major dependencies**:

- Python 3.9
- Selenium 4.15.1
- Chromium version 126.0.6478.126

**Changes in syn-python-selenium-4.1**:

- **Addresses security vulnerability**– This runtime has
  an update to address the
  [CVE-2024-39689](https://nvd.nist.gov/vuln/detail/CVE-2024-39689 "https://nvd.nist.gov/vuln/detail/CVE-2024-39689") vulnerability.

###

syn-python-selenium-4.0

**Major dependencies**:

- Python 3.9
- Selenium 4.15.1
- Chromium version 126.0.6478.126

**Changes in syn-python-selenium-4.0**:

- **Bug fixes** for errors in HAR parser logging.

###

syn-python-selenium-3.0

**Major dependencies**:

- Python 3.8
- Selenium 4.15.1
- Chromium version 121.0.6167.139

**Changes in syn-python-selenium-3.0**:

- **Updated versions of the bundled libraries in Chromium**— The Chromium
  dependency is updated to a new version.

###

syn-python-selenium-2.1

**Major dependencies**:

- Python 3.8
- Selenium 4.15.1
- Chromium version 111.0.5563.146

**Changes in syn-python-selenium-2.1**:

- **Updated versions of the bundled libraries in Chromium**— The Chromium and
  Selenium dependencies are updated to new versions.

The following earlier runtime versions for Python and Selenium have been deprecated. For information about
runtime deprecation dates, see [CloudWatch Synthetics runtime deprecation dates](CloudWatch_Synthetics_Runtime_Support_Policy.md#runtime_deprecation_dates "CloudWatch_Synthetics_Runtime_Support_Policy.md#runtime_deprecation_dates").

###

syn-python-selenium-2.0

**Major dependencies**:

- Python 3.8
- Selenium 4.10.0
- Chromium version 111.0.5563.146

**Changes in syn-python-selenium-2.0**:

- **Updated dependencies**— The Chromium and
  Selenium dependencies are updated to new versions.

**Bug fixes in syn-python-selenium-2.0**:

- **Timestamp added**— A timestamp has been
  added to canary logs.
- **Session re-use**— A bug was fixed so that canaries
  are now prevented from reusing the session from their previous canary run.

###

syn-python-selenium-1.3

**Major dependencies**:

- Python 3.8
- Selenium 3.141.0
- Chromium version 92.0.4512.0

**Changes in syn-python-selenium-1.3**:

- **More precise timestamps**— The start time
  and stop time of canary runs are now precise to the millisecond.

###

syn-python-selenium-1.2

**Major dependencies**:

- Python 3.8
- Selenium 3.141.0
- Chromium version 92.0.4512.0

- **Updated dependencies**— The only
  new features in this runtime are the updated dependencies.

###

syn-python-selenium-1.1

**Major dependencies**:

- Python 3.8
- Selenium 3.141.0
- Chromium version 83.0.4103.0

**Features**:

- **Custom handler function**— You can now use a
  custom handler function for your canary scripts. Previous runtimes required the script entry point
  to include `.handler`.

You can also put canary scripts in any folder and pass the folder name as part of the handler. For
example, `MyFolder/MyScriptFile.functionname` can be used as an entry point.

- **Configuration options for adding metrics and step failure
  configurations**— These options were already available in runtimes for Node.js
  canaries. For more information, see
  [SyntheticsConfiguration class](CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_SyntheticsConfiguration_Python "CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_SyntheticsConfiguration_Python").
- **Custom arguments in Chrome** — You can now open a browser in incognito mode
  or pass in proxy server configuration.
  For more information, see
  [Chrome()](CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_Chrome "CloudWatch_Synthetics_Canaries_Library_Python.md#CloudWatch_Synthetics_Library_Python_Chrome").
- **Cross-Region artifact buckets**— A canary
  can store its artifacts in an Amazon S3 bucket in a different Region.
- **Bug fixes, including a fix for the `index.py`
  issue**— With previous runtimes, a canary file named `index.py` caused exceptions
  because it conflicted with the name of the library file. This issue is now fixed.

###

syn-python-selenium-1.0

**Major dependencies**:

- Python 3.8
- Selenium 3.141.0
- Chromium version 83.0.4103.0

**Features**:

- **Selenium support**— You can write canary scripts using
  the Selenium test framework. You can bring your Selenium scripts from elsewhere into
  CloudWatch Synthetics with minimal changes, and they will work with AWS services.
