# Auto Validation

Auto Validation automatically reviews all outbound email addresses before sending and only
delivers messages to recipients that meet your selected validation threshold. This
helps you protect your sender reputation by preventing sends to likely invalid or risky addresses without
requiring manual intervention or API integration.

When Auto Validation is enabled, Amazon SES validates each recipient address as part of attempting
delivery. Addresses that don't meet your threshold are automatically suppressed.
You can also set up configuration set [event destinations](event-publishing-add-event-destination.md "event-publishing-add-event-destination.md") to track
which emails did not pass the validation threshold.

###### Validation thresholds

Auto Validation currently supports three validation thresholds:

- SES managed – Amazon SES automatically manages the
  threshold to suppress invalid addresses. This option allows Amazon SES to optimize the
  validation threshold based on your sending patterns and reputation.
- High – Allows emails to be sent only to
  addresses with high delivery likelihood. This provides maximum protection
  for your sender reputation but may suppress some legitimate addresses with medium
  delivery confidence.
- Medium – Allows emails to be sent to
  addresses with medium or high delivery likelihood. This balances reputation protection
  with delivery reach by allowing addresses with medium and high delivery confidence. This suppresses delivery to email addresses with low
  delivery confidence.

###### Important

If you choose High or Medium thresholds instead of SES managed, it is important to
monitor your delivery metrics and validation results regularly.

## Managing Auto Validation with the Amazon SES

console

The following procedure shows you how to enable or change Auto Validation settings
using the Amazon SES console.

###### To manage Auto Validation using the Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Auto Validation** under
   **Email Validation**.
3. Select **Enabled** checkbox to turn on the
   feature.
4. Choose a validation threshold.
5. Choose **Save changes**.

The **Auto Validation** panel shows your updated
settings.

###### Important

Auto Validation applies to all outbound emails sent through your account. Addresses
that don't meet your threshold will be suppressed. You also have an option to enable auto validation at the configuration set level.
Suppressed sends still count towards your daily send quota and you will still be charged the standard outgoing message fee for suppressed sends in addition to the fee for auto validation.
For pricing information, see the [SES pricing page](https://aws.amazon.com/ses/pricing/ "https://aws.amazon.com/ses/pricing/").

## Enable Auto Validation at Configuration set level

You can override account-level Auto Validation settings for specific configuration
sets. This allows you to apply different validation thresholds for different types of
email campaigns.

###### To configure Auto Validation for a configuration set

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Configuration sets**
   under **Configuration**.
3. Choose the configuration set you want to configure.
4. In the **Auto Validation options** section, choose
   **Edit**.
5. Select the **Override account level Auto Validation
   settings** checkbox.
6. Select the **Auto Validation enabled** checkbox to enable
   Auto Validation for this configuration set.
7. For **Validation threshold**, select either:
   - **SES managed** – Amazon SES automatically manages
     the threshold.
     or
   - **High** – Only addresses with high
     delivery likelihood.
   - **Medium** – Addresses with medium
     delivery likelihood.

8. Choose **Save changes**.

If you don't override the account-level settings, the configuration set will use the
Auto Validation settings defined at the account level. You can also set up [event destinations](event-publishing-add-event-destination.md "event-publishing-add-event-destination.md") to track
which emails did not pass the validation threshold.

## Managing Auto Validation with the

AWS CLI

The following examples show you how to enable and configure Auto Validation using the
AWS CLI.

###### To manage Auto Validation using the AWS CLI

You can use the [`PutAccountSuppressionAttributes`](../APIReference-V2/API_PutAccountSuppressionAttributes.md "../APIReference-V2/API_PutAccountSuppressionAttributes.md") operation in the
Amazon SES API v2 to manage Auto Validation. You can call this operation from the AWS CLI,
as shown in the following examples.

- Enable Auto Validation with a high threshold:

```
aws --region us-east-1 sesv2 put-account-suppression-attributes --cli-input-json file://auto-validation.json
```

The input file looks similar to this:

```
{
    "SuppressedReasons": ["BOUNCE", "COMPLAINT"],
    "ValidationOptions": {
        "ConditionThreshold": {
            "ConditionThresholdEnabled": "ENABLED",
            "OverallConfidenceThreshold": {
                "Verdict": "HIGH"
            }
        }
    }
}
```

- Change the threshold to medium:

```
{
    "SuppressedReasons": ["BOUNCE", "COMPLAINT"],
    "ValidationOptions": {
        "ConditionThreshold": {
            "ConditionThresholdEnabled": "ENABLED",
            "OverallConfidenceThreshold": {
                "Verdict": "MEDIUM"
            }
        }
    }
}
```

- Use SES managed threshold:

```
{
    "SuppressedReasons": ["BOUNCE", "COMPLAINT"],
    "ValidationOptions": {
        "ConditionThreshold": {
            "ConditionThresholdEnabled": "ENABLED",
            "OverallConfidenceThreshold": {
                "Verdict": "MANAGED"
            }
        }
    }
}
```

- Disable Auto Validation:

```
{
    "SuppressedReasons": ["BOUNCE", "COMPLAINT"],
    "ValidationOptions": {
        "ConditionThreshold": {
            "ConditionThresholdEnabled": "DISABLED"
        }
    }
}
```

- To verify the outcome:

```
aws --region us-east-1 sesv2 get-account
```

For more information about parameter values and data types, see the [`SuppressionAttributes`](../APIReference-V2/API_SuppressionAttributes.md "../APIReference-V2/API_SuppressionAttributes.md") data type in the Amazon SES API v2
reference.

###### To configure Auto Validation for a configuration set using the AWS CLI

You can use the [`PutConfigurationSetSuppressionOptions`](../APIReference-V2/API_PutConfigurationSetSuppressionOptions.md "../APIReference-V2/API_PutConfigurationSetSuppressionOptions.md") operation to
override Auto Validation settings for a specific configuration set.

- Override account-level settings for a configuration set:

```
aws --region us-east-1 sesv2 put-configuration-set-suppression-options --cli-input-json file://config-set-auto-validation.json
```

The input file looks similar to this:

```
{
    "ConfigurationSetName": "my-config-set",
    "SuppressedReasons": ["BOUNCE", "COMPLAINT"],
    "ValidationOptions": {
        "ConditionThreshold": {
            "ConditionThresholdEnabled": "ENABLED",
            "OverallConfidenceThreshold": {
                "Verdict": "HIGH"
            }
        }
    }
}
```

- To verify the outcome:

```
aws --region us-east-1 sesv2 get-configuration-set --configuration-set-name my-config-set
```
