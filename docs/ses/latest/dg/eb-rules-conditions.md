

# Rule conditions

Rule conditions compare a property of an accepted email or one of its recipients with a configured value. Use the `Conditions` list to identify the recipients to which a rule applies. Use the `Unless` list to remove recipients from that match.

The rule's actions run only for recipients that match every `Conditions` entry and do not match any `Unless` entry. An `Unless` match skips the current rule's actions for that recipient. It does not remove the recipient from the email. For example, if `test@example.com` matches an `Unless` condition, the next rule can still match `test@example.com`. If expected actions do not run, see [No actions ran](eb-rules-monitoring.md#eb-rules-monitoring-no-actions).

## How rule condition matching works
<a name="eb-rules-conditions-how-matching-works"></a>

Each condition contains an expression. The expression specifies the property to check, an operator, and any values required by that operator.

The following rules control how expressions and condition lists match.
+ **Multiple values in one expression** – For positive operators, any configured value can make the expression match. For example, `SUBJECT EQUALS` with the values `Invoice overdue` and `Payment failed` matches either subject.
+ **Negative operators** – `NOT_EQUALS` matches only when the checked value equals none of the configured values. `NOT_CIDR_MATCHES` matches only when the source IP address is outside every configured range.
+ **Multiple `Conditions` entries** – Every condition must match for a recipient to remain selected.
+ **Multiple `Unless` entries** – A match on any `Unless` condition skips this rule's actions for that recipient.
+ **No `Conditions` entries** – The rule initially selects every current recipient. It then evaluates the `Unless` conditions. A recipient that matches an `Unless` condition skips this rule's actions. The actions run for the other recipients.

**Multiple values in one expression**  
The following expression matches an email with either listed subject.

```
Property: SUBJECT
Operator: EQUALS
Values: Invoice overdue, Payment failed
```

The same expression in JSON is as follows.

```json
{
  "StringExpression": {
    "Evaluate": {"Attribute": "SUBJECT"},
    "Operator": "EQUALS",
    "Values": ["Invoice overdue", "Payment failed"]
  }
}
```

**Multiple conditions**  
The following conditions select a recipient only when its address ends with `@example.com` and the email passes the SPF check.

```
Condition 1: RECIPIENT ENDS_WITH @example.com
Condition 2: SPF EQUALS PASS
```

The same `Conditions` list in JSON is as follows.

```json
{
  "Conditions": [
    {
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "ENDS_WITH",
        "Values": ["@example.com"]
      }
    },
    {
      "VerdictExpression": {
        "Evaluate": {"Attribute": "SPF"},
        "Operator": "EQUALS",
        "Values": ["PASS"]
      }
    }
  ]
}
```

**Multiple Unless conditions**  
The following rule initially selects all three recipients. Its `Unless` conditions skip the rule's actions for `test@example.com` and `archive@example.com`. The actions run only for `orders@example.com`.

```
Recipients: orders@example.com, test@example.com, archive@example.com
Condition: RECIPIENT ENDS_WITH @example.com
Unless 1: RECIPIENT EQUALS test@example.com
Unless 2: RECIPIENT EQUALS archive@example.com
```

The same `Conditions` and `Unless` lists in JSON are as follows.

```json
{
  "Conditions": [
    {
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "ENDS_WITH",
        "Values": ["@example.com"]
      }
    }
  ],
  "Unless": [
    {
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "EQUALS",
        "Values": ["test@example.com"]
      }
    },
    {
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "EQUALS",
        "Values": ["archive@example.com"]
      }
    }
  ]
}
```

## Recipient-level and message-level matching
<a name="eb-rules-conditions-recipient-message"></a>

An *SMTP envelope recipient* is an address that the sending mail server supplies with the SMTP `RCPT TO` command. This address controls where the email is delivered. It can differ from an address displayed in the email's `To` or `CC` header.

The `RECIPIENT` property checks each SMTP envelope recipient separately. This matching model lets one recipient match a rule without selecting other recipients of the same email.

For example, the following condition selects only `sales@example.com`.

```
Recipients: sales@example.com, support@example.com
Condition: RECIPIENT EQUALS sales@example.com
```

A condition that checks an email or connection property gives the same result for every current recipient. These properties include the subject, message size, source IP address, TLS state, authentication results, and most message headers.

In the following example, both recipients remain selected because the subject matches. If the subject does not match, neither recipient remains selected.

```
Recipients: orders@example.com, audit@example.com
Subject: Invoice overdue
Condition: SUBJECT EQUALS Invoice overdue
```

### Recipient address matching and subaddressing
<a name="eb-rules-conditions-recipient-subaddressing"></a>

The `RECIPIENT` property uses the full SMTP envelope recipient address exactly as received, including any subaddress extension, also known as plus addressing. For example, a condition evaluates `user+tag@example.com` as `user+tag@example.com`, not `user@example.com`.

An `EQUALS` or `CONTAINS` condition for `user@example.com` does not match `user+tag@example.com`. To match all subaddressed variants, use an address list with a pattern such as `user*@example.com`. To match every recipient in the domain, use `ENDS_WITH` with `@example.com`.

### SMTP envelope recipient and message headers
<a name="eb-rules-conditions-recipient-message-headers"></a>

The `TO` and `CC` properties check addresses in the email's visible `To` and `CC` headers. They do not check the SMTP envelope recipients.

```
SMTP envelope recipient: archive@example.com
To header: billing@example.com
```

A `RECIPIENT EQUALS archive@example.com` condition matches the delivery recipient. A `TO EQUALS billing@example.com` condition matches the visible `To` header. Both expressions can match the same email even though they check different addresses.

This difference also applies to a blind carbon copy (BCC). The SMTP envelope can contain `archive@example.com` even when that address does not appear in the `To` or `CC` header.

When a `To` or `CC` header contains multiple addresses, a positive string expression matches if any address matches. `NOT_EQUALS` matches only if none of the header addresses equals a configured value.

## Rule condition reference
<a name="eb-rules-conditions-reference"></a>

Each condition uses one of the expression types in the following lists. Place the resulting condition object in either the rule's `Conditions` list or its `Unless` list.

### SMTP connection and envelope conditions
<a name="eb-rules-conditions-reference-smtp"></a>

Recipient address  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) with `RECIPIENT` to check one SMTP envelope recipient at a time. String operators are `EQUALS`, `NOT_EQUALS`, `STARTS_WITH`, `ENDS_WITH`, and `CONTAINS`. The following condition matches recipients in the `example.com` domain.  

