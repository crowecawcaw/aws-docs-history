# How AMS logging works

AMS single-account landing zone (SALZ) log management uses a variety of pre-installed agents and tools that are
implemented when instances and applications are onboarded or provisioned.

Logging is configured during the account onboarding process and when a stack is
launched.

AMS multi-account landing zone (MALZ) logs produced by instances and AWS services are available in
CloudWatch Logs or Amazon Simple Storage Service (Amazon S3), within each account managed
by AMS. AMS multi-account landing zone provides a central Logging Account that acts as a central aggregation
location for some logs produced by individual application accounts.

The tables in the [Accessing your logs](access-to-logs.md "access-to-logs.md") subsections describe
which logs are available in
individual accounts, and which are available in the central Logging Account.
