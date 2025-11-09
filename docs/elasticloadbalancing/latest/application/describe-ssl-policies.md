# Security policies for your Application Load Balancer

Elastic Load Balancing uses a Secure Socket Layer (SSL) negotiation configuration, known as a
security policy, to negotiate SSL connections between a client and the load
balancer. A security policy is a combination of protocols and ciphers. The protocol
establishes a secure connection between a client and a server and ensures that all
data passed between the client and your load balancer is private. A cipher is an
encryption algorithm that uses encryption keys to create a coded message. Protocols
use several ciphers to encrypt data over the internet. During the connection
negotiation process, the client and the load balancer present a list of ciphers and
protocols that they each support, in order of preference. By default, the first
cipher on the server's list that matches any one of the client's ciphers is selected
for the secure connection.

###### Considerations

- Application Load Balancers support SSL renegotiation for target connections only.
- Application Load Balancers do not support custom security policies.
- An HTTPS listener requires a security policy. If you do not specify a security
  policy when you create the listener, we use the default security policy. The
  default security policy depends on how you created the HTTPS listener:
  - Console – The default security
    policy is `ELBSecurityPolicy-TLS13-1-2-Res-2021-06`.
  - Other methods (for example, the
    AWS CLI, AWS CloudFormation, and the AWS CDK) – The default security policy
    is `ELBSecurityPolicy-2016-08`.

- You can choose the security policy that is used for front-end connections, but
  not backend connections. The security policy for backend connections depends on
  the listener security policy:
  - If the HTTPS listener uses a TLS 1.3 security policy, backend connections
    use the `ELBSecurityPolicy-TLS13-1-0-2021-06` policy.
  - If the HTTPS listener uses a FIPS policy, backend connections use the
    `ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04` policy.
  - Otherwise, backend connections use the `ELBSecurityPolicy-2016-08`
    policy.

- To meet compliance and security standards that require disabling certain TLS protocol versions, or to
  support legacy clients requiring deprecated ciphers, you can use one of the `ELBSecurityPolicy-TLS-`
  security policies. To view the TLS protocol version for requests to your Application Load Balancer, enable access logging for
  your load balancer and examine the corresponding access log entries. For more information, see
  [Access logs](load-balancer-access-logs.md "load-balancer-access-logs.md").
