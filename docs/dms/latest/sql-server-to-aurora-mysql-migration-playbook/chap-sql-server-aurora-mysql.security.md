# Column encryption for Aurora MySQL

This topic provides reference information about encryption and decryption functions in SQL Server and Amazon Aurora MySQL. You can use these functions to secure sensitive data in your database, such as individual column contents or application user security tokens.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Three star feature compatibility | No automation                      | N/A                       | Difference.     |

## SQL Server Usage

SQL Server provides encryption and decryption functions to secure the content of individual columns. The following list identifies common encryption functions:

- EncryptByKey and DecryptByKey.
- EncryptByCert and DecruptByCert.
- EncryptByPassPhrase and DecruptByPassPhrase.
- EncryptByAsymKey and DecryptByAsymKey.

You can use these functions anywhere in your code; they aren’t limited to encrypting table columns. A common use case is to increase run time security by encrypting of application user security tokens passed as parameters.

These functions follow the general SQL Server encryption hierarchy, which in turn use the Windows Server Data Protection API.

Symmetric encryption and decryption consume minimal resources and can be used for large data sets.

###### Note

This section doesn’t cover Transparent Data Encryption (TDE) or AlwaysEncrypted end-to-end encryption.

### Syntax

The following example includes the general syntax for EncryptByKey and DecryptByKey.

```
EncryptByKey ( <key GUID> , { 'text to be encrypted' }, { <use authenticator flag>}, { <authenticator> } );
```

```
DecryptByKey ( 'Encrypted Text' , <use authenticator flag>, { <authenticator> )
```

### Examples

The following example demonstrates how to encrypt an employee Social Security Number.

The following example creates a database master key.

```
USE MyDatabase;
CREATE MASTER KEY
ENCRYPTION BY PASSWORD = '<MyPassword>';
```

The following examples create a certificate and a key.

```
CREATE CERTIFICATE Cert01
WITH SUBJECT = 'SSN';
```

```
CREATE SYMMETRIC KEY SSN_Key
WITH ALGORITHM = AES_256
ENCRYPTION BY CERTIFICATE Cert01;
```

The following example creates an employees table.

```
CREATE TABLE Employees
(
    EmployeeID INT PRIMARY KEY,
    SSN_encrypted VARBINARY(128) NOT NULL
);
```

Open the symmetric key for encryption.

```
OPEN SYMMETRIC KEY SSN_Key
DECRYPTION BY CERTIFICATE Cert01;
```

Insert the encrypted data.

```
INSERT INTO Employees (EmployeeID, SSN_encrypted)
VALUES
(1, EncryptByKey(Key_GUID('SSN_Key') , '1112223333', 1, HashBytes('SHA1', CONVERT(VARBINARY, 1)));
```

```
SELECT EmployeeID,
CONVERT(CHAR(10), DecryptByKey(SSN, 1 , HashBytes('SHA1', CONVERT(VARBINARY, EmployeeID)))) AS SSN
FROM Employees;

EmployeeID  SSN_Encrypted              SSN
1           0x00F983FF436E32418132...  1112223333
```

For more information, see [Encrypt a Column of Data](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data?view=sql-server-ver15") and [Encryption Hierarchy](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/encryption-hierarchy?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/encryption-hierarchy?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) provides encryption and decryption functions similar to SQL Server with a much less elaborate security hierarchy that is easier to manage.

The encryption functions require the actual key as a string, so you must take extra measures to protect the data. For example, hashing the key values on the client.

Aurora MySQL supports the AES and DES encryption algorithms. You can use the following functions for data encryption and decryption:

- `AES_DECRYPT`
- `AES_ENCRYPT`
- `DES_DECRYPT`
- `DEC_ENCRYPT`

###### Note

The `ENCRYPT`, `DECRYPT`, `ENCODE`, and `DECODE` functions are deprecated beginning with MySQL version 5.7.2 and 5.7.6. Asymmetric encryption isn’t supported in Aurora MySQL.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL 8 supports FIPS mode if compiled using OpenSSL and an OpenSSL library and FIPS Object Module are available at runtime. FIPS mode imposes conditions on cryptographic operations such as restrictions on acceptable encryption algorithms or requirements for longer key lengths. For more information, see [FIPS Support](https://dev.mysql.com/doc/refman/8.0/en/fips-mode.html "https://dev.mysql.com/doc/refman/8.0/en/fips-mode.html") in the _MySQL documentation_.

### Syntax

The following example shows the general syntax for the encryption functions:

```
[A|D]ES_ENCRYPT(<string to be encrypted>, <key string> [,<initialization vector>])
[A|D]ES_DECRYPT(<encrypted string>, <key string> [,<initialization vector>])
```

For more information, see [AES_ENCRYPT](https://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html#function_aes-encrypt "https://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html#function_aes-encrypt") in the _MySQL documentation_.

It is highly recommended to use the optional initialization vector to circumvent whole value replacement attacks. When encrypting column data, it is common to use an immutable key as the initialization vector. With this approach, decryption fails if a whole value moves to another row.

Consider using SHA2 instead of SHA1 or MD5 because there are known exploits available for the SHA1 and MD5. Passwords, keys, or any sensitive data passed to these functions from the client aren’t encrypted unless you are using an SSL connection. One benefit of using AWS IAM is that database connections are encrypted with SSL by default.

### Examples

The following examples demonstrate how to encrypt an employee Social Security Number.

The following example creates an employees table.

```
CREATE TABLE Employees
(
    EmployeeID INT NOT NULL PRIMARY KEY,
    SSN_Encrypted BINARY(32) NOT NULL
);
```

The following example inserts the encrypted data.

```
INSERT INTO Employees (EmployeeID, SSN_Encrypted)
VALUES (1, AES_ENCRYPT('1112223333', UNHEX(SHA2('MyPassword',512)), 1));
```

###### Note

Use the UNHEX function for more efficient storage and comparisons.

Verify decryption.

```
SELECT EmployeeID,
SSN_Encrypted,
AES_DECRYPT(SSN_Encrypted, UNHEX(SHA2('MyPassword',512)), EmployeeID) AS SSN
FROM Employees

EmployeeID SSN_Encrypted     SSN
1          ` ©> +yp°øýNZ~Gø  1112223333
```

For more information, see [Encryption and Compression Functions](https://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html "https://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html") in the _MySQL documentation_.
