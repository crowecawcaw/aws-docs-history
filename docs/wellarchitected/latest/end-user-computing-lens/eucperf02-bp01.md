# EUCPERF02-BP01 Identify geographic distribution of end users and design to minimize

latency

When migrating to or implementing AWS EUC services, consider the location of each
group of users with respect to the service endpoints for AWS WorkSpaces, WorkSpaces Applications, or
WorkSpaces Secure Browser. You should deliver services from the Region with the lowest latency to
most users.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Capture the location of each user group, and calculate the average latency between
each group and their most proximal AWS Region that supports the required AWS EUC
service. Due to Regional network routing and capabilities, it is possible the most
proximal AWS Region does not necessarily offer the lowest latency.

If you must deploy AWS EUC services in a non-optimal Region (which is sometimes
necessary to access other AWS services which have already been deployed), then be sure
that you test your application to verify that they offer acceptable performance at the
latency levels being experienced.

For an example of how latency might affect the user experience, see [EUC latency
trade-offs](https://guide.aws.dev/en/articles/ARiy3h1QGUSWePxGqdV_SYLA "https://guide.aws.dev/en/articles/ARiy3h1QGUSWePxGqdV_SYLA").
