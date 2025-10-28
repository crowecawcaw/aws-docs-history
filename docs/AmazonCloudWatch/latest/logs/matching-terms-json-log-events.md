# Using filter patterns to match terms in JSON log events

Use JSON filter patterns when your logs are structured in JSON format. These patterns let you target specific fields and values within JSON objects, making them ideal for:

- **Application logs:** Target specific event types, user IDs, or error codes
- **AWS service logs:** Filter CloudTrail, VPC Flow Logs, or
  other structured AWS logs
- **Microservices:** Monitor containerized applications that output structured JSON
  For example, use `{ $.eventType = "UpdateTrail" }` to find specific CloudTrail events, or `{ $.sourceIPAddress != 123.123.* }` to identify traffic from unexpected IP ranges.

Expand the following sections and browse the tabs to see examples that show how to create JSON filter patterns for common monitoring scenarios, from basic single-condition patterns to complex compound expressions.

The following examples show how to use filter patterns with JSON log events in common monitoring and troubleshooting scenarios. Each example includes the filter pattern syntax and practical use cases where you would apply it.

These patterns work with any JSON-formatted logs from applications, AWS services, containers, or custom systems. You can use them with metric filters to create CloudWatch metrics, subscription filters to route logs to other services, or Live Tail to monitor logs in real-time.

###### Note

If you test an example filter pattern
with the example JSON log event,
you must enter the example JSON log
on a single line.

**Sample JSON log event for testing:**

```
{
  "eventType": "UpdateTrail",
  "sourceIPAddress": "111.111.111.111",
  "arrayKey": [
        "value",
        "another value"
  ],
  "objectList": [
       {
         "name": "a",
         "id": 1
       },
       {
         "name": "b",
         "id": 2
       }
  ],
  "SomeObject": null,
  "cluster.name": "c"
}
```

Monitor application events by type
Track specific event types in your JSON application logs to monitor system behavior.

**Filter pattern:**

```

{ $.eventType = "UpdateTrail" }

```

**Use cases:**

- Application monitoring: Track specific user actions or system events
- Business analytics: Count occurrences of particular event types
- Troubleshooting: Focus on specific operations when investigating issues

This pattern works with any JSON logs containing an eventType field, such as:

- Application logs: `{"eventType": "UserLogin", "userId": "123"}`
- System logs: `{"eventType": "ConfigUpdate", "component": "database"}`
- API logs: `{"eventType": "UpdateTrail", "source": "cloudtrail"}`

Block suspicious IP addresses
Identify traffic that doesn't match expected IP address patterns for security monitoring.

**Filter pattern:**

```

{ $.sourceIPAddress != 123.123.* }

```

**Use cases:**

- Security monitoring: Find requests from unexpected IP ranges
- Access control: Monitor traffic outside your corporate network
- Threat detection: Identify potential unauthorized access attempts

Track specific application events
Monitor specific values in JSON arrays to track application behavior and user actions.

**Filter pattern:**

```

{ $.arrayKey[0] = "value" }

```

**Use cases:**

- User behavior tracking: Monitor specific user actions in application logs
- Feature usage: Track when specific application features are used
- Error analysis: Find logs with specific error categories in arrays

Find events using pattern matching
Use regex patterns to find events with flexible matching for field values.

**Filter pattern:**

```

{ $.eventType = %Trail% }

```

**Use cases:**

- Flexible event tracking: Find all events containing specific text patterns
- API monitoring: Track API families without specifying exact names
- Log analysis: Search for partial matches in event names or descriptions

Monitor application data with wildcards
Use wildcards and regex to find specific patterns in any array element.

**Filter pattern:**

```

{ $.arrayKey[*] = %val.{2}% }

```

**Use cases:**

- Data validation: Find arrays containing values matching specific patterns
- Content filtering: Monitor user-generated content for specific patterns
- Quality assurance: Track data format compliance across application logs

Track network traffic patterns
Monitor IP addresses within specific ranges using regex patterns and wildcards.

**Filter pattern:**

```

{ $.* = %111\.111\.111\.1[0-9]{1,2}% }

```

**Use cases:**

