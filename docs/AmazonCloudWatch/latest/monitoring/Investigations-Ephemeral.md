# Conduct an CloudWatch investigation without

additional configuration

You can conduct a CloudWatch investigations AI-powered root cause analysis without any additional
configuration of your AWS account using the **Investigations**
feature available in **Operational troubleshooting**.

These investigations provide instant access to CloudWatch investigations capabilities from commonly used
telemetry sources in the AWS console. This type of investigation is session-based,
read-only, and automatically deleted after 24 hours.

The investigation pane provides you:

- **AI-generated observations** - Telemetry that
  fans out from your initial observation you provided to locate additional
  supporting data that can lead to a potential root cause.
- **Root cause hypotheses** - Potential
  explanations for what's causing the problem, including causal diagrams when
  multiple resources are involved
- **Natural language explanations** -
  Easy-to-understand descriptions of findings and recommendations
  You can use the suggestions from the investigation pane to help accelerate your
  troubleshooting process.

## To start an investigation

1. Navigate to any supported telemetry source showing an issue you want to
   investigate, such as:
   - A CloudWatch metric showing unusual patterns
   - A CloudWatch alarm in ALARM state
   - A Lambda function's monitoring tab showing performance
     issues

2. In **Operational troubleshooting**, choose the
   **Investigate** tab, then choose **Start
   investigation**.
3. Watch as CloudWatch investigations analyzes your telemetry and generates insights about
   potential root causes.
4. (Optional) To add additional telemetry sources or collaborate on the
   investigation with others, choose **Get started** in the
   information box at the bottom of the **Investigate** tab.
   You'll be guided through the investigation group configuration process. For
   more information, see [Configure CloudWatch investigations](Investigations-GetStarted.md "Investigations-GetStarted.md")

###### Important

You must have the appropriate IAM permissions to create or access
investigation groups. Users with read-only permissions will see
information about requesting additional permissions from their
administrators.
