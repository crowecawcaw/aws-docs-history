# Using filter patterns to match

terms in unstructured log events

Use unstructured filter patterns when your logs are plain text without a specific format like JSON. These patterns work with application logs, system logs, web server logs, and any text-based log format where you need to find specific words or phrases.

Unstructured patterns are ideal for:

- **Simple monitoring:** Track error keywords, status messages, or user actions
- **Legacy systems:** Work with older applications that don't output structured JSON logs
- **Quick setup:** Start monitoring immediately without parsing complex log formats
  For example, use `ERROR` to find any log entry containing that word, or `"INTERNAL SERVER ERROR"` to match that exact phrase.

Expand the following section and browse the tabs to see examples that show different ways to create unstructured filter patterns for common monitoring scenarios.

The following examples contain code snippets that show how you can use filter
patterns to match terms in unstructured log events.

###### Note

Filter patterns are case sensitive. Enclose exact phrases and terms that
include non-alphanumeric characters in double quotation marks
(**""**).

Monitor application errors
Find all log entries containing errors to track application health
and troubleshoot issues.

**Filter pattern:**

```

ERROR

```

**Use cases:**

- Live Tail: Monitor errors in real-time as they
  occur
- Metric Filter: Create CloudWatch metrics to count error
  occurrences
- Subscription Filter: Forward error logs to alerting
  systems

This pattern matches log entries such as:

- `[ERROR 400] BAD REQUEST`
- `[ERROR 401] UNAUTHORIZED REQUEST`
- `[ERROR 419] MISSING ARGUMENTS`

Track related application issues
Find log entries that contain multiple related terms to identify
specific types of problems.

**Filter pattern:**

```

ERROR ARGUMENTS

```

**Use cases:**

- Troubleshoot parameter validation issues in APIs
- Monitor configuration problems in applications
- Track input validation failures

This pattern matches log entries such as:

- `[ERROR 419] MISSING ARGUMENTS`
- `[ERROR 420] INVALID ARGUMENTS`

Monitor any type of issue
Create flexible monitoring that captures different types of
problems without requiring all terms to be present.

**Filter pattern:**

```

?ERROR ?ARGUMENTS

```

**Use cases:**

- Broad error monitoring across different application
  components
- Initial troubleshooting when you're not sure what specific
  errors to look for
- Creating comprehensive error dashboards

This pattern matches log entries such as:

- `[ERROR 400] BAD REQUEST`
- `[ERROR 419] MISSING ARGUMENTS`
- `[INFO] INVALID ARGUMENTS PROVIDED`

Find specific error messages
Search for exact error messages to identify specific system
problems.

**Filter pattern:**

```

"INTERNAL SERVER ERROR"

```

**Use cases:**

- Monitor critical system failures (HTTP 500 errors)
- Track specific database connection issues
- Alert on exact error conditions that require immediate
  attention

This pattern matches log entries such as:

- `[ERROR 500] INTERNAL SERVER ERROR`

Filter out noise from monitoring
Focus on important errors by excluding common, less critical
issues.

**Filter pattern:**

```

ERROR -ARGUMENTS

```

**Use cases:**

- Monitor serious errors while ignoring user input
  validation issues
- Focus alerts on system problems rather than user
  mistakes
- Reduce alert fatigue by filtering out expected error
  types

This pattern matches log entries such as:

- `[ERROR 400] BAD REQUEST`
- `[ERROR 401] UNAUTHORIZED REQUEST`

Capture all log activity
Monitor all log events for comprehensive logging or when setting
up new monitoring.

**Filter pattern:**

```

" "

```

**Use cases:**

- Forward all logs to external log analysis systems
- Create comprehensive log archives
- Test subscription filters before applying specific
  patterns
