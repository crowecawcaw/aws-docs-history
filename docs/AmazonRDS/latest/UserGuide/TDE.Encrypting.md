

# Encrypting data on RDS for SQL Server
<a name="TDE.Encrypting"></a>

When the TDE option is added to an option group, Amazon RDS generates a certificate that's used in the encryption process. You can then use the certificate to run SQL statements that encrypt data in a database on the DB instance.

The following example uses the RDS-created certificate called `RDSTDECertificateName` to encrypt a database called `myDatabase`.

```
 1. ---------- Turning on TDE -------------
 2. 
 3. -- Find an RDS TDE certificate to use
 4. USE [master]
 5. GO
 6. SELECT name FROM sys.certificates WHERE name LIKE 'RDSTDECertificate%'
 7. GO
 8. 
 9. USE [myDatabase]
10. GO
11. -- Create a database encryption key (DEK) using one of the certificates from the previous step
12. CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES_256
13. ENCRYPTION BY SERVER CERTIFICATE [{{RDSTDECertificateName}}]
14. GO
15. 
16. -- Turn on encryption for the database
17. ALTER DATABASE [{{myDatabase}}] SET ENCRYPTION ON
18. GO
19. 
20. -- Verify that the database is encrypted
21. USE [master]
22. GO
23. SELECT name FROM sys.databases WHERE is_encrypted = 1
24. GO
25. SELECT db_name(database_id) as DatabaseName, * FROM sys.dm_database_encryption_keys
26. GO
```

The time that it takes to encrypt a SQL Server database using TDE depends on several factors. These include the size of the DB instance, whether the instance uses Provisioned IOPS storage, the amount of data, and other factors.