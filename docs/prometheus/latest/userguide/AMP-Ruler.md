# Using rules to modify or monitor metrics as they are

received

You can set up rules to act upon metrics as they are received by Amazon Managed Service for Prometheus. These rules
can monitor the metrics or even create new, computed, metrics based on the metrics
received.

Amazon Managed Service for Prometheus supports two types of _rules_ that it evaluates at regular
intervals:

- _Recording rules_ allow you to precompute frequently needed or
  computationally expensive expressions and save their results as a new set of time
  series. Querying the precomputed result is often much faster than running the
  original expression every time it is needed.
- _Alerting rules_ allow you to define alert conditions based on
  PromQL and a threshold. When the rule triggers the threshold, a notification is sent
  to [alert manager](AMP-alert-manager.md "AMP-alert-manager.md"), which can be configured
  to managed the rules, or forward them to notification downstream to receivers such
  as Amazon Simple Notification Service.
  To use rules in Amazon Managed Service for Prometheus, you create one or more YAML rules files that define the rules.
  An Amazon Managed Service for Prometheus rules file has the same format as a rules file in standalone Prometheus. For
  more information, see [Defining Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/ "https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/") and [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ "https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/") in the Prometheus documentation.

You can have multiple rules files in a workspace. Each separate rules file is contained
within a separate _namespace_. Having multiple rules files lets you
import existing Prometheus rules files to a workspace without having to change or combine
them. Different rule group namespaces can also have different tags.

**Rule sequencing**

Within a rules file, rules are contained within _rules groups_. Rules
within a single rules group in a rules file are always evaluated in order from top to
bottom. Therefore, in recording rules, the result of one recording rule can be used in the
computation of a later recording rule or in an alerting rule in the same rule group.
However, because you can't specify the order in which to run separate rules files, you can't
use the results from one recording rule to compute a rule in a different rule group or a
different rules file.

###### Topics

- [Understanding IAM permissions needed for
  using rules](AMP-ruler-IAM-permissions.md "AMP-ruler-IAM-permissions.md")
- [Create a rules file](AMP-ruler-rulesfile.md "AMP-ruler-rulesfile.md")
- [Upload a rules configuration file to
  Amazon Managed Service for Prometheus](AMP-rules-upload.md "AMP-rules-upload.md")
- [Edit or replace a rules configuration file](AMP-rules-edit.md "AMP-rules-edit.md")
- [Troubleshoot rule evaluations](troubleshoot-rule-evaluations.md "troubleshoot-rule-evaluations.md")
- [Troubleshooting Ruler](Troubleshooting-rule-fail-error.md "Troubleshooting-rule-fail-error.md")
