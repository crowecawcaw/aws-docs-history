# start-connection

The **start-connection** command initiates a connection with the Outpost
service in the Region for the Outposts server. This command sources the Signature Version 4 (SigV4)
credentials from the environment variables you loaded with **export**. The
connection runs asynchronously and returns immediately. To check the status of the connection,
use [get-connection](oct-get-connection.md "oct-get-connection.md").

**Syntax**

```
`Outpost>`start-connection [`index`]
```

**Parameters**

This command takes an optional index. The valid values are 0 and 1.

###### Example output: Connection is started

```
is_started: True
asset_id: `asset-id`
connection_id: `connection-id`
timestamp: `2021-10-01T23:30:26Z`
checksum: `checksum`
```
