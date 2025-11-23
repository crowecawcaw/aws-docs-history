# Troubleshooting Appium Python web application tests in

AWS Device Farm

The following topic lists error messages that occur during the upload of Appium Python Web application tests and
recommends workarounds to resolve each error.

## APPIUM_WEB_PYTHON_TEST_PACKAGE_UNZIP_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not open your Appium test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

A valid Appium Python package should produce output like the following:

```
.
|-- requirements.txt
|-- test_bundle.zip
|-- tests (directory)
|      `-- test_unittest.py
`-- wheelhouse (directory)
       |-- Appium_Python_Client-0.20-cp27-none-any.whl
       |-- py-1.4.31-py2.py3-none-any.whl
       |-- pytest-2.9.0-py2.py3-none-any.whl
       |-- selenium-2.52.0-cp27-none-any.whl
       `-- wheel-0.26.0-py2.py3-none-any.whl
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEEL_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find a dependency wheel file in the wheelhouse directory tree. Please unzip your test package
and then open the wheelhouse directory, verify that at least one wheel file is in the directory, and try
again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Python package is valid, you will find at least one `.whl`
dependent file like the highlighted files inside the `wheelhouse` directory.

```
.
|-- requirements.txt
|-- test_bundle.zip
|-- tests (directory)
|      `-- test_unittest.py
`-- wheelhouse (directory)
       |-- `Appium_Python_Client-0.20-cp27-none-any.whl`
       |-- `py-1.4.31-py2.py3-none-any.whl`
       |-- `pytest-2.9.0-py2.py3-none-any.whl`
       |-- `selenium-2.52.0-cp27-none-any.whl`
       `-- `wheel-0.26.0-py2.py3-none-any.whl`
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_PLATFORM

If you see the following message, follow these steps to fix the issue.

###### Warning

We found at least one wheel file specified a platform that we do not support. Please unzip your test package
and then open the wheelhouse directory, verify that names of wheel files end with -any.whl or -linux_x86_64.whl,
and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Python package is valid, you will find at least one `.whl`
dependent file like the highlighted files inside the `wheelhouse` directory. The
file's name may be different, but it should end with `-any.whl` or
`-linux_x86_64.whl`, which specifies the platform. Any other platforms like `windows` are not supported.

```
.
|-- requirements.txt
|-- test_bundle.zip
|-- tests (directory)
|      `-- test_unittest.py
`-- wheelhouse (directory)
       |-- `Appium_Python_Client-0.20-cp27-none-any.whl`
       |-- `py-1.4.31-py2.py3-none-any.whl`
       |-- `pytest-2.9.0-py2.py3-none-any.whl`
       |-- `selenium-2.52.0-cp27-none-any.whl`
       `-- `wheel-0.26.0-py2.py3-none-any.whl`
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_TEST_DIR_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the tests directory inside your test package. Please unzip your test package, verify that
the tests directory is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Python package is valid, you will find the `tests` directory inside
the working directory.

```
.
|-- requirements.txt
|-- test_bundle.zip
|-- `tests` (directory)
|      `-- test_unittest.py
`-- wheelhouse (directory)
       |-- Appium_Python_Client-0.20-cp27-none-any.whl
       |-- py-1.4.31-py2.py3-none-any.whl
       |-- pytest-2.9.0-py2.py3-none-any.whl
       |-- selenium-2.52.0-cp27-none-any.whl
       `-- wheel-0.26.0-py2.py3-none-any.whl
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_TEST_FILE_NAME

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find a valid test file in the tests directory tree. Please unzip your test package and then
open the tests directory, verify that at least one file's name starts or ends with the keyword "test", and try
again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Python package is valid, you will find the `tests` directory inside
the working directory. The file's name may be different, but it should start with
`test_` or end with `_test.py`.

```
.
|-- requirements.txt
|-- test_bundle.zip
|-- tests (directory)
|      `-- `test_unittest.py`
`-- wheelhouse (directory)
       |-- Appium_Python_Client-0.20-cp27-none-any.whl
       |-- py-1.4.31-py2.py3-none-any.whl
       |-- pytest-2.9.0-py2.py3-none-any.whl
       |-- selenium-2.52.0-cp27-none-any.whl
       `-- wheel-0.26.0-py2.py3-none-any.whl
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_REQUIREMENTS_TXT_FILE_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the requirements.txt file inside your test package. Please unzip your test package, verify
that the requirements.txt file is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the Appium Python package is valid, you will find the `requirements.txt` file
inside the working directory.

