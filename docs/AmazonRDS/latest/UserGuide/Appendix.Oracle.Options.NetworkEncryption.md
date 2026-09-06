

# Oracle native network encryption
<a name="Appendix.Oracle.Options.NetworkEncryption"></a>

Amazon RDS supports Oracle native network encryption (NNE). With the `NATIVE_NETWORK_ENCRYPTION` option, you can encrypt data as it moves to and from a DB instance. Amazon RDS supports NNE for all editions of Oracle Database.

A detailed discussion of Oracle native network encryption is beyond the scope of this guide, but you should understand the strengths and weaknesses of each algorithm and key before you decide on a solution for your deployment. For information about the algorithms and keys that are available through Oracle native network encryption, see [Configuring network data encryption and integrity](https://docs.oracle.com/en/database/oracle/oracle-database/19/asoag/configuring-network-data-encryption-and-integrity.html) in the Oracle documentation. For more information about AWS security, see the [AWS security center](https://aws.amazon.com/security).

**Note**  
You can use Native Network Encryption or Secure Sockets Layer, but not both. For more information, see [Oracle Secure Sockets Layer](Appendix.Oracle.Options.SSL.md). 

**Topics**
+ [NATIVE\_NETWORK\_ENCRYPTION option settings](Oracle.Options.NNE.Options.md)
+ [Adding the NATIVE\_NETWORK\_ENCRYPTION option](Oracle.Options.NNE.Add.md)
+ [Verifying that NNE is active](#Oracle.Options.NNE.Verify)
+ [Setting NNE values in the sqlnet.ora](Oracle.Options.NNE.Using.md)
+ [Modifying NATIVE\_NETWORK\_ENCRYPTION option settings](Oracle.Options.NNE.ModifySettings.md)
+ [Removing the NATIVE\_NETWORK\_ENCRYPTION option](Oracle.Options.NNE.Remove.md)

## Verifying that NNE is active
<a name="Oracle.Options.NNE.Verify"></a>

After connecting to your DB instance, query `V$SESSION_CONNECT_INFO` for your session to confirm that native network encryption is active:

```
SELECT NETWORK_SERVICE_BANNER
FROM V$SESSION_CONNECT_INFO
WHERE SID = SYS_CONTEXT('USERENV', 'SID');
```

If NNE is active, the results include a banner that contains `encryption service adapter`. The banner text shows the negotiated algorithm, for example `AES256`. If checksumming is also enabled, the results include a `crypto-checksumming service adapter` banner. If the query returns no encryption service adapter banner, the connection is not using native network encryption.