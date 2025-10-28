# Using the `devicefarm-cli` tool in

AWS Device Farm

AWS Device Farm uses Amazon Elastic Compute Cloud (EC2) host machines running Amazon Linux 2 to execute Android tests. The Amazon
Linux 2 test host uses a standardized version management tool called `devicefarm-cli` to select
software versions. This tool is separate from the AWS CLI and only available on the Device Farm Test Host. With
`devicefarm-cli`, you can switch to any pre-installed software version on the test host. This
provides a straightforward way to maintain your Device Farm test spec file over time and gives you a predictable
mechanism to upgrade software versions in the future.

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

Let's review a couple of examples using `devicefarm-cli`. To use the tool to change the Python
version from `3.10` to `3.9` in your test spec file, run
the following commands:

```
$ python --version
Python 3.10.12
$ devicefarm-cli use python 3.9
$ python --version
Python 3.9.17
```

To change the Appium version from `1` to `2`:

```
$ appium --version
1.22.3
$ devicefarm-cli use appium 2
$ appium --version
2.1.2
```

###### Tip

Note that when you select a software version, `devicefarm-cli` also switches the supporting
tools for those languages, such as `pip` for Python and `npm` for NodeJS.

For more information about how Device Farm tests Android devices, see [Amazon Linux 2 test environment for Android tests](amazon-linux-2.md "amazon-linux-2.md").

For more information about the preinstalled software on the Amazon Linux 2 test host, see [Pre-installed software libraries to support Device Farm tests
of Android devices](amazon-linux-2-supported-software.md "amazon-linux-2-supported-software.md").
