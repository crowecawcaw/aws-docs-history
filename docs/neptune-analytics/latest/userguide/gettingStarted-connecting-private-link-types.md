# Types of interface endpoint services for Neptune Analytics

Neptune Analytics supports two services via interface VPC endpoints on AWS PrivateLink: `neptune-graph` for
accessing Neptune Analytics control plane API operations like `CreateGraph`, `DeleteGraph` etc.
and `neptune-graph-data` for accessing Neptune Analytics data plane API operations like `GetQuery`,
`ListQueries`, `ExecuteQuery` etc. For more information about Neptune Analytics API operations see
[Neptune Analytics APIs](../apiref/Welcome.md "../apiref/Welcome.md").
