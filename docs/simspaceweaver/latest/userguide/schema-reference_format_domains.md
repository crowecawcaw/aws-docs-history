End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Domains

The `domains` section (required) specifies the properties for each of your domains.
All simulations must have at least one section for a spatial domain. You can create
multiple sections for additional domains. Each type of
domain has its own configuration format.

###### Important

Versions `1.13` and `1.12` don't support multiple spatial domains.

###### Important

SimSpace Weaver supports up to 5 domains for
each simulation. This includes all spatial, custom, and service domains.

```
domains:
  `domain-name`:
    `domain-configuration`
  `domain-name`:
    `domain-configuration`
  `...`

```

###### Domain configuration

- [Spatial](schema-reference_format_domains_spatial.md "schema-reference_format_domains_spatial.md")
- [Custom](schema-reference_format_domains_custom.md "schema-reference_format_domains_custom.md")
- [Service](schema-reference_format_domains_service.md "schema-reference_format_domains_service.md")
