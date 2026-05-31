# Oracle native network encryption

Amazon RDS supports Oracle native network encryption (NNE). With the
`NATIVE_NETWORK_ENCRYPTION` option, you can encrypt data as it moves to and
from a DB instance. Amazon RDS supports NNE for all editions of Oracle Database.

A detailed discussion of Oracle native network encryption is beyond the scope of this guide, but you should
understand the strengths and weaknesses of each algorithm and key before you decide on a solution for your
deployment. For information about the algorithms and keys that are available through Oracle native network
encryption, see [Configuring network data encryption and integrity](https://docs.oracle.com/en/database/oracle/oracle-database/19/asoag/configuring-network-data-encryption-and-integrity.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/asoag/configuring-network-data-encryption-and-integrity.html") in the Oracle documentation. For more information about AWS
security, see the [AWS security center](https://aws.amazon.com/security "https://aws.amazon.com/security").

###### Note

You can use Native Network Encryption
or Secure Sockets Layer,
but not both.
For more information, see
[Oracle Secure Sockets Layer](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md").

###### Topics

- [NATIVE_NETWORK_ENCRYPTION option settings](Oracle.Options.NNE.Options.md "Oracle.Options.NNE.Options.md")
- [Adding the NATIVE_NETWORK_ENCRYPTION option](Oracle.Options.NNE.Add.md "Oracle.Options.NNE.Add.md")
- [Verifying that NNE is active](#Oracle.Options.NNE.Verify "#Oracle.Options.NNE.Verify")
- [Setting NNE values in the sqlnet.ora](Oracle.Options.NNE.Using.md "Oracle.Options.NNE.Using.md")
- [Modifying NATIVE_NETWORK_ENCRYPTION option settings](Oracle.Options.NNE.ModifySettings.md "Oracle.Options.NNE.ModifySettings.md")
- [Removing the NATIVE_NETWORK_ENCRYPTION option](Oracle.Options.NNE.Remove.md "Oracle.Options.NNE.Remove.md")

## Verifying that NNE is active

After connecting to your DB instance, run the following query to confirm your session is encrypted:

```
SELECT SYS_CONTEXT('USERENV', 'NETWORK_PROTOCOL') AS PROTOCOL,
       SYS_CONTEXT('USERENV', 'ENCRYPTION_TYPE') AS ENCRYPTION
FROM DUAL;
```

If NNE is active, the `ENCRYPTION` column shows the algorithm in use (for example, `AES256`). If it shows blank or NULL, the connection is not encrypted.
