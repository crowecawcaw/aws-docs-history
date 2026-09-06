

# Turning off TDE for RDS for SQL Server
<a name="TDE.Disabling"></a>

To turn off TDE for an RDS for SQL Server DB instance, first make sure that there are no encrypted objects left on the DB instance. To do so, either decrypt the objects or drop them. If any encrypted objects exist on the DB instance, you can't turn off TDE for the DB instance. If a user TDE certificate for encryption was restored (imported), then it should be dropped. When you use the console to remove the TDE option from an option group, the console indicates that it's processing. In addition, an error event is created if the option group is associated with an encrypted DB instance or DB snapshot.

The following example removes the TDE encryption from a database called `customerDatabase`. 

```
 1. ------------- Removing TDE ----------------
 2. 
 3. USE [customerDatabase]
 4. GO
 5. 
 6. -- Turn off encryption of the database
 7. ALTER DATABASE [customerDatabase]
 8. SET ENCRYPTION OFF
 9. GO
10. 
11. -- Wait until the encryption state of the database becomes 1. The state is 5 (Decryption in progress) for a while
12. SELECT db_name(database_id) as DatabaseName, * FROM sys.dm_database_encryption_keys
13. GO
14. 
15. -- Drop the DEK used for encryption
16. DROP DATABASE ENCRYPTION KEY
17. GO
18. 
19. -- Drop a user TDE certificate if it was restored (imported)
20. EXECUTE msdb.dbo.rds_drop_tde_certificate @certificate_name='UserTDECertificate_certificate_name';
21. 
22. -- Alter to SIMPLE Recovery mode so that your encrypted log gets truncated
23. USE [master]
24. GO
25. ALTER DATABASE [customerDatabase] SET RECOVERY SIMPLE
26. GO
```

When all objects are decrypted, you have two options:

1. You can modify the DB instance to be associated with an option group without the TDE option.

1. You can remove the TDE option from the option group.