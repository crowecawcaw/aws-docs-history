

# Security policies for your Application Load Balancer

Elastic Load Balancing uses a Secure Socket Layer (SSL) negotiation configuration, known as a security policy, to negotiate SSL connections between a client and the load balancer. A security policy is a combination of protocols and ciphers. The protocol establishes a secure connection between a client and a server and ensures that all data passed between the client and your load balancer is private. A cipher is an encryption algorithm that uses encryption keys to create a coded message. Protocols use several ciphers to encrypt data over the internet. During the connection negotiation process, the client and the load balancer present a list of ciphers and protocols that they each support, in order of preference. By default, the first cipher on the server's list that matches any one of the client's ciphers is selected for the secure connection.

**Considerations**
+ An HTTPS listener requires a security policy. If you do not specify a security policy when you create the listener, we use the default security policy. The default security policy depends on how you created the HTTPS listener:
  + **Console** – The default security policy is `ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09`.
  + **Other methods** (for example, the AWS CLI, AWS CloudFormation, and the AWS CDK) – The default security policy is `ELBSecurityPolicy-2016-08`.
  + To view the TLS protocol version (log field position 5) and key exchange (log field position 13) for connection requests to your load balancer, enable connection logging and examine the corresponding log entries. For more information, see [Connection logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html).
  + Security policies with PQ in their names offer hybrid post-quantum key exchange. For compatibility, they support both classical and post-quantum Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) key exchange algorithms. Clients must support ML-KEM key exchange to use hybrid post-quantum TLS. The hybrid post-quantum policies support the `X25519MLKEM768`, `SecP256r1MLKEM768`, and `SecP384r1MLKEM1024` groups. Hybrid post-quantum key exchange is available on TLS 1.3 connections only. A client that connects to a PQ policy with TLS 1.2 uses a classical key exchange group. For the groups that each policy supports, see [TLS key exchange groups](#tls-key-exchange-groups), [FIPS key exchange groups](#fips-key-exchange-groups), [RFC 9151 key exchange groups](#rfc9151-key-exchange-groups), and [FS key exchange groups](#fs-key-exchange-groups). For more information, see [Post-quantum Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/) on the AWS website.
  + In TLS 1.2, the key exchange is part of the cipher suite. Ciphers whose names start with ECDHE use ephemeral elliptic curve Diffie-Hellman key exchange. Ciphers with no ECDHE prefix, such as AES128-GCM-SHA256, use RSA key exchange. In TLS 1.3, the cipher suite does not include the key exchange. The client and the load balancer negotiate a key exchange group separately, from the groups that the security policy allows. The *Policies by cipher* tables show the key exchange for each cipher. The *Key exchange groups by policy* tables show the groups for each policy.
  + AWS recommends implementing the new post-quantum TLS (PQ-TLS) based security policy  `ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09` or `ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09`. This policy ensures backward compatibility by supporting clients capable of negotiating hybrid PQ-TLS, TLS 1.3 only, or TLS 1.2 only, thereby minimizing service disruption during the transition to post-quantum cryptography. You can progressively migrate to more restrictive security policies as your client applications develop the capability to negotiate PQ-TLS for key exchange operations.
  + Security policies with RFC 9151 in their names help you comply with RFC 9151, which defines TLS requirements for the Commercial National Security Algorithm (CNSA) 1.0 suite as specified by the US National Security Agency (NSA). To help with transition, they are available in two categories: strict policies that enforce full RFC 9151 requirements, and interop policies (containing "INTEROP" in their name) that support both RFC 9151-compliant and non-RFC 9151 ciphers to facilitate gradual transition. We recommend starting with `ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07` to minimize disruption, then gradually moving to stricter policies as clients support RFC 9151. You can use the `tls_protocol`, `tls_cipher`, and `tls_keyexchange` fields in ALB connection logs to monitor client connections. For more information about RFC 9151, see [RFC 9151](https://datatracker.ietf.org/doc/html/rfc9151) on the IETF website.
  + Security policies with CNSA2 in their names help you transition to the Commercial National Security Algorithm Suite (CNSA) 2.0, the post-quantum cryptography (PQC) algorithm set that the US National Security Agency (NSA) requires. CNSA 2.0 requires ML-KEM-1024 (FIPS 203) for key exchange. These interop policies offer ML-KEM-1024 and keep the RFC 9151 (CNSA 1.0) algorithms as a fallback during the transition. If your listener is not currently using an RFC 9151 (CNSA 1.0) policy, we recommend that you first move to an RFC 9151 interop policy and validate client compatibility. Then transition to a CNSA 2.0 interop policy. For more information, see [CNSA 2.0 security policies](#cnsa2-security-policies).
+ To meet compliance and security standards that require disabling certain TLS protocol versions, or to support legacy clients requiring deprecated ciphers, you can use one of the `ELBSecurityPolicy-TLS-` security policies. To view the TLS protocol version for requests to your Application Load Balancer, enable access logging for your load balancer and examine the corresponding access log entries. For more information, see [Access logs](load-balancer-access-logs.md).
+ You can restrict which security policies are available to users across your AWS accounts and AWS Organizations by using the [ Elastic Load Balancing condition keys](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html) in your IAM and service control policies (SCPs), respectively. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.
+ Policies that support only TLS 1.3 support Forward Secrecy (FS). Policies whose ciphers all use ECDHE or TLS 1.3 key exchange also provide FS. Policies that include RSA key exchange ciphers do not provide FS for connections that negotiate those ciphers.
+ Application Load Balancers support TLS resumption using PSK (TLS 1.3) and session IDs/session Tickets (TLS 1.2 and older). Resumptions are only supported in connections to the same Application Load Balancer IP address. The 0-RTT Data feature and early\_data extension are not implemented. 
+ Application Load Balancers do not support custom security policies.
+ Application Load Balancers support SSL renegotiation for target connections only.

**Backend connections**
+ You can choose the security policy that is used for front-end connections, but not backend connections. The security policy for backend connections depends on the listener security policy. If any of your listeners are using: 
  + **CNSA 2.0 interop policy** – Backend connections use `ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP3-FIPS-PQ-2026-07`
  + **RFC 9151 policy (including any interop policy)** – Backend connections use `ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07`
  + **FIPS post-quantum TLS policy** - Backend connections use `ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09`
  + **FIPS policy** - Backend connections use `ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04`
  + **Post-quantum TLS policy** - Backend connections use `ELBSecurityPolicy-TLS13-1-0-PQ-2025-09`
  + **TLS 1.3 policy** - Backend connections use `ELBSecurityPolicy-TLS13-1-0-2021-06`
  + **Other TLS policy** - Backend connections use `ELBSecurityPolicy-2016-08`

**Note**  
`ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP3-FIPS-PQ-2026-07` is a backend-only policy. You can't select it for a listener. It is `ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07` with ML-KEM-1024 key exchange added. It supports the same protocols and ciphers, and adds `MLKEM1024` to the key exchange groups. Targets that don't support ML-KEM-1024 use `secp384r1`, `secp256r1`, or `secp521r1`.

**Contents**
+ [Example describe-ssl-policies commands](#describe-ssl-policies-examples)
+ [TLS security policies](#tls-security-policies)
  + [Protocols by policy](#tls-protocols)
  + [Ciphers by policy](#tls-policy-ciphers)
  + [Policies by cipher](#tls-cipher-policies)
  + [Key exchange groups by policy](#tls-key-exchange-groups)
  + [Policies by post-quantum key exchange mechanisms](#tls-pq-key-exchange)
+ [FIPS security policies](#fips-security-policies)
  + [Protocols by policy](#fips-protocols)
  + [Ciphers by policy](#fips-policy-ciphers)
  + [Policies by cipher](#fips-cipher-policies)
  + [Key exchange groups by policy](#fips-key-exchange-groups)
  + [Policies by post-quantum key exchange mechanisms](#fips-pq-key-exchange)
+ [RFC 9151 (CNSA 1.0) security policies](#rfc9151-security-policies)
  + [Protocols by policy](#rfc9151-protocols)
  + [Ciphers by policy](#rfc9151-policy-ciphers)
  + [Policies by cipher](#rfc9151-cipher-policies)
  + [Key exchange groups by policy](#rfc9151-key-exchange-groups)
+ [CNSA 2.0 security policies](#cnsa2-security-policies)
  + [Protocols by policy](#cnsa2-protocols)
  + [Ciphers by policy](#cnsa2-policy-ciphers)
  + [Policies by cipher](#cnsa2-cipher-policies)
  + [Key exchange groups by policy](#cnsa2-key-exchange-groups)
  + [Policies by post-quantum key exchange mechanisms](#cnsa2-pq-key-exchange)
+ [FS supported policies](#fs-supported-policies)
  + [Protocols by policy](#fs-protocols)
  + [Ciphers by policy](#fs-policy-ciphers)
  + [Policies by cipher](#fs-cipher-policies)
  + [Key exchange groups by policy](#fs-key-exchange-groups)

## Example describe-ssl-policies commands
<a name="describe-ssl-policies-examples"></a>

You can describe the protocols and ciphers for a security policy, or find a policy that meets your needs, using the [describe-ssl-policies](https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-ssl-policies.html) AWS CLI command.

The `describe-ssl-policies` command returns the protocols and ciphers for each policy. It does not return the key exchange groups. For the groups that each policy supports, see [TLS key exchange groups](#tls-key-exchange-groups), [FIPS key exchange groups](#fips-key-exchange-groups), [RFC 9151 key exchange groups](#rfc9151-key-exchange-groups), and [FS key exchange groups](#fs-key-exchange-groups).

The following example describes the specified policy.

```
aws elbv2 describe-ssl-policies \
    --names "{{ELBSecurityPolicy-TLS13-1-2-Res-2021-06}}"
```

The following example lists policies with the specified string in the policy name.

```
aws elbv2 describe-ssl-policies \
    --query "SslPolicies[?contains(Name,'{{FIPS}}')].Name"
```

The following example lists policies that support the specified protocol.

```
aws elbv2 describe-ssl-policies \
    --query "SslPolicies[?contains(SslProtocols,'{{TLSv1.3}}')].Name"
```

The following example lists policies that support the specified cipher.

```
aws elbv2 describe-ssl-policies \
    --query "SslPolicies[?Ciphers[?contains(Name,'{{TLS_AES_128_GCM_SHA256}}')]].Name"
```

The following example lists policies that do not support the specified cipher.

```
aws elbv2 describe-ssl-policies \
    --query 'SslPolicies[?length(Ciphers[?starts_with(Name,`{{AES128-GCM-SHA256}}`)]) == `0`].Name'
```

## TLS security policies
<a name="tls-security-policies"></a>

You can use the TLS security policies to meet compliance and security standards that require disabling certain TLS protocol versions, or to support legacy clients that require deprecated ciphers.

Policies that support only TLS 1.3 support Forward Secrecy (FS). Policies whose ciphers all use ECDHE or TLS 1.3 key exchange also provide FS. Policies that include RSA key exchange ciphers do not provide FS for connections that negotiate those ciphers.

**Topics**
+ [Protocols by policy](#tls-protocols)
+ [Ciphers by policy](#tls-policy-ciphers)
+ [Policies by cipher](#tls-cipher-policies)
+ [Key exchange groups by policy](#tls-key-exchange-groups)
+ [Policies by post-quantum key exchange mechanisms](#tls-pq-key-exchange)

### Protocols by policy
<a name="tls-protocols"></a>

The following table describes the protocols that each TLS security policy supports.


| Security policies | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 | 
| --- | --- | --- | --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-3-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Res-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-1-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-0-2021-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | 
| ELBSecurityPolicy-TLS13-1-0-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | 
| ELBSecurityPolicy-TLS-1-2-Ext-2018-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS-1-2-2017-01 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS-1-1-2017-01 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-2016-08 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | 

### Ciphers by policy
<a name="tls-policy-ciphers"></a>

The following table describes the ciphers that each TLS security policy supports.


| Security policy | Ciphers | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-2021-06<br />ELBSecurityPolicy-TLS13-1-3-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256  | 
| ELBSecurityPolicy-TLS13-1-2-2021-06<br />ELBSecurityPolicy-TLS13-1-2-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256  | 
| ELBSecurityPolicy-TLS13-1-1-2021-06 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-TLS13-1-0-2021-06<br />ELBSecurityPolicy-TLS13-1-0-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_CHACHA20\_POLY1305\_SHA256<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-TLS-1-2-Ext-2018-06 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-TLS-1-2-2017-01 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256  | 
| ELBSecurityPolicy-TLS-1-1-2017-01 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-2016-08 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 

### Policies by cipher
<a name="tls-cipher-policies"></a>

The following table describes the TLS security policies that support each cipher, and the key exchange that each cipher uses. For TLS 1.2 ciphers, the key exchange is part of the cipher suite. For TLS 1.3 ciphers, the client and the load balancer negotiate the key exchange separately. For the groups that each policy supports, see [Key exchange groups by policy](#tls-key-exchange-groups).


| Cipher name | Key exchange | Security policies | Cipher suite | 
| --- | --- | --- | --- | 
| **OpenSSL** – TLS\_AES\_128\_GCM\_SHA256<br />**IANA** – TLS\_AES\_128\_GCM\_SHA256 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#tls-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-2021-06<br />+ ELBSecurityPolicy-TLS13-1-3-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09  | 1301 | 
| **OpenSSL** – TLS\_AES\_256\_GCM\_SHA384<br />**IANA** – TLS\_AES\_256\_GCM\_SHA384 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#tls-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-2021-06<br />+ ELBSecurityPolicy-TLS13-1-3-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09  | 1302 | 
| **OpenSSL** – TLS\_CHACHA20\_POLY1305\_SHA256<br />**IANA** – TLS\_CHACHA20\_POLY1305\_SHA256 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#tls-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-2021-06<br />+ ELBSecurityPolicy-TLS13-1-3-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09  | 1303 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c02b | 
| **OpenSSL** – ECDHE-RSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c02f | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c023 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c027 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c009 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c013 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c02c | 
| **OpenSSL** – ECDHE-RSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c030 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c024 | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c028 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c00a | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | c014 | 
| **OpenSSL** – AES128-GCM-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | 9c | 
| **OpenSSL** – AES128-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | 3c | 
| **OpenSSL** – AES128-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | 2f | 
| **OpenSSL** – AES256-GCM-SHA384<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | 9d | 
| **OpenSSL** – AES256-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-2-2017-01<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | 3d | 
| **OpenSSL** – AES256-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-2021-06<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09<br />+ ELBSecurityPolicy-TLS-1-2-Ext-2018-06<br />+ ELBSecurityPolicy-TLS-1-1-2017-01<br />+ ELBSecurityPolicy-2016-08  | 35 | 

### Key exchange groups by policy
<a name="tls-key-exchange-groups"></a>

The following table describes the key exchange groups that each TLS security policy supports. For TLS 1.3 connections, the client and the load balancer negotiate one of these groups. For TLS 1.2 and earlier connections, these groups are the elliptic curves available to ECDHE ciphers. Hybrid post-quantum groups are available on TLS 1.3 connections only.


| Security policy | Key exchange groups | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-3-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Res-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-1-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-0-2021-06 |  + x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-0-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ x25519<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS-1-2-Ext-2018-06 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS-1-2-2017-01 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS-1-1-2017-01 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-2016-08 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 

### Policies by post-quantum key exchange mechanisms
<a name="tls-pq-key-exchange"></a>

The following table describes the TLS security policies that support key exchange mechanisms that incorporate ML-KEM for quantum-resistant confidentiality.


| Key exchange mechanism | Security policies | 
| --- | --- | 
| X25519MLKEM768 |  + ELBSecurityPolicy-TLS13-1-3-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09  | 
| SecP256r1MLKEM768 |  + ELBSecurityPolicy-TLS13-1-3-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09  | 
| SecP384r1MLKEM1024 |  + ELBSecurityPolicy-TLS13-1-3-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-PQ-2025-09  | 

## FIPS security policies
<a name="fips-security-policies"></a>

The Federal Information Processing Standard (FIPS) is a US and Canadian government standard that specifies the security requirements for cryptographic modules that protect sensitive information. To learn more, see [Federal Information Processing Standard (FIPS) 140](https://aws.amazon.com/compliance/fips/) on the *AWS Cloud Security Compliance* page.

All FIPS policies leverage the AWS-LC FIPS validated cryptographic module. To learn more, see the [ AWS-LC Cryptographic Module](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4631) page on the *NIST Cryptographic Module Validation Program* site.

**Important**  
Policies `ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04` and `ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04` are provided for legacy compatibility only. While they utilize FIPS cryptography using the FIPS140 module, they may not conform to the latest NIST guidance for TLS configuration.

**Topics**
+ [Protocols by policy](#fips-protocols)
+ [Ciphers by policy](#fips-policy-ciphers)
+ [Policies by cipher](#fips-cipher-policies)
+ [Key exchange groups by policy](#fips-key-exchange-groups)
+ [Policies by post-quantum key exchange mechanisms](#fips-pq-key-exchange)

### Protocols by policy
<a name="fips-protocols"></a>

The following table describes the protocols that each FIPS security policy supports.


| Security policies | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 | 
| --- | --- | --- | --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | 
| ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | 

### Ciphers by policy
<a name="fips-policy-ciphers"></a>

The following table describes the ciphers that each FIPS security policy supports.


| Security policy | Ciphers | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256  | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA  | 
| ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 
| ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09 |  + TLS\_AES\_128\_GCM\_SHA256<br />+ TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA  | 

### Policies by cipher
<a name="fips-cipher-policies"></a>

The following table describes the FIPS security policies that support each cipher, and the key exchange that each cipher uses. For TLS 1.2 ciphers, the key exchange is part of the cipher suite. For TLS 1.3 ciphers, the client and the load balancer negotiate the key exchange separately. For the groups that each policy supports, see [Key exchange groups by policy](#fips-key-exchange-groups).


| Cipher name | Key exchange | Security policies | Cipher suite | 
| --- | --- | --- | --- | 
| **OpenSSL** – TLS\_AES\_128\_GCM\_SHA256<br />**IANA** – TLS\_AES\_128\_GCM\_SHA256 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#fips-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 1301 | 
| **OpenSSL** – TLS\_AES\_256\_GCM\_SHA384<br />**IANA** – TLS\_AES\_256\_GCM\_SHA384 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#fips-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 1302 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c02b | 
| **OpenSSL** – ECDHE-RSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c02f | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c023 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c027 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c009 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c013 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c02c | 
| **OpenSSL** – ECDHE-RSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c030 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c024 | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c028 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c00a | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | c014 | 
| **OpenSSL** – AES128-GCM-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 9c | 
| **OpenSSL** – AES128-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 3c | 
| **OpenSSL** – AES128-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 2f | 
| **OpenSSL** – AES256-GCM-SHA384<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 9d | 
| **OpenSSL** – AES256-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 3d | 
| **OpenSSL** – AES256-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 35 | 

### Key exchange groups by policy
<a name="fips-key-exchange-groups"></a>

The following table describes the key exchange groups that each FIPS security policy supports. Post-quantum key exchange is only available on TLS 1.3 connections.


| Security policy | Key exchange groups | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-1-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-0-FIPS-2023-04 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09 |  + X25519MLKEM768<br />+ SecP256r1MLKEM768<br />+ SecP384r1MLKEM1024<br />+ secp256r1<br />+ secp384r1<br />+ secp521r1  | 

### Policies by post-quantum key exchange mechanisms
<a name="fips-pq-key-exchange"></a>

The following table describes the FIPS security policies that support key exchange mechanisms that incorporate ML-KEM for quantum-resistant confidentiality.


| Key exchange mechanism | Security policies | 
| --- | --- | 
| X25519MLKEM768 |  + ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 
| SecP256r1MLKEM768 |  + ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 
| SecP384r1MLKEM1024 |  + ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext2-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext1-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-FIPS-PQ-2025-09<br />+ ELBSecurityPolicy-TLS13-1-0-FIPS-PQ-2025-09  | 

## RFC 9151 (CNSA 1.0) security policies
<a name="rfc9151-security-policies"></a>

With Application Load Balancer, you can use security policies to comply with RFC 9151, which defines TLS requirements for the Commercial National Security Algorithm (CNSA) 1.0 suite as specified by the US National Security Agency (NSA). RFC 9151 specifies how to use the CNSA suite with TLS 1.2 and TLS 1.3 protocols, defining the cryptographic requirements for secure communications that meet government security standards. To learn more about RFC 9151, see [RFC 9151](https://datatracker.ietf.org/doc/html/rfc9151) on the IETF website.

RFC 9151 policies are available in two categories:
+ **Strict policies** – Enforce strict RFC 9151 cipher and signature scheme requirements. Use these when all your clients can support RFC 9151.
+ **Interop policies** – Support both RFC 9151-compliant and non-RFC 9151 ciphers and signature schemes to facilitate a gradual transition to RFC 9151 compliance. Use these when you are uncertain whether all clients can support RFC 9151, or you want to avoid disrupting clients during the transition. All interop policies contain "INTEROP" in their policy name.

We recommend starting with the interop policy `ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07`, which supports clients that can negotiate classical TLS 1.3, TLS 1.2, or strict RFC 9151 algorithms, minimizing disruption. You can gradually move to stricter policies as your clients can negotiate strict RFC 9151. You can use the `tls_protocol`, `tls_cipher`, and `tls_keyexchange` fields in ALB connection logs to monitor how clients are connecting.

**Important**  
When you select an RFC 9151 security policy for your listener, the load balancer uses `ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07` for backend connections to targets and other services. However, the load balancer cannot guarantee or enforce RFC 9151 compliance on egress connections, including connections to targets, or customer-configured external services (such as third-party identity providers or authentication endpoints).  
It is your responsibility to ensure the following:  
Your targets and any external services you configure can support the protocols and ciphers in the backend connection policy.
For strict RFC 9151 compliance between the load balancer and your targets, your targets must have RFC 9151-compliant certificates and ciphers implemented.
If your backend targets only support TLS 1.0 or TLS 1.1, connections will fail. You must update the protocols and ciphers on your targets to align with the ciphers supported by the `ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07` policy.

**Topics**
+ [Protocols by policy](#rfc9151-protocols)
+ [Ciphers by policy](#rfc9151-policy-ciphers)
+ [Policies by cipher](#rfc9151-cipher-policies)
+ [Key exchange groups by policy](#rfc9151-key-exchange-groups)

### Protocols by policy
<a name="rfc9151-protocols"></a>

The following table describes the protocols that each RFC 9151 security policy supports.


| Security policies | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 | 
| --- | --- | --- | --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-RFC9151-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 

### Ciphers by policy
<a name="rfc9151-policy-ciphers"></a>

The following table describes the ciphers that each RFC 9151 security policy supports.


| Security policy | Ciphers | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-RFC9151-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ AES256-GCM-SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_AES\_128\_GCM\_SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_AES\_128\_GCM\_SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_AES\_128\_GCM\_SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ TLS\_AES\_128\_GCM\_SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-ECDSA-AES256-SHA<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ AES256-GCM-SHA384<br />+ AES256-SHA256<br />+ AES256-SHA<br />+ AES128-GCM-SHA256<br />+ AES128-SHA256<br />+ AES128-SHA  | 

### Policies by cipher
<a name="rfc9151-cipher-policies"></a>

The following table describes the RFC 9151 security policies that support each cipher, and the key exchange that each cipher uses. For TLS 1.2 ciphers, the key exchange is part of the cipher suite. For TLS 1.3 ciphers, the client and the load balancer negotiate the key exchange separately. For the groups that each policy supports, see [Key exchange groups by policy](#rfc9151-key-exchange-groups).


| Cipher name | Key exchange | Security policies | Cipher suite | 
| --- | --- | --- | --- | 
| **OpenSSL** – TLS\_AES\_256\_GCM\_SHA384<br />**IANA** – TLS\_AES\_256\_GCM\_SHA384 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#rfc9151-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 1302 | 
| **OpenSSL** – TLS\_AES\_128\_GCM\_SHA256<br />**IANA** – TLS\_AES\_128\_GCM\_SHA256 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#rfc9151-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 1301 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c02c | 
| **OpenSSL** – ECDHE-RSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c030 | 
| **OpenSSL** – AES256-GCM-SHA384<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | RSA |  + ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 9d | 
| **OpenSSL** – ECDHE-ECDSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c02b | 
| **OpenSSL** – ECDHE-RSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c02f | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c024 | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c028 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c023 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c027 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c00a | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c014 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c009 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07<br />+ ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | c013 | 
| **OpenSSL** – AES256-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 3d | 
| **OpenSSL** – AES256-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA | RSA |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 35 | 
| **OpenSSL** – AES128-GCM-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 9c | 
| **OpenSSL** – AES128-SHA256<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | RSA |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 3c | 
| **OpenSSL** – AES128-SHA<br />**IANA** – TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA | RSA |  + ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07  | 2f | 

### Key exchange groups by policy
<a name="rfc9151-key-exchange-groups"></a>

The following table describes the key exchange groups that each RFC 9151 security policy supports. RFC 9151 policies do not support hybrid post-quantum key exchange groups.


| Security policy | Key exchange groups | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-RFC9151-FIPS-2023-07 |  + secp384r1  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-FIPS-2023-07 |  + secp384r1  | 
| ELBSecurityPolicy-TLS13-1-2-Ext0-RFC9151-FIPS-2023-07 |  + secp384r1  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP1-FIPS-2023-07 |  + secp384r1<br />+ secp256r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP2-FIPS-2023-07 |  + secp384r1<br />+ secp256r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP3-FIPS-2023-07 |  + secp384r1<br />+ secp256r1<br />+ secp521r1  | 
| ELBSecurityPolicy-TLS13-1-2-RFC9151-INTEROP4-FIPS-2023-07 |  + secp384r1<br />+ secp256r1<br />+ secp521r1  | 

## CNSA 2.0 security policies
<a name="cnsa2-security-policies"></a>

Security policies with CNSA2 in their names help you transition to the Commercial National Security Algorithm Suite (CNSA) 2.0, the post-quantum cryptography (PQC) algorithm set that the US National Security Agency (NSA) requires. CNSA 2.0 requires ML-KEM-1024 (FIPS 203) for key exchange. These interop policies offer ML-KEM-1024 and keep the RFC 9151 (CNSA 1.0) algorithms as a fallback during the transition.

You can use these interoperable security policies on your Application Load Balancer if you need to migrate to CNSA 2.0 TLS security requirements. The policies support post-quantum key exchange by default, while maintaining compatibility with classical (non-post-quantum) clients during the transition, which minimizes service disruption. Post-quantum-capable clients negotiate key exchange using ML-KEM-1024. Classical-only clients fall back to the RFC 9151 algorithm set.

**Important**  
If your listener is not currently using an RFC 9151 (CNSA 1.0) policy, we recommend that you first move to an RFC 9151 interop policy and validate client compatibility, to avoid TLS connection failures. Then transition to a CNSA 2.0 interop policy. To see how clients connect, use the `tls_protocol`, `tls_cipher`, and `tls_keyexchange` fields in [connection logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html).

The CNSA 2.0 interop policies use ML-KEM-1024 for key exchange. They do not use hybrid key exchange groups such as `X25519MLKEM768`. ML-KEM-1024 key exchange is available on TLS 1.3 connections only. A client that connects with TLS 1.2, or that does not support ML-KEM-1024, uses the classical `secp384r1` group.

**Important**  
When you select a CNSA 2.0 interop policy for your listener, the load balancer uses `ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP3-FIPS-PQ-2026-07` for backend connections to targets and other services. The load balancer cannot guarantee or enforce CNSA 2.0 compliance on egress connections, including connections to targets and to customer-configured external services (such as third-party identity providers or authentication endpoints).  
It is your responsibility to ensure that your targets and any external services that you configure support the protocols and ciphers of the backend connection policy. If your backend targets support only TLS 1.0 or TLS 1.1, connections fail.

**Topics**
+ [Protocols by policy](#cnsa2-protocols)
+ [Ciphers by policy](#cnsa2-policy-ciphers)
+ [Policies by cipher](#cnsa2-cipher-policies)
+ [Key exchange groups by policy](#cnsa2-key-exchange-groups)
+ [Policies by post-quantum key exchange mechanisms](#cnsa2-pq-key-exchange)

### Protocols by policy
<a name="cnsa2-protocols"></a>

The following table describes the protocols that each CNSA 2.0 security policy supports.


| Security policies | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 | 
| --- | --- | --- | --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-CNSA2-INTEROP1-FIPS-PQ-2026-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 

### Ciphers by policy
<a name="cnsa2-policy-ciphers"></a>

The following table describes the ciphers that each CNSA 2.0 security policy supports.


| Security policy | Ciphers | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-CNSA2-INTEROP1-FIPS-PQ-2026-07 |  + TLS\_AES\_256\_GCM\_SHA384  | 
| ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07 |  + TLS\_AES\_256\_GCM\_SHA384<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384  | 

### Policies by cipher
<a name="cnsa2-cipher-policies"></a>

The following table describes the CNSA 2.0 security policies that support each cipher, and the key exchange that each cipher uses. For TLS 1.2 ciphers, the key exchange is part of the cipher suite.


| Cipher name | Key exchange | Security policies | Cipher suite | 
| --- | --- | --- | --- | 
| **OpenSSL** – TLS\_AES\_256\_GCM\_SHA384<br />**IANA** – TLS\_AES\_256\_GCM\_SHA384 | Negotiated separately (TLS 1.3). See [Key exchange groups by policy](#cnsa2-key-exchange-groups). |  + ELBSecurityPolicy-TLS13-1-3-CNSA2-INTEROP1-FIPS-PQ-2026-07<br />+ ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07  | 1302 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07  | c02c | 
| **OpenSSL** – ECDHE-RSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | ECDHE |  + ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07  | c030 | 

### Key exchange groups by policy
<a name="cnsa2-key-exchange-groups"></a>

The following table describes the key exchange groups that each CNSA 2.0 security policy supports. Groups are listed in order of preference. CNSA 2.0 policies use pure ML-KEM-1024. They do not support hybrid post-quantum key exchange groups.


| Security policy | Key exchange groups | 
| --- | --- | 
| ELBSecurityPolicy-TLS13-1-3-CNSA2-INTEROP1-FIPS-PQ-2026-07 |  + MLKEM1024<br />+ secp384r1  | 
| ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07 |  + MLKEM1024<br />+ secp384r1  | 

### Policies by post-quantum key exchange mechanisms
<a name="cnsa2-pq-key-exchange"></a>

The following table describes the CNSA 2.0 security policies that support key exchange mechanisms that use ML-KEM for quantum-resistant confidentiality.


| Key exchange mechanism | Security policies | 
| --- | --- | 
| MLKEM1024 |  + ELBSecurityPolicy-TLS13-1-3-CNSA2-INTEROP1-FIPS-PQ-2026-07<br />+ ELBSecurityPolicy-TLS13-1-2-CNSA2-INTEROP2-FIPS-PQ-2026-07  | 

## FS supported policies
<a name="fs-supported-policies"></a>

FS (Forward Secrecy) supported security policies provide additional safeguards against the eavesdropping of encrypted data, through the use of a unique random session key. This prevents the decoding of captured data, even if the secret long-term key is compromised.

The policies in this section support FS, and "FS" is included in their names. However, these are not the only policies that support FS. Policies that support only TLS 1.3 support FS. Policies that support TLS 1.3 and TLS 1.2 that have only ciphers of the form TLS\_\* and ECDHE\_\* also provide FS.

**Topics**
+ [Protocols by policy](#fs-protocols)
+ [Ciphers by policy](#fs-policy-ciphers)
+ [Policies by cipher](#fs-cipher-policies)
+ [Key exchange groups by policy](#fs-key-exchange-groups)

### Protocols by policy
<a name="fs-protocols"></a>

The following table describes the protocols that each FS supported security policy supports.


| Security policies | TLS 1.3 | TLS 1.2 | TLS 1.1 | TLS 1.0 | 
| --- | --- | --- | --- | --- | 
| ELBSecurityPolicy-FS-1-2-Res-2020-10 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-FS-1-2-Res-2019-08 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-FS-1-2-2019-08 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-FS-1-1-2019-08 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | 
| ELBSecurityPolicy-FS-2018-06 | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/images/success_icon.png) Yes | 

### Ciphers by policy
<a name="fs-policy-ciphers"></a>

The following table describes the ciphers that each FS supported security policy supports.


| Security policy | Ciphers | 
| --- | --- | 
| ELBSecurityPolicy-FS-1-2-Res-2020-10 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384  | 
| ELBSecurityPolicy-FS-1-2-Res-2019-08 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384  | 
| ELBSecurityPolicy-FS-1-2-2019-08 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA  | 
| ELBSecurityPolicy-FS-1-1-2019-08 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA  | 
| ELBSecurityPolicy-FS-2018-06 |  + ECDHE-ECDSA-AES128-GCM-SHA256<br />+ ECDHE-RSA-AES128-GCM-SHA256<br />+ ECDHE-ECDSA-AES128-SHA256<br />+ ECDHE-RSA-AES128-SHA256<br />+ ECDHE-ECDSA-AES128-SHA<br />+ ECDHE-RSA-AES128-SHA<br />+ ECDHE-ECDSA-AES256-GCM-SHA384<br />+ ECDHE-RSA-AES256-GCM-SHA384<br />+ ECDHE-ECDSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA384<br />+ ECDHE-RSA-AES256-SHA<br />+ ECDHE-ECDSA-AES256-SHA  | 

### Policies by cipher
<a name="fs-cipher-policies"></a>

The following table describes the FS supported security policies that support each cipher.


| Cipher name | Security policies | Cipher suite | 
| --- | --- | --- | 
| **OpenSSL** – ECDHE-ECDSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 |  + ELBSecurityPolicy-FS-1-2-Res-2020-10<br />+ ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c02b | 
| **OpenSSL** – ECDHE-RSA-AES128-GCM-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 |  + ELBSecurityPolicy-FS-1-2-Res-2020-10<br />+ ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c02f | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256 |  + ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+  ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c023 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA256<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 |  + ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c027 | 
| **OpenSSL** – ECDHE-ECDSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA |  + ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c009 | 
| **OpenSSL** – ECDHE-RSA-AES128-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA |  + ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c013 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 |  + ELBSecurityPolicy-FS-1-2-Res-2020-10<br />+ ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c02c | 
| **OpenSSL** – ECDHE-RSA-AES256-GCM-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 |  + ELBSecurityPolicy-FS-1-2-Res-2020-10<br />+ ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c030 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 |  + ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c024 | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA384<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 |  + ELBSecurityPolicy-FS-1-2-Res-2019-08<br />+ ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c028 | 
| **OpenSSL** – ECDHE-ECDSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA |  + ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c00a | 
| **OpenSSL** – ECDHE-RSA-AES256-SHA<br />**IANA** – TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA |  + ELBSecurityPolicy-FS-1-2-2019-08<br />+ ELBSecurityPolicy-FS-1-1-2019-08<br />+ ELBSecurityPolicy-FS-2018-06  | c014 | 

### Key exchange groups by policy
<a name="fs-key-exchange-groups"></a>

The following table describes the key exchange groups that each FS supported security policy supports. These policies support TLS 1.2 and earlier, so these groups are the elliptic curves available to ECDHE ciphers. FS supported policies do not support hybrid post-quantum key exchange groups.


| Security policy | Key exchange groups | 
| --- | --- | 
| ELBSecurityPolicy-FS-1-2-Res-2020-10 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-FS-1-2-Res-2019-08 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-FS-1-2-2019-08 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-FS-1-1-2019-08 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 
| ELBSecurityPolicy-FS-2018-06 |  + secp256r1<br />+ secp384r1<br />+ secp521r1  | 