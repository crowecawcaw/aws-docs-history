# Library functions available for canary scripts

CloudWatch Synthetics includes several built-in classes and functions that you can call when writing
Node.js scripts to use as canaries.

Some apply to both UI and API canaries. Others apply to UI canaries only. A UI canary
is a canary that uses the `getPage()` function and uses Puppeteer as a web driver
to navigate and interact with webpages.

###### Note

Whenever you upgrade a canary to use a new version of the the Synthetics runtime, all
Synthetics library functions that your canary uses are also automatically upgraded to the same version of
NodeJS that the Synthetics runtime supports.

###### Topics

- [Library functions available for Node.js canary](Library_function_Nodejs.md "Library_function_Nodejs.md")
- [Library functions available for Java canary](CloudWatch_Synthetics_Canaries_Java.md "CloudWatch_Synthetics_Canaries_Java.md")
- [Library functions available for Node.js canary scripts using Playwright](CloudWatch_Synthetics_Canaries_Nodejs_Playwright.md "CloudWatch_Synthetics_Canaries_Nodejs_Playwright.md")
- [Library functions available for Node.js canary scripts using Puppeteer](CloudWatch_Synthetics_Canaries_Library_Nodejs.md "CloudWatch_Synthetics_Canaries_Library_Nodejs.md")
- [Library functions available for Python canary scripts using Selenium](CloudWatch_Synthetics_Canaries_Library_Python.md "CloudWatch_Synthetics_Canaries_Library_Python.md")
