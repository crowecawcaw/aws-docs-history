# Configure alarms to create investigations

You can configure an existing CloudWatch alarm to automatically create investigations in
CloudWatch investigations. When the alarm enters the ALARM state, CloudWatch automatically creates a new
investigation or adds to an existing investigation based on the deduplication
string.

When configuring an alarm to automatically create investigations, you'll need to
specify an Amazon Resource Name (ARN) in the alarm's actionArns. This ARN identifies the
investigation group where alarm-triggered investigations will be created. You can
optionally include a deduplication string in the ARN to group related alarms.

## ARN format and parameters

The ARN pattern for investigation group alarm actions follows this format:

```
arn:aws:aiops:region:account-id:investigation-group/investigation-group-identifier#DEDUPE_STRING=value
```

The following table describes each ARN component:

| Parameter                                   | Description                                                                                                                                                                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `region` (required)                         | The AWS Region where your investigation group is located. For<br>example: `us-east-1`.                                                                                                                                       |
| `account-id` (required)                     | Your 12-digit AWS account ID. For example:<br>`123456789012`.                                                                                                                                                                |
| `investigation-group-identifier` (required) | The unique identifier of your investigation group. Fore example,<br>`sMwwg1IogXdvL7UZ`                                                                                                                                       |
| `DEDUPE_STRING=value` (optional)            | A deduplication string that groups related alarms into the same<br>investigation. When multiple alarms use the same deduplication<br>string, they contribute to a single investigation instead of<br>creating separate ones. |

**Example without deduplication string:**

```
arn:aws:aiops:us-east-1:123456789012:investigation-group/sMwwg1IogXdvL7UZ
```

**Example with deduplication string:**

```
arn:aws:aiops:us-east-1:123456789012:investigation-group/sMwwg1IogXdvL7UZ#DEDUPE_STRING=performance
```

### Benefits of deduplication strings

Deduplication strings help you organize related alarms and reduce
investigation fragmentation. Use deduplication strings when:

- **Multiple alarms monitor the same
  system** - CPU, memory, and disk alarms for the same EC2
  instance can share a deduplication string to create one comprehensive
  investigation.
- **Cascading failures occur** - When one
  issue triggers multiple related alarms, the same deduplication string
  prevents creating separate investigations for each symptom.
- **You want to categorize by problem
  type** - Use descriptive strings like "performance",
  "connectivity", or "security" to group alarms by issue category.

Effective deduplication string examples:

- `DEDUPE_STRING=webserver-performance` - Groups
  performance-related alarms for web servers
- `DEDUPE_STRING=database-connectivity` - Groups database
  connection issues
- `DEDUPE_STRING=instance-i-1234567890abcdef0` - Groups all
  alarms for a specific EC2 instance

###### Note

If no deduplication string is specified, the system uses a default
combination of alarm name, account ID, and region to group
investigations.

For more information about investigation groups, see [Set up an investigation group](Investigations-GetStarted-Group.md "Investigations-GetStarted-Group.md").
