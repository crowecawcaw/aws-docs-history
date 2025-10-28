# Test spec syntax in Device Farm

The test spec is a file that you use to define custom test environments in AWS Device Farm. For more information
about the custom environments and the test spec file, see [Custom test environments in AWS Device Farm](custom-test-environments.md "custom-test-environments.md").

The following is the YAML test spec file structure. Following the structure is a description of each
property.

To see an example test spec file, refer to [Example of the Device Farm test spec file](custom-test-environment-example.md "custom-test-environment-example.md").

```
version: 0.1

phases:
  install:
    commands:
      - command
      - command
  pre_test:
    commands:
      - command
      - command
  test:
    commands:
      - command
      - command
  post_test:
    commands:
      - command
      - command

artifacts:
  - location
  - location

```

The test spec contains the following:

**`version`**

Reflects the Device Farm supported test spec version. The current version number is 0.1.

**`phases`**

This section contains groups of commands executed during a test run.

The allowed test phase names are:

**`install`**

Optional.

Default dependencies for testing frameworks supported by Device Farm are already
installed. This phase contains additional commands, if any, that Device Farm runs during
installation.

**`pre_test`**

Optional.

The commands, if any, executed before your automated test run.

**`test`**

Optional.

The commands executed during your automated test run. If any command in the test
phase fails, the test is marked as failed.

**`post_test`**

Optional.

The commands, if any, executed after your automated test run.

**`artifacts`**

Optional.

Device Farm gathers artifacts such as custom reports, log files, and images from a location
specified here. Wildcard characters are not supported as part of an artifact location, so you
must specify a valid path for each location.

These test artifacts are available for each device in your test run. For information about
retrieving your test artifacts, see [Downloading artifacts in a custom test
environment](using-artifacts-custom.md "using-artifacts-custom.md").

###### Important

A test spec must be formatted as a valid YAML file. If the indenting or spacing in your test spec are
invalid, your test run can fail. Tabs are not allowed in YAML files. You can use a YAML validator to
test whether your test spec is a valid YAML file. For more information, see the [YAML website](http://yaml.org/spec/1.2/spec.html "http://yaml.org/spec/1.2/spec.html").
