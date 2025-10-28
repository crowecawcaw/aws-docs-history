# Using the Query API

The following sections briefly discuss the parameters and request authentication used with the
Query API.

For general information about how the Query API works, see
[Query requests](../../../AWSEC2/latest/APIReference/Query-Requests.md "../../../AWSEC2/latest/APIReference/Query-Requests.md")
in the _Amazon EC2 API Reference._

## Query parameters

HTTP Query-based requests are HTTP requests that use the HTTP verb GET or POST and
a Query parameter named `Action`.

Each Query request must include some common parameters to handle authentication
and selection of an action.

Some operations take lists of parameters. These lists are specified using the
`param.`n``notation. Values of
`n` are integers starting from 1.

For information about Amazon RDS Regions and endpoints, go to [Amazon Relational Database Service
(RDS)](../../../general/latest/gr/rande.md#rds_region "../../../general/latest/gr/rande.md#rds_region") in the Regions and Endpoints section of the
_Amazon Web Services General Reference_.

## Query request authentication

You can only send Query requests over HTTPS, and you must include a signature in
every Query request. You must use either AWS signature version 4 or signature
version 2. For more information, see [Signature Version 4 signing
process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") and [Signature version 2 signing process](../../../general/latest/gr/signature-version-2.md "../../../general/latest/gr/signature-version-2.md").