```json
{
  "StringExpression": {
    "Evaluate": {"Attribute": "RECIPIENT"},
    "Operator": "ENDS_WITH",
    "Values": ["@example.com"]
  }
}
```

SMTP envelope sender and sending server  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) with `MAIL_FROM` to check the SMTP envelope sender. Use `HELO` to check the server name supplied when the sending mail server introduces itself. The following condition matches an SMTP envelope sender in the `mailer.example` domain.  

```json
{
  "StringExpression": {
    "Evaluate": {"Attribute": "MAIL_FROM"},
    "Operator": "ENDS_WITH",
    "Values": ["@mailer.example"]
  }
}
```

Source IP address  
Use an [IP expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleIpExpression.html) with `SOURCE_IP`. The supported operators are `CIDR_MATCHES` and `NOT_CIDR_MATCHES`. The following condition matches source IP addresses in `192.0.2.0/24`.  

```json
{
  "IpExpression": {
    "Evaluate": {"Attribute": "SOURCE_IP"},
    "Operator": "CIDR_MATCHES",
    "Values": ["192.0.2.0/24"]
  }
}
```

TLS protection  
Use a [boolean expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanExpression.html) with `IS_TRUE` or `IS_FALSE`. `TLS` checks whether the connection uses TLS, including a connection upgraded with `STARTTLS`. `TLS_WRAPPED` checks whether the connection starts with TLS instead of upgrading with `STARTTLS`. The following condition matches a connection that uses TLS.  

