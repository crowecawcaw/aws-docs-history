

# Client certificate identity filters

Client certificate identity filters admit connections only from specific client identities. The load balancer applies the filters after trust-store validation passes, and runs revocation checks after a certificate matches a filter. You configure filters in the `ClientCertificateIdentityFilters` property of `MutualAuthenticationAttributes`.

Filters are optional. If you do not configure any filter, the load balancer admits every client certificate that passes trust-store validation and revocation checks.

Each filter rule matches a field in the client certificate. You can match the following fields.
+ `subject-cn` – the common name in the certificate subject.
+ `subject-ou` – the organizational unit in the certificate subject.
+ `san-dns` – a DNS name in the subject alternative name (SAN).
+ `san-uri` – a URI in the subject alternative name (SAN).

Each filter rule uses the `accept` action, which is the only supported action. Because the only action is `accept`, the load balancer rejects a certificate that does not match at least one filter rule. If the filter list is empty, the load balancer applies no filtering, so every trust-store-valid certificate passes.

If a client certificate does not contain a field that a filter references (for example, no SAN extension, or no organizational unit in the subject), that filter does not match. If no other filter matches, the load balancer rejects the connection. For a field that has multiple values (for example, multiple organizational units in the subject, or multiple DNS names in the SAN), a filter matches if it matches any one of the values.

When the load balancer rejects a connection because the certificate matched no filter, it records `CertificateFilterNoMatch` in the access log `tls_verify_status` field. For more information, see [Error reason codes](load-balancer-access-logs.md#access-log-error-reason-codes).

Each filter rule uses a match type of `exact` or `prefix`, and a value of 1–256 printable ASCII characters. The load balancer combines rules with OR logic, so it admits a connection if the certificate matches at least one rule. You can configure up to 100 filter rules per listener.

**Important**  
The following case rules apply to both the `exact` and `prefix` match types:  
For the `subject-cn`, `subject-ou`, and `san-dns` fields, matching is case-insensitive.
For the `san-uri` field, the scheme and host are matched case-insensitively, and the rest of the URI, such as the path, is matched case-sensitively. For example, a filter value of `SPIFFE://EXAMPLE.COM/workload` matches `spiffe://example.com/workload`, but does not match `spiffe://example.com/Workload`.

**Note**  
The `san-uri` field requires values in URI format. In addition to the general value rules, a `san-uri` value must meet the following requirements:  
The value must begin with a letter.
Before the first colon, the value can contain only letters, digits, plus signs (`+`), hyphens (`-`), or periods (`.`). This part is the URI scheme.
If the match type is `exact`, the value must contain a colon.
For example, `spiffe://example.com/workload` is a valid value. The load balancer rejects values such as `1spiffe://example.com` (begins with a digit), `spiffe_id://example.com` (contains an underscore before the colon), or an `exact` value that contains no colon.

## Configure client certificate identity filters
<a name="configure-client-certificate-filters"></a>

You add client certificate identity filters to a TLS listener that already uses mTLS in verify mode.

------
#### [ AWS Management Console ]

**To add client certificate identity filters**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the name of the load balancer to open its details page.

1. On the **Listeners and rules** tab, select the TLS listener, and then choose **Edit listener**.

1. In the mutual authentication (mTLS) settings, under **Client certificate identity filters (optional)**, choose **Add OR filter** to add a filter.

1. For **Field**, choose the certificate field to match: **Subject Common Name (Subject.CN)**, **Subject Organizational Unit (Subject.OU)**, **DNS Subject Alternative Name (SAN.DNS)**, or **URI Subject Alternative Name (SAN.URI)**. For **Match type**, choose **Exact** or **Prefix**. For **Value**, enter the text to match.
**Note**  
The **Action to take when there is a match** field is preset to **Accept**. Accept is the only supported action.

1. To admit any of several identities, choose **Add OR filter** again, and then add another rule.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To add client certificate identity filters**  
Use the [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command, and pass the filter list in the `--mutual-authentication` argument. Each filter requires the `Field`, `Action`, `MatchType`, and `Value` members.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --mutual-authentication '{
        "Mode": "verify",
        "TrustStoreArn": "{{trust-store-arn}}",
        "ClientCertificateIdentityFilters": [
            { "Field": "subject-cn", "Action": "accept", "MatchType": "exact",  "Value": "client1.example.com" },
            { "Field": "subject-ou", "Action": "accept", "MatchType": "prefix", "Value": "Engineer" },
            { "Field": "san-dns",    "Action": "accept", "MatchType": "exact",  "Value": "client1.example.com" },
            { "Field": "san-uri",    "Action": "accept", "MatchType": "prefix", "Value": "spiffe://example.com/" }
        ]
    }'
```

**Note**  
The `ClientCertificateIdentityFilters` parameter requires a recent version of the AWS CLI or AWS SDK that includes it. If your version does not recognize the parameter, update to the latest version.

Because the load balancer combines rules with OR logic, it admits a certificate that matches any one of these four rules.

**To turn off filtering while keeping mTLS on**  
Pass an empty filter list.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --mutual-authentication '{"Mode":"verify","TrustStoreArn":"{{trust-store-arn}}","ClientCertificateIdentityFilters":[]}'
```

**To view the current filters**  
Use the [describe-listeners](https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-listeners.html) command.

```
aws elbv2 describe-listeners \
    --listener-arns {{listener-arn}} \
    --query 'Listeners[0].MutualAuthentication'
```

------
#### [ CloudFormation ]

Use the `AWS::ElasticLoadBalancingV2::Listener` resource with a `MutualAuthentication` property that includes a `ClientCertificateIdentityFilters` list. The load balancer combines rules with OR logic, so it admits a certificate that matches any one of the filters.

```yaml
Resources:
  MyTlsListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      Protocol: TLS
      Port: 443
      MutualAuthentication:
        Mode: verify
        TrustStoreArn: {{trust-store-arn}}
        ClientCertificateIdentityFilters:
          - Field: subject-cn
            Action: accept
            MatchType: exact
            Value: client1.example.com
          - Field: san-uri
            Action: accept
            MatchType: prefix
            Value: spiffe://example.com/
```

------