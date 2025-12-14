# Best practices for using

Security Hub CSPM policies

When implementing Security Hub CSPM policies across your organization, following established best
practices helps ensure successful deployment and maintenance of your security
configurations. These guidelines specifically address the unique aspects of Security Hub CSPM policy
management and enforcement within AWS Organizations.

## Policy design principles

Before creating Security Hub CSPM policies, establish clear principles for your policy structure.
Keep policies simple and avoid complex cross-attribute or nested rules that make it
difficult to determine the final outcome. Start with broad policies at the organization
root level and refine them through child policies where needed.

Consider using empty region lists strategically. You can leave
`enable_in_regions` empty when you only need to disable Security Hub CSPM in specific
regions, or leave `disable_in_regions` empty to keep regions unmanaged by
policy. This flexibility helps you maintain precise control over your security
monitoring coverage.

## Region management strategies

When managing regions through Security Hub CSPM policies, consider these proven approaches. Use
`ALL_SUPPORTED` when you want to automatically include future regions in
your security coverage. For more granular control, explicitly list regions rather than
relying on `ALL_SUPPORTED`, especially when different regions require
different security configurations.

Document your region-specific requirements, particularly for:

- Compliance-mandated regions that require specific configurations
- Development versus production environment differences
- Opt-in regions with special considerations
- Regions where Security Hub CSPM must remain disabled

## Policy inheritance planning

Carefully plan your policy inheritance structure to maintain effective security
control while allowing necessary flexibility. Document which organizational units can
modify inherited policies and what modifications are allowed. Consider restricting
inheritance operators (@@assign, @@append, @@remove) at parent levels when you need to
enforce strict security controls.

## Monitoring and validation

Implement regular monitoring practices to ensure your policies remain effective.
Review policy attachments periodically, especially after organizational changes.
Validate that region configurations match your intended security coverage, particularly
when using `ALL_SUPPORTED` or when managing multiple region lists.

## Troubleshooting strategies

When troubleshooting Security Hub CSPM policies, focus first on policy precedence and inheritance.
Remember that disable configurations take precedence over enable configurations when
regions appear in both lists. Check policy inheritance chains to understand how parent
and child policies combine to create the effective policy for each account.
