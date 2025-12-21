# Email Validation API

API validation allows you to validate individual email addresses through API calls,
providing immediate feedback about address validity, deliverability, and risk factors. This
feature is designed for validating addresses at the point of collection, such as during user
registration, subscription forms, or any other scenario where you need timely validation
results.

API validation performs multiple checks on each email address, including syntax
validation, domain verification, mailbox existence checks, and others. The
validation results include confidence verdicts (HIGH, MEDIUM, or LOW) for overall validity
and individual evaluations.

###### Validation checks performed

API validation performs the following evaluations on each email address:

- Syntax Validation ('HasValidSyntax') – Checks that the email
  address follows proper RFC standards and contains valid characters in the correct
  format.
- DNS Records ('HasValidDnsRecords') – Checks that the domain
  exists, has valid DNS records, and is configured to receive email.
- Mailbox Existence ('MailboxExists') – Checks that the mailbox
  exists and can receive messages without actually sending an email.
- Role Address ('IsRoleAddress') – Identifies role-based
  addresses (such as admin@, support@, or info@) that may have lower engagement
  rates.
- Disposable Domain ('IsDisposable') – Checks disposable or
  temporary email addresses that could negatively impact your sender reputation.
- Random String Patterns ('IsRandomInput') – Checks randomly generated
  patterns.

## Using API validation with the

Amazon SES console

The following procedure shows you how to validate an email address using the Amazon SES
console.

###### To validate an email address using the Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Email addresses
   validation** under **Email Validation**.
3. In the **Validate email address** section, enter the email
   address you want to validate in the **Email address**
   field.
4. Choose **Validate**.

The validation results appear in the **Validation results**
panel, showing:

    * **IsValid** – Overall validity with a
     confidence verdict (HIGH, MEDIUM, or LOW).
    * **Evaluations** – Individual evaluation results
     with confidence verdicts for syntax, DNS records, mailbox existence, and
     risk factors listed above.

## Using API validation with the

AWS CLI

The following examples show you how to validate email addresses using the
AWS CLI.

###### To validate an email address using the AWS CLI

You can use the [`GetEmailAddressInsights`](../APIReference-V2/API_GetEmailAddressInsights.md "../APIReference-V2/API_GetEmailAddressInsights.md") operation in the Amazon SES API v2 to
validate email addresses. You can call this operation from the AWS CLI, as shown in
the following examples.

- Validate a single email address:

```
aws --region us-east-1 sesv2 get-email-address-insights --email-address user@example.com
```

- The response looks similar to this:

```
{
    "MailboxValidation": {
        "IsValid": {
            "ConfidenceVerdict": "HIGH"
        },
        "Evaluations": {
            "HasValidSyntax": {
                "ConfidenceVerdict": "HIGH"
            },
            "HasValidDnsRecords": {
                "ConfidenceVerdict": "MEDIUM"
            },
            "MailboxExists": {
                "ConfidenceVerdict": "MEDIUM"
            },
            "IsRoleAddress": {
                "ConfidenceVerdict": "LOW"
            },
            "IsDisposable": {
                "ConfidenceVerdict": "LOW"
            },
            "IsRandomInput": {
                "ConfidenceVerdict": "LOW"
            }
        }
    }
}
```

- For more information about response values and data types, see the [`MailboxValidation`](../APIReference-V2/API_MailboxValidation.md "../APIReference-V2/API_MailboxValidation.md") data type in the Amazon SES API v2
  reference.
- Ensure your IAM identity has the required permissions for Email Validation API
  calls and CloudWatch metrics publishing:

```
{
  "Version": "2012-10-17		 	 	 ",
  "Statement": [
    {
      "Sid": "EmailValidationPermissions",
      "Effect": "Allow",
      "Action": [
        "ses:GetEmailAddressInsights",
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": "*"
    }
  ]
}
```

The `GetEmailAddressInsights` permission is required for API
validation calls, and `CreateServiceLinkedRole` enables CloudWatch
metrics publishing for validation activity.

###### Interpreting validation results

The validation response includes confidence verdicts to help you make decisions
about email addresses:

- `IsValid` – Overall validity assessment with a confidence
  verdict of HIGH, MEDIUM, or LOW. HIGH validity confidence indicates high delivery likelihood for the email address, MEDIUM indicates moderate delivery likelihood and LOW indicates low delivery likelihood.
- `Evaluations` – Individual evaluation results, each with a
  confidence verdict:
  - `HIGH` – Strong indication of the specific check
    (e.g., HIGH for IsRandomInput means the email is very likely randomly generated).
  - `MEDIUM` – Moderate indication of the specific check
    (e.g., MEDIUM for IsRandomInput means that there is some likelihood that the email address is randomly generated).
  - `LOW` – Weak or no indication of the specific check
    (e.g., LOW for IsRandomInput means that the email address is less likely randomly generated).
