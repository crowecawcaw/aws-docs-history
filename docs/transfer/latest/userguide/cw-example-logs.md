# Example CloudWatch log entries

This topic presents example log entries.

###### Topics

- [Example transfer sessions log entries](#session-log-examples "#session-log-examples")
- [Example log entries for SFTP
  connectors](#example-sftp-connector-logs "#example-sftp-connector-logs")
- [Example log entries for VPC Lattice
  connectors](#example-vpc-lattice-connector-logs "#example-vpc-lattice-connector-logs")
- [Example log entries for Key exchange algorithm
  failures](#example-kex-logs "#example-kex-logs")

## Example transfer sessions log entries

In this example, an SFTP user connects to a Transfer Family server, uploads a file, then
disconnects from the session.

The following log entry reflects an SFTP user connecting to a Transfer Family server.

```
{
   "role": "arn:aws:iam::500655546075:role/transfer-s3",
   "activity-type": "CONNECTED",
   "ciphers": "chacha20-poly1305@openssh.com,chacha20-poly1305@openssh.com",
   "client": "SSH-2.0-OpenSSH_7.4",
   "source-ip": "52.94.133.133",
   "resource-arn": "arn:aws:transfer:us-east-1:500655546075:server/s-3fe215d89f074ed2a",
   "home-dir": "/test/log-me",
   "ssh-public-key": "AAAAC3NzaC1lZDI1NTE5AAAAIA9OY0qV6XYVHaaOiWAcj2spDJVbgjrqDPY4pxd6GnHl",
   "ssh-public-key-fingerprint": "SHA256:BY3gNMHwTfjd4n2VuT4pTyLOk82zWZj4KEYEu7y4r/0",
   "ssh-public-key-type": "ssh-ed25519",
   "user": "log-me",
   "kex": "ecdh-sha2-nistp256",
   "session-id": "9ca9a0e1cec6ad9d"
}
```

The following log entry reflects the SFTP user uploading a file into their Amazon S3
bucket.

```
{
   "mode": "CREATE|TRUNCATE|WRITE",
   "path": "/test/log-me/config-file",
   "activity-type": "OPEN",
   "resource-arn": "arn:aws:transfer:us-east-1:500655546075:server/s-3fe215d89f074ed2a",
   "session-id": "9ca9a0e1cec6ad9d"
}
```

The following log entries reflect the SFTP user disconnecting from their SFTP session.
First, the client closes the connection to the bucket, and then the client disconnects
the SFTP session.

```
{
   "path": "/test/log-me/config-file",
   "activity-type": "CLOSE",
   "resource-arn": "arn:aws:transfer:us-east-1:500655546075:server/s-3fe215d89f074ed2a",
   "bytes-in": "121",
   "session-id": "9ca9a0e1cec6ad9d"
}

{
   "activity-type": "DISCONNECTED",
   "resource-arn": "arn:aws:transfer:us-east-1:500655546075:server/s-3fe215d89f074ed2a",
   "session-id": "9ca9a0e1cec6ad9d"
}
```

###### Note

The available activity types are as follows:
`AUTH_FAILURE`, `CONNECTED`,
`DISCONNECTED`, `ERROR`,
`EXIT_REASON`, `CLOSE`,
`CREATE_SYMLINK`, `DELETE`,
`MKDIR`, `OPEN`, `PARTIAL_CLOSE`,
`RENAME`, `RMDIR`, `SETSTAT`,
`TLS_RESUME_FAILURE`.

## Example log entries for SFTP

connectors

This section contains example logs for both a successful and an unsuccessful transfer.
Logs are generated to a log group named
`/aws/transfer/`connector-id``,
 where `connector-id`is the identifier for your SFTP connector.
 Log entries for SFTP connectors are generated when you run either a
`StartFileTransfer`or`StartDirectoryListing` command.

This log entry is for a transfer that completed successfully.

```
{
    "operation": "RETRIEVE",
    "timestamp": "2023-10-25T16:33:27.373720Z",
    "connector-id": "`connector-id`",
    "transfer-id": "`transfer-id`",
    "file-transfer-id": "`transfer-id`/`file-transfer-id`",
    "url": "sftp://192.0.2.0",
    "file-path": "/remotebucket/remotefilepath",
    "status-code": "COMPLETED",
    "start-time": "2023-10-25T16:33:26.945481Z",
    "end-time": "2023-10-25T16:33:27.159823Z",
    "account-id": "480351544584",
    "connector-arn": "arn:aws:transfer:us-east-1:`account-id`:connector/`connector-id`",
    "local-directory-path": "/connectors-localbucket",
    "bytes": 514,
    "egress-type": "SERVICE_MANAGED"
}
```

This log entry is for a transfer that timed out, and thus was not completed
successfully.

```
{
    "operation": "RETRIEVE",
    "timestamp": "2023-10-25T22:33:47.625703Z",
    "connector-id": "`connector-id`",
    "transfer-id": "`transfer-id`",
    "file-transfer-id": "`transfer-id`/`file-transfer-id`",
    "url": "sftp://192.0.2.0",
    "file-path": "/remotebucket/remotefilepath",
    "status-code": "FAILED",
    "failure-code": "TIMEOUT_ERROR",
    "failure-message": "Transfer request timeout.",
    "account-id": "480351544584",
    "connector-arn": "arn:aws:transfer:us-east-1:`account-id`:connector/`connector-id`",
    "local-directory-path": "/connectors-localbucket",
    "egress-type": "SERVICE_MANAGED"
}
```

This log entry is for a SEND operation that succeeds.

```
{
    "operation": "SEND",
    "timestamp": "2024-04-24T18:16:12.513207284Z",
    "connector-id": "`connector-id`",
    "transfer-id": "`transfer-id`",
    "file-transfer-id": "`transfer-id`/`file-transfer-id`",
    "url": "sftp://`server-id`.server.transfer.us-east-1.amazonaws.com",
    "file-path": "/amzn-s3-demo-bucket/my-test-folder/connector-metrics-us-east-1-2024-01-02.csv",
    "status-code": "COMPLETED",
    "start-time": "2024-04-24T18:16:12.295235884Z",
    "end-time": "2024-04-24T18:16:12.461840732Z",
    "account-id": "255443218509",
    "connector-arn": "arn:aws:transfer:us-east-1:`account-id`:connector/`connector-id`",
    "bytes": 275,
    "egress-type": "SERVICE_MANAGED"
}
```

Descriptions for some key fields in the previous log examples.

- `timestamp` represents when the log is added to CloudWatch.
  `start-time` and `end-time` correspond to when the
  connector actually starts and finishes a transfer.
- `transfer-id` is a unique identifier that is assigned for each
  `start-file-transfer` request. If the user passes multiple file
  paths in a single `start-file-transfer` API operation, all the files
  share the same `transfer-id`.
- `file-transfer-id` is a unique value generated for each file
  transferred. Note that the initial portion of the `file-transfer-id`
  is the same as `transfer-id`.

## Example log entries for VPC Lattice

connectors

This section contains example logs for VPC Lattice connectors. For VPC Lattice
connectors, logs include additional fields that provide information about the connector
configuration and network setup.

This log entry is for a VPC Lattice connector SEND operation that completed
successfully.

```
{
  "operation": "SEND",
  "timestamp": "2025-09-05T14:20:19.577192454Z",
  "connector-id": "`connector-id`",
  "transfer-id": "`transfer-id`",
  "file-transfer-id": "`transfer-id`/`file-transfer-id`",
  "file-path": ""/amzn-s3-demo-bucket/my-test-folder/connector-vpc-lattice-us-east-1-2025-03-22.csv"",
  "status-code": "COMPLETED",
  "start-time": "2025-09-05T14:20:19.434072509Z",
  "end-time": "2025-09-05T14:20:19.481453346Z",
  "account-id": "`account-id`",
  "connector-arn": "arn:aws:transfer:us-east-1:`account-id`:connector/`connector-id`",
  "remote-directory-path": "/test-bucket/test-folder/",
  "bytes": 262,
  "egress-type": "VPC_LATTICE",
  "vpc-lattice-resource-configuration-arn": "arn:aws:vpc-lattice:us-east-1:`account-id`:resourceconfiguration/`resource-configuration-arn-id`,
  "vpc-lattice-port-number": 22
}
```

VPC Lattice connector logs include the following additional fields:

- `egress-type` - Type of egress configuration for the
  connector
- `vpc-lattice-resource-configuration-arn` - ARN of the VPC Lattice
  Resource Configuration that defines the target SFTP server location
- `vpc-lattice-port-number` - Port number for connecting to the SFTP
  server through VPC Lattice

## Example log entries for Key exchange algorithm

failures

This section contains example logs where the Key exchange algorithm (KEX) failed.
These are examples from the **ERRORS** log stream for structured
logs.

This log entry is an example where there is a host key type error.

```
{
    "activity-type": "KEX_FAILURE",
    "source-ip": "999.999.999.999",
    "resource-arn": "arn:aws:transfer:us-east-1:999999999999:server/s-999999999999999999",
    "message": "no matching host key type found",
    "kex": "ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ssh-ed25519,ssh-rsa,ssh-dss"
}
```

This log entry is an example where there is a KEX mismatch.

```
{
    "activity-type": "KEX_FAILURE",
    "source-ip": "999.999.999.999",
    "resource-arn": "arn:aws:transfer:us-east-1:999999999999:server/s-999999999999999999",
    "message": "no matching key exchange method found",
    "kex": "diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group14-sha256"
}
```
