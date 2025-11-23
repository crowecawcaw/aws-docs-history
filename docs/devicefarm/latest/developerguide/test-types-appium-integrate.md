# Integrating Appium tests with Device Farm

Use the following instructions to integrate Appium tests with AWS Device Farm. For more information about using Appium
tests in Device Farm, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## Configure your Appium test package

Use the following instructions to configure your test package.

Java (JUnit)

1. Modify `pom.xml` to set packaging to a JAR file:

```
<groupId>com.acme</groupId>
<artifactId>acme-myApp-appium</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>jar</packaging>
```

2. Modify `pom.xml` to use `maven-jar-plugin` to
   build your tests into a JAR file.

The following plugin builds your test source code (anything in the
`src/test` directory) into a JAR file:

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

3. Modify `pom.xml` to use
   `maven-dependency-plugin` to build dependencies as JAR
   files.

The following plugin copies your dependencies into the
`dependency-jars` directory:

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

4. Save the following XML assembly to
   `src/main/assembly/zip.xml`.

The following XML is an assembly definition that, when configured, instructs Maven
to build a .zip file that contains everything in the root of your build output directory and
the `dependency-jars` directory:

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

5. Modify `pom.xml` to use `maven-assembly-plugin`
   to package tests and all dependencies into a single .zip file.

The following plugin uses the preceding assembly to create a .zip file named
`zip-with-dependencies` in the build output directory every time
**mvn package** is run:

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

###### Note

If you receive an error that says annotation is not supported in 1.3, add the following to
`pom.xml`:

```
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.7</source>
    <target>1.7</target>
  </configuration>
</plugin>
```

Java (TestNG)

1. Modify `pom.xml` to set packaging to a JAR file:

```
<groupId>com.acme</groupId>
<artifactId>acme-myApp-appium</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>jar</packaging>
```

2. Modify `pom.xml` to use `maven-jar-plugin` to
   build your tests into a JAR file.

The following plugin builds your test source code (anything in the
`src/test` directory) into a JAR file:

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

3. Modify `pom.xml` to use
   `maven-dependency-plugin` to build dependencies as JAR
   files.

The following plugin copies your dependencies into the
`dependency-jars` directory:

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

4. Save the following XML assembly to
   `src/main/assembly/zip.xml`.

The following XML is an assembly definition that, when configured, instructs Maven
to build a .zip file that contains everything in the root of your build output directory and
the `dependency-jars` directory:

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

5. Modify `pom.xml` to use `maven-assembly-plugin`
   to package tests and all dependencies into a single .zip file.

The following plugin uses the preceding assembly to create a .zip file named
`zip-with-dependencies` in the build output directory every time
**mvn package** is run:

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

###### Note

If you receive an error that says annotation is not supported in 1.3, add the following to
`pom.xml`:

```
<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.7</source>
    <target>1.7</target>
  </configuration>
</plugin>
```

Node.JS
To package your Appium Node.js tests and upload them to Device Farm, you must install the following on your local
machine:

