NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Launching test instances

After you have added all of your source servers and configured their launch settings, you
are ready to launch a test instance. It is crucial to test the migration of your source servers
to AWS prior to initiating a cutover in order to verify that your source servers function
properly within the AWS environment.

###### Important

- It is a best practice to perform a test at least two weeks before you plan to migrate
  your source servers. This time frame allows you to identify potential problems and solve them,
  before the actual cutover takes place. After launching test instances, use either SSH (Linux)
  or RDP (Windows) to connect to your instance and ensure that everything is working
  correctly.
- When launching a test or cutover instance, you can launch up to 100 source servers in a
  single operation. Additional source servers can be launched in subsequent operations.
  You can test one source server at a time, or simultaneously test multiple source servers.
  For each source server, you are informed of the success or failure of the test. You can test
  your source server as many times as you want. Each new test first deletes any previously launched
  Test instance and dependent resources. Then, a new test instance is launched, which reflects the
  most up-to-date state of the source server. After the test, data replication continues as before.
  The new and modified data on the source server is transferred to the Staging Area Subnet and not
  to the test instances that were launched during the test.

###### Note

- Windows source servers need to have at least 2 GB of free space to successfully launch a
  test instance.
- Take into consideration that once a test instance is launched resources are
  used in your AWS account and you will be billed for these resources. You can terminate the
  operation of launched Test instances once you verify that they are working properly without
  impact in order to data replication.

###### Topics

- [Review ready for testing indicators](ready-for-testing.md "ready-for-testing.md")
- [Starting a test](starting-test.md "starting-test.md")
- [Reverting a test](revert-finalize-test.md "revert-finalize-test.md")
- [Marking as Ready for cutover](finalizing-test.md "finalizing-test.md")
