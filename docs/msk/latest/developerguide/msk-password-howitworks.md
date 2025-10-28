# How sign-in credentials authentication works

Sign-in credentials authentication for Amazon MSK uses SASL/SCRAM (Simple Authentication
and Security Layer/ Salted Challenge Response Mechanism) authentication. To set up
sign-in credentials authentication for a cluster, you create a Secret resource in
[AWS
Secrets Manager](../../../secretsmanager.md "../../../secretsmanager.md"), and associate sign-in credentials with that secret.

SASL/SCRAM is defined in [RFC
5802](https://tools.ietf.org/html/rfc5802 "https://tools.ietf.org/html/rfc5802"). SCRAM uses secured hashing algorithms, and does not transmit plaintext
sign-in credentials between client and server.

###### Note

When you set up SASL/SCRAM authentication for your cluster, Amazon MSK turns on
TLS encryption for all traffic between clients and brokers.
