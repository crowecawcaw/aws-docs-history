

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support for Python 3.11 and Node.js 18 on December 29, 2023
<a name="release-2023-12-29-python-node-prebuild"></a>

AWS App Runner now supports Python 3.11 and Node.js 18.

**Release date:** December 29, 2023

## Changes
<a name="release-2023-12-29-python-node-prebuild.changes"></a>

AWS App Runner now supports the following runtime versions of Python and Node.js:
+ **Python 3.11** — For more information, see [Using the Python platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python.html) in the *AWS App Runner Developer Guide*. 
+ **Node.js 18** — For more information, see [Using the Node.js platform](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs.html) in the *AWS App Runner Developer Guide*.

App Runner now offers an updated build process for specific runtimes. It will invoke the revised build process for the managed runtime versions in this release: Python 3.11 and Node.js 18.

This revised build process is faster and more efficient. It also creates a final image with a smaller footprint that only contains your source code, build artifacts, and runtimes needed to run your application.

For more information, see [ Managed runtime versions and the App Runner build](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.build-detail) in the *AWS App Runner Developer Guide*.