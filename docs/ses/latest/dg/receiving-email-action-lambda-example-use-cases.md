# Use case examples

The following examples outline some rules that you might set up to use Lambda function
outcomes to control your mail flow. For demonstration purposes, many of these examples use
the S3 action as the outcome.

## Use case 1: Drop

spam across all domains

This example demonstrates a global rule that drops spam across all of your domains.
Rules 2 and 3 are included to show that you can apply domain-specific rules after the
spam is dropped over all the domains.

### Rule

1

_Recipient list:_ Empty. This rule will therefore apply to all
recipients under all of your verified domains.

_Actions_

1. Lambda action (synchronous) that returns `STOP_RULE_SET` if the
   email is spam. Otherwise, it returns `CONTINUE`. See the example
   Lambda function for dropping spam in [Lambda function
   examples](receiving-email-action-lambda-example-functions.md "receiving-email-action-lambda-example-functions.md").

### Rule

2

_Recipient list:_ example1.com

_Actions_

1. Any action.

### Rule

3

_Recipient list:_ example2.com

_Actions_

1. Any action.

## Use case 2: Bounce

spam across all domains

This example demonstrates a global rule that bounces spam across all of your domains.
Rules 2 and 3 are included to show that you can apply domain-specific rules after the
spam is bounced over all the domains.

### Rule

1

_Recipient list:_ Empty. This rule will therefore apply to all
recipients under all of your verified domains.

_Actions_

1. Lambda action (synchronous) that returns `CONTINUE` if the
   email is spam. Otherwise, it returns `STOP_RULE`.
2. Bounce action ("500 5.6.1. Message content rejected").
3. Stop action.

### Rule

2

_Recipient list:_ example1.com

_Actions_

1. Any action

### Rule

3

_Recipient list:_ example2.com

_Actions_

1. Any action

## Use case 3: Apply

the most specific rule

This example demonstrates how you can use the Stop action to prevent emails from being
processed by multiple rules. In this example, you have one rule for a specific address,
and another rule for all email addresses under the domain. By using the Stop action,
messages that match the rule for the specific email address are not processed by the
more generic rule that applies to the domain.

### Rule

1

_Recipient list:_ user@example.com

_Actions_

1. Lambda action (asynchronous).
2. Stop action.

### Rule

2

_Recipient list:_ example.com

_Actions_

1. Any action.

## Use case 4: Log mail

events to CloudWatch

This example demonstrates how to keep an audit log of all mail going through your
system before saving the mail to Amazon SES.

### Rule

1

_Recipient list:_ example.com

_Actions_

1. Lambda action (asynchronous) that writes the event object to a CloudWatch log.
   The example Lambda functions in [Lambda function
   examples](receiving-email-action-lambda-example-functions.md "receiving-email-action-lambda-example-functions.md") log to
   CloudWatch.
2. S3 action.

## Use case 5: Drops

mail that fails DKIM

This example demonstrates how you can save all incoming email to an Amazon S3 bucket, but
only send email that goes to a specific email address, and passes DKIM, to your
automated email application.

### Rule

1

_Recipient list:_ example.com

_Actions_

1. S3 action.
2. Lambda action (synchronous) that returns `STOP_RULE_SET` if the
   message fails DKIM. Otherwise, it returns `CONTINUE`.

### Rule

2

_Recipient list:_ support@example.com

_Actions_

1. Lambda action (asynchronous) that triggers the automated
   application.

## Use case 6: Filters

mail based on subject line

This example demonstrates how you can drop all of a domain's incoming mail that
contains the word "discount" in the subject line, and then process mail intended for an
automated system one way, and process mail addressed to all other recipients in the
domain a different way.

### Rule

1

_Recipient list:_ example.com

_Actions_

1. Lambda action (synchronous) that returns `STOP_RULE_SET` if the
   subject line contains the word "discount". Otherwise, it returns
   `CONTINUE`.

### Rule

2

_Recipient list:_ support@example.com

_Actions_

1. S3 action with bucket 1.
2. Lambda action (asynchronous) that triggers the automated
   application.
3. Stop action.

### Rule

3

_Recipient list:_ example.com

_Actions_

1. S3 action with bucket 2.
2. Lambda action (asynchronous) that processes email for the rest of the
   domain.
