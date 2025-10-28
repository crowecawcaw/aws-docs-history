# Release: App Runner adds support for Python 3.11 and Node.js 18 on December 29, 2023

AWS App Runner now supports Python 3.11 and Node.js 18.

**Release date:** December 29, 2023

## Changes

AWS App Runner now supports the following runtime versions of Python and Node.js:

- Python 3.11 — For more information, see [Using the Python platform](../dg/service-source-code-python.md "../dg/service-source-code-python.md") in the _AWS App Runner Developer Guide_.
- Node.js 18 — For more information, see [Using the Node.js platform](../dg/service-source-code-nodejs.md "../dg/service-source-code-nodejs.md") in the
  _AWS App Runner Developer Guide_.

App Runner now offers an updated build process for specific runtimes. It will invoke the revised build process for the managed runtime versions in
this release: Python 3.11 and Node.js 18.

This revised build process is faster and more efficient. It also creates a final image with a smaller footprint that only contains your source code,
build artifacts, and runtimes needed to run your application.

For more information, see [Managed
runtime versions and the App Runner build](../dg/service-source-code.md#service-source-code.build-detail "../dg/service-source-code.md#service-source-code.build-detail") in the _AWS App Runner Developer Guide_.
