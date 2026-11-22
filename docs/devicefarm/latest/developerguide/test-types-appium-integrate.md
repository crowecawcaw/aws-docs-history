

# Integrating Appium tests with Device Farm

Use the following instructions to integrate Appium tests with AWS Device Farm. For more information about using Appium tests in Device Farm, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Configure Appium test reports using a custom test environment
<a name="test-types-appium-generate-reports"></a>

Any test report that your tests write to `$DEVICEFARM_LOG_DIR` in your test spec YAML file is available in your test output artifacts after the run completes. By default, Device Farm also generates its own test report, called test insights. Test insights give you a per-test breakdown of results, durations, and stack traces for failures. You can view test insights in the console, and through the AWS CLI and APIs. Test insights are in addition to the artifacts that your tests produce, not a replacement for them.

Web app tests use the same report as mobile app tests, so this section applies to both.

Before you begin, make sure that your run meets the following requirements:
+ Your run uses a custom test environment. Device Farm does not generate test insights in the standard test environment. For more information, see [Test environments in AWS Device Farm](test-environments.md).
+ Your run uses an Appium framework other than Ruby. Device Farm does not generate test insights for Ruby tests. If you set `insightsTypes` to `TEST_REPORT` for a Ruby run, `ScheduleRun` returns an [`ArgumentException`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRun.html#API_ScheduleRun_Errors).

To configure test reports for your Appium tests:

1. Configure your tests to write a results file that Device Farm can read. Choose your framework tab to see which file to produce.

------
#### [ Java (JUnit) ]

   Device Farm reads every JUnit XML report that your tests write under `$DEVICEFARM_LOG_DIR`. It does not read reports stored anywhere else. It accepts reports from the JUnit Platform Console Launcher, Maven Surefire, and Gradle. It supports JUnit 5 tests, and JUnit 4 tests that run on the JUnit Vintage engine. The default Appium Java JUnit test spec produces and stores the reports. If you use the default test spec, you don't need to change anything.

   If you replace the default test command in your test spec file, set up the reports in one of the following ways. We recommend Option 1, because it records a start and end time for each test. You need the start times to get per-test video. JUnit XML reports don't include per-test timestamps. For more information, see [Per-test video](reports.md#reports-test-insights-video).

Option 1: Console Launcher with open test reporting (recommended)  
In the `test` phase of your test spec file, run the Console Launcher with the report directory and the open test reporting flag. Open test reporting requires JUnit Platform 1.9 or later, with `junit-platform-reporting` on the classpath. The following command runs the tests in a package with open test reporting enabled:  

   ```bash
   java -cp "$DEVICEFARM_TEST_PACKAGE_PATH/*:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*" \
     org.junit.platform.console.ConsoleLauncher \
     --config=junit.platform.reporting.open.xml.enabled=true \
     --select-package {{com.example.tests}} \
     --reports-dir "$DEVICEFARM_LOG_DIR/test-output"
   ```
This writes an `open-test-report.xml` file to the report directory. Device Farm uses this file when it contains results.

Option 2: Console Launcher with JUnit XML reports only  
In the `test` phase of your test spec file, run the Console Launcher with the report directory, as in the following command. The test report has durations but no per-test start or end times, so you don't get per-test video.  

   ```bash
   java -cp "$DEVICEFARM_TEST_PACKAGE_PATH/*:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*" \
     org.junit.platform.console.ConsoleLauncher \
     --select-package {{com.example.tests}} \
     --reports-dir "$DEVICEFARM_LOG_DIR/test-output"
   ```

Option 3: Maven or Gradle  
The build tool writes its reports to its own directory: `target/surefire-reports` for Maven and `build/test-results/test` for Gradle. Copy the reports into `$DEVICEFARM_LOG_DIR` in the `post_test` phase of your test spec file. Device Farm reads only what that directory contains.  
To record per-test timestamps, export `JAVA_TOOL_OPTIONS` in the `test` phase of your test spec file before your build command. The value enables open test reporting and points its output directory at `$DEVICEFARM_LOG_DIR`:  

   ```yaml
   phases:
     test:
       commands:
         - export JAVA_TOOL_OPTIONS="-Djunit.platform.reporting.open.xml.enabled=true -Djunit.platform.reporting.output.dir=$DEVICEFARM_LOG_DIR/test-output"
         - {{your build command}}
   ```

   If Device Farm does not generate a report for your run, see [Troubleshooting test reports and insights in AWS Device Farm](troubleshooting-test-insights.md).

------
#### [ Java (TestNG) ]

   TestNG writes its results as an XML report named `testng-results.xml`. Device Farm reads that report to build your test insights, so your tests must write it to `$DEVICEFARM_LOG_DIR`. Device Farm accepts a file named `testng-results.xml`, or any XML file in that directory that has the TestNG root element.

   The default Appium Java TestNG test spec produces and stores this report if you keep the default configuration, so most customers do not need to change anything. The report records a start time for each test, so you also get per-test video. If you run TestNG yourself in your test spec file, set its output directory to `$DEVICEFARM_LOG_DIR`, as in the following example:

   ```bash
   java org.testng.TestNG -d $DEVICEFARM_LOG_DIR/test-output testng.xml
   ```

   If your build tool writes the report somewhere else, copy it into `$DEVICEFARM_LOG_DIR` in the `post_test` phase of your test spec file. Device Farm reads only what that directory contains.

   The report must be well-formed XML in the standard TestNG report format.

------
#### [ Node.JS ]

   Device Farm reads the output of a [WebdriverIO](https://webdriver.io/) reporter. If you run your tests with WebdriverIO, enable one of the following reporters:
   + [@wdio/json-reporter](https://webdriver.io/docs/json-reporter/). Records test names, results, durations, stack traces, and a start and end time for each test. This is the recommended reporter, and the only one that gives you per-test video.
   + [@wdio/junit-reporter](https://webdriver.io/docs/junit-reporter/). Records test names, results, durations, and stack traces, but no per-test start or end times, so you don't get per-test video. If you enable both reporters, Device Farm builds the report from the JSON output.

   Install the reporter that you chose so that it is available inside your test package:

   ```bash
   npm install --save-dev @wdio/json-reporter
   ```

   Next, add the reporter to the `reporters` array in your `wdio.conf.js` file and set its `outputDir` to a directory under `$DEVICEFARM_LOG_DIR`:

   ```javascript
   exports.config = {
     // ...
     reporters: [
       ['json', { outputDir: `${process.env.DEVICEFARM_LOG_DIR}/wdio-reports` }]
     ]
   }
   ```

   Keep the default file name that the reporter produces. Device Farm reads only files that end in `.json` for the JSON reporter, or `.xml` or `.log` for the JUnit reporter. The `spec` reporter writes to the console only, so it produces no file for Device Farm to read.

   Install the reporter and update `wdio.conf.js` before you package your tests so that both are inside the package that you upload. For more information, see [Create a zipped test package file](#test-types-appium-create-a-zip).

   If Device Farm does not generate a report for your run, see [Troubleshooting test reports and insights in AWS Device Farm](troubleshooting-test-insights.md).

------
#### [ Python ]

   Device Farm reads the JUnit XML report that pytest writes when you run it with the `--junit-xml` option. The default Appium Python test spec already does this. If you use it, you don't need to change anything. If you use your own test spec file, follow these steps.

   1. In the `test` phase of your test spec file, run pytest with `--junit-xml` and write the report to a file under `$DEVICEFARM_LOG_DIR`:

      ```yaml
      phases:
        test:
          commands:
            - python -m pytest tests/ --junit-xml $DEVICEFARM_LOG_DIR/junitreport.xml
      ```

      Device Farm finds the report by its content, not by its name. It reads any file under `$DEVICEFARM_LOG_DIR` whose name ends in `.xml` and that is a JUnit XML report.

   1. If your test spec file runs pytest more than once, for example to retry failed tests, write each run to its own file. For example, use `junitreport-1.xml` and `junitreport-2.xml`. If two runs write to the same file, only the last run is reported.

   1. (Optional) To record a start and end time for each test, and get per-test video, save the following code as `conftest.py` in your `tests` directory. If you already have a `conftest.py` file, add the code to it. pytest does not record these times, so without this code the report has no `startTimestamp` or `endTimestamp` field.

      ```python
      import datetime
      
      import pytest
      
      
      def _utc(epoch):
          return datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).isoformat()
      
      
      @pytest.hookimpl(hookwrapper=True)
      def pytest_runtest_makereport(item, call):
          outcome = yield
          if call.when == "setup":
              item.devicefarm_start = call.start
          elif call.when == "teardown":
              report = outcome.get_result()
              start = getattr(item, "devicefarm_start", call.start)
              report.user_properties.append(("start_timestamp", _utc(start)))
              report.user_properties.append(("end_timestamp", _utc(call.stop)))
      ```

      pytest loads `conftest.py` automatically. The code records a start and end time for every test that pytest runs, including tests that are skipped or that fail during setup. The times cover the test's setup, the test itself, and its teardown.

   1. If you added `conftest.py`, package your tests after you add it, so that the file is in the package that you upload. For more information, see [Create a zipped test package file](#test-types-appium-create-a-zip).

   If Device Farm does not generate a report for your run, see [Troubleshooting test reports and insights in AWS Device Farm](troubleshooting-test-insights.md).

------

1. Schedule the run in a custom test environment. Test insights are on by default. If you don't set the `insightsTypes` field of the `configuration` parameter of your `ScheduleRun` request, Device Farm sets it to `TEST_REPORT`. To turn off test insights for a run, see [Creating a test run in Device Farm](how-to-create-test-run.md).

To view the report after the run completes, see [View a test report](#test-types-appium-view-insights).

## Configure your Appium test package
<a name="test-types-appium-prepare"></a>

Use the following instructions to configure your test package.

------
#### [ Java (JUnit) ]

1. Modify `pom.xml` to set packaging to a JAR file:

   ```
   <groupId>com.acme</groupId>
   <artifactId>acme-myApp-appium</artifactId>
   <version>1.0-SNAPSHOT</version>
   <packaging>jar</packaging>
   ```

1. Modify `pom.xml` to use `maven-jar-plugin` to build your tests into a JAR file.

   The following plugin builds your test source code (anything in the `src/test` directory) into a JAR file:

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-jar-plugin</artifactId>
     <version>2.6</version>
     <executions>
       <execution>
         <goals>
           <goal>test-jar</goal>
         </goals>
       </execution>
     </executions>
   </plugin>
   ```

1. Modify `pom.xml` to use `maven-dependency-plugin` to build dependencies as JAR files.

   The following plugin copies your dependencies into the `dependency-jars` directory: 

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-dependency-plugin</artifactId>
     <version>2.10</version>
     <executions>
       <execution>
         <id>copy-dependencies</id>
         <phase>package</phase>
         <goals>
           <goal>copy-dependencies</goal>
         </goals>
         <configuration>
           <outputDirectory>${project.build.directory}/dependency-jars/</outputDirectory>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

1. Save the following XML assembly to `src/main/assembly/zip.xml`.

   The following XML is an assembly definition that, when configured, instructs Maven to build a .zip file that contains everything in the root of your build output directory and the `dependency-jars` directory: 

   ```
   <assembly
       xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0 http://maven.apache.org/xsd/assembly-1.1.0.xsd">
     <id>zip</id>
     <formats>
       <format>zip</format>
     </formats>
     <includeBaseDirectory>false</includeBaseDirectory>
     <fileSets>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>*.jar</include>
         </includes>
       </fileSet>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>/dependency-jars/</include>
         </includes>
       </fileSet>
     </fileSets>
   </assembly>
   ```

1. Modify `pom.xml` to use `maven-assembly-plugin` to package tests and all dependencies into a single .zip file.

   The following plugin uses the preceding assembly to create a .zip file named `zip-with-dependencies` in the build output directory every time **mvn package** is run: 

   ```
   <plugin>
     <artifactId>maven-assembly-plugin</artifactId>
     <version>2.5.4</version>
     <executions>
       <execution>
         <phase>package</phase>
         <goals>
           <goal>single</goal>
         </goals>
         <configuration>
           <finalName>zip-with-dependencies</finalName>
           <appendAssemblyId>false</appendAssemblyId>
           <descriptors>
             <descriptor>src/main/assembly/zip.xml</descriptor>
           </descriptors>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

**Note**  
If you receive an error that says annotation is not supported in 1.3, add the following to `pom.xml`:  

```
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.7</source>
    <target>1.7</target>
  </configuration>
</plugin>
```

------
#### [ Java (TestNG) ]

1. Modify `pom.xml` to set packaging to a JAR file:

   ```
   <groupId>com.acme</groupId>
   <artifactId>acme-myApp-appium</artifactId>
   <version>1.0-SNAPSHOT</version>
   <packaging>jar</packaging>
   ```

1. Modify `pom.xml` to use `maven-jar-plugin` to build your tests into a JAR file.

   The following plugin builds your test source code (anything in the `src/test` directory) into a JAR file:

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-jar-plugin</artifactId>
     <version>2.6</version>
     <executions>
       <execution>
         <goals>
           <goal>test-jar</goal>
         </goals>
       </execution>
     </executions>
   </plugin>
   ```

1. Modify `pom.xml` to use `maven-dependency-plugin` to build dependencies as JAR files.

   The following plugin copies your dependencies into the `dependency-jars` directory: 

   ```
   <plugin>
     <groupId>org.apache.maven.plugins</groupId>
     <artifactId>maven-dependency-plugin</artifactId>
     <version>2.10</version>
     <executions>
       <execution>
         <id>copy-dependencies</id>
         <phase>package</phase>
         <goals>
           <goal>copy-dependencies</goal>
         </goals>
         <configuration>
           <outputDirectory>${project.build.directory}/dependency-jars/</outputDirectory>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

1. Save the following XML assembly to `src/main/assembly/zip.xml`.

   The following XML is an assembly definition that, when configured, instructs Maven to build a .zip file that contains everything in the root of your build output directory and the `dependency-jars` directory: 

   ```
   <assembly
       xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0 http://maven.apache.org/xsd/assembly-1.1.0.xsd">
     <id>zip</id>
     <formats>
       <format>zip</format>
     </formats>
     <includeBaseDirectory>false</includeBaseDirectory>
     <fileSets>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>*.jar</include>
         </includes>
       </fileSet>
       <fileSet>
         <directory>${project.build.directory}</directory>
         <outputDirectory>./</outputDirectory>
         <includes>
           <include>/dependency-jars/</include>
         </includes>
       </fileSet>
     </fileSets>
   </assembly>
   ```

1. Modify `pom.xml` to use `maven-assembly-plugin` to package tests and all dependencies into a single .zip file.

   The following plugin uses the preceding assembly to create a .zip file named `zip-with-dependencies` in the build output directory every time **mvn package** is run: 

   ```
   <plugin>
     <artifactId>maven-assembly-plugin</artifactId>
     <version>2.5.4</version>
     <executions>
       <execution>
         <phase>package</phase>
         <goals>
           <goal>single</goal>
         </goals>
         <configuration>
           <finalName>zip-with-dependencies</finalName>
           <appendAssemblyId>false</appendAssemblyId>
           <descriptors>
             <descriptor>src/main/assembly/zip.xml</descriptor>
           </descriptors>
         </configuration>
       </execution>
     </executions>
   </plugin>
   ```

**Note**  
If you receive an error that says annotation is not supported in 1.3, add the following to `pom.xml`:  

```
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.7</source>
    <target>1.7</target>
  </configuration>
</plugin>
```

------
#### [ Node.JS ]

To package your Appium Node.js tests and upload them to Device Farm, you must install the following on your local machine:
+ [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) 

  Use this tool when you develop and package your tests so that unnecessary dependencies are not included in your test package.
+ Node.js
+ npm-bundle (installed globally)

1. Verify that nvm is present

   ```bash
   command -v nvm
   ```

   You should see `nvm` as output.

   For more information, see [nvm](https://github.com/nvm-sh/nvm) on GitHub.

1. Run this command to install Node.js:

   ```bash
   nvm install node
   ```

   You can specify a particular version of Node.js:

   ```bash
   nvm install 11.4.0
   ```

1. Verify that the correct version of Node is in use:

   ```bash
   node -v
   ```

1. Install **npm-bundle** globally:

   ```bash
   npm install -g npm-bundle
   ```

------
#### [ Python ]

1. We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for developing and packaging tests so that unnecessary dependencies are not included in your app package.

   ```
   $ virtualenv workspace
   $ cd workspace
   $ source bin/activate
   ```
**Tip**  
Do not create a Python virtualenv with the `--system-site-packages` option, because it inherits packages from your global site-packages directory. This can result in including dependencies in your virtual environment that are not required by your tests.
You should also verify that your tests do not use dependencies that are dependent on native libraries, because these native libraries might not be present on the instance where these tests run.

1. Install **py.test** in your virtual environment.

   ```
   $ pip install pytest
   ```

1. Install the Appium Python client in your virtual environment.

   ```
   $ pip install Appium-Python-Client
   ```

1. Unless you specify a different path in custom mode, Device Farm expects your tests to be stored in `tests/`. You can use `find` to show all files inside a folder:

   ```
   $ find tests/
   ```

   Confirm that these files contain test suites you wand to run on Device Farm

   ```
   tests/
   tests/{{my-first-tests.py}}
   tests/{{my-second-tests/py}}
   ```

1. Run this command from your virtual environment workspace folder to show a list of your tests without running them.

   ```
   $ py.test --collect-only tests/
   ```

   Confirm the output shows the tests that you want to run on Device Farm.

1. Clean all cached files under your tests/ folder:

   ```
   $ find . -name '__pycache__' -type d -exec rm -r {} +
   $ find . -name '*.pyc' -exec rm -f {} +
   $ find . -name '*.pyo' -exec rm -f {} +
   $ find . -name '*~' -exec rm -f {} +
   ```

1. Run the following command in your workspace to generate the requirements.txt file:

   ```
   $ pip freeze > requirements.txt
   ```

------
#### [ Ruby ]

To package your Appium Ruby tests and upload them to Device Farm, you must install the following on your local machine:
+ [Ruby Version Manager (RVM)](https://rvm.io/rvm/install)

  Use this command-line tool when you develop and package your tests so that unnecessary dependencies are not included in your test package. 
+ Ruby
+ Bundler (This gem is typically installed with Ruby.)

1. Install the required keys, RVM, and Ruby. For instructions, see [Installing RVM](https://rvm.io/rvm/install) on the RVM website.

   After the installation is complete, reload your terminal by signing out and then signing in again.
**Note**  
RVM is loaded as a function for the bash shell only.

1. Verify that **rvm** is installed correctly

   ```bash
   command -v rvm
   ```

   You should see `rvm` as output.

1. If you want to install a specific version of Ruby, such as {{2.5.3}}, run the following command:

   ```bash
   rvm install ruby 2.5.3 --autolibs=0
   ```

   Verify that you are on the requested version of Ruby:

   ```bash
   ruby -v
   ```

1. Configure the bundler to compile packages for your desired testing platforms:

   ```
   bundle config specific_platform true
   ```

1. Update your .lock file to add the platforms needed to run tests.
   + If you're compiling tests to run on Android devices, then run this command to configure the Gemfile to use dependencies for the Android test host:

     ```
     bundle lock --add-platform x86_64-linux
     ```
   + If you're compiling tests to run on iOS devices, then run this command to configure the Gemfile to use dependencies for the iOS test host:

     ```
     bundle lock --add-platform x86_64-darwin
     ```

1. The **bundler** gem is usually installed by default. If it is not, install it:

   ```bash
   gem install bundler -v 2.3.26
   ```

------

## Create a zipped test package file
<a name="test-types-appium-create-a-zip"></a>

**Warning**  
In Device Farm, the folder structure of files in your zipped test package matters, and some archival tools will change the structure of your ZIP file implicitly. We recommend that you follow the specified command-line utilities below rather than use the archival utilities built into the file manager of your local desktop (such as Finder or Windows Explorer).

Now, bundle your tests for Device Farm.

------
#### [ Java (JUnit) ]

Build and package your tests:

```
$ mvn clean package -DskipTests=true
```

The file `zip-with-dependencies.zip` will be created as a result. This is your test package.

------
#### [ Java (TestNG) ]

Build and package your tests:

```
$ mvn clean package -DskipTests=true
```

The file `zip-with-dependencies.zip` will be created as a result. This is your test package.

------
#### [ Node.JS ]

**Note**  
If you want Device Farm to generate a test report for your run, enable a WebdriverIO reporter before you follow this procedure, so that the reporter is in the package that you build. For more information, see [Configure Appium test reports using a custom test environment](#test-types-appium-generate-reports).

1. Check out your project.

   Make sure you are at the root directory of your project. You can see `package.json` at the root directory.

1. Run this command to install your local dependencies.

   ```bash
   npm install
   ```

   This command also creates a `node_modules` folder inside your current directory.
**Note**  
At this point, you should be able to run your tests locally.

1. Run this command to package the files in your current folder into a \*.tgz file. The file is named using the `name` property in your `package.json` file.

   ```bash
   npm-bundle
   ```

   This tarball (.tgz) file contains all your code and dependencies, including your `wdio.conf.js` file and any reporter you installed.

1. Run this command to bundle the tarball (\*.tgz file) generated in the previous step into a single zipped archive:

   ```bash
   zip -r {{MyTests.zip}} *.tgz
   ```

   This is the `MyTests.zip` file that you upload to Device Farm in the following procedure.

------
#### [ Python ]

Python 2  
Generate an archive of the required Python packages (called a "wheelhouse") using pip:  

```
$ pip wheel --wheel-dir wheelhouse -r requirements.txt
```
Package your wheelhouse, tests, and pip requirements into a zip archive for Device Farm:  

```
$ zip -r {{test_bundle.zip}} tests/ wheelhouse/ requirements.txt
```

Python 3  
Package your tests and pip requirements into a zip file:  

```
$ zip -r {{test_bundle.zip}} tests/ requirements.txt
```

------
#### [ Ruby ]

1. Run this command to create a virtual Ruby environment:

   ```bash
   # myGemset is the name of your virtual Ruby environment
   rvm gemset create {{myGemset}}
   ```

1. Run this command to use the environment you just created:

   ```bash
   rvm gemset use {{myGemset}}
   ```

1. Check out your source code.

   Make sure you are at the root directory of your project. You can see `Gemfile` at the root directory.

1. Run this command to install your local dependencies and all gems from the `Gemfile`:

   ```bash
   bundle install
   ```
**Note**  
At this point, you should be able to run your tests locally. Use this command to run a test locally:  

   ```bash
   bundle exec $test_command
   ```

1. Package your gems in the `vendor/cache` folder.

   ```bash
   # This will copy all the .gem files needed to run your tests into the vendor/cache directory
   bundle package --all-platforms
   ```

1. Run the following command to bundle your source code, along with all your dependencies, into a single zipped archive:

   ```bash
   zip -r MyTests.zip Gemfile vendor/ $(any other source code directory files)
   ```

   This is the `MyTests.zip` file that you upload to Device Farm in the following procedure.

------

## Run your Appium tests
<a name="test-types-appium-upload"></a>

You can use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. If you are a new user, choose **New project**, enter a name for the project, and then choose **Submit**. If you already have a project, you can choose it to upload your tests to it.

1. Open your project, and then choose **Create run**.

1. Under **Select app and run type**, in the **Run type** section, select your run type. Select **Android app** for an Android (.apk) app, **iOS app** for an iOS app, or **Web App** for a mobile web application.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app. If you are bringing your own app, select **Upload own app**. Then choose your APK (.apk file format) for Android or your `.ipa` file for iOS. For the iOS build that your devices need, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

1. Under **Configure test**, in the **Select test framework** section, choose the Appium framework that you test with, and then select **Upload your own test package**. Browse to and choose the .zip file that contains your tests. The .zip file must follow the format described in [Configure your Appium test package](#test-types-appium-prepare).

1. You can use the default test spec, or choose **Upload own test spec** to provide your own.

1. Under **Select devices**, choose a device selection method. Select **Use Device Pool** to choose from a curated collection of devices or a custom device pool you created. Select **Manually select devices** to pick individual devices to run your tests against. The **Device compatibility** section shows how many devices in the selected pool are compatible with your app. For more information, see [Device support in AWS Device Farm](devices.md).

1. To configure run-level properties, update the **Run settings** section.

1. Choose **Confirm and start run**. For more information, see [Creating a test run in Device Farm](how-to-create-test-run.md).

**Note**  
Device Farm does not modify Appium tests.

## View a test report
<a name="test-types-appium-view-insights"></a>

After your run completes, Device Farm generates a test report for each device. The report shows a per-test breakdown, including each test's name, class, result, and duration, plus a stack trace for any failed test. You can view the test report in the console or retrieve it through the API.

To open a completed job in the Device Farm console:

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Choose the project that contains the run you want to inspect.

1. Choose the completed run to open its details.

1. Choose one of the completed jobs to open the results for that device.

What you see in the job results depends on the test framework and whether test insights are enabled.

### With test insights enabled
<a name="test-types-appium-view-insights-enabled"></a>

The job results include a **Test report** tab. Choose it to see a per-test breakdown. Choose your framework tab below to see the **Test report** tab for that framework. For a description of each field, see [Test report fields](#test-types-appium-view-insights-fields).

To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

When the run records a video, the **Video** column has a play button for each test that plays the test in the job video. For more information, see [Watch a test in the job video](reports.md#reports-test-insights-video-console).

To choose which columns appear, choose the gear icon. In the settings, you can select the columns to display and turn **Group by class** on or off. **Group by class** is on by default, which groups the tests by their test class. Turn it off to see a flat list of all tests.

------
#### [ Java (JUnit) ]

The following screenshot shows the **Test report** tab for a run that wrote an open test reporting file.

![The Test report tab for a completed Appium Java JUnit job, with the tests grouped by test class.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-junit-insights-enabled-test-report-column.png)


The following screenshot shows the **Test report** tab with the **Test video** panel open.

![The Test report tab for a completed Appium Java JUnit job, with the Test video panel open on the selected test.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-junit-insights-enabled-test-video-panel.png)


If Device Farm doesn't find a test report file, the **Start time** and **End time** columns do not appear, and the report doesn't show per-test video. The following screenshot shows a run that did not write one.

![The Test report tab for a run without a test report file, which has no Start time or End time column.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-junit-insights-enabled-test-report-without-open-test-reporting.png)


------
#### [ Java (TestNG) ]

The following screenshot shows the **Test report** tab.

![The Test report tab for a completed Appium Java TestNG job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-testng-insights-enabled-test-report-column.png)


The following screenshot shows the same tab with **Group by class** turned off.

![The Test report tab with Group by class turned off, showing a flat list of tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-testng-insights-enabled-test-report-without-grouping.png)


The following screenshot shows the **Test report** tab with the **Test video** panel open.

![The Test report tab for a completed Appium Java TestNG job, with the Test video panel open on the selected test.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-testng-insights-enabled-test-video-panel.png)


------
#### [ Node.JS ]

Device Farm builds the report from the WebdriverIO reporter you enabled. The JSON reporter records a start and end time for each test and the JUnit reporter does not. A report built from the JUnit reporter omits the `startTimestamp` and `endTimestamp` fields and doesn't show per-test video. If you enable both reporters, Device Farm uses the JSON output.

The following screenshot shows the **Test report** tab.

![The Test report tab for a completed Appium Node.js job, with the stack trace of a failed test open.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-node-insights-enabled-test-report-column.png)


The following screenshot shows the same tab with **Group by class** turned off.

![The Test report tab with Group by class turned off, showing a flat list of tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-node-insights-enabled-test-report-without-grouping.png)


The following screenshot shows the **Test report** tab with the **Test video** panel open.

![The Test report tab for a completed Appium Node.js job, with the Test video panel open on the selected test.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-node-insights-enabled-test-video-panel.png)


------
#### [ Python ]

The following screenshot shows the **Test report** tab for a run that recorded start and end times with the `conftest.py` code described in [Configure Appium test reports using a custom test environment](#test-types-appium-generate-reports). Without that code, the **Start time** and **End time** columns do not appear, and the report doesn't show per-test video.

![The Test report tab for a completed Appium Python job, with the tests grouped by test class.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-pytest-insights-enabled-test-report.png)


The following screenshot shows the **Test report** tab with the **Test video** panel open.

![The Test report tab for a completed Appium Python job, with the Test video panel open on the selected test.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/appium-pytest-insights-enabled-test-video-panel.png)


------

### Without test insights enabled
<a name="test-types-appium-view-insights-disabled"></a>

The job results show the standard test output and artifacts, but no **Test report** tab, in the following cases: the run used the standard test environment, you turned off test insights, or Device Farm does not generate test insights for the framework. To get a test report for a supported framework, schedule a new run in a custom test environment with **Generate test report** selected.

![The job results for a completed job without test insights enabled.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-disabled-test-report.png)


### View a test report (AWS CLI)
<a name="test-types-appium-view-insights-cli"></a>

Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

If the run did not generate test insights, for example because it used the standard test environment or you turned off test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```json
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "name": "Example Android Phone",
        "created": "2026-07-31T16:58:20.000000-07:00",
        "status": "COMPLETED",
        "result": "FAILED",
        "counters": {
            "total": 3,
            "passed": 1,
            "failed": 1,
            "warned": 0,
            "errored": 0,
            "stopped": 0,
            "skipped": 1
        },
        "device": {
            "arn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
            "name": "Example Android Phone",
            "platform": "ANDROID",
            "os": "14",
            "formFactor": "PHONE",
            "fleetType": "PUBLIC"
        },
        "deviceMinutes": {
            "total": 1.42,
            "metered": 0.0,
            "unmetered": 1.17
        },
        "videoCapture": true
    }
}
```

If the run generated test insights, the response also includes an `insights` object. This object contains the test report status, high-level metrics, and a presigned URL to the detailed report:

```json
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "status": "COMPLETED",
        "result": "FAILED",
        "counters": { ... },
        "device": { ... },
        "deviceMinutes": { ... },
        "videoCapture": true,
        "insights": {
            "status": "COMPLETED",
            "testReport": {
                "message": "Results: 3 Executed | 1 passed | 1 failed | 1 skipped, Median test duration: 1.83 seconds.",
                "metrics": {
                    "testsTotal": 3,
                    "testsPassed": 1,
                    "testsFailed": 1,
                    "testsSkipped": 1,
                    "testsErrored": 0,
                    "testsOther": 0,
                    "testsPassedPercentage": 33.33
                },
                "testDetailsUrl": "https://EXAMPLE-PRESIGNED-URL"
            }
        }
    }
}
```

The `testDetailsUrl` field is a presigned URL to the full test report JSON. Download it to get the per-test breakdown:

```
curl -o test-report.json "{{PRESIGNED_URL}}"
```

Choose your framework tab for an example test report.

------
#### [ Java (JUnit) ]

The following report is from a job that wrote an open test reporting file:

```json
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "deviceName": "Example Android Phone",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
  "deviceOsVersion": "15",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 2,
    "testsFailed": 0,
    "testsSkipped": 0,
    "testsErrored": 1,
    "testsOther": 0,
    "testsPassedPercentage": 66.67,
    "totalTestExecutionDurationSeconds": 13.842,
    "medianTestExecutionDurationSeconds": 1.192
  },
  "testDetails": [
    {
      "testName": "shouldConnect(ExecutionHardware)[1]",
      "testClass": "com.example.tests.ConnectivityTest",
      "frameworkResult": "SUCCESSFUL",
      "result": "PASSED",
      "durationSeconds": 1.192,
      "startTimestamp": "2026-10-05T06:08:38.021000Z",
      "endTimestamp": "2026-10-05T06:08:39.213000Z",
      "params": ["[1] MOBILE_DEVICE"]
    },
    {
      "testName": "shouldConnect(ExecutionHardware)[2]",
      "testClass": "com.example.tests.ConnectivityTest",
      "frameworkResult": "SUCCESSFUL",
      "result": "PASSED",
      "durationSeconds": 0.341,
      "startTimestamp": "2026-10-05T06:08:39.240000Z",
      "endTimestamp": "2026-10-05T06:08:39.581000Z",
      "params": ["[2] HOST"]
    },
    {
      "testName": "shouldSwitchContext()",
      "testClass": "com.example.tests.HybridAppTest",
      "frameworkResult": "FAILED",
      "result": "ERRORED",
      "durationSeconds": 12.309,
      "startTimestamp": "2026-10-05T06:09:04.112000Z",
      "endTimestamp": "2026-10-05T06:09:16.421000Z",
      "stackTrace": "io.appium.java_client.NoSuchContextException: No Chromedriver found that can automate Chrome '154.0.8037'.\n\tat ..."
    }
  ]
}
```

A report built from JUnit XML files has the same shape, without the `startTimestamp` and `endTimestamp` fields, and `frameworkResult` uses the JUnit XML outcome names instead of the open test reporting statuses. For the values, see [Test report fields](#test-types-appium-view-insights-fields).

------
#### [ Java (TestNG) ]

```json
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "deviceName": "Google Pixel 7",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
  "deviceOsVersion": "14",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 1,
    "testsFailed": 1,
    "testsSkipped": 1,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 33.33,
    "totalTestExecutionDurationSeconds": 5.421,
    "medianTestExecutionDurationSeconds": 1.83
  },
  "testDetails": [
    {
      "testName": "testValidLogin",
      "testClass": "com.example.app.LoginTest",
      "frameworkResult": "PASS",
      "result": "PASSED",
      "durationSeconds": 1.83,
      "startTimestamp": "2026-07-31T16:58:26.646000Z",
      "endTimestamp": "2026-07-31T16:58:28.476000Z",
      "videoStartSeconds": 12.4,
      "videoEndSeconds": 14.23
    },
    {
      "testName": "testCheckout",
      "testClass": "com.example.app.CheckoutTest",
      "frameworkResult": "FAIL",
      "result": "FAILED",
      "durationSeconds": 3.102,
      "startTimestamp": "2026-07-31T16:58:28.500000Z",
      "endTimestamp": "2026-07-31T16:58:31.602000Z",
      "videoStartSeconds": 14.254,
      "videoEndSeconds": 17.356,
      "stackTrace": "java.lang.AssertionError: expected [true] but found [false]\n\tat org.testng.Assert.fail(Assert.java:99)\n\t...",
      "params": ["premium-user", "US"]
    },
    {
      "testName": "testLogout",
      "testClass": "com.example.app.LoginTest",
      "frameworkResult": "SKIP",
      "result": "SKIPPED",
      "durationSeconds": 0.489,
      "startTimestamp": "2026-07-31T16:58:31.700000Z",
      "endTimestamp": "2026-07-31T16:58:32.189000Z",
      "videoStartSeconds": 17.454,
      "videoEndSeconds": 17.943
    }
  ]
}
```

------
#### [ Node.JS ]

The following report is from a job that used the JSON reporter:

```json
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "deviceName": "Google Pixel 8a",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
  "deviceOsVersion": "14",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 1,
    "testsFailed": 1,
    "testsSkipped": 1,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 33.33,
    "totalTestExecutionDurationSeconds": 4.932,
    "medianTestExecutionDurationSeconds": 1.83
  },
  "testDetails": [
    {
      "testName": "should log in with valid credentials",
      "testClass": "Login tests",
      "frameworkResult": "passed",
      "result": "PASSED",
      "durationSeconds": 1.83,
      "startTimestamp": "2026-09-10T19:28:17.265000Z",
      "endTimestamp": "2026-09-10T19:28:19.095000Z",
      "specs": ["login.e2e.js"]
    },
    {
      "testName": "should complete checkout",
      "testClass": "Checkout tests",
      "frameworkResult": "failed",
      "result": "FAILED",
      "durationSeconds": 3.102,
      "startTimestamp": "2026-09-10T19:28:19.120000Z",
      "endTimestamp": "2026-09-10T19:28:22.222000Z",
      "stackTrace": "Error: element (\"~submit\") still not displayed after 5000ms\n    at Context.<anonymous> (./test/specs/checkout.e2e.js:24:5)",
      "specs": ["checkout.e2e.js"]
    },
    {
      "testName": "should log out",
      "testClass": "Login tests",
      "frameworkResult": "pending",
      "result": "SKIPPED",
      "durationSeconds": 0.0,
      "specs": ["login.e2e.js"]
    }
  ]
}
```

A report built from the JUnit reporter has the same shape, without the `startTimestamp` and `endTimestamp` fields.

------
#### [ Python ]

The following report is from a job that recorded start and end times:

```json
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "deviceName": "Google Pixel 8a",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
  "deviceOsVersion": "14",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 1,
    "testsFailed": 1,
    "testsSkipped": 1,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 33.33,
    "totalTestExecutionDurationSeconds": 1.602,
    "medianTestExecutionDurationSeconds": 0.401
  },
  "testDetails": [
    {
      "testName": "test_valid_credentials",
      "testClass": "tests.test_login.TestLogin",
      "frameworkResult": "passed",
      "result": "PASSED",
      "durationSeconds": 1.201,
      "startTimestamp": "2026-10-28T22:51:55.232606Z",
      "endTimestamp": "2026-10-28T22:51:56.433885Z"
    },
    {
      "testName": "test_checkout_total",
      "testClass": "tests.test_login.TestLogin",
      "frameworkResult": "failure",
      "result": "FAILED",
      "durationSeconds": 0.401,
      "startTimestamp": "2026-10-28T22:51:56.441280Z",
      "endTimestamp": "2026-10-28T22:51:56.842530Z",
      "stackTrace": "self = <test_login.TestLogin object at 0x7f92d7509de0>\n\n    def test_checkout_total(self):\n        time.sleep(0.4)\n        total = 41\n>       assert total == 42\nE       assert 41 == 42\n\ntests/test_login.py:11: AssertionError"
    },
    {
      "testName": "test_logout",
      "testClass": "tests.test_login.TestLogin",
      "frameworkResult": "skipped",
      "result": "SKIPPED",
      "durationSeconds": 0.0,
      "startTimestamp": "2026-10-28T22:51:56.902408Z",
      "endTimestamp": "2026-10-28T22:51:56.902565Z",
      "stackTrace": "tests/test_login.py:13: feature flag off"
    }
  ]
}
```

A report from a job that did not record start and end times has the same shape, without the `startTimestamp` and `endTimestamp` fields.

------

**Note**  
Device Farm omits any field it has no value for, so a passing test has no `stackTrace` field at all.

### Test report fields
<a name="test-types-appium-view-insights-fields"></a>

The report contains the following top-level fields:

`version`  
The report schema version.

`jobArn`  
The ARN of the job.

`deviceName`, `deviceArn`, `deviceOsVersion`  
The device that the tests ran on, and its operating system version.

`metrics`  
Aggregate results for the job. The `metrics` object contains the following fields:    
`testsTotal`  
The total number of tests in the job.  
`testsPassed`  
The number of tests that passed.  
`testsFailed`  
The number of tests that failed.  
`testsSkipped`  
The number of tests that were skipped.  
`testsErrored`  
The number of tests that errored.  
`testsOther`  
The number of tests with another result.  
`testsPassedPercentage`  
The percentage of tests that passed.  
`totalTestExecutionDurationSeconds`  
The total duration of all tests, in seconds.  
`medianTestExecutionDurationSeconds`  
The median duration of a test, in seconds.

`testDetails`  
A list of per-test results. The fields in each entry depend on your test framework.

Choose your framework tab to see the fields in each `testDetails` entry.

------
#### [ Java (JUnit) ]

Each test execution is counted, so a test that ran more than once counts each time in the metrics. A test that throws an exception other than an assertion failure is reported as errored. Gradle records such an exception as a failure, so `testsErrored` is 0 for a report that Gradle produced. Open test reporting has no separate error status, so an errored test has a `frameworkResult` of `FAILED` and a `result` of `ERRORED`.

`testName`  
The name of the test method, as the report records it. Depending on your JUnit version and report producer, the same method can appear as `myTest` or `myTest()`.

`testClass`  
The name of the test class.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The result that JUnit reported. A report built from an open test reporting file uses `SUCCESSFUL`, `FAILED`, `SKIPPED`, or `ABORTED`. A report built from JUnit XML files uses `passed`, `failure`, `error`, or `skipped`. Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration of the test, in seconds.

`startTimestamp` and `endTimestamp`  
The time when the test started and ended. Present only in a report built from an open test reporting file, because the JUnit XML format records a timestamp for the suite rather than for each test.

`params`  
For a parameterized test, the argument values for the invocation. Present when the report comes from the JUnit Platform Console Launcher or from open test reporting. Maven and Gradle reports do not carry the argument values.

`stackTrace`  
For a failed or errored test, the stack trace of the failure.

`videoStartSeconds`  
Where the test started in the job video, in seconds. See [Per-test video](reports.md#reports-test-insights-video).

`videoEndSeconds`  
Where the test ended in the job video, in seconds.

------
#### [ Java (TestNG) ]

`testName`  
The name of the test method.

`testClass`  
The name of the test class.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The result that TestNG reported (`PASS`, `FAIL`, or `SKIP`). Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration of the test, in seconds.

`startTimestamp`  
The time when the test started.

`endTimestamp`  
The time when the test ended.

`params`  
For a parameterized test, the parameter values that TestNG passed to the test.

`stackTrace`  
For a failed test, the stack trace of the failure.

`videoStartSeconds`  
Where the test started in the job video, in seconds. See [Per-test video](reports.md#reports-test-insights-video).

`videoEndSeconds`  
Where the test ended in the job video, in seconds.

------
#### [ Node.JS ]

WebdriverIO reports a test that did not run as pending, which Device Farm maps to skipped. WebdriverIO has no errored state, so a test that throws is reported as failed rather than errored.

`testName`  
The name of the test.

`testClass`  
The name of the suite that contains the test. Node.js tests have no test class, so Device Farm reports the suite name in this field.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The state that WebdriverIO reported. The JSON reporter reports `passed`, `failed`, `skipped`, or `pending`. The JUnit reporter reports only `passed`, `failed`, or `skipped`, because it records a pending test as skipped. Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration of the test, in seconds.

`startTimestamp` and `endTimestamp`  
The time when the test started and ended. Present only in a report built from the JSON reporter, and only for a test that ran. The JUnit reporter records only a suite-level timestamp, with no time zone and no subsecond precision, so Device Farm omits these fields rather than report a time it cannot place. A pending test never started, so these fields are omitted for it on both routes.

`specs`  
The names of the spec files that the test came from. WebdriverIO runs your spec files in parallel, so the same suite and test title can appear more than once in a job. This field tells those runs apart. It can name several spec files. That happens when one WebdriverIO runner handles a group of spec files, or when Device Farm reads a merged JSON report, which does not record which runner each suite came from.

`stackTrace`  
For a failed test, the stack trace of the failure.

`videoStartSeconds`  
Where the test started in the job video, in seconds. See [Per-test video](reports.md#reports-test-insights-video).

`videoEndSeconds`  
Where the test ended in the job video, in seconds.

------
#### [ Python ]

Device Farm lists and counts each test once, with the result of its last attempt, even if pytest ran it more than once. pytest reports an exception in a test as a failure and an exception in a fixture as an error. Device Farm reports an expected failure (`xfailed`) as skipped.

`testName`  
The name of the test function. For a parameterized test, pytest adds the parameter ID in brackets, for example `test_login[admin]`.

`testClass`  
The dotted path of the test module, followed by the class name when the test is a method of a class, for example `tests.test_login.TestLogin`.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The result that pytest reported: `passed`, `failure`, `error`, `skipped`, or `xfailed`. Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration that pytest recorded for the test, in seconds. By default, this includes the setup and teardown of the test. If the pytest-rerunfailures plugin reran the test, this is the duration of the last attempt.

`startTimestamp` and `endTimestamp`  
The time when the test's setup started and when its teardown ended. Present only if you add the `conftest.py` code. For more information, see [Configure Appium test reports using a custom test environment](#test-types-appium-generate-reports).

`stackTrace`  
For a failed or errored test, the failure output that pytest recorded. For a skipped test, the location and reason of the skip.

`videoStartSeconds`  
Where the test started in the job video, in seconds. See [Per-test video](reports.md#reports-test-insights-video).

`videoEndSeconds`  
Where the test ended in the job video, in seconds.

------

## Take screenshots of your tests (Optional)
<a name="test-types-appium-screenshots"></a>

You can take screenshots as part of your tests.

Device Farm sets the `DEVICEFARM_SCREENSHOT_PATH` property to a fully qualified path on the local file system where Device Farm expects Appium screenshots to be saved. The test-specific directory where the screenshots are stored is defined at runtime. The screenshots are pulled into your Device Farm reports automatically. To view the screenshots, in the Device Farm console, choose the **Screenshots** section.

 For more information on taking screenshots in Appium tests, see [Take Screenshot](http://appium.io/docs/en/commands/session/screenshot/) in the Appium API documentation. 