```json
{
  "BooleanExpression": {
    "Evaluate": {"Attribute": "TLS"},
    "Operator": "IS_TRUE"
  }
}
```

Client certificate values  
For an mTLS ingress endpoint, use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) to check `CN`, `SERIAL_NUMBER`, or a supported subject alternative name: `SAN_RFC822_NAME`, `SAN_DNS_NAME`, `SAN_DIRECTORY_NAME`, `SAN_UNIFORM_RESOURCE_IDENTIFIER`, `SAN_IP_ADDRESS`, or `SAN_REGISTERED_ID`. The following condition checks the certificate common name.  

```json
{
  "StringExpression": {
    "Evaluate": {"ClientCertificateAttribute": "CN"},
    "Operator": "EQUALS",
    "Values": ["mail.partner.example"]
  }
}
```

### Message header and metadata conditions
<a name="eb-rules-conditions-reference-message"></a>

From and Sender headers  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) with `FROM` to check the email's `From` header. Use `SENDER` to check the `Sender` header when present, or the `From` header when no `Sender` header is present. The following condition matches a visible `From` address.  

```json
{
  "StringExpression": {
    "Evaluate": {"Attribute": "FROM"},
    "Operator": "EQUALS",
    "Values": ["billing@example.com"]
  }
}
```

To and CC headers  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) with `TO` or `CC` to check addresses in the corresponding message header. The following condition matches a `To` header that contains an address in the `example.com` domain.  

```json
{
  "StringExpression": {
    "Evaluate": {"Attribute": "TO"},
    "Operator": "ENDS_WITH",
    "Values": ["@example.com"]
  }
}
```

Subject  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) with `SUBJECT`. The following condition matches either listed subject.  

```json
{
  "StringExpression": {
    "Evaluate": {"Attribute": "SUBJECT"},
    "Operator": "EQUALS",
    "Values": ["Invoice overdue", "Payment failed"]
  }
}
```

Custom message header  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) with `MimeHeaderAttribute` to check a custom header whose name starts with `X-`. The following condition checks an `X-Message-Type` header.  

```json
{
  "StringExpression": {
    "Evaluate": {"MimeHeaderAttribute": "X-Message-Type"},
    "Operator": "EQUALS",
    "Values": ["transactional"]
  }
}
```

Read-receipt request  
Use a [boolean expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanExpression.html) with `READ_RECEIPT_REQUESTED`. The following condition matches an email that requests a read receipt.  

```json
{
  "BooleanExpression": {
    "Evaluate": {"Attribute": "READ_RECEIPT_REQUESTED"},
    "Operator": "IS_TRUE"
  }
}
```

Message size  
Use a [number expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleNumberExpression.html) with `MESSAGE_SIZE`. The value is the message size in bytes. Supported operators are `EQUALS`, `NOT_EQUALS`, `LESS_THAN`, `GREATER_THAN`, `LESS_THAN_OR_EQUAL`, and `GREATER_THAN_OR_EQUAL`. The following condition matches an email larger than 1,048,576 bytes.  

```json
{
  "NumberExpression": {
    "Evaluate": {"Attribute": "MESSAGE_SIZE"},
    "Operator": "GREATER_THAN",
    "Value": 1048576
  }
}
```

### Authentication-result conditions
<a name="eb-rules-conditions-reference-authentication"></a>

SPF and DKIM verdicts  
Use a [verdict expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleVerdictExpression.html) with `SPF` or `DKIM`. Supported values are `PASS`, `FAIL`, `GRAY`, and `PROCESSING_FAILED`. Supported operators are `EQUALS` and `NOT_EQUALS`. The following condition matches an email that passes SPF.  

```json
{
  "VerdictExpression": {
    "Evaluate": {"Attribute": "SPF"},
    "Operator": "EQUALS",
    "Values": ["PASS"]
  }
}
```

