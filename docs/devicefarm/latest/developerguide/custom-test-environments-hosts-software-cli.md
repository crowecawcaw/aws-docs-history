#

Using the devicefarm-cli tool in custom test environments

The test host uses a standardized version management tool called `devicefarm-cli` to select software versions. This tool is separate from the AWS CLI and
only available on the Device Farm test host. With `devicefarm-cli`, you can switch to any
pre-installed software version on the test host. This provides a straightforward way to
maintain your Device Farm test spec file over time and gives you a predictable mechanism to upgrade
software versions in the future.

###### Important

This command line tool is not available on legacy iOS hosts. For more information, see
the topic on the [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host "custom-test-environments-hosts-ios.md#legacy-ios-host").

The snippet below shows the `help` page of `devicefarm-cli`:

```
$ devicefarm-cli help
 Usage: devicefarm-cli COMMAND [ARGS]

     Commands:
         help                         Prints this usage message.
         list                         Lists all versions of software configurable
                                      via this CLI.
         use <software> <version>     Configures the software for usage within the
                                      current shell's environment.
```

Let's review a couple of examples using `devicefarm-cli`. To use the tool to
change the Python version from `3.10` to `3.9`
in your test spec file, run the following commands:

```
$ python --version
Python 3.10.12
$ devicefarm-cli use python 3.9
$ python --version
Python 3.9.17
```

To change the Appium version from `1` to `2`
:

```
$ appium --version
1.22.3
$ devicefarm-cli use appium 2
$ appium --version
2.1.2
```

###### Tip

Note that when you select a software version, `devicefarm-cli` also switches
the supporting tools for those languages, such as `pip` for Python and `npm`
for NodeJS.

For more information about the preinstalled software on the test host, see [Supported software within custom test
environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").
