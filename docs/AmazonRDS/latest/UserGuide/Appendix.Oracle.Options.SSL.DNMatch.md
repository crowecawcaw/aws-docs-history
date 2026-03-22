# Enforcing a DN match with an SSL connection

You can use the Oracle parameter `SSL_SERVER_DN_MATCH` to enforce that
the distinguished name (DN) for the database server matches its service name. If you
enforce the match verifications, then SSL ensures that the certificate is from the
server. If you don't enforce the match verification, then SSL performs the
check but allows the connection, regardless if there is a match. If you do not
enforce the match, you allow the server to potentially fake its identity.

To enforce DN matching, add the DN match property and use the connection string specified below.

Add the property to the client connection to enforce DN matching.

```
properties.put("oracle.net.ssl_server_dn_match", "TRUE");
```

Use the following connection string to enforce DN matching when using SSL.

```
final String connectionString = String.format(
    "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCPS)(HOST=%s)(PORT=%d))" +
    "(CONNECT_DATA=(SID=%s))" +
    "(SECURITY = (SSL_SERVER_CERT_DN =
\"C=US,ST=Washington,L=Seattle,O=Amazon.com,OU=RDS,CN=%s\")))",
    DB_SERVER_NAME, SSL_PORT, DB_SID, DB_SERVER_NAME);
```