- You can restrict which security policies are available to users across your AWS accounts and AWS Organizations
  by using the [Elastic Load Balancing condition keys](../userguide/security_iam_service-with-iam.md "../userguide/security_iam_service-with-iam.md")
  in your IAM and service control policies (SCPs), respectively. For more information, see [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md")
  in the _AWS Organizations User Guide_.
- Policies that support only TLS 1.3 support Forward Secrecy (FS). Policies that
  support TLS 1.3 and TLS 1.2 that have only ciphers of the form TLS\_\* and ECDHE\_\*
  also provide FS.
- Application Load Balancers support TLS resumption using PSK (TLS 1.3) and session IDs/session Tickets (TLS 1.2 and older).
  Resumptions are only supported in connections to the same Application Load Balancer IP address. The 0-RTT Data feature and
  early_data extension are not implemented.
- Application Load Balancers support the Extended Master Secret (EMS) extension for TLS 1.2.

###### Security policies

- [Example describe-ssl-policies commands](describe-ssl-policies.md#describe-ssl-policies-examples "describe-ssl-policies.md#describe-ssl-policies-examples")
- [TLS security policies](describe-ssl-policies.md#tls-security-policies "describe-ssl-policies.md#tls-security-policies")
  - [Protocols by policy](describe-ssl-policies.md#tls-protocols "describe-ssl-policies.md#tls-protocols")
  - [Ciphers by policy](describe-ssl-policies.md#tls-policy-ciphers "describe-ssl-policies.md#tls-policy-ciphers")
  - [Policies by cipher](describe-ssl-policies.md#tls-cipher-policies "describe-ssl-policies.md#tls-cipher-policies")

- [FIPS security policies](describe-ssl-policies.md#fips-security-policies "describe-ssl-policies.md#fips-security-policies")
  - [Protocols by policy](describe-ssl-policies.md#fips-protocols "describe-ssl-policies.md#fips-protocols")
  - [Ciphers by policy](describe-ssl-policies.md#fips-policy-ciphers "describe-ssl-policies.md#fips-policy-ciphers")
  - [Policies by cipher](describe-ssl-policies.md#fips-cipher-policies "describe-ssl-policies.md#fips-cipher-policies")

- [FS supported policies](describe-ssl-policies.md#fs-supported-policies "describe-ssl-policies.md#fs-supported-policies")
  - [Protocols by policy](describe-ssl-policies.md#fs-protocols "describe-ssl-policies.md#fs-protocols")
  - [Ciphers by policy](describe-ssl-policies.md#fs-policy-ciphers "describe-ssl-policies.md#fs-policy-ciphers")
  - [Policies by cipher](describe-ssl-policies.md#fs-cipher-policies "describe-ssl-policies.md#fs-cipher-policies")

## Example describe-ssl-policies commands

You can describe the protocols and ciphers for a security policy,
or find a policy that meets your needs, using the
[describe-ssl-policies](../../../cli/latest/reference/elbv2/describe-ssl-policies.md "../../../cli/latest/reference/elbv2/describe-ssl-policies.md")
AWS CLI command.

The following example describes the specified policy.

```
aws elbv2 describe-ssl-policies \
    --names "`ELBSecurityPolicy-TLS13-1-2-Res-2021-06`"
```

The following example lists policies with the specified string in the policy name.

```
aws elbv2 describe-ssl-policies \
    --query "SslPolicies[?contains(Name,'`FIPS`')].Name"
```

The following example lists policies that support the specified protocol.

```
aws elbv2 describe-ssl-policies \
    --query "SslPolicies[?contains(SslProtocols,'`TLSv1.3`')].Name"
```

The following example lists policies that support the specified cipher.

```
aws elbv2 describe-ssl-policies \
    --query "SslPolicies[?Ciphers[?contains(Name,'`TLS_AES_128_GCM_SHA256`')]].Name"
```

The following example lists policies that do not support the specified cipher.

```
aws elbv2 describe-ssl-policies \
    --query 'SslPolicies[?length(Ciphers[?starts_with(Name,``AES128-GCM-SHA256``)]) == `0`].Name'
```

## TLS security policies

You can use the TLS security policies to meet compliance and security standards
that require disabling certain TLS protocol versions, or to support legacy clients
that require deprecated ciphers.

Policies that support only TLS 1.3 support Forward Secrecy (FS). Policies that
support TLS 1.3 and TLS 1.2 that have only ciphers of the form TLS\_\* and ECDHE\_\*
also provide FS.

###### Contents

- [Protocols by policy](#tls-protocols "#tls-protocols")
- [Ciphers by policy](#tls-policy-ciphers "#tls-policy-ciphers")
- [Policies by cipher](#tls-cipher-policies "#tls-cipher-policies")

### Protocols by policy

The following table describes the protocols that each TLS security policy supports.

| Security policies                        | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 |
| ---------------------------------------- | ------- | ------- | ------- | ------- |
| ELBSecurityPolicy-TLS13-1-3-2021-06      | Yes     | No      | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-2021-06      | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Res-2021-06  | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06 | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06 | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-1-2021-06      | Yes     | Yes     | Yes     | No      |
| ELBSecurityPolicy-TLS13-1-0-2021-06      | Yes     | Yes     | Yes     | Yes     |
| ELBSecurityPolicy-TLS-1-2-Ext-2018-06    | No      | Yes     | No      | No      |
| ELBSecurityPolicy-TLS-1-2-2017-01        | No      | Yes     | No      | No      |
| ELBSecurityPolicy-TLS-1-1-2017-01        | No      | Yes     | Yes     | No      |
| ELBSecurityPolicy-2016-08                | No      | Yes     | Yes     | Yes     |

### Ciphers by policy

The following table describes the ciphers that each TLS security policy supports.

| Security policy                          | Ciphers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ELBSecurityPolicy-TLS13-1-3-2021-06      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ELBSecurityPolicy-TLS13-1-2-2021-06      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384                                                                                                                                                                                                                                 |
| ELBSecurityPolicy-TLS13-1-2-Res-2021-06  | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384                                                                                                                                                                                                                                                                                                                                                         |
| ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06 | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |
| ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06 | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES256-GCM-SHA384<br>• AES256-SHA256                                                                                                                                             |
| ELBSecurityPolicy-TLS13-1-1-2021-06      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |
| ELBSecurityPolicy-TLS13-1-0-2021-06      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• TLS_CHACHA20_POLY1305_SHA256<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |
| ELBSecurityPolicy-TLS-1-2-Ext-2018-06    | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA                                                                                           |
| ELBSecurityPolicy-TLS-1-2-2017-01        | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES256-GCM-SHA384<br>• AES256-SHA256                                                                                                                                                                                                                                       |
| ELBSecurityPolicy-TLS-1-1-2017-01        | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA                                                                                           |
| ELBSecurityPolicy-2016-08                | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-ECDSA-AES256-SHA<br>• ECDHE-RSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA                                                                                           |

### Policies by cipher

The following table describes the TLS security policies that support each cipher.

| Cipher name                                                                                                 | Security policies                                                                                                                                                                                                                                                                                                                                                                                                        | Cipher suite |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| **OpenSSL\*<br>• – TLS_AES_128_GCM_SHA256<br>**IANA\*<br>• – TLS_AES_128_GCM_SHA256                         | • ELBSecurityPolicy-TLS13-1-3-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06                                                                                                                | 1301         |
| **OpenSSL\*<br>• – TLS_AES_256_GCM_SHA384<br>**IANA\*<br>• – TLS_AES_256_GCM_SHA384                         | • ELBSecurityPolicy-TLS13-1-3-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06                                                                                                                | 1302         |
| **OpenSSL\*<br>• – TLS_CHACHA20_POLY1305_SHA256<br>**IANA\*<br>• – TLS_CHACHA20_POLY1305_SHA256             | • ELBSecurityPolicy-TLS13-1-3-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06                                                                                                                | 1303         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08 | c02b         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256     | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08 | c02f         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256     | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                              | c023         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256         | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                              | c027         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA           | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                                                                                                            | c009         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA               | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                                                                                                            | c013         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08 | c02c         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384     | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08 | c030         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384     | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                              | c024         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384         | • ELBSecurityPolicy-TLS13-1-2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                              | c028         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA           | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                                                                                                            | c00a         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA               | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                                                                                                            | c014         |
| **OpenSSL\*<br>• – AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_GCM_SHA256                     | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                       | 9c           |
| **OpenSSL\*<br>• – AES128-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_CBC_SHA256                         | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                       | 3c           |
| **OpenSSL\*<br>• – AES128-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_CBC_SHA                               | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                                                                                                            | 2f           |
| **OpenSSL\*<br>• – AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_GCM_SHA384                     | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                       | 9d           |
| **OpenSSL\*<br>• – AES256-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_CBC_SHA256                         | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-2-2017-01<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                       | 3d           |
| **OpenSSL\*<br>• – AES256-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_CBC_SHA                               | • ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br>• ELBSecurityPolicy-TLS13-1-1-2021-06<br>• ELBSecurityPolicy-TLS13-1-0-2021-06<br>• ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br>• ELBSecurityPolicy-TLS-1-1-2017-01<br>• ELBSecurityPolicy-2016-08                                                                                                                                                                            | 35           |

## FIPS security policies

###### Important

All secure listeners attached to an Application Load Balancer must use either FIPS security
policies or non-FIPS security policies; they cannot be mixed. If an existing
Application Load Balancer has two or more listeners using non-FIPS policies and you want the listeners
to use FIPS security policies instead, remove all listeners until there is only one.
Change the security policy of the listener to FIPS and then create additional listeners
using FIPS security policies. Alternatively, you can create a new Application Load Balancer with new
listeners using only FIPS security policies.

The Federal Information Processing Standard (FIPS) is a US and Canadian
government standard that specifies the security requirements for cryptographic
modules that protect sensitive information. To learn more, see [Federal Information Processing Standard (FIPS) 140](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/")
on the _AWS Cloud Security Compliance_ page.

All FIPS policies leverage the AWS-LC FIPS validated cryptographic module. To learn more,
see the [AWS-LC Cryptographic Module](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4631 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4631") page on the _NIST Cryptographic Module Validation Program_ site.

###### Important

Policies `ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04` and `ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04`
are provided for legacy compatibility only. While they utilize FIPS cryptography using the FIPS140 module, they may not
conform to the latest NIST guidance for TLS configuration.

###### Contents

- [Protocols by policy](#fips-protocols "#fips-protocols")
- [Ciphers by policy](#fips-policy-ciphers "#fips-policy-ciphers")
- [Policies by cipher](#fips-cipher-policies "#fips-cipher-policies")

### Protocols by policy

The following table describes the protocols that each FIPS security policy supports.

| Security policies                             | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 |
| --------------------------------------------- | ------- | ------- | ------- | ------- |
| ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04      | Yes     | No      | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04      | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04  | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04 | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04 | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04 | Yes     | Yes     | No      | No      |
| ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04      | Yes     | Yes     | Yes     | No      |
| ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04      | Yes     | Yes     | Yes     | Yes     |

### Ciphers by policy

The following table describes the ciphers that each FIPS security policy supports.

| Security policy                               | Ciphers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384                                                                                                                                                                                                                                 |
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04  | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384                                                                                                                                                                                                                                                                                                                                                         |
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04 | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04 | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES256-GCM-SHA384<br>• AES256-SHA256                                                                                                                                             |
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04 | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA                                                                                                                     |
| ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |
| ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04      | • TLS_AES_128_GCM_SHA256<br>• TLS_AES_256_GCM_SHA384<br>• ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA<br>• AES128-GCM-SHA256<br>• AES128-SHA256<br>• AES128-SHA<br>• AES256-GCM-SHA384<br>• AES256-SHA256<br>• AES256-SHA |

### Policies by cipher

The following table describes the FIPS security policies that support each cipher.

| Cipher name                                                                                                 | Security policies                                                                                                                                                                                                                                                                                                                                                                               | Cipher suite |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **OpenSSL\*<br>• – TLS_AES_128_GCM_SHA256<br>**IANA\*<br>• – TLS_AES_128_GCM_SHA256                         | • ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04 | 1301         |
| **OpenSSL\*<br>• – TLS_AES_256_GCM_SHA384<br>**IANA\*<br>• – TLS_AES_256_GCM_SHA384                         | • ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04 | 1302         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | • ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                               | c02b         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256     | • ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                               | c02f         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256     | • ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                 | c023         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256         | • ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                 | c027         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA           | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | c009         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA               | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | c013         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | • ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                               | c02c         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384     | • ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                               | c030         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384     | • ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                 | c024         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384         | • ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                 | c028         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA           | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | c00a         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA               | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | c014         |
| **OpenSSL\*<br>• – AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_GCM_SHA256                     | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | 9c           |
| **OpenSSL\*<br>• – AES128-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_CBC_SHA256                         | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | 3c           |
| **OpenSSL\*<br>• – AES128-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_AES_128_CBC_SHA                               | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                                                                     | 2f           |
| **OpenSSL\*<br>• – AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_GCM_SHA384                     | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | 9d           |
| **OpenSSL\*<br>• – AES256-SHA256<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_CBC_SHA256                         | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                  | 3d           |
| **OpenSSL\*<br>• – AES256-SHA<br>**IANA\*<br>• – TLS_RSA_WITH_AES_256_CBC_SHA                               | • ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br>• ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04                                                                                                                                                                                                                                                     | 35           |

## FS supported policies

FS (Forward Secrecy) supported security policies provide additional safeguards
against the eavesdropping of encrypted data, through the use of a unique random
session key. This prevents the decoding of captured data, even if the secret
long-term key is compromised.

The policies in this section support FS, and "FS" is included in their names.
However, these are not the only policies that support FS. Policies that support
only TLS 1.3 support FS. Policies that support TLS 1.3 and TLS 1.2 that have only
ciphers of the form TLS\_\* and ECDHE\_\* also provide FS.

###### Contents

- [Protocols by policy](#fs-protocols "#fs-protocols")
- [Ciphers by policy](#fs-policy-ciphers "#fs-policy-ciphers")
- [Policies by cipher](#fs-cipher-policies "#fs-cipher-policies")

### Protocols by policy

The following table describes the protocols that each FS supported security
policy supports.

| Security policies                    | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 |
| ------------------------------------ | ------- | ------- | ------- | ------- |
| ELBSecurityPolicy-FS-1-2-Res-2020-10 | No      | Yes     | No      | No      |
| ELBSecurityPolicy-FS-1-2-Res-2019-08 | No      | Yes     | No      | No      |
| ELBSecurityPolicy-FS-1-2-2019-08     | No      | Yes     | No      | No      |
| ELBSecurityPolicy-FS-1-1-2019-08     | No      | Yes     | Yes     | No      |
| ELBSecurityPolicy-FS-2018-06         | No      | Yes     | Yes     | Yes     |

### Ciphers by policy

The following table describes the ciphers that each FS supported security policy supports.

| Security policy                      | Ciphers                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ELBSecurityPolicy-FS-1-2-Res-2020-10 | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384                                                                                                                                                                                                                                     |
| ELBSecurityPolicy-FS-1-2-Res-2019-08 | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384                                                                                                             |
| ELBSecurityPolicy-FS-1-2-2019-08     | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA |
| ELBSecurityPolicy-FS-1-1-2019-08     | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA |
| ELBSecurityPolicy-FS-2018-06         | • ECDHE-ECDSA-AES128-GCM-SHA256<br>• ECDHE-RSA-AES128-GCM-SHA256<br>• ECDHE-ECDSA-AES128-SHA256<br>• ECDHE-RSA-AES128-SHA256<br>• ECDHE-ECDSA-AES128-SHA<br>• ECDHE-RSA-AES128-SHA<br>• ECDHE-ECDSA-AES256-GCM-SHA384<br>• ECDHE-RSA-AES256-GCM-SHA384<br>• ECDHE-ECDSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA384<br>• ECDHE-RSA-AES256-SHA<br>• ECDHE-ECDSA-AES256-SHA |

### Policies by cipher

The following table describes the FS supported security policies that support each cipher.

| Cipher name                                                                                                 | Security policies                                                                                                                                                                              | Cipher suite |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | • ELBSecurityPolicy-FS-1-2-Res-2020-10<br>• ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06 | c02b         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-GCM-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256     | • ELBSecurityPolicy-FS-1-2-Res-2020-10<br>• ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06 | c02f         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256     | • ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                           | c023         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA256<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256         | • ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                           | c027         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA           | • ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                                                                     | c009         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES128-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA               | • ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                                                                     | c013         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | • ELBSecurityPolicy-FS-1-2-Res-2020-10<br>• ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06 | c02c         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-GCM-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384     | • ELBSecurityPolicy-FS-1-2-Res-2020-10<br>• ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06 | c030         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384     | • ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                           | c024         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA384<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384         | • ELBSecurityPolicy-FS-1-2-Res-2019-08<br>• ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                           | c028         |
| **OpenSSL\*<br>• – ECDHE-ECDSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA           | • ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                                                                     | c00a         |
| **OpenSSL\*<br>• – ECDHE-RSA-AES256-SHA<br>**IANA\*<br>• – TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA               | • ELBSecurityPolicy-FS-1-2-2019-08<br>• ELBSecurityPolicy-FS-1-1-2019-08<br>• ELBSecurityPolicy-FS-2018-06                                                                                     | c014         |
