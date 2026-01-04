# Service quotas in Amazon SES

The following sections list and describe the quotas that apply to Amazon SES resources and
operations. Some quotas can be increased, while others can't. To determine whether you can
request an increase for a quota, refer to the **Adjustable**
column.

###### Note

SES quotas are for each AWS Region that you use in your AWS account.

## Email sending quotas

The following quotas apply to sending email through SES.

### Sending quotas

Quotas are based on the number of recipients, rather than on the number of
messages.

| Resource                                                         | Default Quota                                                                                                                                                                            | Adjustable                                                                                   |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Number of emails that can be sent per 24-hour period             | If your account is in the sandbox, you can send up to 200<br>emails per 24-hour period.<br>If your account is out of the sandbox, this number varies<br>based on your specific use case. | [Yes](manage-sending-quotas-request-increase.md "manage-sending-quotas-request-increase.md") |
| Number of emails that can be sent per second (_sending<br>rate_) | If your account is in the sandbox, you can send 1 email per<br>second.<br>If your account is out of the sandbox, this rate varies based<br>on your specific use case.                    | [Yes](manage-sending-quotas-request-increase.md "manage-sending-quotas-request-increase.md") |

### Message quotas

| Resource                                                                                                                                                                      | Default Quota                              | Adjustable                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Using the [SES v1 API](../APIReference.md "../APIReference.md")<br>• Maximum message size<br>(including attachments)                                                          | 10 MB per message (after base64 encoding). | No _(For workloads with message sizes in excess of<br>10MB, consider migrating to the [SES v2<br>API](../APIReference-V2.md "../APIReference-V2.md").)_ |
| Using the [SES v2 API](../APIReference-V2.md "../APIReference-V2.md") or [SMTP](send-email-smtp.md "send-email-smtp.md")<br>• Maximum message size (including<br>attachments) | 40 MB per message (after base64 encoding). | No                                                                                                                                                      |

###### Note

Messages larger than 10MB are subject to bandwidth throttling, and depending
on your sending rate, you may be throttled to as low as 40MB/s. For example, you
could send a 40MB message at the rate of 1 message per second, or two 20MB
messages per second.

### Sender and recipient quotas

| Resource                                                                                  | Default Quota                                                                                                                          | Adjustable                                                           |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Maximum number of recipients per message                                                  | 50 recipients per message.<br>NoteA recipient is any "To", "CC", or "BCC" address.                                                     | No.                                                                  |
| Maximum number of identities that you can verify                                          | 10,000 identities per AWS Region.<br>NoteAn \*identity<br>• is a domain or email<br>address that you use to send email through<br>SES. | Please contact your<br>AWS Account Manager to discuss your use case. |
| Maximum number of dedicated IP pools (inclusive of both<br>managed and standard IP pools) | 50                                                                                                                                     | No                                                                   |

### Quotas related to event publishing

| Resource                                                      | Default Quota                                                                                                                                                                                                            | Adjustable |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| Maximum number of configuration sets                          | 10,000                                                                                                                                                                                                                   | No         |
| Maximum length of configuration set name                      | Configuration set names can contain up to 64 alphanumeric<br>characters. They can also contain hyphens (-) and underscores<br>(\_). Names can't contain spaces, accented characters, or any<br>other special characters. | No         |
| Maximum number of event destinations per configuration<br>set | 10                                                                                                                                                                                                                       | No         |
| Maximum number of dimensions per CloudWatch event destination | 10                                                                                                                                                                                                                       | No         |

### Email template quotas

| Resource                                                 | Default Quota                                                                                                                                                                                                                               | Adjustable |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Maximum number of email templates in each AWS Region     | 20,000                                                                                                                                                                                                                                      | No         |
| Maximum template size                                    | 500 KB                                                                                                                                                                                                                                      | No         |
| Maximum number of replacement values in each template    | Unlimited                                                                                                                                                                                                                                   | N/A        |
| Maximum number of recipients for each templated<br>email | 50 destinations. A \*destination<br>• is any<br>email address on the "To", "CC", or "BCC" lines.<br>NoteThe number of destinations you can contact in a single<br>call to the API may be limited by your account's maximum<br>sending rate. | No         |

## Email receiving quotas

The following table lists the quotas associated with receiving email through
SES.

| Resource                                                                                         | Default Quota | Adjustable |
| ------------------------------------------------------------------------------------------------ | ------------- | ---------- |
| Maximum number of rules per receipt rule set                                                     | 200           | No         |
| Maximum number of actions per receipt rule                                                       | 10            | No         |
| Maximum number of recipients per receipt rule                                                    | 500           | No         |
| Maximum number of receipt rule sets per AWS account                                              | 40            | No         |
| Maximum number of IP address filters per AWS account                                             | 100           | No         |
| Maximum email size (including headers) that can be stored in an<br>Amazon S3 bucket              | 40 MB         | No         |
| Maximum email size (including headers) that can be published using<br>an Amazon SNS notification | 150 KB        | No         |
| Maximum email headers size that can be published using an Amazon SNS<br>notification             | 10 KB         | No         |
| Maximum email headers size that can be published using an<br>AWS Lambda function                 | 50 KB         | No         |

## Mail Manager quotas

The following table lists the quotas associated with Mail Manager.

| Resource                                                 | Default Quota | Adjustable |
| -------------------------------------------------------- | ------------- | ---------- |
| Maximum number of open ingress endpoints                 | 10            | No         |
| Maximum number of authorized ingress endpoints           | 50            | No         |
| Maximum number of recipients per message                 | 100           | No         |
| Maximum email size (including headers)                   | 40 MB         | No         |
| Maximum number of traffic policy statements              | 20            | No         |
| Maximum number of traffic policy statement conditions    | 10            | No         |
| Maximum number of traffic policies per region            | 100           | No         |
| Maximum number of SMTP relays                            | 40            | No         |
| Maximum number of Address Lists per region               | 100           | No         |
| Maximum number of addresses per Address List             | 100,000       | No         |
| Maximum number of rule sets                              | 40            | No         |
| Maximum number of rules per rule set                     | 40            | No         |
| Maximum number of conditions per rule                    | 10            | No         |
| Maximum number of actions per rule                       | 10            | No         |
| Maximum number of relay or send actions per rule set     | 10            | No         |
| Maximum number of \*active<br>• archives                 | 10            | No         |
| Maximum number of archive search results                 | 1000          | No         |
| Maximum number of exported archive search results        | 250,000       | No         |
| Maximum number of running search requests in parallel    | 1             | No         |
| Maximum number of running export requests in parallel    | 1             | No         |
| Maximum number of retention changes for archive per week | 1             | No         |

## General quotas

The following table lists quotas that apply to both sending and receiving email
through SES.

### SES API sending quotas

| Resource                                          | Default Quota                                                                                                                    | Adjustable |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Rate at which you can call Amazon SES API actions | All actions (except for `SendEmail`,<br>`SendRawEmail`, and<br>`SendTemplatedEmail`) are throttled at one<br>request per second. | No         |
| MIME parts                                        | 500                                                                                                                              | No         |

### SES miscellaneous quotas

| Resource                                 | Default Quota | Adjustable |
| ---------------------------------------- | ------------- | ---------- |
| Maximum number of concurrent import jobs | 20            | No         |
| Maximum number of concurrent export jobs | 20            | No         |
