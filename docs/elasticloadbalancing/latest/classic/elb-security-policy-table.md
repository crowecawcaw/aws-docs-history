# Predefined SSL security policies for Classic Load Balancers

You can choose one of the predefined security policies for your HTTPS/SSL
listeners. You can use one of the
`ELBSecurityPolicy-TLS` policies to meet compliance and security
standards that require disabling certain TLS protocol versions. Alternatively, you
can create a custom security policy. For more information, see [Update the SSL negotiation
configuration](ssl-config-update.md "ssl-config-update.md").

The RSA- and DSA-based ciphers are specific to the signing algorithm used to
create SSL certificate. Make sure to create an SSL certificate using the signing
algorithm that is based on the ciphers that are enabled for your security
policy.

If you select a policy that is enabled for Server Order Preference, the load
balancer uses the ciphers in the order that they are specified here to negotiate
connections between the client and load balancer. Otherwise, the load balancer uses
the ciphers in the order that they are presented by the client.

The following sections describe the most recent predefined security policies for
Classic Load Balancers, including their enabled SSL protocols and SSL ciphers. You can also describe
the predefined policies using the [describe-load-balancer-policies](../../../cli/latest/reference/elb/describe-load-balancer-policies.md "../../../cli/latest/reference/elb/describe-load-balancer-policies.md") command.

###### Tip

This information applies only to Classic Load Balancers. For information that applies to other
load balancers, see [Security policies for your Application Load Balancer](../application/describe-ssl-policies.md "../application/describe-ssl-policies.md")
and [Security policies for your Network Load Balancer](../network/describe-ssl-policies.md "../network/describe-ssl-policies.md").

###### Contents

- [Protocols by policy](#tls-protocols "#tls-protocols")
- [Ciphers by policy](#tls-policy-ciphers "#tls-policy-ciphers")
- [Policies by cipher](#tls-cipher-policies "#tls-cipher-policies")

## Protocols by policy

The following table describes the TLS protocols that each security policy supports.

| Security policies                 | TLS 1.2 | TLS 1.1 | TLS 1.0 |
| --------------------------------- | ------- | ------- | ------- |
| ELBSecurityPolicy-TLS-1-2-2017-01 | Yes     | No      | No      |
| ELBSecurityPolicy-TLS-1-1-2017-01 | Yes     | Yes     | No      |
| ELBSecurityPolicy-2016-08         | Yes     | Yes     | Yes     |
| ELBSecurityPolicy-2015-05         | Yes     | Yes     | Yes     |
| ELBSecurityPolicy-2015-03         | Yes     | Yes     | Yes     |
| ELBSecurityPolicy-2015-02         | Yes     | Yes     | Yes     |

## Ciphers by policy

The following table describes the ciphers that each security policy supports.

| Security policy                   | Ciphers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ELBSecurityPolicy-TLS-1-2-2017-01 | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES256-GCM-SHA384<br>• AES256-SHA256                                                                                                                                                                                                               |
| ELBSecurityPolicy-TLS-1-1-2017-01 | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA                                                                   |
| ELBSecurityPolicy-2016-08         | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA                                                                   |
| ELBSecurityPolicy-2015-05         | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA<br>• DES-CBC3-SHA                                                 |
| ELBSecurityPolicy-2015-03         | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA<br>• DHE-RSA-AES128-SHA<br>• DHE-DSS-AES128-SHA<br>• DES-CBC3-SHA |
| ELBSecurityPolicy-2015-02         | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA<br>• DHE-RSA-AES128-SHA<br>• DHE-DSS-AES128-SHA                   |

## Policies by cipher

The following table describes the security policies that support each cipher.

| Cipher name                                                                                                 | Security policies                                                                                                                                                                                      | Cipher suite |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c02b         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256     | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c02f         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256     | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c023         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256         | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c027         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA           | • ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                        | c009         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA               | • ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                        | c013         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c02c         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384     | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c030         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384     | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c024         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384         | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | c028         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA             | • ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                        | c014         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA             | • ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                        | c00a         |
| **OpenSSL\*<br>• – AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_GCM_SHA256                     | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | 9c           |
| **OpenSSL\*<br>• – AES128-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_CBC_SHA256                         | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | 3c           |
| **OpenSSL\*<br>• – AES128-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_CBC_SHA                               | • ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                        | 2f           |
| **OpenSSL\*<br>• – AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_GCM_SHA384                     | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | 9d           |
| **OpenSSL\*<br>• – AES256-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_CBC_SHA256                         | • ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02 | 3d           |
| **OpenSSL\*<br>• – AES256-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_CBC_SHA                               | • ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08<br>• ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                        | 35           |
| **OpenSSL\*<br>• – DHE-RSA-AES128-SHA<br>**IANA\*<br>• – TLS_DHE_RSA_WITH_AES_128_CBC_SHA                   | • ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                                                                                                                             | 33           |
| **OpenSSL\*<br>• – DHE-DSS-AES128-SHA<br>**IANA\*<br>• – TLS_DHE_DSS_WITH_AES_128_CBC_SHA                   | • ELBSecurityPolicy-2015-03<br>• ELBSecurityPolicy-2015-02                                                                                                                                             | 32           |
| **OpenSSL\*<br>• – DES-CBC3-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_3DES_EDE_CBC_SHA                            | • ELBSecurityPolicy-2015-05<br>• ELBSecurityPolicy-2015-03                                                                                                                                             | 0a           |
