# get-connection

The **get-connection** command returns the status of the service link
connection between the Outposts server and the Outpost service in the AWS Region for the
Outposts server.

**Syntax**

```
`Outpost>`get-connection [`index`]
```

**Parameters**

This command takes an optional connection index. The valid values are 0 and

1.

###### Example output: Successful connection

```
keys_exchanged: True
connection_established: True
exchange_active: False
primary_peer: `xx.xx.xx.xx:xxx`
primary_status: success
primary_connection_id: `a1b2c3d4567890abcdefEXAMPLE11111`
primary_handshake_age: `1111111111`
primary_server_public_key: `AKIAIOSFODNN7EXAMPLE`
primary_client_public_key: `AKIAI44QH8DHBEXAMPLE`
primary_server_endpoint: `xx.xx.xx.xx:xxx`
secondary_peer: `xx.xxx.xx.xxx:xxx`
secondary_status: success
secondary_connection_id: `a1b2c3d4567890abcdefEXAMPLE22222`
secondary_handshake_age: `1111111111`
secondary_server_public_key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
secondary_client_public_key: `je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY`
secondary_server_endpoint: `xx.xxx.xx.xxx:xxx`
timestamp: `2023-02-22T22:19:28Z`
checksum: `0x83FA0123`
```

###### Note

- If `exchange_active` is `True`, the connection is still
  establishing. Retry in 5 minutes.
- If `keys_exchanged` or `connection_established` is
  `False`, and if `exchange_active` is `True`, the
  connection is still establishing. Retry in 5 minutes.
  If the issue persists after 1 hour, contact Support.
