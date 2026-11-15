

# Server lifecycle states
<a name="transform-vmware-ms-server-lifecycle"></a>

During migration, each server progresses through the following lifecycle states. For more information, see [Source server lifecycle](https://docs.aws.amazon.com/mgn/latest/ug/migration-dashboard.html) in the *MGN User Guide*.
+ **Not ready** – The server is undergoing the initial sync process and is not yet ready for testing.
+ **Ready for testing** – Data replication has started and test or cutover instances can be launched.
+ **Test in progress** – A test instance is currently being launched.
+ **Ready for cutover** – The server has been tested and is ready for cutover.
+ **Cutover in progress** – A cutover instance is currently being launched.
+ **Cutover complete** – The server has been cutover. All data has been migrated to the AWS cutover instance.
+ **Disconnected** – The server has been disconnected from MGN.

You can ask AWS Transform about the status of your servers at any time during the migration. AWS Transform provides an interactive wave status table that displays all relevant server information including migration lifecycle, replication status, and recommended next steps. You can also ask in natural language, for example:
+ What is the status of my servers?
+ What's the status of my wave?
+ What's the status of the step that I'm currently in?

During wave migration, you can ask AWS Transform to update or change the status of individual servers. For example, if 9 out of 10 servers in your wave passed the test phase but one failed, you can allow AWS Transform to continue moving the 9 servers into the next phase while re-running the test on the failed server.