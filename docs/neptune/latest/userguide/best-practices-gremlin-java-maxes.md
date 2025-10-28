# Set `maxInProcessPerConnection`

and `maxSimultaneousUsagePerConnection` to the same value

Both the `maxInProcessPerConnection` and the `maxSimultaneousUsagePerConnection`
parameters are related to the maximum number of simultaneous queries you can submit on a single WebSocket
connection. Internally, these parameters are co-related and modification of one without the
other could lead to a client receiving a timeout while trying to fetch a connection from the
client connection pool.

We recommend keeping the default minimum in-process and simultaneous usage values, and setting
`maxInProcessPerConnection` and `maxSimultaneousUsagePerConnection`
to the same value.

The value to set these parameters at is a function of query complexity and the
data model. A use case where the query returns a lot of data would require more
connection bandwidth per query and hence, should have lower values for the
parameters,
and a higher value for `maxConnectionPoolSize`.

By contrast, in a case where the query returns a smaller amount of data,
`maxInProcessPerConnection` and `maxSimultaneousUsagePerConnection`
should be set to a higher value than `maxConnectionPoolSize`.
