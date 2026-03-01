# Synthetics runtime versions

When you create or update a canary, you choose a Synthetics runtime version for the canary.
A Synthetics runtime is a combination of the Synthetics code that calls your script handler,
and the Lambda layers of bundled dependencies.

CloudWatch Synthetics currently supports runtimes that use Node.js, Python, or Java languages. The frameworks supported are Puppeteer, Playwright, and Selenium.

We recommend that you always use the most recent runtime version for your canaries, to be
able to use the latest features and updates made to the Synthetics library.

**Please note**: whenever you run a canary to use the new version of the Synthetics runtime, all
Synthetics library functions that your canary uses are also automatically moved to the same version of
NodeJS that the Synthetics runtime supports.

###### Topics

- [Runtime versions using Java](CloudWatch_Synthetics_Library_Java.md "CloudWatch_Synthetics_Library_Java.md")
- [Runtime versions using Node.js and Playwright](CloudWatch_Synthetics_Library_nodejs_playwright.md "CloudWatch_Synthetics_Library_nodejs_playwright.md")
- [Runtime versions using Node.js and Puppeteer](CloudWatch_Synthetics_Library_nodejs_puppeteer.md "CloudWatch_Synthetics_Library_nodejs_puppeteer.md")
- [Runtime versions using Python and Selenium Webdriver](CloudWatch_Synthetics_Library_python_selenium.md "CloudWatch_Synthetics_Library_python_selenium.md")
- [Runtime versions using Node.js](CloudWatch_Synthetics_Library_Nodejs.md "CloudWatch_Synthetics_Library_Nodejs.md")
- [Runtime versions support policy](CloudWatch_Synthetics_Runtime_Support_Policy.md "CloudWatch_Synthetics_Runtime_Support_Policy.md")
- [Runtime versions update](CloudWatch_Synthetics_Runtime_Version_Update.md "CloudWatch_Synthetics_Runtime_Version_Update.md")
