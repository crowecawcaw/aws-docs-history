# Troubleshooting Appium Java JUnit tests in AWS Device Farm

The following topic lists error messages that occur during the upload of Appium Java JUnit tests and recommends
workarounds to resolve each error.

###### Note

The instructions below are based on Linux x86_64 and Mac.

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_UNZIP_FAILED

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

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_DEPENDENCY_DIR_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the dependency-jars directory inside your test package. Please unzip your test package,
verify that the dependency-jars directory is inside the package, and try again.

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
directory inside the working directory:

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

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR

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
inside the `dependency-jars` directory:

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

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_TESTS_JAR_FILE_MISSING

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

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR

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

3. After you successfully extract the files, you should find at least one class in the working directory tree
   by running the command:

```
$ tree .
```

You should see output like this:

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing
everything built from the ./src/test directory)
|- `one-class-file.class`
|- folder
|    `-`another-class-file.class`
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_JUNIT_VERSION_VALUE_UNKNOWN

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find a JUnit version value. Please unzip your test package and open the dependency-jars
directory, verify that the JUnit JAR file is inside the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip zip-with-dependencies.zip
```

2. After you successfully unzip the package, you can find the working-directory tree structure by running the
   following command:

```
tree .
```

The output should look like this:

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
    |— `junit-4.10.jar`
    |— com.some-dependency.bar-4.1.jar
    |— com.another-dependency.thing-1.0.jar
    |— joda-time-2.7.jar
    `— log4j-1.2.14.jar
```

If the Appium Java JUnit package is valid, you will find the JUnit dependency file that is similar to the
jar file `junit-4.10.jar` in our example. The name should consist of the keyword
`junit` and its version number, which in this example is 4.10.

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_JAVA_JUNIT_TEST_PACKAGE_INVALID_JUNIT_VERSION

If you see the following message, follow these steps to fix the issue.

###### Warning

We found the JUnit version was lower than the minimum version 4.10 we support. Please change the JUnit
version and try again.

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

You should find a JUnit dependency file like `junit-4.10.jar` in our example and
its version number, which in our example is 4.10:

```
.
|— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
|— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
|— zip-with-dependencies.zip (this .zip file contains all of the items)
`— dependency-jars (this is the directory that contains all of your dependencies, built as JAR files)
      |— `junit-4.10.jar`
      |— com.some-dependency.bar-4.1.jar
      |— com.another-dependency.thing-1.0.jar
      |— joda-time-2.7.jar
      `— log4j-1.2.14.jar
```

###### Note

Your tests may not execute correctly if the JUnit version specified in your test package is lower than
the minimum version 4.10 we support.

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").
