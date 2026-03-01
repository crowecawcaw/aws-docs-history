# Setting up end-to-end Cypress tests for your Amplify application

You can run end-to-end (E2E) tests in the test phase of your Amplify app to catch
regressions before pushing code to production. The test phase can be configured in the build
specification YAML. Currently, you can run only the Cypress testing framework during a
build.

Cypress is a JavaScript-based testing framework that allows you to run E2E tests on a
browser. For a tutorial that demonstrates how to set up E2E tests, see the blog post [Running end-to-end Cypress tests for your fullstack CI/CD deployment with Amplify](https://aws.amazon.com/blogs/mobile/run-end-to-end-cypress-tests-for-your-fullstack-ci-cd-deployment-with-amplify-console/ "https://aws.amazon.com/blogs/mobile/run-end-to-end-cypress-tests-for-your-fullstack-ci-cd-deployment-with-amplify-console/").

## Adding Cypress tests to an existing Amplify application

You can add Cypress tests to an existing app by updating the app's build settings in the
Amplify console. The build specification YAML contains a collection of build commands and
related settings that Amplify uses to run your build. Use the `test` step to
run any test commands at build time. For E2E tests, Amplify Hosting offers a deeper
integration with Cypress that allows you to generate a UI report for your tests.

The following list describes the test settings and how
they are used.

**preTest**

Install the dependencies required to
run Cypress tests. Amplify Hosting uses [mochawesome](https://github.com/adamgruber/mochawesome "https://github.com/adamgruber/mochawesome") to generate a
report to view your test results and [wait-on](https://github.com/jeffbski/wait-on "https://github.com/jeffbski/wait-on") to set up the localhost server during the build.

**test**

Run cypress commands to perform tests using mochawesome.

**postTest**

The mochawesome report is generated from
the output JSON. Note that if you are using Yarn, you must run this command in silent mode to generate the mochawesome report. For Yarn, you can use the following command.

```
yarn run --silent mochawesome-merge cypress/report/mochawesome-report/mochawesome*.json > cypress/report/mochawesome.json

```

**artifacts>baseDirectory**
The directory from
which tests are run.

**artifacts>configFilePath**
The generated test report data.

**artifacts>files**
The generated artifacts
(screenshots and videos) available for download.

The following example excerpt from a build specification `amplify.yml` file shows how to add Cypress tests to your app.

```
test:
  phases:
    preTest:
      commands:
        - npm ci
        - npm install -g pm2
        - npm install -g wait-on
        - npm install mocha mochawesome mochawesome-merge mochawesome-report-generator
        - pm2 start npm -- start
        - wait-on http://localhost:3000
    test:
      commands:
        - 'npx cypress run --reporter mochawesome --reporter-options "reportDir=cypress/report/mochawesome-report,overwrite=false,html=false,json=true,timestamp=mmddyyyy_HHMMss"'
    postTest:
      commands:
        - npx mochawesome-merge cypress/report/mochawesome-report/mochawesome*.json > cypress/report/mochawesome.json
        - pm2 kill
  artifacts:
    baseDirectory: cypress
    configFilePath: '**/mochawesome.json'
    files:
      - '**/*.png'
      - '**/*.mp4'
```

## Turning off tests for an Amplify application or branch

After the test configuration has been added to your `amplify.yml`
build settings, the `test` step runs for every build, on every branch. If you
want to globally disable tests from running, or only run tests for specific branches, you
can use the USER_DISABLE_TESTS environment variable without modifying your
build settings.

To **globally** disable tests for all branches, add the
USER_DISABLE_TESTS environment variable with a value of `true`
for all branches. The following screenshot, shows the **Environment variables** section in the
Amplify console with tests disabled for all branches.

![The Environment variables section in the Amplify console.](images/amplify-disable-test-global.png)

To disable tests for a specific branch, add the
USER_DISABLE_TESTS environment variable with a value of `false` for all branches, and then
add an override for each branch you want to disable with a value of `true`. In the
following screenshot, tests are disabled on the _main_ branch, and enabled for every other
branch.

![The Environment variables section in the Amplify console.](images/amplify-disable-test-branch.png)

Disabling tests with this variable will cause the test step to be skipped altogether
during a build. To re-enable tests, set this value to `false`, or delete
the environment variable.
