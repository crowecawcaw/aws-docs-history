**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Finding your protection pack (web ACL) records

This section explains how to find your protection pack (web ACL) records.

###### Note

You are charged for logging in addition to the charges for using AWS WAF.
For information, see [Pricing for logging protection pack (web ACL) traffic information](logging-pricing.md "logging-pricing.md").

###### If you can't find a log record in your logs

On rare occasions, it's possible for AWS WAF log delivery to fall below 100%, with logs
delivered on a best effort basis. The AWS WAF architecture prioritizes the security of
your applications over all other considerations. In some situations, such as when
logging flows experience traffic throttling, this can result in records being dropped.
This shouldn't affect more than a few records. If you notice a number of missing log
entries, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

In the logging configuration for your protection pack (web ACL), you can customize what AWS WAF sends to
the logs.

- **Field redaction** – You can redact the
  following fields from the log records for the rules that use the corresponding
  match settings: **URI path**, **Query
  string**, **Single header**, and **HTTP
  method**. Redacted fields appear as `REDACTED` in the
  logs. For example, if you redact the **Query string** field, in
  the logs, it will be listed as `REDACTED` for all rules that use the
  **Query string** match component setting. Redaction applies
  only to the request component that you specify for matching in the rule, so the
  redaction of the **Single header** component doesn't apply to
  rules that match on **Headers**. For a list of the log fields,
  see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").

###### Note

This setting has no impact on request sampling. You can exclude fields from request sampling
by configuring protection pack (web ACL) data protection or by disabling sampling for the protection pack (web ACL).

- **Log filtering** – You can add filtering
  to specify which web requests are kept in the logs and which are dropped. You
  filter on the settings that AWS WAF applies during the web request evaluation. You can filter
  on the following settings:
  - **Fully qualified label** – Fully
    qualified labels have a prefix, optional namespaces, and label name. The
    prefix identifies the rule group or protection pack (web ACL) context of the rule that
    added the label. For information about labels, see [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").
  - **Rule action** – You can filter on any normal rule action
    setting and also on the legacy `EXCLUDED_AS_COUNT` override
    option for rule group rules. For information about rule action settings,
    see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").
    For information about current and legacy rule action overrides for rule
    group rules, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").
    - The normal rule action filters apply to actions that are
      configured in rules and also to actions that are configured
      using the current option for overriding a rule group rule
      action.
    - The `EXCLUDED_AS_COUNT` log filter overlaps with
      the `Count` action log filter.
      `EXCLUDED_AS_COUNT` filters both the current and
      legacy options for overriding a rule group rule action to
      Count.
