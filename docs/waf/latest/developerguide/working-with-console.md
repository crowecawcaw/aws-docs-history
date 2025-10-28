**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Working with the updated console experience

AWS WAF offers two options for using the console:

The **new console** aims to simplify web ACL configuration process required by standard console workflows.
You can use guided workflows to simplify the web ACL creation and management process
through a protection pack (web ACL). A protection pack (web ACL) makes it easier to use and manage web ACLs in the console,
but is not functionally different from a web ACL.
In addition to the improved protection configuration process, the new
console offers enhanced visibility into your protections through
security dashboards, making it easier to monitor your security posture within the AWS WAF console.

The **standard AWS WAF console** provides a traditional approach to configuring web application
firewall protections using web ACLs. It offers granular control over individual rules
and rule groups and is familiar to existing AWS WAF users. With this console, you have
detailed control over your protection configurations, allowing for precise customization
of your security settings.

###### Tip

Choose the console experience that best fits your needs. If
you're new to AWS WAF or want to begin configuring protections based on AWS recommendations,
we recommend starting with the new console experience.
However, the standard experience is always available to open from the navigation
pane in the console.

## Feature parity between the new and standard console experience

The new console experience maintains complete feature parity with the existing console while introducing new capabilities:

- All existing AWS WAF functionality remains available
- Enhanced visibility through unified dashboards
- Simplified configuration workflows
- New protection pack (web ACL) templates

###### Important

The new console experience uses the same WAFv2 APIs as the existing console. This means
that protection packs created in the new console are implemented as standard WAFv2
web ACLs at the API level.

## Key differences

| Comparison of Console Experiences | Feature                  | Previous AWS WAF console experience        | Updated console experience |
| --------------------------------- | ------------------------ | ------------------------------------------ | -------------------------- |
| Configuration process             | Multi-page workflow      | Single-page interface                      |
| Rule configuration                | Individual rule creation | Option for pre-configured protection packs |
| Monitoring                        | Separate dashboards      | Unified visibility                         |
