# Sample code for canary scripts

This section contains code samples that illustrate some possible functions for
 CloudWatch Synthetics canary scripts.


## Samples for Node.js and Playwright


### Playwright canary
 with multiple steps


The following script is an example of a Node.js Playwright canary with multiple
 steps.



```
import { synthetics } from '@amzn/synthetics-playwright';

export async function handler(event, context) {
  try {
    console.log('Running Synthetics Playwright canary');
    const browser = await synthetics.launch();
    const browserContext = await browser.newContext();
    const page = await synthetics.getPage(browserContext);
    

    // Add steps
    // Step 1
    await synthetics.executeStep("home-page", async () => {
      console.log("Verify home page loads")
      await page.goto('https://www.amazon.com', {waitUntil: "load"});
      await new Promise(r => setTimeout(r, 5000));
    });
    
    // Step 2
    await synthetics.executeStep("search", async () => {
      console.log("Searching for a product")
      const searchInput = page.getByPlaceholder("Search Amazon").first();
      await searchInput.click()
      await searchInput.fill('Amazon echo');
      const btn = page.getByRole('button', { name: 'Go' }).first()
      await btn.click({ timeout: 15000 })
      console.log("Clicked search button")
    });

    // Step 3
    await synthetics.executeStep("search-results", async () => {
      console.log("Verifying search results")
      const resultsHeading = page.getByText("Results", {exact: true}).first()
      await resultsHeading.highlight();
      await new Promise(r => setTimeout(r, 5000));
    });

  } finally {
    // Close all browser contexts and browser
    await synthetics.close();
  }
}
```

### Playwright canaries
 setting cookies


The following script is an example of a Node.js Playwright canary setting three
 cookies.



```
import { synthetics } from '@amzn/synthetics-playwright';

export const handler = async (event, context) => {
  try {
    let url = "http://smile.amazon.com/";
    const browser = await synthetics.launch();
    const page = await synthetics.getPage(browser);
    const cookies = [{
        'name': 'cookie1',
        'value': 'val1',
        'url': url
    },
    {
        'name': 'cookie2',
        'value': 'val2',
        'url': url
    },
    {
        'name': 'cookie3',
        'value': 'val3',
        'url': url
    }
   ];
   await page.context().addCookies(cookies);
   await page.goto(url, {waitUntil: 'load', timeout: 30000});
   await page.screenshot({ path: '/tmp/smile.png' });
    
  } finally {
    await synthetics.close();
  }
};
```

## Samples
 for Node.js and Puppeteer


### Setting cookies


Web sites rely on cookies to provide custom functionality or track users. By setting 
 cookies in CloudWatch Synthetics scripts, you can mimic this custom behavior and validate it.


For example, a web site might display a **Login** link for a revisiting user
 instead of a **Register** link.



```
var synthetics = require('Synthetics');
const log = require('SyntheticsLogger');

const pageLoadBlueprint = async function () {

    let url = "http://smile.amazon.com/";

    let page = await synthetics.getPage();

    // Set cookies.  I found that name, value, and either url or domain are required fields.
    const cookies = [{
      'name': 'cookie1',
      'value': 'val1',
      'url': url
    },{
      'name': 'cookie2',
      'value': 'val2',
      'url': url
    },{
      'name': 'cookie3',
      'value': 'val3',
      'url': url
    }];
    
    await page.setCookie(...cookies);

    // Navigate to the url
    await synthetics.executeStep('pageLoaded_home', async function (timeoutInMillis = 30000) {
        
        var response = await page.goto(url, {waitUntil: ['load', 'networkidle0'], timeout: timeoutInMillis});

        // Log cookies for this page and this url
        const cookiesSet = await page.cookies(url);
        log.info("Cookies for url: " + url + " are set to: " + JSON.stringify(cookiesSet));
    });

};

exports.handler = async () => {
    return await pageLoadBlueprint();
};
```

### Device emulation


You can write scripts that emulate various devices so that you can approximate how a
 page looks and behaves on those devices.


