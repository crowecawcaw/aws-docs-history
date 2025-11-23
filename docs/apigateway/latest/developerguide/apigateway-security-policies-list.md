# Supported security policies

The following tables describe the [security policies](apigateway-security-policies.md "apigateway-security-policies.md") that
can be specified for each REST API endpoint type and custom domain name type. These policies allow you to control
incoming connections. API Gateway only supports TLS 1.2 on egress. You can update the security policy for your API
or custom domain name at any time.

Policies that contain `FIPS` in the title are compatible with the Federal Information Processing Standard
(FIPS), which is a US and Canadian government standard that specifies the security requirements for cryptographic modules
that protect sensitive information. To learn more, see [Federal Information Processing Standard (FIPS) 140](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/")
on the _AWS Cloud Security Compliance_ page.

All FIPS policies leverage the AWS-LC FIPS validated cryptographic module. To learn more,
see the [AWS-LC Cryptographic Module](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4631 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4631") page on the _NIST Cryptographic Module Validation Program_ site.

Policies that contain `PQ` in the title use
[Post-Quantum Cryptography (PQC)](https://aws.amazon.com/security/post-quantum-cryptography/ "https://aws.amazon.com/security/post-quantum-cryptography/") to implement hybrid key
exchange algorithms for TLS to ensure traffic confidentiality against future quantum computing threats.

Policies that contain `PFS` in the title use
[Perfect Forward Secrecy (PFS)](https://en.wikipedia.org/wiki/Forward_secrecy "https://en.wikipedia.org/wiki/Forward_secrecy") to make sure session keys
aren't compromised.

Policies that contain both `FIPS` and `PQ` in their title support both of these
features.

## Default security policies

When you create a new REST API or custom domain, the resource is assigned a default security policy. The
following table shows the default security policy for these resources.

| **Resource**          | **Default security policy name** |
| --------------------- | -------------------------------- |
| Regional APIs         | TLS_1_0                          |
| Edge-optimized APIs   | TLS_1_0                          |
| Private APIs          | TLS_1_2                          |
| Regional domain       | TLS_1_2                          |
| Edge-optimized domain | TLS_1_2                          |
| Private domain        | TLS_1_2                          |

## Supported security policies for Regional and private

APIs and custom domain names

The following table describes the security policies that can be specified for Regional and private
APIs and custom domain names:

| **Security policy**                     | **Supported TLS versions**           | **Supported ciphers**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SecurityPolicy_TLS13_1_3_2025_09        | TLS1.3                               | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SecurityPolicy_TLS13_1_3_FIPS_2025_09   | TLS1.3                               | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | TLS1.3<br>TLS1.2                     | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.2<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384                                                                                                                                                                                                                                                                                                        |
| SecurityPolicy_TLS13_1_2_PQ_2025_09     | TLS1.3<br>TLS1.2                     | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.2<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES256-GCM-SHA384<br>• AES256-SHA256                                                                                            |
| TLS_1_2                                 | TLS1.3<br>TLS1.2                     | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.2<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES256-GCM-SHA384<br>• AES256-SHA256                                                                                                                                                    |
| TLS_1_0                                 | TLS1.3<br>TLS1.2<br>TLS1.1<br>TLS1.0 | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.0-TLS1.2<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |

## Supported security policies for edge-optimized

APIs and custom domain names

The following table describes the security policies that can be specified for edge-optimized
APIs and edge-optimized custom domain names:

| **Security policy name**           | **Supported TLS versions**           | **Supported ciphers**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SecurityPolicy_TLS13_2025_EDGE     | TLS1.3                               | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SecurityPolicy_TLS12_PFS_2025_EDGE | TLS1.3<br>TLS1.2                     | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.2<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-CHACHA20-POLY1305<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-RSA-CHACHA20-POLY1305                                                                                                                                                                                                           |
| SecurityPolicy_TLS12_2018_EDGE     | TLS1.3<br>TLS1.2                     | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.2<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-CHACHA20-POLY1305<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-RSA-CHACHA20-POLY1305<br>• ECDHE-RSA-AES256-SHA384                                                                                   |
| TLS_1_0                            | TLS1.3<br>TLS1.2<br>TLS1.1<br>TLS1.0 | TLS1.3<br>• TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>TLS1.0-TLS1.2<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES256-SHA256<br>• AES256-SHA |

## OpenSSL and

RFC cipher names

OpenSSL and IETF RFC 5246 use different names
for the same ciphers. The following table maps the OpenSSL name to the RFC name for
each cipher. For more information, see
[ciphers](https://docs.openssl.org/1.1.1/man1/ciphers/ "https://docs.openssl.org/1.1.1/man1/ciphers/") in the OpenSSL Documentation.

| **OpenSSL cipher name**      | **RFC cipher name**                   |
| ---------------------------- | ------------------------------------- |
| TLS_AES_128_GCM_SHA256       | TLS_AES_128_GCM_SHA256                |
| TLS_AES_256_GCM_SHA384       | TLS_AES_256_GCM_SHA384                |
| TLS_CHACHA20_POLY1305_SHA256 | TLS_CHACHA20_POLY1305_SHA256          |
| ECDHE-RSA-AES128-GCM-SHA256  | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 |
| ECDHE-RSA-AES128-SHA256      | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 |
| ECDHE-RSA-AES128-SHA         | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA    |
| ECDHE-RSA-AES256-GCM-SHA384  | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 |
| ECDHE-RSA-AES256-SHA384      | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 |
| ECDHE-RSA-AES256-SHA         | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA    |
| AES128-GCM-SHA256            | TLS_RSA_WITH_AES_128_GCM_SHA256       |
| AES256-GCM-SHA384            | TLS_RSA_WITH_AES_256_GCM_SHA384       |
| AES128-SHA256                | TLS_RSA_WITH_AES_128_CBC_SHA256       |
| AES256-SHA                   | TLS_RSA_WITH_AES_256_CBC_SHA          |
| AES128-SHA                   | TLS_RSA_WITH_AES_128_CBC_SHA          |
| DES-CBC3-SHA                 | TLS_RSA_WITH_3DES_EDE_CBC_SHA         |
