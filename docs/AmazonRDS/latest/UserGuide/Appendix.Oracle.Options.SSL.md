# Troubleshooting SSL

connections

You might query your database and receive the `ORA-28860` error.

```
ORA-28860: Fatal SSL error
28860. 00000 - "Fatal SSL error"
*Cause: An error occurred during the SSL connection to the peer. It is likely that this side sent data which the peer rejected.
*Action: Enable tracing to determine the exact cause of this error.
```

This error occurs when the client attempts to connect using a version of TLS that the
server doesn't support. To avoid this error, edit the sqlnet.ora and set
`SSL_VERSION` to the correct TLS version. For more information, see
[Oracle Support Document 2748438.1](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2748438.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=2748438.1") in My Oracle Support.