DMARC policy  
Use a [DMARC expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleDmarcExpression.html) to compare the published DMARC policy with `NONE`, `QUARANTINE`, or `REJECT`. Supported operators are `EQUALS` and `NOT_EQUALS`. The following condition matches a published `REJECT` policy.  

```json
{
  "DmarcExpression": {
    "Operator": "EQUALS",
    "Values": ["REJECT"]
  }
}
```

### Address-list membership conditions
<a name="eb-rules-conditions-reference-address-lists"></a>

Use `IsInAddressList` in a [boolean expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanExpression.html) to check whether an address is in an address list. Supported properties are `RECIPIENT`, `MAIL_FROM`, `SENDER`, `FROM`, `TO`, and `CC`. Use `IS_TRUE` to match an address in the list. Use `IS_FALSE` to match an address that is not in the list.

For instructions on creating and maintaining address lists, see [Address Lists](eb-addlist.md). In the following example, replace the AWS Region, account ID, and address list ID with your own values. The condition checks whether each SMTP envelope recipient is in the address list.

```json
{
  "BooleanExpression": {
    "Evaluate": {
      "IsInAddressList": {
        "Attribute": "RECIPIENT",
        "AddressLists": [
          "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/{{al-0123456789abcdef}}"
        ]
      }
    },
    "Operator": "IS_TRUE"
  }
}
```

### Email Add On result conditions
<a name="eb-rules-conditions-reference-addons"></a>

Use an `Analysis` operand to compare an Email Add On result. The result field controls which expression type and operators apply.
+ Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html) for text results.
+ Use a [boolean expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanExpression.html) for true or false results.
+ Use a [verdict expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleVerdictExpression.html) for verdict results.

Available result fields depend on the Email Add On. For supported fields, see [Email Add Ons](eb-addons.md). In the following example, replace the AWS Region, account ID, and add-on instance ID with your own values. The condition checks a boolean `isListed` result.

```json
{
  "BooleanExpression": {
    "Evaluate": {
      "Analysis": {
        "Analyzer": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:addon-instance/{{ai-0123456789abcdef}}",
        "ResultField": "isListed"
      }
    },
    "Operator": "IS_TRUE"
  }
}
```

## Choosing between similar properties
<a name="eb-rules-conditions-choose-property"></a>

Use the property that represents the information you intend to check.

`RECIPIENT`, `TO`, and `CC`  
Use `RECIPIENT` for one SMTP envelope recipient. Use `TO` or `CC` for addresses displayed in the corresponding message header.

`MAIL_FROM`, `FROM`, and `SENDER`  
Use `MAIL_FROM` for the SMTP envelope sender. Use `FROM` for the visible `From` header. Use `SENDER` for the `Sender` header, with the `From` header used when `Sender` is absent.

`TLS` and `TLS_WRAPPED`  
Use `TLS` for any TLS-protected connection. Use `TLS_WRAPPED` only when the connection starts with TLS rather than upgrading through `STARTTLS`.

SPF or DKIM verdict and DMARC policy  
Use a verdict expression for SPF or DKIM results. Use a DMARC expression for the domain's published DMARC policy.

For example, one email can contain the following different sender values. A condition on `MAIL_FROM`, `FROM`, or `SENDER` checks only its corresponding value.

```
SMTP MAIL FROM: bounce@mailer.example
From header: billing@example.com
Sender header: notifications@example.net
```

## Limits and considerations
<a name="eb-rules-conditions-limits"></a>
+ A rule can contain up to 10 entries in `Conditions` and up to 10 entries in `Unless`.
+ Each condition contains one expression type.
+ String, IP, verdict, and DMARC expressions accept from 1 through 10 values.
+ A number expression accepts one numeric value.
+ A boolean expression does not contain a `Values` field.
+ An address-list condition accepts exactly one address-list ARN.
+ Follow the linked API reference for value lengths, patterns, and other field constraints.