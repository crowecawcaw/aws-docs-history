# Troubleshooting Appium Java TestNG tests in AWS Device Farm

The following topic lists error messages that occur during the upload of Appium Java TestNG tests and recommends
workarounds to resolve each error.

## Upload errors

The following errors can occur when you upload your Appium Java TestNG tests.

### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_UNZIP\_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip zip-with-dependencies.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

A valid Appium Java JUnit package should produce output like the following:

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the `dependency-jars` directory inside your test package. Please unzip your
test package, verify that the `dependency-jars` directory is inside the package, and try
again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip zip-with-dependencies.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Java JUnit package is valid, you will find the `dependency-jars`
directory inside the working directory.

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— `dependency-jars`  (this is the directory that contains all of your dependencies, built as JAR files)
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then
open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip zip-with-dependencies.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Java JUnit package is valid, you will find at least one `jar` file
inside the `dependency-jars` directory.

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
      |— `com.some-dependency.bar-4.1.jar`
      |— `com.another-dependency.thing-1.0.jar`
      |— `joda-time-2.7.jar`
      `— `log4j-1.2.14.jar`
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at
least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip zip-with-dependencies.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Java JUnit package is valid, you will find at least one `jar` file
like `acme-android-appium-1.0-SNAPSHOT-tests.jar` in our example. The file's name may
be different, but it should end with `–tests.jar`.

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— `acme-android-appium-1.0-SNAPSHOT-tests.jar` (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the
tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip zip-with-dependencies.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

You should find at least one jar file like
`acme-android-appium-1.0-SNAPSHOT-tests.jar` in our example. The file's name may be
different, but it should end with `–tests.jar`.

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— `acme-android-appium-1.0-SNAPSHOT-tests.jar` (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

3. To extract files from the jar file, you can run the following command:

```
$ jar xf acme-android-appium-1.0-SNAPSHOT-tests.jar
```

4. After you successfully extract the files, run the following command:

```
$ tree .
```

You should find at least one class in the working directory tree:

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing
everything built from the ./src/test directory)
|- `one-class-file.class`
|- folder
|    `— `another-class-file.class`
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## Test insights

When you opt in to test insights, Device Farm generates a summarized report for your run and each job under it. If the
service cannot generate the report, the insights report status is `SKIPPED` or
`ERRORED`, and the report message explains why. The following messages can occur
when generating insights for Appium Java TestNG tests.

### The job did not run to completion

`Unable to generate test insights because the job was
 `status`.`

The job ended in a non-successful state (where
`status` is `STOPPED`, `ERRORED`, or
`SKIPPED`), so there was no result to summarize. A run that ends in a failed
state still receives insights.

To resolve this issue, investigate why the job did not run to completion.
In many cases, the `message` field of the job itself might explain why the job didn't complete.

### The results contained no test cases

`Test insights could not be generated. The testng-results.xml file was
 parsed successfully but contained no test cases.`

The results artifact parsed successfully but contained zero test cases.

To resolve this issue, verify that your test suite includes at least one test case and
that results are stored correctly under `$DEVICEFARM_LOG_DIR`.

### The test output exceeds the maximum supported size

`Unable to generate test insights: test output "testng-results.xml"
 exceeds the maximum supported size of 1GB.`

The testng-results.xml is larger than 1 GB.

To resolve this issue, reduce the testng-results.xml size to below 1 GB by trimming logs or
attachments.

### The testng-results.xml file was not found

`Unable to generate test insights. The test results file
 (testng-results.xml) was not found.`

No `testng-results.xml` file (and no XML entry with the TestNG root
signature) was found.

To resolve this issue, configure your framework to emit TestNG XML into the artifacts
directory (`$DEVICEFARM_LOG_DIR`).

### The testng-results.xml file could not be processed

`Test insights could not be generated because of an error while processing
 testng-results.xml.`

The XML file was malformed or could not be parsed.

To resolve this issue, ensure that the file is a well-formed XML in the standard TestNG
report format.
