# Managing Your Rules

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

**Proxy Rules** - proxy rules are the fundamental components of proxy configuration, controlling how traffic is processed and managed. Each rule operates as part of the traffic evaluation process, combining specific match conditions with defined actions. Each rule must be associated with exactly one rule group and defines the core logic for filtering, inspecting, and handling HTTP/HTTPS traffic.

## Rule Structure

A filtering rule requires these components:

- Rule name - The name serves as a unique identifier (such as "block-social-media" or "allow-aws-apis"), while the description documents the rule's purpose and function.
- Phase - The phase type determines the processing stage (PreDNS, PreREQUEST, or PostRESPONSE). Match conditions establish the criteria for traffic evaluation with operators and values.
- Action - The action specifies the response to matching traffic (allow, deny, or alert)
- Position - The insert position determines priority ordering within the rule sequence. The rules within a rule group have priority
- The rule groups within a proxy configuration have priority.
- Rule Conditions - Conditions are specified as an array where all criteria must be met for the rule to trigger (logical AND). Each rule can belong to only one rule group at a time, ensuring clear organizational structure and preventing conflicts.

###### Condition keys:

`request:SourceAccount`
`request:SourceVpc`
`request:SourceVpce`
`request:Time`
`request:SourceIp`
`request:DestinationIp`
`request:SourcePort`
`request:DestinationPort`
`request:Protocol`
`request:DestinationDomain`
`request:Http:Uri`
`request:Http:Method`
`request:Http:UserAgent`
`request:Http:ContentType`
`request:Http:Header/CustomHeaderName`
`response:Http:StatusCode`
`response:Http:ContentType`
`response:Http:Header/CustomHeaderName`

###### Note

Without TLS decryption, you can only filter based on IP in the pre-request phase. Rules which match on HTTP fields will not match for HTTPS requests unless you have turned on TLS intercept.

## Rule operations

Network Firewall Proxy provides several operations to manage your proxy rules effectively. These actions allow you to create, modify, delete, and monitor rules within your rule groups. On the console, all the above rule operations can be performed only within a rule group. On the AWS console, click on rule groups and select the rule that you want to perform the operation on. Here are the available rule management actions:

- Create Rules - Adds new rules to an existing rule group.
- Delete Rules - Removes specified rules from a rule group.
- Modify Rule - Updates existing rule, including the action or conditions for a specified rule.
- Describe Rule - Retrieves detailed information about a specific rule.
- List Rules - Displays all proxy rule resource names associated with an account.

## Managing proxy rule priority and evaluation order

Understanding rule evaluation order is crucial for creating effective proxy policies. Rules are evaluated in a specific sequence. This sequence determines which rules take precedence.

###### Traffic Phases evaluation order

Rules are evaluated in the following traffic phase order, and this sequence cannot be changed:

1. Pre-DNS – Evaluated before domain name resolution
2. Pre-request – Evaluated after DNS resolution but before sending the HTTP/s request
3. Post-response – Evaluated after receiving the HTTP/s response

###### Note

If a rule in an earlier phase denies traffic, subsequent phases are not evaluated for that connection.

###### Within-phase priority

Within each phase type, rules are evaluated by insert position in ascending order (0, 1, 2, 3, etc.). The first rule that matches determines the action taken. Lower insert position numbers have higher priority. Example rule evaluation sequence:

```

    PreDNS Rules:
    1. insertPosition: 0 - Allow *.amazonaws.com (matches. action: ALLOW)
    2. insertPosition: 1 - Deny *.com (not evaluated - previous rule matched)

    PreREQUEST Rules:
    1. insertPosition: 0 - Deny POST methods (no match)
    2. insertPosition: 1 - Allow GET methods (matches. action: ALLOW)

    PostRESPONSE Rules:
    1. insertPosition: 0 - Alert on 5xx status codes (matches. action: ALERT + ALLOW)

```

In the above sequence, traffic to \*.amazonaws.com is first evaluated by Pre-DNS rules, where it matches and is allowed by the first rule. In the Pre-request phase, since it's a GET method (not POST), it doesn't match the first rule and matches the second rule allowing GET methods. Finally, if this traffic returns a 5xx status code, it will trigger an alert in the Post-response phase while still being allowed through.

If a new rule is added to the list of rules, then the rules get down shifted. If a rule is added to a certain position where another rule already exists, then the rules automatically be re-ordered, existing rules will move down the priority order.

## Example filtering rules

These examples demonstrate common proxy filtering patterns that address typical security and compliance requirements.

###### Account-based access control

Restrict DNS resolution to specific AWS accounts:

```
{
  "proxyRuleName": "allow-trusted-accounts",
  "description": "Allow DNS resolution from trusted AWS accounts only",
  "action": "allow",
  "insertPosition": 1,
  "conditions": [
    {
      "conditionKey": "request:SourceAccount",
      "conditionOperator": "StringEquals",
      "conditionValues": ["&ExampleAccountNo1;", "&ExampleAccountNo2;"]
    }
  ]
}
```

###### VPC-based blocking

Block requests from specific VPCs:

```
{
  "proxyRuleName": "block-untrusted-vpcs",
  "description": "Block requests from untrusted VPCs",
  "action": "deny",
  "insertPosition": 2,
  "conditions": [
    {
      "conditionKey": "request:SourceVpc",
      "conditionOperator": "StringEquals",
      "conditionValues": [
        "vpc-094feb95245dfde25",
        "vpc-0b8f8319f8db21ba1"
      ]
    }
  ]
}
```

###### Custom header validation

Require specific authentication headers:

```
{
  "proxyRuleName": "require-auth-token",
  "description": "Allow requests with valid authentication token",
  "action": "allow",
  "insertPosition": 1,
  "conditions": [
    {
      "conditionKey": "request:Http:Header/x-auth-token",
      "conditionOperator": "StringEquals",
      "conditionValues": ["valid-token-value"]
    }
  ]
}
```

###### Port-based monitoring

Alert on connections to high-numbered ports:

```
{
  "proxyRuleName": "monitor-high-ports",
  "description": "Alert on connections to ports above 8000",
  "action": "alert",
  "insertPosition": 10,
  "conditions": [
    {
      "conditionKey": "request:DestinationPort",
      "conditionOperator": "NumericGreaterThan",
      "conditionValues": ["8000"]
    }
  ]
}
```

###### Error response monitoring

Alert on server error responses:

```
{
  "proxyRuleName": "alert-server-errors",
  "description": "Alert on HTTP 5xx server errors",
  "action": "alert",
  "insertPosition": 1,
  "conditions": [
    {
      "conditionKey": "response:HttpStatusCode",
      "conditionOperator": "NumericGreaterThanEquals",
      "conditionValues": ["500"]
    }
  ]
}
```
