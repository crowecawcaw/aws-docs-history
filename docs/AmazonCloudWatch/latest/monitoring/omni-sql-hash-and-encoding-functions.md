

# Hash and encoding functions

Use these functions to hash a string, or to encode a string as text and decode it back. For information about other functions, see [Operators and functions](omni-sql-operators-and-functions.md).

The following table describes the hash and encoding functions.


| Function | Description | 
| --- | --- | 
| md5(s) | Returns the MD5 hash as a hexadecimal string. | 
| sha256(s), sha512(s) | Returns the SHA-256 or SHA-512 hash as binary. To compare it with a hexadecimal string, wrap it in encode(..., 'hex'). | 
| digest(s, algorithm) | Returns a hash with the algorithm that you specify, such as 'sha256'. | 
| encode(s, format) | Encodes a string as 'base64' or 'hex' text. | 
| decode(s, format) | Decodes 'base64' or 'hex' text back to binary. | 

The following example counts requests for each user. It identifies each user by a SHA-256 hash of the user ID.

```sql
SELECT encode(sha256(user_id), 'hex') AS user_key, COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
GROUP BY 1
```