- Network monitoring: Track traffic from specific IP subnets
- Security analysis: Monitor access from particular network ranges
- Load balancing: Analyze traffic distribution across IP ranges

###### Note

**Quotas**

You can only use up to one wildcard selector in a property selector.

Handle JSON properties with special characters
Access JSON properties that contain periods or other special characters in their names.

**Filter pattern:**

```

{ $.['cluster.name'] = "c" }

```

**Use cases:**

- Kubernetes monitoring: Track cluster names in container logs
- Configuration tracking: Monitor settings with dotted property names
- Third-party integration: Handle logs from systems using special naming conventions

Find null or missing values
Monitor for missing data or null values that might indicate application problems.

**Filter pattern:**

```

{ $.SomeObject IS NULL }

```

**Use cases:**

- Data quality monitoring: Find records with missing required fields
- Application debugging: Track when expected data is not present
- Error detection: Monitor for incomplete API responses or database queries

Detect missing configuration fields
Find logs that are missing expected fields entirely, which can indicate configuration issues.

**Filter pattern:**

```

{ $.SomeOtherObject NOT EXISTS }

```

**Use cases:**

- Configuration validation: Ensure all required fields are present in logs
- API monitoring: Track incomplete requests or responses
- Data pipeline monitoring: Find records missing expected schema fields

###### Note

The variables `IS NOT` and `EXISTS` currently aren't supported.

Use compound expressions when you need to combine multiple conditions using logical operators AND ("&&") and OR ("||"). These patterns help you create sophisticated monitoring rules that require multiple criteria to be met or trigger on any of several conditions.

Compound expressions support parentheses ("()") and follow standard order of operations: () > && > ||. Use these patterns when simple single-condition filters aren't sufficient for your monitoring needs.

**Sample JSON log event for testing:**

```
{
    "user": {
        "id": 1,
        "email": "John.Stiles@example.com"
    },
    "users": [
        {
         "id": 2,
         "email": "John.Doe@example.com"
        },
        {
         "id": 3,
         "email": "Jane.Doe@example.com"
        }
    ],
    "actions": [
        "GET",
        "PUT",
        "DELETE"
    ],
    "coordinates": [
        [0, 1, 2],
        [4, 5, 6],
        [7, 8, 9]
    ]
}
```

Monitor specific user actions
Track when specific users perform particular actions by combining user identification with action monitoring.

**Filter pattern:**

```

{ ($.user.id = 1) && ($.users[0].email = "John.Doe@example.com") }

```

**Use cases:**

- Security auditing: Track when specific admin users access sensitive resources
- Compliance monitoring: Ensure certain users only perform approved actions
- User behavior analysis: Monitor correlations between user attributes and actions

Alert on any suspicious activity
Create broad monitoring that triggers when any of several concerning conditions occur.

**Filter pattern:**

```

{ $.user.email = "John.Stiles@example.com" || $.coordinates[0][1] = "nonmatch" && $.actions[2] = "nonmatch" }

```

**Use cases:**

- Security monitoring: Alert when specific users are active OR when unusual data patterns occur
- System health: Monitor for any of several different error conditions
- Flexible alerting: Create catch-all rules for various concerning scenarios

Require multiple conditions for alerts
Reduce false positives by requiring multiple specific conditions to be met before triggering alerts.

**Filter pattern:**

```

{ ($.user.email = "John.Stiles@example.com" || $.coordinates[0][1] = "nonmatch") && $.actions[2] = "nonmatch" }

```

**Use cases:**

- High-confidence alerting: Only alert when multiple suspicious indicators align
- Complex business rules: Monitor scenarios requiring multiple criteria
- Noise reduction: Prevent alerts from single isolated events

###### Note

**Quotas**

You can only use up to one wildcard selector in a property selector, and up to three wildcard selectors in a filter pattern with compound expressions.

Monitor failed correlation attempts
Track when expected relationships between data fields don't match, which can indicate data quality issues.

**Filter pattern:**

```

{ ($.user.id = 2 && $.users[0].email = "nonmatch") || $.actions[2] = "GET" }

```

**Use cases:**

- Data validation: Find records where related fields don't match expected patterns
- System integrity: Monitor for data corruption or synchronization issues
- Quality assurance: Track when data relationships break down
