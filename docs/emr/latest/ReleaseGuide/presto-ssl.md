# Using SSL/TLS and configuring LDAPS with Presto on

Amazon EMR

With Amazon EMR release version 5.6.0 and later, you can enable SSL/TLS to help [secure
internal communication](https://prestodb.io/docs/current/security/internal-communication.html "https://prestodb.io/docs/current/security/internal-communication.html") between Presto nodes. You do this by setting up a
security configuration for in-transit encryption. For more information, see [Encryption options](../ManagementGuide/emr-data-encryption-options.md "../ManagementGuide/emr-data-encryption-options.md") and
[Use security
configurations to set up cluster security](../ManagementGuide/emr-security-configurations.md "../ManagementGuide/emr-security-configurations.md") in the
_Amazon EMR Management Guide_.

When you use a security configuration with in-transit encryption, Amazon EMR does the
following for Presto:

- Distributes the encryption artifacts, or certificates, that you specify for
  in-transit encryption throughout the Presto cluster. For more information, see
  [Providing certificates for in-transit data encryption](../ManagementGuide/emr-encryption-enable.md#emr-encryption-certificates "../ManagementGuide/emr-encryption-enable.md#emr-encryption-certificates").
- Sets the following properties using the `presto-config`
  configuration classification, which corresponds to the
  `config.properties` file for Presto:

      + Sets `http-server.http.enabled` to `false` on
       all nodes, which disables HTTP in favor of HTTPS. This requires you to
       provide certificates that work for public and private DNS when setting
       up the security configuration for in-transit encryption. One way to do
       this is to use SAN (Subject Alternative Name) certificates which support
       multiple domains.
      + Sets `http-server.https.*` values. For configuration
       details, see [LDAP
       authentication](https://prestodb.io/docs/current/security/ldap.html "https://prestodb.io/docs/current/security/ldap.html") in Presto documentation.

  In addition, with Amazon EMR release version 5.10.0 and later, you can set up [LDAP
  authentication](https://prestodb.io/docs/current/security/ldap.html "https://prestodb.io/docs/current/security/ldap.html") for client connections to the Presto coordinator using HTTPS.
  This setup uses secure LDAP (LDAPS). TLS must be enabled on your LDAP server, and the
  Presto cluster must use a security configuration with in-transit data encryption
  enabled. Additional configuration is required. The configuration options are different
  depending on the release version of Amazon EMR that you use. For more information, see [Using LDAP authentication for Presto on
  Amazon EMR](emr-presto-ldap.md "emr-presto-ldap.md").

Presto on Amazon EMR uses port 8446 for internal HTTPS by default. The port used for
internal communication must be the same port used for client HTTPS access to the Presto
coordinator. The `http-server.https.port` property in the
`presto-config` configuration classification specifies the port.
