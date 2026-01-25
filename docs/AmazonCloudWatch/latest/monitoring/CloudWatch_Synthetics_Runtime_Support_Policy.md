# Runtime versions support policy

Synthetics runtime versions are subject to maintenance and security updates. When any
component of a runtime version is no longer supported, that
Synthetics runtime version is deprecated.

You can't create canaries using deprecated runtime versions. Canaries that use
deprecated runtimes continue to run. You can stop, start, and delete these canaries. You
can update an existing canary that uses a deprecated runtime version by updating the canary
to use a supported runtime version.

CloudWatch Synthetics notifies you by email if you have canaries that use runtimes that are scheduled to
be deprecated in the next 60 days. We recommend that you migrate your canaries to a supported runtime
version to benefit from the new functionality, security, and performance enhancements that are included in
more recent releases.

## CloudWatch Synthetics runtime deprecation dates

The following table lists the date of deprecation of each deprecated CloudWatch Synthetics runtime.

| Runtime Version            | Deprecation date  |
| -------------------------- | ----------------- |
| `syn-python-selenium-5.1`  | February 3, 2026  |
| `syn-python-selenium-5.0`  | February 3, 2026  |
| `syn-python-selenium-4.1`  | February 3, 2026  |
| `syn-python-selenium-4.0`  | February 3, 2026  |
| `syn-nodejs-puppeteer-7.0` | January 22, 2026  |
| `syn-nodejs-puppeteer-6.2` | January 22, 2026  |
| `syn-nodejs-puppeteer-5.2` | January 22, 2026  |
| `syn-python-selenium-3.0`  | January 22, 2026  |
| `syn-python-selenium-2.1`  | January 22, 2026  |
| `syn-nodejs-puppeteer-6.1` | March 8, 2024     |
| `syn-nodejs-puppeteer-6.0` | March 8, 2024     |
| `syn-nodejs-puppeteer-5.1` | March 8, 2024     |
| `syn-nodejs-puppeteer-5.0` | March 8, 2024     |
| `syn-nodejs-puppeteer-4.0` | March 8, 2024     |
| `syn-nodejs-puppeteer-3.9` | January 8, 2024   |
| `syn-nodejs-puppeteer-3.8` | January 8, 2024   |
| `syn-python-selenium-2.0`  | March 8, 2024     |
| `syn-python-selenium-1.3`  | March 8, 2024     |
| `syn-python-selenium-1.2`  | March 8, 2024     |
| `syn-python-selenium-1.1`  | March 8, 2024     |
| `syn-python-selenium-1.0`  | March 8, 2024     |
| `syn-nodejs-puppeteer-3.7` | January 8, 2024   |
| `syn-nodejs-puppeteer-3.6` | January 8, 2024   |
| `syn-nodejs-puppeteer-3.5` | January 8, 2024   |
| `syn-nodejs-puppeteer-3.4` | November 13, 2022 |
| `syn-nodejs-puppeteer-3.3` | November 13, 2022 |
| `syn-nodejs-puppeteer-3.2` | November 13, 2022 |
| `syn-nodejs-puppeteer-3.1` | November 13, 2022 |
| `syn-nodejs-puppeteer-3.0` | November 13, 2022 |
| `syn-nodejs-2.2`           | May 28, 2021      |
| `syn-nodejs-2.1`           | May 28, 2021      |
| `syn-nodejs-2.0`           | May 28, 2021      |
| `syn-nodejs-2.0-beta`      | February 8, 2021  |
| `syn-1.0`                  | May 28, 2021      |
