# Setting NNE values in the sqlnet.ora

With Oracle native network encryption, you can set network encryption on the server side and client side. The
client is the computer used to connect to the DB instance. You can specify the following client settings in the
sqlnet.ora:

- `SQLNET.ALLOW_WEAK_CRYPTO`
- `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS`
- `SQLNET.CRYPTO_CHECKSUM_CLIENT`
- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT`
- `SQLNET.ENCRYPTION_CLIENT`
- `SQLNET.ENCRYPTION_TYPES_CLIENT`
  For information, see [Configuring network data encryption and integrity for Oracle servers and clients](http://docs.oracle.com/cd/E11882_01/network.112/e40393/asoconfg.htm "http://docs.oracle.com/cd/E11882_01/network.112/e40393/asoconfg.htm") in the Oracle
  documentation.

Sometimes, the DB instance rejects a connection request from an application. For example, a rejection can occur
when the encryption algorithms on the client and on the server don't match. To test Oracle native network
encryption, add the following lines to the sqlnet.ora file on the client:

```
DIAG_ADR_ENABLED=off
TRACE_DIRECTORY_CLIENT=/tmp
TRACE_FILE_CLIENT=nettrace
TRACE_LEVEL_CLIENT=16
```

When a connection is attempted, the preceding lines generate a trace file on the client called
`/tmp/nettrace*`. The trace file contains information about the connection. For more information
about connection-related issues when you are using Oracle Native Network Encryption, see [About negotiating
encryption and integrity](http://docs.oracle.com/cd/E11882_01/network.112/e40393/asoconfg.htm#autoId12 "http://docs.oracle.com/cd/E11882_01/network.112/e40393/asoconfg.htm#autoId12") in the Oracle Database documentation.
