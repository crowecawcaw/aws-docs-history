# Column encryption for Aurora PostgreSQL

This topic provides reference information comparing encryption and decryption capabilities between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can understand the encryption functions available in SQL Server and their counterparts in Aurora PostgreSQL. The topic highlights the similarities in functionality while noting the differences in syntax and options. It introduces the encryption hierarchy in SQL Server and the various encryption algorithms supported by Aurora PostgreSQL.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                       |
| -------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Syntax and option differences, similar functionality. |

## SQL Server Usage

SQL Server provides encryption and decryption functions to secure the content of individual columns. The following list identifies common encryption functions:

- `EncryptByKey` and `DecryptByKey`.
- `EncryptByCert` and `DecryptByCert`.
- `EncryptByPassPhrase` and `DecryptByPassPhrase`.
- `EncryptByAsymKey` and `DecryptByAsymKey`.

You can use these functions anywhere in your code; they aren’t limited to encrypting table columns. A common use case is to increase run time security by encrypting of application user security tokens passed as parameters.

These functions follow the general SQL Server encryption hierarchy, which in turn use the Windows Server Data Protection API.

Symmetric encryption and decryption consume minimal resources. You can use them for large data sets.

###### Note

This section doesn’t cover Transparent Data Encryption (TDE) or Always Encrypted end-to-end encryption.

### Syntax

General syntax for `EncryptByKey` and `DecryptByKey`:

```
EncryptByKey ( <key GUID> , { 'text to be encrypted' }, { <use authenticator flag>}, { <authenticator> } );
```

```
DecryptByKey ( 'Encrypted Text' , <use authenticator flag>, { <authenticator> )
```

### Examples

The following examples demonstrate how to encrypt an employee Social Security Number.

Create a database master key.

```
USE MyDatabase;
CREATE MASTER KEY
ENCRYPTION BY PASSWORD = '<MyPassword>';
```

Create a certificate and a key.

```
CREATE CERTIFICATE Cert01
WITH SUBJECT = 'SSN';
```

```
CREATE SYMMETRIC KEY SSN_Key
WITH ALGORITHM = AES_256
ENCRYPTION BY CERTIFICATE Cert01;
```

Create an `Employees` table.

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

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) provides encryption and decryption functions similar to SQL Server using the `pgcrypto` extension. To use this feature, you must first install the `pgcrypto` extension.

```
CREATE EXTENSION pgcrypto;
```

Aurora PostgreSQL supports many encryption algorithms:

- MD5
- SHA1
- SHA224/256/384/512
- Blowfish
- AES
- Raw encryption
- PGP Symmetric encryption
- PGP Public-Key encryption

This section describes the use of `PGP_SYM_ENCRYPT` and `PGP_SYM_DECRYPT`, but there are many more options available. For more information, see the link and the end of this section.

### Syntax

Encrypt columns using `PGP_SYM_ENCRYPT`.

```
pgp_sym_encrypt(data text, psw text [, options text ]) returns bytea
pgp_sym_decrypt(msg bytea, psw text [, options text ]) returns text
```

### Examples

The following examples demonstrate how to encrypt an employee’s Social Security Number.

Create the `users` table.

```
CREATE TABLE users (id SERIAL, name VARCHAR(60), pass TEXT);
```

Insert the encrypted data.

```
INSERT INTO users (name, pass) VALUES ('John',PGP_SYM_ENCRYPT('123456', 'AES_KEY'));
```

Verify the data is encrypted.

```
SELECT * FROM users;

id  name  pass
2   John  \xc30d04070302c30d07ff8b3b12f26ad233015a72bab4d3bb73f5a80d5187b1b043149dd961da58e76440ca9eb4a5f7483cc8ce957b47e39b143cf4b1192bb39
```

Query using the encryption key.

```
SELECT name, PGP_SYM_DECRYPT(pass::bytea, 'AES_KEY') as pass
FROM users WHERE (name LIKE '%John%');

name  pass
John  123456
```

Update the data.

```
UPDATE users SET (name, pass) = ('John',PGP_SYM_ENCRYPT('0000', 'AES_KEY')) WHERE id='2';

SELECT name, PGP_SYM_DECRYPT(pass::bytea, 'AES_KEY') as pass
  FROM users WHERE (name LIKE '%John%');

name  pass
John  0000
```

For more information, see [pgcrypto](https://www.postgresql.org/docs/13/pgcrypto.html "https://www.postgresql.org/docs/13/pgcrypto.html") in the _PostgreSQL documentation_.
