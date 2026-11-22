

# Connecting to Rollbar in AWS Glue Studio

SDKs report occurrences (individual error/message events) which Rollbar groups into items (deduplicated errors, the unit a developer triages), scoped to a project within an account. Because you are a Rollbar user, you can connect AWS Glue to your Rollbar account. You can then use Rollbar as a data source in your AWS Glue ETL jobs to transfer data between Rollbar and AWS services or other supported applications.

**Topics**
+ [AWS Glue support for Rollbar](rollbar-support.md)
+ [Policies containing the API operations for creating and using connections](rollbar-configuring-iam-permissions.md)
+ [Configuring Rollbar](rollbar-configuring.md)
+ [Configuring Rollbar connections](rollbar-configuring-connections.md)
+ [Reading from Rollbar entities](rollbar-reading-from-entities.md)
+ [Rollbar connection options](rollbar-connection-options.md)
+ [Limitations and notes for the Rollbar connector](rollbar-connector-limitations.md)