The following sample emulates an iPhone 6 device. For more information about emulation, 
 see [page.emulate(options)](https://pptr.dev/#?product=Puppeteer&version=v5.3.1&show=api-pageemulateoptions "https://pptr.dev/#?product=Puppeteer&version=v5.3.1&show=api-pageemulateoptions") in the Puppeteer documentation.



```
var synthetics = require('Synthetics');
const log = require('SyntheticsLogger');
const puppeteer = require('puppeteer-core');

const pageLoadBlueprint = async function () {
    
    const iPhone = puppeteer.devices['iPhone 6'];

    // INSERT URL here
    const URL = "https://amazon.com";

    let page = await synthetics.getPage();
    await page.emulate(iPhone);

    //You can customize the wait condition here. For instance,
    //using 'networkidle2' may be less restrictive.
    const response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});
    if (!response) {
        throw "Failed to load page!";
    }
    
    await page.waitFor(15000);

    await synthetics.takeScreenshot('loaded', 'loaded');
    
    //If the response status code is not a 2xx success code
    if (response.status() < 200 || response.status() > 299) {
        throw "Failed to load page!";
    }
};

exports.handler = async () => {
    return await pageLoadBlueprint();
};
```

### Multi-step API canary


This sample code demonstrates an API canary with two HTTP steps: testing the same API 
 for positive and negative test cases. The step configuration is passed to enable 
 reporting of request/response headers. Additionally, it hides the Authorization header and
 X-Amz-Security-Token, because they contain user credentials. 
 


When this script is used as a canary, you can view details about each step and 
 the associated HTTP requests such as step pass/fail, duration, and performance metrics 
 like DNS look up time and first byte time. You can view the number of 2xx, 4xx and 5xx 
 for your canary run.
 



```

var synthetics = require('Synthetics');
const log = require('SyntheticsLogger');

const apiCanaryBlueprint = async function () {
    
    // Handle validation for positive scenario
    const validatePositiveCase = async function(res) {
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
    
    // Handle validation for negative scenario
    const validateNegativeCase = async function(res) {
        return new Promise((resolve, reject) => {
            if (res.statusCode < 400) {
                throw res.statusCode + ' ' + res.statusMessage;
            }
            
            resolve();
        });
    };
    
    let requestOptionsStep1 = {
        'hostname': 'myproductsEndpoint.com',
        'method': 'GET',
        'path': '/test/product/validProductName',
        'port': 443,
        'protocol': 'https:'
    };
    
    let headers = {};
    headers['User-Agent'] = [synthetics.getCanaryUserAgentString(), headers['User-Agent']].join(' ');
    
    requestOptionsStep1['headers'] = headers;

    // By default headers, post data and response body are not included in the report for security reasons. 
    // Change the configuration at global level or add as step configuration for individual steps
    let stepConfig = {
        includeRequestHeaders: true, 
        includeResponseHeaders: true,
        restrictedHeaders: ['X-Amz-Security-Token', 'Authorization'], // Restricted header values do not appear in report generated.
        includeRequestBody: true,
        includeResponseBody: true
    };
       

    await synthetics.executeHttpStep('Verify GET products API with valid name', requestOptionsStep1, validatePositiveCase, stepConfig);
    
    let requestOptionsStep2 = {
        'hostname': 'myproductsEndpoint.com',
        'method': 'GET',
        'path': '/test/canary/InvalidName(',
        'port': 443,
        'protocol': 'https:'
    };
    
    headers = {};
    headers['User-Agent'] = [synthetics.getCanaryUserAgentString(), headers['User-Agent']].join(' ');
    
    requestOptionsStep2['headers'] = headers;

    // By default headers, post data and response body are not included in the report for security reasons. 
    // Change the configuration at global level or add as step configuration for individual steps
    stepConfig = {
        includeRequestHeaders: true, 
        includeResponseHeaders: true,
        restrictedHeaders: ['X-Amz-Security-Token', 'Authorization'], // Restricted header values do not appear in report generated.
        includeRequestBody: true,
        includeResponseBody: true
    };
    
    await synthetics.executeHttpStep('Verify GET products API with invalid name', requestOptionsStep2, validateNegativeCase, stepConfig);
    
};

exports.handler = async () => {
    return await apiCanaryBlueprint();
};
```

## Samples
 for Python and Selenium


The following sample Selenium code is a canary that fails with a custom error
 message when a target element is not loaded.



```
from aws_synthetics.selenium import synthetics_webdriver as webdriver
from aws_synthetics.common import synthetics_logger as logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def custom_selenium_script():
    # create a browser instance
    browser = webdriver.Chrome()
    browser.get('https://www.example.com/')
    logger.info('navigated to home page')
    # set cookie
    browser.add_cookie({'name': 'foo', 'value': 'bar'})
    browser.get('https://www.example.com/')
    # save screenshot
    browser.save_screenshot('signed.png')
    # expected status of an element
    button_condition = EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-button'))
    # add custom error message on failure
    WebDriverWait(browser, 5).until(button_condition, message='Submit button failed to load').click()
    logger.info('Submit button loaded successfully')
    # browser will be quit automatically at the end of canary run, 
    # quit action is not necessary in the canary script
    browser.quit()

# entry point for the canary
def handler(event, context):
    return custom_selenium_script()
```
