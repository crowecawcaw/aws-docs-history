# Aurora MySQL database engine updates: 2016-10-26 (version 1.8.1) (Deprecated)

**Version:** 1.8.1

## Improvements

- Fixed an issue where bulk inserts that use triggers that invoke AWS Lambda
  procedures fail.
- Fixed an issue where catalog migration fails when autocommit is off
  globally.
- Resolved a connection failure to Aurora when using SSL and improved
  Diffie-Hellman group to deal with LogJam attacks.

## Integration of MySQL bug fixes

- OpenSSL changed the Diffie-Hellman key length parameters due to the LogJam
  issue. (Bug #18367167)
