**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Best practices for handling managed rule group

versions

Follow this best practice guidance for handling versioning when you use a versioned
managed rule group.

When you use a managed rule group in your protection pack (web ACL), you can choose to use a specific, static version
of the rule group, or you can choose to use the default version:

- **Default version** – AWS WAF always sets the default
  version to the static version that's currently recommended by the
  provider. When the provider updates their recommended static version,
  AWS WAF automatically updates the default version setting for the rule
  group in your protection pack (web ACL).

When you use the default version of a managed rule group, do the
following as best practice:

    + **Subscribe to notifications** – Subscribe to
     notifications for changes to the rule group and keep an eye on
     those. Most providers send advanced notification of new static
     versions and of default version changes. These let you check the
     effects of a new static version before AWS switches the
     default version to it. For more information see [Getting
     notified of new versions and updates](waf-using-managed-rule-groups-sns-topic.md "waf-using-managed-rule-groups-sns-topic.md").
    + **Review the effects of static version settings and make adjustments
     as needed before your default is set to it**
     – Before your default is set to a new static version,
     review the effects of the static version on the monitoring and
     management of your web requests. The new static version might
     have new rules to review. Look for false positives or other
     unexpected behavior, in case you need to modify how you use the
     rule group. You can set rules to count, for example, to stop
     them from blocking traffic while you figure out how you want to
     handle the new behavior. For more information, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

- **Static version** – If you choose to use a static
  version, you must manually update the version setting when you're ready to
  adopt a new version of the rule group.

When you use a static version of a managed rule group, do the following as best practice:

    + **Keep your version up to date** – Keep your managed
     rule group as close as you can to the latest version. When a new
     version is released, test it, adjust settings as needed, and
     implement it in a timely manner. For information about testing,
     see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").
    + **Subscribe to notifications** – Subscribe to
     notifications for changes to the rule group, so you know when
     your provider releases new static versions. Most providers give
     advanced notification of version changes. Additionally, your
     provider might need to update the static version that you're
     using to close a security loophole or for other urgent reasons.
     You'll know what's happening if you're subscribed to the
     provider's notifications. For more information, see [Getting
     notified of new versions and updates](waf-using-managed-rule-groups-sns-topic.md "waf-using-managed-rule-groups-sns-topic.md").
    + **Avoid version expiration** – Don't allow a static
     version to expire while you're using it. Provider handling of
     expired versions can vary and might include forcing an upgrade
     to an available version or other changes that can have
     unexpected consequences. Track the AWS WAF expiry metric and set
     an alarm that gives you a sufficient number of days to
     successfully upgrade to a supported version. For more
     information, see [Tracking version
     expiration](waf-using-managed-rule-groups-expiration.md "waf-using-managed-rule-groups-expiration.md").
