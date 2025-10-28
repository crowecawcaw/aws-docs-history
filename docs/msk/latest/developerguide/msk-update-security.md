# Update security settings of a Amazon MSK cluster

Use the [UpdateSecurity](../../1.0/apireference/clusters-clusterarn-security.md#UpdateSecurity "../../1.0/apireference/clusters-clusterarn-security.md#UpdateSecurity") Amazon MSK operation to update the authentication and client-broker encryption
settings of your MSK cluster. You can also update the Private Security
Authority used to sign certificates for mutual TLS authentication. You can't change the
in-cluster (broker-to-broker) encryption setting.

The cluster must be in the `ACTIVE` state for you to update its security
settings.

If you turn on authentication using IAM, SASL, or TLS, you must also turn on
encryption between clients and brokers. The following table shows the possible
combinations.

| Authentication  | Client-broker encryption options | Broker-broker encryption |
| --------------- | -------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unauthenticated | TLS, PLAINTEXT, TLS_PLAINTEXT    | Can be on or off.        |
| mTLS            | TLS, TLS_PLAINTEXT               | Must be on.              |
| SASL/SCRAM      | TLS                              | Must be on.              |
| SASL/IAM        | TLS                              | Must be on.              | When client-broker encryption is set to `TLS_PLAINTEXT` and client-authentication is set to `mTLS`, Amazon MSK creates two types of listeners for clients to connect to: one listener for clients to connect using mTLS authentication with TLS Encryption, and another for clients to connect without authentication or encryption (plaintext). For more information about security settings, see [Security in Amazon MSK](security.md "security.md"). |
