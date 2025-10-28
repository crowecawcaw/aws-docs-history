# Synthetics runtime versions

When you create or update a canary, you choose a Synthetics runtime version for the canary.
A Synthetics runtime is a combination of the Synthetics code that calls your script handler,
and the Lambda layers of bundled dependencies.

CloudWatch Synthetics currently supports runtimes that use Node.js, Python, or Java languages. The frameworks supported are Puppeteer, Playwright, and Selenium.

We recommend that you always use the most recent runtime version for your canaries, to be
able to use the latest features and updates made to the Synthetics library.

###### Note

Whenever you run a canary to use the new version of the Synthetics runtime, all
Synthetics library functions that your canary uses are also automatically moved to the same version of
NodeJS that the Synthetics runtime supports.

###### Topics

- [CloudWatch Synthetics runtime support policy](#CloudWatch_Synthetics_Canaries_runtime_support "#CloudWatch_Synthetics_Canaries_runtime_support")
- [Runtime versions using
  Java](CloudWatch_Synthetics_Library_Java.md "CloudWatch_Synthetics_Library_Java.md")
- [Runtime versions using
  Node.js and Playwright](CloudWatch_Synthetics_Library_nodejs_playwright.md "CloudWatch_Synthetics_Library_nodejs_playwright.md")
- [Runtime versions using Node.js
  and Puppeteer](CloudWatch_Synthetics_Library_nodejs_puppeteer.md "CloudWatch_Synthetics_Library_nodejs_puppeteer.md")
- [Runtime versions using Python
  and Selenium Webdriver](CloudWatch_Synthetics_Library_python_selenium.md "CloudWatch_Synthetics_Library_python_selenium.md")
- [Runtime versions using Node.js](CloudWatch_Synthetics_Library_Nodejs.md "CloudWatch_Synthetics_Library_Nodejs.md")

## CloudWatch Synthetics runtime support policy

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

**How do I update a canary to a new runtime version?**

You can update a canary’s runtime version by using the CloudWatch console, AWS CloudFormation, the AWS CLI or the AWS SDK.
When you use the CloudWatch console, you can update up to five canaries at once by selecting them in the
canary list page and then choosing **Actions**, **Update Runtime**.

You can verify the update by first testing your update before committing the runtime update. When updating the runtime versions, choose the **Start Dry Run** or **Validate and save later** options in the CloudWatch console to create a
dry run of the original canary along with any changes you made to the configuration. The dry run will update and execute the canary to validate whether the runtime update is safe for the canary.
Once you have verified your canary with the new runtime version, you can update the runtime version of your canary. For more information, see [Performing safe canary updates](performing-safe-canary-upgrades.md "performing-safe-canary-upgrades.md").

Alternatively, you can verify the update by first cloning the canary using the CloudWatch console and updating the runtime version. This creates another canary which is a clone of your original canary.
Once you have verified your canary with the new runtime version, you can update the runtime version of your original canary and delete the clone canary.

You can also update multiple canaries using an upgrade script.
For more information, see [Canary runtime upgrade script](#CloudWatch_Synthetics_Canaries_upgrade_script "#CloudWatch_Synthetics_Canaries_upgrade_script").

If you upgrade a canary and it fails, see
[Troubleshooting a failed canary](CloudWatch_Synthetics_Canaries_Troubleshoot.md "CloudWatch_Synthetics_Canaries_Troubleshoot.md").

### CloudWatch Synthetics runtime deprecation dates

The following table lists the date of deprecation of each deprecated CloudWatch Synthetics runtime.

| Runtime Version            | Deprecation date  |
| -------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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
| `syn-1.0`                  | May 28, 2021      | ### Canary runtime upgrade script To upgrade a canary script to a supported runtime version, use the following script. ``` const AWS = require('aws-sdk'); // You need to configure your AWS credentials and Region. //   https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html //   https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-region.html const synthetics = new AWS.Synthetics(); const DEFAULT_OPTIONS = { /** <br>• The number of canaries to upgrade during a single run of this script. */ count: 10, /** <br>• No canaries are upgraded unless force is specified. */ force: false }; /** <br>• The number of milliseconds to sleep between GetCanary calls when <br>• verifying that an update succeeded. */ const SLEEP_TIME = 5000; (async () => { try { const options = getOptions(); const versions = await getRuntimeVersions(); const canaries = await getAllCanaries(); const upgrades = canaries .filter(canary => !versions.isLatestVersion(canary.RuntimeVersion)) .map(canary => { return { Name: canary.Name, FromVersion: canary.RuntimeVersion, ToVersion: versions.getLatestVersion(canary.RuntimeVersion) }; }); if (options.force) { const promises = []; for (const upgrade of upgrades.slice(0, options.count)) { const promise = upgradeCanary(upgrade); promises.push(promise); // Sleep for 100 milliseconds to avoid throttling. await usleep(100); } const succeeded = []; const failed = []; for (let i = 0; i < upgrades.slice(0, options.count).length; i++) { const upgrade = upgrades[i]; const promise = promises[i]; try { await promise; console.log(`The update of ${upgrade.Name} succeeded.`); succeeded.push(upgrade.Name); } catch (e) { console.log(`The update of ${upgrade.Name} failed with error: ${e}`); failed.push({ Name: upgrade.Name, Reason: e }); } } if (succeeded.length) { console.group('The following canaries were upgraded successfully.'); for (const name of succeeded) { console.log(name); } console.groupEnd() } else { console.log('No canaries were upgraded successfully.'); } if (failed.length) { console.group('The following canaries were not upgraded successfully.'); for (const failure of failed) { console.log('\x1b[31m', `${failure.Name}: ${failure.Reason}`, '\x1b[0m'); } console.groupEnd(); } } else { console.log('Run with --force [--count <count>] to perform the first <count> upgrades shown. The default value of <count> is 10.') console.table(upgrades); } } catch (e) { console.error(e); } })(); function getOptions() { const force = getFlag('--force', DEFAULT_OPTIONS.force); const count = getOption('--count', DEFAULT_OPTIONS.count); return { force, count }; function getFlag(key, defaultValue) { return process.argv.includes(key) |     | defaultValue; } function getOption(key, defaultValue) { const index = process.argv.indexOf(key); if (index < 0) { return defaultValue; } const value = process.argv[index + 1]; if (typeof value === 'undefined' |     | value.startsWith('-')) { throw `The ${key} option requires a value.`; } return value; } } function getAllCanaries() { return new Promise((resolve, reject) => { const canaries = []; synthetics.describeCanaries().eachPage((err, data) => { if (err) { reject(err); } else { if (data === null) { resolve(canaries); } else { canaries.push(...data.Canaries); } } }); }); } function getRuntimeVersions() { return new Promise((resolve, reject) => { const jsVersions = []; const pythonVersions = []; synthetics.describeRuntimeVersions().eachPage((err, data) => { if (err) { reject(err); } else { if (data === null) { jsVersions.sort((a, b) => a.ReleaseDate - b.ReleaseDate); pythonVersions.sort((a, b) => a.ReleaseDate - b.ReleaseDate); resolve({ isLatestVersion(version) { const latest = this.getLatestVersion(version); return latest === version; }, getLatestVersion(version) { if (jsVersions.some(v => v.VersionName === version)) { return jsVersions[jsVersions.length - 1].VersionName; } else if (pythonVersions.some(v => v.VersionName === version)) { return pythonVersions[pythonVersions.length - 1].VersionName; } else { throw Error(`Unknown version ${version}`); } } }); } else { for (const version of data.RuntimeVersions) { if (version.VersionName === 'syn-1.0') { jsVersions.push(version); } else if (version.VersionName.startsWith('syn-nodejs-2.')) { jsVersions.push(version); } else if (version.VersionName.startsWith('syn-nodejs-puppeteer-')) { jsVersions.push(version); } else if (version.VersionName.startsWith('syn-python-selenium-')) { pythonVersions.push(version); } else { throw Error(`Unknown version ${version.VersionName}`); } } } } }); }); } async function upgradeCanary(upgrade) { console.log(`Upgrading canary ${upgrade.Name} from ${upgrade.FromVersion} to ${upgrade.ToVersion}`); await synthetics.updateCanary({ Name: upgrade.Name, RuntimeVersion: upgrade.ToVersion }).promise(); while (true) { await usleep(SLEEP_TIME); console.log(`Getting the state of canary ${upgrade.Name}`); const response = await synthetics.getCanary({ Name: upgrade.Name }).promise(); const state = response.Canary.Status.State; console.log(`The state of canary ${upgrade.Name} is ${state}`); if (state === 'ERROR' |     | response.Canary.Status.StateReason) { throw response.Canary.Status.StateReason; } if (state !== 'UPDATING') { return; } } } function usleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); } ``` |