- [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm")

Use this tool when you develop and package your tests so that unnecessary dependencies are not included in
your test package.

- Node.js
- npm-bundle (installed globally)

1. Verify that nvm is present

```
command -v nvm
```

You should see `nvm` as output.

For more information, see [nvm](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm") on GitHub. 2. Run this command to install Node.js:

```
nvm install node
```

You can specify a particular version of Node.js:

```
nvm install 11.4.0
```

3. Verify that the correct version of Node is in use:

```
node -v
```

4. Install **npm-bundle** globally:

```
npm install -g npm-bundle
```

Python

1. We strongly recommend that you set up [Python
   virtualenv](https://pypi.python.org/pypi/virtualenv "https://pypi.python.org/pypi/virtualenv") for developing and packaging tests so that unnecessary dependencies are not included in
   your app package.

```
`$` virtualenv workspace
`$` cd workspace
`$` source bin/activate
```

###### Tip

    * Do not create a Python virtualenv with the `--system-site-packages` option, because it
     inherits packages from your global site-packages directory. This can result in including dependencies in
     your virtual environment that are not required by your tests.
    * You should also verify that your tests do not use dependencies that are dependent on native libraries,
     because these native libraries might not be present on the instance where these tests run.

2. Install **py.test** in your virtual environment.

```
`$` pip install pytest
```

3. Install the Appium Python client in your virtual environment.

```
`$` pip install Appium-Python-Client
```

4. Unless you specify a different path in custom mode, Device Farm expects your tests to be stored in
   `tests/`. You can use `find` to show all files inside a folder:

```
`$` find tests/
```

Confirm that these files contain test suites you wand to run on Device Farm

```
tests/
tests/`my-first-tests.py`
tests/`my-second-tests/py`
```

5. Run this command from your virtual environment workspace folder to show a list of your tests without
   running them.

```
`$` py.test --collect-only tests/
```

Confirm the output shows the tests that you want to run on Device Farm. 6. Clean all cached files under your tests/ folder:

```
`$` find . -name '__pycache__' -type d -exec rm -r {} +
`$` find . -name '*.pyc' -exec rm -f {} +
`$` find . -name '*.pyo' -exec rm -f {} +
`$` find . -name '*~' -exec rm -f {} +
```

7. Run the following command in your workspace to generate the requirements.txt file:

```
`$` pip freeze > requirements.txt
```

Ruby
To package your Appium Ruby tests and upload them to Device Farm, you must install the following on your local
machine:

- [Ruby Version Manager (RVM)](https://rvm.io/rvm/install "https://rvm.io/rvm/install")

Use this command-line tool when you develop and package your tests so that unnecessary dependencies are
not included in your test package.

- Ruby
- Bundler (This gem is typically installed with Ruby.)

1. Install the required keys, RVM, and Ruby. For instructions, see [Installing RVM](https://rvm.io/rvm/install "https://rvm.io/rvm/install") on the RVM website.

After the installation is complete, reload your terminal by signing out and then signing in again.

###### Note

RVM is loaded as a function for the bash shell only. 2. Verify that **rvm** is installed correctly

```
command -v rvm
```

You should see `rvm` as output. 3. If you want to install a specific version of Ruby, such as `2.5.3`, run the
following command:

```
rvm install ruby 2.5.3 --autolibs=0
```

Verify that you are on the requested version of Ruby:

```
ruby -v
```

4. Configure the bundler to compile packages for your desired testing platforms:

```
bundle config specific_platform true
```

5. Update your .lock file to add the platforms needed to run tests.
   - If you're compiling tests to run on Android devices, then run this command to configure the Gemfile to
     use dependencies for the Android test host:

   ```
   bundle lock --add-platform x86_64-linux
   ```

   - If you're compiling tests to run on iOS devices, then run this command to configure the Gemfile to use
     dependencies for the iOS test host:

   ```
   bundle lock --add-platform x86_64-darwin
   ```

6. The **bundler** gem is usually installed by default. If it is not, install it:

```
gem install bundler -v 2.3.26
```

## Create a zipped test package file

###### Warning

In Device Farm, the folder structure of files in your zipped test package matters, and some archival tools
will change the structure of your ZIP file implicitly. We recommend that you follow the specified command-line
utilities below rather than use the archival utilities built into the file manager of your local desktop (such as
Finder or Windows Explorer).

Now, bundle your tests for Device Farm.

Java (JUnit)
Build and package your tests:

```
$ mvn clean package -DskipTests=true
```

The file `zip-with-dependencies.zip` will be created as a result. This is your test
package.

Java (TestNG)
Build and package your tests:

```
$ mvn clean package -DskipTests=true
```

The file `zip-with-dependencies.zip` will be created as a result. This is your test
package.

Node.JS

1. Check out your project.

Make sure you are at the root directory of your project. You can see `package.json` at
the root directory. 2. Run this command to install your local dependencies.

```
npm install
```

This command also creates a `node_modules` folder inside your current directory.

###### Note

At this point, you should be able to run your tests locally. 3. Run this command to package the files in your current folder into a \*.tgz file. The file is named using
the `name` property in your `package.json` file.

```
npm-bundle
```

This tarball (.tgz) file contains all your code and dependencies. 4. Run this command to bundle the tarball (\*.tgz file) generated in the previous step into a single zipped
archive:

```
zip -r `MyTests.zip` *.tgz
```

This is the `MyTests.zip` file that you upload to Device Farm in the following
procedure.

Python

Python 2

Generate an archive of the required Python packages (called a "wheelhouse") using pip:

```
`$` pip wheel --wheel-dir wheelhouse -r requirements.txt
```

Package your wheelhouse, tests, and pip requirements into a zip archive for Device Farm:

```
`$` zip -r `test_bundle.zip` tests/ wheelhouse/ requirements.txt
```

Python 3

Package your tests and pip requirements into a zip file:

```
`$` zip -r `test_bundle.zip` tests/ requirements.txt
```

Ruby

1. Run this command to create a virtual Ruby environment:

```
# myGemset is the name of your virtual Ruby environment
rvm gemset create `myGemset`
```

2. Run this command to use the environment you just created:

```
rvm gemset use `myGemset`
```

3. Check out your source code.

Make sure you are at the root directory of your project. You can see `Gemfile` at the
root directory. 4. Run this command to install your local dependencies and all gems from the
`Gemfile`:

```
bundle install
```

###### Note

At this point, you should be able to run your tests locally. Use this command to run a test
locally:

```
bundle exec $test_command
```

5. Package your gems in the `vendor/cache` folder.

```
# This will copy all the .gem files needed to run your tests into the vendor/cache directory
bundle package --all-platforms
```

6. Run the following command to bundle your source code, along with all your dependencies, into a single
   zipped archive:

```
zip -r MyTests.zip Gemfile vendor/ $(any other source code directory files)
```

This is the `MyTests.zip` file that you upload to Device Farm in the following
procedure.

## Upload your test package to Device Farm

You can use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm
   navigation panel,
   choose **Mobile Device Testing**,
   then choose
   **Projects**.
3. If you are a new user, choose **New
   project**,
   enter a name for the project, then choose **Submit**.

If you already have a project, you can choose it to upload your tests to it. 4. Open your project, and then choose **Create run**. 5. Under **Run settings**, give your test an appropriate name.
This may contain any combination of spaces or punctuation. 6. For native Android and iOS tests

Under **Run settings**, choose **Android app** if you are
testing an Android (.apk) application, or choose **iOS app** if you are testing an
iOS (.ipa) application. Then, under **Select app**, select **Upload own
app** to upload your application's distributable package.

###### Note

The file must be either an Android `.apk` or an iOS `.ipa`. iOS
Applications must be built for real devices, not the Simulator.

For Mobile Web application tests

Under **Run settings**, choose **Web App**. 7. Under **Configure test**, in the **Select test framework** section, choose
the Appium framework that you test with, and then **Upload your own test package**. 8. Browse to and choose the .zip file that contains your tests. The .zip file must follow the format described
in [Configure your Appium test package](#test-types-appium-prepare "#test-types-appium-prepare"). 9. Follow the instructions to select devices and start the run. For
more information, see [Creating a test run in Device Farm](how-to-create-test-run.md "how-to-create-test-run.md").

###### Note

Device Farm does not modify Appium tests.

## Take screenshots of your tests (Optional)

You can take screenshots as part of your tests.

Device Farm sets the `DEVICEFARM_SCREENSHOT_PATH` property to a fully qualified path on the local
file system where Device Farm expects Appium screenshots to be saved. The test-specific directory where the
screenshots are stored is defined at runtime. The screenshots are pulled into your Device Farm reports
automatically. To view the screenshots, in the Device Farm console, choose the **Screenshots** section.

For more information on taking screenshots in Appium tests, see [Take Screenshot](http://appium.io/docs/en/commands/session/screenshot/ "http://appium.io/docs/en/commands/session/screenshot/") in the Appium API
documentation.