```
.
|-- `requirements.txt`
|-- test_bundle.zip
|-- tests (directory)
|      `-- test_unittest.py
`-- wheelhouse (directory)
       |-- Appium_Python_Client-0.20-cp27-none-any.whl
       |-- py-1.4.31-py2.py3-none-any.whl
       |-- pytest-2.9.0-py2.py3-none-any.whl
       |-- selenium-2.52.0-cp27-none-any.whl
       `-- wheel-0.26.0-py2.py3-none-any.whl
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_PYTEST_VERSION

If you see the following message, follow these steps to fix the issue.

###### Warning

We found the pytest version was lower than the minimum version 2.8.0 we support. Please change the pytest
version inside the requirements.txt file, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

You should find the `requirement.txt` file inside the working directory.

```
.
|-- `requirements.txt`
|-- test_bundle.zip
|-- tests (directory)
|      `--test_unittest.py
`-- wheelhouse (directory)
       |-- Appium_Python_Client-0.20-cp27-none-any.whl
       |-- py-1.4.31-py2.py3-none-any.whl
       |-- pytest-2.9.0-py2.py3-none-any.whl
       |-- selenium-2.52.0-cp27-none-any.whl
       `-- wheel-0.26.0-py2.py3-none-any.whl
```

3. To get the pytest version, you can run the following command:

```
$ grep "pytest" requirements.txt
```

You should find output like the following:

```
pytest==2.9.0
```

It shows the pytest version, which in this example is 2.9.0. If the Appium Python package is valid, the
pytest version should be larger than or equal to 2.8.0.

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_INSTALL_DEPENDENCY_WHEELS_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We failed to install the dependency wheels. Please unzip your test package and then open the
requirements.txt file and the wheelhouse directory, verify that the dependency wheels specified in the
requirements.txt file exactly match the dependency wheels inside the wheelhouse directory, and try again.

We strongly recommend that you set up [Python
virtualenv](https://pypi.python.org/pypi/virtualenv "https://pypi.python.org/pypi/virtualenv") for packaging tests. Here is an example flow of creating a virtual environment using Python
virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. To test installing wheel files, you can run the following command:

```
$ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
```

A valid Appium Python package should produce output like the following:

```
Ignoring indexes: https://pypi.python.org/simple
Collecting Appium-Python-Client==0.20 (from -r ./requirements.txt (line 1))
Collecting py==1.4.31 (from -r ./requirements.txt (line 2))
Collecting pytest==2.9.0 (from -r ./requirements.txt (line 3))
Collecting selenium==2.52.0 (from -r ./requirements.txt (line 4))
Collecting wheel==0.26.0 (from -r ./requirements.txt (line 5))
Installing collected packages: selenium, Appium-Python-Client, py, pytest, wheel
  Found existing installation: wheel 0.29.0
    Uninstalling wheel-0.29.0:
      Successfully uninstalled wheel-0.29.0
Successfully installed Appium-Python-Client-0.20 py-1.4.31 pytest-2.9.0 selenium-2.52.0 wheel-0.26.0
```

3. To deactivate the virtual environment, you can run the following command:

```
$ deactivate
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").

## APPIUM_WEB_PYTHON_TEST_PACKAGE_PYTEST_COLLECT_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We failed to collect tests in the tests directory. Please unzip your test package, very that the test
package is valid by running the command "py.test --collect-only <path to your tests directory>", and try
again after the command does not print any error.

We strongly recommend that you set up [Python
virtualenv](https://pypi.python.org/pypi/virtualenv "https://pypi.python.org/pypi/virtualenv") for packaging tests. Here is an example flow of creating a virtual environment using Python
virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is
**test_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip test_bundle.zip
```

2. To install wheel files, you can run the following command:

```
$ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
```

3. To collect tests, you can run the following command:

```
$ py.test --collect-only tests
```

A valid Appium Python package should produce output like the following:

```
==================== test session starts ====================
platform darwin -- Python 2.7.11, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
rootdir: /Users/zhena/Desktop/Ios/tests, inifile:
collected 1 items
<Module 'test_unittest.py'>
  <UnitTestCase 'DeviceFarmAppiumWebTests'>
    <TestCaseFunction 'test_devicefarm'>

==================== no tests ran in 0.11 seconds ====================
```

4. To deactivate the virtual environment, you can run the following command:

```
$ deactivate
```

For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md "test-types-appium.md").
