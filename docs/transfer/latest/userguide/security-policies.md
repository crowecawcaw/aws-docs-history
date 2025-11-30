# Security policies for AWS Transfer Family servers

Server security policies in AWS Transfer Family allow you to limit the set of cryptographic
algorithms (message authentication codes (MACs), key exchanges (KEXs), cipher suites,
content encryption ciphers, and hash algorithms) associated with your server.

AWS Transfer Family supports post-quantum security policies that use hybrid key exchange algorithms,
combining traditional cryptographic methods with post-quantum algorithms to provide enhanced
security against future quantum computing threats. Details are provided in [Using hybrid post-quantum key exchange with
AWS Transfer Family](post-quantum-security-policies.md "post-quantum-security-policies.md").

For a list of supported cryptographic algorithms, see [Cryptographic algorithms](#cryptographic-algorithms "#cryptographic-algorithms"). For a
list of supported key algorithms for use with server host keys and service-managed user
keys, see [Managing SSH and PGP keys in Transfer Family](key-management.md "key-management.md").

###### Note

We strongly recommend updating your servers to our latest security policy.

- `TransferSecurityPolicy-2024-01` is the default security policy
  attached to your server when creating a server using the console, API, or
  CLI.
- If you create a Transfer Family server using CloudFormation and accept the default security
  policy, the server is assigned
  `TransferSecurityPolicy-2018-11`.
  If you are concerned about client compatibility, please affirmatively state which
  security policy you wish to use when creating or updating a server rather than using the
  default policy, which is subject to change. To change the security policy for a server,
  see [Edit the security policy](edit-server-config.md#edit-cryptographic-algorithm "edit-server-config.md#edit-cryptographic-algorithm").

For more information on security in Transfer Family, see the following blog posts:

- [Six tips to improve the security of your AWS Transfer Family server](https://aws.amazon.com/blogs/security/six-tips-to-improve-the-security-of-your-aws-transfer-family-server/ "https://aws.amazon.com/blogs/security/six-tips-to-improve-the-security-of-your-aws-transfer-family-server/")
- [How Transfer Family can help you build a secure, compliant managed file transfer
  solution](https://aws.amazon.com/blogs/security/how-transfer-family-can-help-you-build-a-secure-compliant-managed-file-transfer-solution/ "https://aws.amazon.com/blogs/security/how-transfer-family-can-help-you-build-a-secure-compliant-managed-file-transfer-solution/")

###### Topics

- [Cryptographic algorithms](#cryptographic-algorithms "#cryptographic-algorithms")
- [TransferSecurityPolicy-2024-01](#security-policy-transfer-2024-01 "#security-policy-transfer-2024-01")
- [TransferSecurityPolicy-SshAuditCompliant-2025-02](#security-policy-transferSecurityPolicy-SshAuditCompliant-2025-02 "#security-policy-transferSecurityPolicy-SshAuditCompliant-2025-02")
- [TransferSecurityPolicy-2023-05](#security-policy-transfer-2023-05 "#security-policy-transfer-2023-05")
- [TransferSecurityPolicy-2022-03](#security-policy-transfer-2022-03 "#security-policy-transfer-2022-03")
- [TransferSecurityPolicy-2020-06 and
  TransferSecurityPolicy-Restricted-2020-06](#security-policy-transfer-2020-06 "#security-policy-transfer-2020-06")
- [TransferSecurityPolicy-2018-11 and
  TransferSecurityPolicy-Restricted-2018-11](#security-policy-transfer-2018-11 "#security-policy-transfer-2018-11")
- [TransferSecurityPolicy-FIPS-2024-01/TransferSecurityPolicy-FIPS-2024-05](#security-policy-transfer-fips-2024-01 "#security-policy-transfer-fips-2024-01")
- [TransferSecurityPolicy-FIPS-2023-05](#security-policy-transfer-fips-2023-05 "#security-policy-transfer-fips-2023-05")
- [TransferSecurityPolicy-FIPS-2020-06](#security-policy-transfer-fips-2020-06 "#security-policy-transfer-fips-2020-06")
- [TransferSecurityPolicy-AS2Restricted-2025-07](#as2-restricted-policy "#as2-restricted-policy")
- [Post Quantum security policies](#pq-policies "#pq-policies")

## Cryptographic algorithms

For host keys, we support the following algorithms:

- `rsa-sha2-256`
- `rsa-sha2-512`
- `ecdsa-sha2-nistp256`
- `ecdsa-sha2-nistp384`
- `ecdsa-sha2-nistp521`
- `ssh-ed25519`

Additionally, the following security policies allow `ssh-rsa`:

- TransferSecurityPolicy-2018-11
- TransferSecurityPolicy-2020-06
- TransferSecurityPolicy-FIPS-2020-06
- TransferSecurityPolicy-FIPS-2023-05
- TransferSecurityPolicy-FIPS-2024-01
- TransferSecurityPolicy-PQ-SSH-FIPS-Experimental-2023-04

###### Note

It is important to understand the distinction between the RSA key type—which
is always `ssh-rsa`—and the RSA host key algorithm, which can be
any of the supported algorithms.

The following is a list of supported cryptographic algorithms for each security
policy.

###### Note

In the following table and policies, note the following use of algorithm
types.

- SFTP servers only use algorithms in the **SshCiphers**, **SshKexs**, and
  **SshMacs** sections.
- FTPS servers only use algorithms in the **TlsCiphers** section.
- FTP servers, since they don't use encryption, do not use any of these
  algorithms.
- AS2 servers only use algorithms in the **ContentEncryptionCiphers** and **HashAlgorithms** sections. These sections define algorithms
  used for encrypting and signing file content.
- The FIPS-2024-05 and FIPS-2024-01 security policies are identical, except
  that FIPS-2024-05 doesn't support the `ssh-rsa` algorithm.
- Transfer Family has introduced new restricted policies that closely parallel existing
  policies:

      + The TransferSecurityPolicy-Restricted-2018-11 and
       TransferSecurityPolicy-2018-11 security policies are identical,
       except that the restricted policy doesn't support the
       `chacha20-poly1305@openssh.com` cipher.
      + The TransferSecurityPolicy-Restricted-2020-06 and
       TransferSecurityPolicy-2020-06 security policies are identical,
       except that the restricted policy doesn't support the
       `chacha20-poly1305@openssh.com` cipher.

  \*In the following table, the
  `chacha20-poly1305@openssh.com` cipher is included in the
  non-restricted policy only,

| Security policy                         | 2024-01 | SshAuditCompliant-2025-02 | 2023-05 | 2022-03 | **2020-06**<br>**2020-06 restricted** | **FIPS-2024-05**<br>**FIPS-2024-01** | FIPS-2023-05 | FIPS-2020-06 | **2018-11**<br>**2018-11 restricted** | TransferSecurityPolicy-AS2Restricted-2025-07 |
| --------------------------------------- | ------- | ------------------------- | ------- | ------- | ------------------------------------- | ------------------------------------ | ------------ | ------------ | ------------------------------------- | -------------------------------------------- |
| **SshCiphers**                          |
| aes128-ctr                              | ♦       | ♦                         |         |         | ♦                                     | ♦                                    |              | ♦            | ♦                                     | ♦                                            |
| aes128-gcm@openssh.com                  | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| aes192-ctr                              | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| aes256-ctr                              | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| aes256-gcm@openssh.com                  | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| chacha20-poly1305@openssh.com           |         |                           |         |         | ♦\*                                   |                                      |              |              | ♦\*                                   |                                              |
| **SshKexs**                             |
| mlkem768x25519-sha256                   |         |                           |         |         |                                       |                                      |              |              |                                       | ♦                                            |
| mlkem768nistp256-sha256                 |         |                           |         |         |                                       |                                      |              |              |                                       | ♦                                            |
| mlkem1024nistp384-sha384                |         |                           |         |         |                                       |                                      |              |              |                                       | ♦                                            |
| curve25519-sha256                       | ♦       | ♦                         | ♦       | ♦       |                                       |                                      |              |              | ♦                                     | ♦                                            |
| curve25519-sha256@libssh.org            | ♦       | ♦                         | ♦       | ♦       |                                       |                                      |              |              | ♦                                     | ♦                                            |
| diffie-hellman-group14-sha1             |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |
| diffie-hellman-group14-sha256           |         |                           |         |         | ♦                                     |                                      |              | ♦            | ♦                                     |                                              |
| diffie-hellman-group16-sha512           | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| diffie-hellman-group18-sha512           | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| diffie-hellman-group-exchange-sha256    | ♦       | ♦                         | ♦       | ♦       | ♦                                     |                                      | ♦            | ♦            | ♦                                     | ♦                                            |
| ecdh-sha2-nistp256                      | ♦       |                           |         |         | ♦                                     | ♦                                    |              | ♦            | ♦                                     | ♦                                            |
| ecdh-sha2-nistp384                      | ♦       |                           |         |         | ♦                                     | ♦                                    |              | ♦            | ♦                                     | ♦                                            |
| ecdh-sha2-nistp521                      | ♦       |                           |         |         | ♦                                     | ♦                                    |              | ♦            | ♦                                     | ♦                                            |
| **SshMacs**                             |
| hmac-sha1                               |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |
| hmac-sha1-etm@openssh.com               |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |
| hmac-sha2-256                           |         |                           |         | ♦       | ♦                                     |                                      |              | ♦            | ♦                                     |                                              |
| hmac-sha2-256-etm@openssh.com           | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| hmac-sha2-512                           |         |                           |         | ♦       | ♦                                     |                                      |              | ♦            | ♦                                     |                                              |
| hmac-sha2-512-etm@openssh.com           | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| umac-128-etm@openssh.com                |         |                           |         |         | ♦                                     |                                      |              |              | ♦                                     |                                              |
| umac-128@openssh.com                    |         |                           |         |         | ♦                                     |                                      |              |              | ♦                                     |                                              |
| umac-64-etm@openssh.com                 |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |
| umac-64@openssh.com                     |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |
| **ContentEncryptionCiphers**            |
| aes256-cbc                              | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| aes192-cbc                              | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| aes128-cbc                              | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| 3des-cbc                                | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| **HashAlgorithms**                      |
| sha256                                  | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| sha384                                  | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| sha512                                  | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     | ♦                                            |
| sha1                                    | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| **TlsCiphers**                          |
| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256   | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256   | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384   | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384   | ♦       | ♦                         | ♦       | ♦       | ♦                                     | ♦                                    | ♦            | ♦            | ♦                                     |                                              |
| TLS_RSA_WITH_AES_128_CBC_SHA256         |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |
| TLS_RSA_WITH_AES_256_CBC_SHA256         |         |                           |         |         |                                       |                                      |              |              | ♦                                     |                                              |

## TransferSecurityPolicy-2024-01

The following shows the TransferSecurityPolicy-2024-01 security policy.

```
{
    "SecurityPolicy": {
        "Fips": false,
        "SecurityPolicyName": "TransferSecurityPolicy-2024-01",
        "SshCiphers": [
            "aes128-gcm@openssh.com",
            "aes256-gcm@openssh.com",
            "aes128-ctr",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "curve25519-sha256",
            "curve25519-sha256@libssh.org",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc",
            "3des-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512",
            "sha1"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ]
    }
}
```

## TransferSecurityPolicy-SshAuditCompliant-2025-02

The following shows the TransferSecurityPolicy-SshAuditCompliant-2025-02 security
policy.

###### Note

This security policy is designed around the recommendations provided by the
`ssh-audit` tool, and is 100% compliant with that tool.

```
{
  "SecurityPolicy": {
    "Fips": false,
    "Protocols": [
      "SFTP",
      "FTPS"
    ],
    "SecurityPolicyName": "TransferSecurityPolicy-SshAuditCompliant-2025-02",
    "SshCiphers": [
      "aes128-gcm@openssh.com",
      "aes256-gcm@openssh.com",
      "aes128-ctr",
      "aes256-ctr",
      "aes192-ctr"
    ],
    "SshKexs": [
      "curve25519-sha256",
      "curve25519-sha256@libssh.org",
      "diffie-hellman-group18-sha512",
      "diffie-hellman-group16-sha512",
      "diffie-hellman-group-exchange-sha256"
    ],
    "SshMacs": [
      "hmac-sha2-256-etm@openssh.com",
      "hmac-sha2-512-etm@openssh.com"
    ],
    "ContentEncryptionCiphers": [
      "aes256-cbc",
      "aes192-cbc",
      "aes128-cbc",
      "3des-cbc"
    ],
    "HashAlgorithms": [
      "sha256",
      "sha384",
      "sha512",
      "sha1"
    ],
    "TlsCiphers": [
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    ],
    "Type": "SERVER"
  }
}
```

## TransferSecurityPolicy-2023-05

The following shows the TransferSecurityPolicy-2023-05 security policy.

```
{
    "SecurityPolicy": {
        "Fips": false,
        "SecurityPolicyName": "TransferSecurityPolicy-2023-05",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "curve25519-sha256",
            "curve25519-sha256@libssh.org",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-512-etm@openssh.com",
            "hmac-sha2-256-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc",
            "3des-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512",
            "sha1"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ]
    }
}
```

## TransferSecurityPolicy-2022-03

The following shows the TransferSecurityPolicy-2022-03 security policy.

```
{
  "SecurityPolicy": {
    "Fips": false,
    "SecurityPolicyName": "TransferSecurityPolicy-2022-03",
    "SshCiphers": [
      "aes256-gcm@openssh.com",
      "aes128-gcm@openssh.com",
      "aes256-ctr",
      "aes192-ctr"
    ],
    "SshKexs": [
      "curve25519-sha256",
      "curve25519-sha256@libssh.org",
      "diffie-hellman-group16-sha512",
      "diffie-hellman-group18-sha512",
      "diffie-hellman-group-exchange-sha256"
    ],
    "SshMacs": [
      "hmac-sha2-512-etm@openssh.com",
      "hmac-sha2-256-etm@openssh.com",
      "hmac-sha2-512",
      "hmac-sha2-256"
    ],
    "ContentEncryptionCiphers": [
      "aes256-cbc",
      "aes192-cbc",
      "aes128-cbc"
      "3des-cbc",
    ],
    "HashAlgorithms": [
      "sha256",
      "sha384",
      "sha512"
      "sha1"
    ],
    "TlsCiphers": [
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    ]
  }
}
```

## TransferSecurityPolicy-2020-06 and

TransferSecurityPolicy-Restricted-2020-06

The following shows the TransferSecurityPolicy-2020-06 security policy.

###### Note

The TransferSecurityPolicy-Restricted-2020-06 and TransferSecurityPolicy-2020-06
security policies are identical, except that the restricted policy doesn't support
the `chacha20-poly1305@openssh.com` cipher.

```
{
  "SecurityPolicy": {
    "Fips": false,
    "SecurityPolicyName": "TransferSecurityPolicy-2020-06",
    "SshCiphers": [
      "chacha20-poly1305@openssh.com", //Not included in TransferSecurityPolicy-Restricted-2020-06
      "aes128-ctr",
      "aes192-ctr",
      "aes256-ctr",
      "aes128-gcm@openssh.com",
      "aes256-gcm@openssh.com"
    ],
    "SshKexs": [
      "ecdh-sha2-nistp256",
      "ecdh-sha2-nistp384",
      "ecdh-sha2-nistp521",
      "diffie-hellman-group-exchange-sha256",
      "diffie-hellman-group16-sha512",
      "diffie-hellman-group18-sha512",
      "diffie-hellman-group14-sha256"
    ],
    "SshMacs": [
      "umac-128-etm@openssh.com",
      "hmac-sha2-256-etm@openssh.com",
      "hmac-sha2-512-etm@openssh.com",
      "umac-128@openssh.com",
      "hmac-sha2-256",
      "hmac-sha2-512"
    ],
    "ContentEncryptionCiphers": [
      "aes256-cbc",
      "aes192-cbc",
      "aes128-cbc"
            "3des-cbc",
    ],
    "HashAlgorithms": [
      "sha256",
      "sha384",
      "sha512"
      "sha1"
    ],
    "TlsCiphers": [
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    ]
  }
}
```

## TransferSecurityPolicy-2018-11 and

TransferSecurityPolicy-Restricted-2018-11

The following shows the TransferSecurityPolicy-2018-11 security policy.

###### Note

The TransferSecurityPolicy-Restricted-2018-11 and TransferSecurityPolicy-2018-11
security policies are identical, except that the restricted policy doesn't support
the `chacha20-poly1305@openssh.com` cipher.

```
{
  "SecurityPolicy": {
    "Fips": false,
    "SecurityPolicyName": "TransferSecurityPolicy-2018-11",
    "SshCiphers": [
      "chacha20-poly1305@openssh.com", //Not included in TransferSecurityPolicy-Restricted-2018-11
      "aes128-ctr",
      "aes192-ctr",
      "aes256-ctr",
      "aes128-gcm@openssh.com",
      "aes256-gcm@openssh.com"
    ],
    "SshKexs": [
      "curve25519-sha256",
      "curve25519-sha256@libssh.org",
      "ecdh-sha2-nistp256",
      "ecdh-sha2-nistp384",
      "ecdh-sha2-nistp521",
      "diffie-hellman-group-exchange-sha256",
      "diffie-hellman-group16-sha512",
      "diffie-hellman-group18-sha512",
      "diffie-hellman-group14-sha256",
      "diffie-hellman-group14-sha1"
    ],
    "SshMacs": [
      "umac-64-etm@openssh.com",
      "umac-128-etm@openssh.com",
      "hmac-sha2-256-etm@openssh.com",
      "hmac-sha2-512-etm@openssh.com",
      "hmac-sha1-etm@openssh.com",
      "umac-64@openssh.com",
      "umac-128@openssh.com",
      "hmac-sha2-256",
      "hmac-sha2-512",
      "hmac-sha1"
    ],
    "ContentEncryptionCiphers": [
      "aes256-cbc",
      "aes192-cbc",
      "aes128-cbc"
            "3des-cbc",
    ],
    "HashAlgorithms": [
      "sha256",
      "sha384",
      "sha512",
      "sha1"
    ],
    "TlsCiphers": [
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384",
      "TLS_RSA_WITH_AES_128_CBC_SHA256",
      "TLS_RSA_WITH_AES_256_CBC_SHA256"
    ]
  }
}
```

## TransferSecurityPolicy-FIPS-2024-01/TransferSecurityPolicy-FIPS-2024-05

The following shows the TransferSecurityPolicy-FIPS-2024-01 and
TransferSecurityPolicy-FIPS-2024-05 security policies.

###### Note

The FIPS service endpoint and TransferSecurityPolicy-FIPS-2024-01 and
TransferSecurityPolicy-FIPS-2024-05 security policies are only available in some
AWS Regions. For more information, see [AWS Transfer Family endpoints and
quotas](../../../general/latest/gr/transfer-service.md "../../../general/latest/gr/transfer-service.md") in the _AWS General Reference_.

The only difference between these two security policies is that
TransferSecurityPolicy-FIPS-2024-01 supports the `ssh-rsa` algorithm, and
TransferSecurityPolicy-FIPS-2024-05 doesn't.

```
{
    "SecurityPolicy": {
        "Fips": true,
        "SecurityPolicyName": "TransferSecurityPolicy-FIPS-2024-01",
        "SshCiphers": [
            "aes128-gcm@openssh.com",
            "aes256-gcm@openssh.com",
            "aes128-ctr",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc"
            "3des-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512"
            "sha1"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ]
    }
}
```

## TransferSecurityPolicy-FIPS-2023-05

The FIPS certification details for AWS Transfer Family can be found at [https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all "https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all")

The following shows the TransferSecurityPolicy-FIPS-2023-05 security policy.

###### Note

The FIPS service endpoint and TransferSecurityPolicy-FIPS-2023-05 security policy
is only available in some AWS Regions. For more information, see [AWS Transfer Family
endpoints and quotas](../../../general/latest/gr/transfer-service.md "../../../general/latest/gr/transfer-service.md") in the _AWS General Reference_.

```
{
    "SecurityPolicy": {
        "Fips": true,
        "SecurityPolicyName": "TransferSecurityPolicy-FIPS-2023-05",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc"
            "3des-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512"
            "sha1"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ]
    }
}
```

## TransferSecurityPolicy-FIPS-2020-06

The FIPS certification details for AWS Transfer Family can be found at [https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all "https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all")

The following shows the TransferSecurityPolicy-FIPS-2020-06 security policy.

###### Note

The FIPS service endpoint and TransferSecurityPolicy-FIPS-2020-06 security policy
are only available in some AWS Regions. For more information, see [AWS Transfer Family
endpoints and quotas](../../../general/latest/gr/transfer-service.md "../../../general/latest/gr/transfer-service.md") in the _AWS General Reference_.

```
{
  "SecurityPolicy": {
    "Fips": true,
    "SecurityPolicyName": "TransferSecurityPolicy-FIPS-2020-06",
    "SshCiphers": [
      "aes128-ctr",
      "aes192-ctr",
      "aes256-ctr",
      "aes128-gcm@openssh.com",
      "aes256-gcm@openssh.com"
    ],
    "SshKexs": [
      "ecdh-sha2-nistp256",
      "ecdh-sha2-nistp384",
      "ecdh-sha2-nistp521",
      "diffie-hellman-group-exchange-sha256",
      "diffie-hellman-group16-sha512",
      "diffie-hellman-group18-sha512",
      "diffie-hellman-group14-sha256"
    ],
    "SshMacs": [
      "hmac-sha2-256-etm@openssh.com",
      "hmac-sha2-512-etm@openssh.com",
      "hmac-sha2-256",
      "hmac-sha2-512"
    ],
    "ContentEncryptionCiphers": [
      "aes256-cbc",
      "aes192-cbc",
      "aes128-cbc"
            "3des-cbc",
    ],
    "HashAlgorithms": [
      "sha256",
      "sha384",
      "sha512"
            "sha1",
    ],
    "TlsCiphers": [
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    ]
  }
}
```

## TransferSecurityPolicy-AS2Restricted-2025-07

This security policy is designed for AS2 file transfers that require enhanced security
by excluding legacy cryptographic algorithms. It supports modern AES encryption and
SHA-2 hash algorithms while removing support for weaker algorithms like 3DES and
SHA-1.

```
{
    "SecurityPolicy": {
        "Fips": false,
        "SecurityPolicyName": "TransferSecurityPolicy-AS2Restricted-2025-07",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes128-ctr",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "mlkem768x25519-sha256",
            "mlkem768nistp256-sha256",
            "mlkem1024nistp384-sha384",
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "curve25519-sha256",
            "curve25519-sha256@libssh.org",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ],
        "Type": "SERVER",
        "Protocols": [
            "AS2"
        ]
    }
}
```

## Post Quantum security policies

This table lists the algorithms for the Transfer Family post quantum security policies. These
polices are described in detail in [Using hybrid post-quantum key exchange with
AWS Transfer Family](post-quantum-security-policies.md "post-quantum-security-policies.md").

The policy listings follow the table.

###### Note

The earlier post quantum policies
(**TransferSecurityPolicy-PQ-SSH-Experimental-2023-04** and
**TransferSecurityPolicy-PQ-SSH-FIPS-Experimental-2023-04** are
deprecated. We recommend that you use the new policies instead.

| Security policy                         | TransferSecurityPolicy-2025-03 | TransferSecurityPolicy-FIPS-2025-03 |
| --------------------------------------- | ------------------------------ | ----------------------------------- |
| **SSH<br>ciphers**                      |
| aes128-ctr                              | ♦                              | ♦                                   |
| aes128-gcm@openssh.com                  | ♦                              | ♦                                   |
| aes192-ctr                              | ♦                              | ♦                                   |
| aes256-ctr                              | ♦                              | ♦                                   |
| aes256-gcm@openssh.com                  | ♦                              | ♦                                   |
| **KEXs**                                |
| mlkem768x25519-sha256                   | ♦                              | ♦                                   |
| mlkem768nistp256-sha256                 | ♦                              | ♦                                   |
| mlkem1024nistp384-sha384                | ♦                              | ♦                                   |
| diffie-hellman-group14-sha256           | ♦                              | ♦                                   |
| diffie-hellman-group16-sha512           | ♦                              | ♦                                   |
| diffie-hellman-group18-sha512           | ♦                              | ♦                                   |
| ecdh-sha2-nistp384                      | ♦                              | ♦                                   |
| ecdh-sha2-nistp521                      | ♦                              | ♦                                   |
| ecdh-sha2-nistp256                      | ♦                              | ♦                                   |
| diffie-hellman-group-exchange-sha256    | ♦                              | ♦                                   |
| curve25519-sha256@libssh.org            | ♦                              |                                     |
| curve25519-sha256                       | ♦                              |                                     |
| **MACs**                                |
| hmac-sha2-256-etm@openssh.com           | ♦                              | ♦                                   |
| hmac-sha2-512-etm@openssh.com           | ♦                              | ♦                                   |
| **ContentEncryptionCiphers**            |
| aes256-cbc                              | ♦                              | ♦                                   |
| aes192-cbc                              | ♦                              | ♦                                   |
| aes128-cbc                              | ♦                              | ♦                                   |
| 3des-cbc                                | ♦                              | ♦                                   |
| **HashAlgorithms**                      |
| sha256                                  | ♦                              | ♦                                   |
| sha384                                  | ♦                              | ♦                                   |
| sha512                                  | ♦                              | ♦                                   |
| sha1                                    | ♦                              | ♦                                   |
| **TLS<br>ciphers**                      |
| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | ♦                              | ♦                                   |
| TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | ♦                              | ♦                                   |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | ♦                              | ♦                                   |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | ♦                              | ♦                                   |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256   | ♦                              | ♦                                   |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256   | ♦                              | ♦                                   |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384   | ♦                              | ♦                                   |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384   | ♦                              | ♦                                   |

### TransferSecurityPolicy-2025-03

The following shows the TransferSecurityPolicy-2025-03 security policy.

```
{
    "SecurityPolicy": {
        "Fips": false,
        "SecurityPolicyName": "TransferSecurityPolicy-2025-03",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes128-ctr",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "mlkem768x25519-sha256",
            "mlkem768nistp256-sha256",
            "mlkem1024nistp384-sha384",
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "curve25519-sha256",
            "curve25519-sha256@libssh.org",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc"
            "3des-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512"
            "sha1"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ],
        "Type": "SERVER",
        "Protocols": [
           "SFTP",
           "FTPS"
        ]
    }
}
```

### TransferSecurityPolicy-FIPS-2025-03

The following shows the TransferSecurityPolicy-FIPS-2025-03 security
policy.

```
{
    "SecurityPolicy": {
        "Fips": true,
        "SecurityPolicyName": "TransferSecurityPolicy-FIPS-2025-03",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes256-ctr",
            "aes192-ctr",
            "aes128-ctr"
        ],
        "SshKexs": [
            "mlkem768x25519-sha256",
            "mlkem768nistp256-sha256",
            "mlkem1024nistp384-sha384",
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "diffie-hellman-group-exchange-sha256",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512"
        ],
        "SshMacs": [
            "hmac-sha2-512-etm@openssh.com",
            "hmac-sha2-256-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc"
            "3des-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512"
            "sha1"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ],
        "Type": "SERVER",
        "Protocols": [
           "SFTP",
           "FTPS"
        ]
    }
}
```

### TransferSecurityPolicy-AS2Restricted-2025-07

The following shows the TransferSecurityPolicy-AS2Restricted-2025-07 security
policy.

###### Note

This security policy is identical to TransferSecurityPolicy-2025-03, except
that it does not support 3DES (in ContentEncryptionCiphers) and does not support
SHA1 (in HashAlgorithms). It includes all algorithms from 2025-03, including
post-quantum cryptographic algorithms (mlkem\* KEXs).

```
{
    "SecurityPolicy": {
        "Fips": false,
        "SecurityPolicyName": "TransferSecurityPolicy-AS2Restricted-2025-07",
        "SshCiphers": [
            "aes256-gcm@openssh.com",
            "aes128-gcm@openssh.com",
            "aes128-ctr",
            "aes256-ctr",
            "aes192-ctr"
        ],
        "SshKexs": [
            "mlkem768x25519-sha256",
            "mlkem768nistp256-sha256",
            "mlkem1024nistp384-sha384",
            "ecdh-sha2-nistp256",
            "ecdh-sha2-nistp384",
            "ecdh-sha2-nistp521",
            "curve25519-sha256",
            "curve25519-sha256@libssh.org",
            "diffie-hellman-group16-sha512",
            "diffie-hellman-group18-sha512",
            "diffie-hellman-group-exchange-sha256"
        ],
        "SshMacs": [
            "hmac-sha2-256-etm@openssh.com",
            "hmac-sha2-512-etm@openssh.com"
        ],
        "ContentEncryptionCiphers": [
            "aes256-cbc",
            "aes192-cbc",
            "aes128-cbc"
        ],
        "HashAlgorithms": [
            "sha256",
            "sha384",
            "sha512"
        ],
        "TlsCiphers": [
            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
        ],
        "Type": "SERVER",
        "Protocols": [
           "SFTP",
           "FTPS"
        ]
    }
}
```
