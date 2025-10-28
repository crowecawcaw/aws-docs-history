# Amazon Linux 2 test environment for Android tests

AWS Device Farm utilizes Amazon Elastic Compute Cloud (EC2) host machines running Amazon Linux 2 to execute Android tests. When you
schedule a test run, Device Farm allocates a dedicated host for each device to independently run tests. The host
machines terminate after the test run along with any generated artifacts.

The Amazon Linux 2 test host is the newest Android test environment, replacing the previous Ubuntu-based
system. Using your test spec file, you can choose to run your Android tests on the Amazon Linux 2 environment.

The Amazon Linux 2 host provides several advantages:

- **Faster, more reliable testing**: Compared to the legacy host, the new
  test host significantly improves test speed, especially reducing test start times. The Amazon Linux 2
  host also demonstrates greater stability and reliability during testing.
- **Enhanced Remote Access for manual testing**: Upgrades to the latest
  test host and improvements lead to lower latency and better video performance for Android manual
  testing.
- **Standard software version selection**: Device Farm now standardizes major
  programming language support on the test host as well as Appium framework versions. For supported
  languages (currently Java, Python, Node.js, and Ruby) and Appium, the new test host provides long-term
  stable releases soon after launch. Centralized version management through the
  `devicefarm-cli` tool enables test spec file development with a consistent experience
  across frameworks.

###### Topics

- [Pre-installed software libraries to support Device Farm tests
  of Android devices](amazon-linux-2-supported-software.md "amazon-linux-2-supported-software.md")
- [Supported IP ranges for the Amazon Linux 2 test environment in
  Device Farm](amazon-linux-2-ip-ranges.md "amazon-linux-2-ip-ranges.md")
- [Using the devicefarm-cli tool in
  AWS Device Farm](amazon-linux-2-devicefarm-cli.md "amazon-linux-2-devicefarm-cli.md")
- [Selecting which Android test host to use in Device Farm](amazon-linux-2-android-test-selection.md "amazon-linux-2-android-test-selection.md")
- [Example: Device Farm test spec file showing an Android test
  host](amazon-linux-2-test-spec-file-example.md "amazon-linux-2-test-spec-file-example.md")
- [Migrating to the Amazon Linux 2 Test Host in
  AWS Device Farm](amazon-linux-2-migrating-to-amazon-linux-2.md "amazon-linux-2-migrating-to-amazon-linux-2.md")
