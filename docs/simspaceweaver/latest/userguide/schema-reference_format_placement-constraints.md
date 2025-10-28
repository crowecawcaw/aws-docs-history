End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Placement constraints

The `placement_constraints` section (optional) specifies which spatial domains
SimSpace Weaver should place together on the same workers. For more information, see
[Configuring spatial domains](working-with_configuring-simulation_domains_spatial.md "working-with_configuring-simulation_domains_spatial.md").

###### Important

Versions `1.13` and `1.12` don't support `placement_constraints`.

```
placement_constraints:
  - placed_together: ["`spatial-domain-name`", "`spatial-domain-name`", `...`]
    on_workers: ["`worker-group-name`"]
```

**Properties**

`placed_together`

Specifies the spatial domains that SimSpace Weaver should place together.

_Required:_ Yes

_Type:_ String array

_Valid values:_ Names of spatial domains specified in the schema

`on_workers`

Specifies the worker group that that SimSpace Weaver should place the domains on.

_Required:_ Yes

_Type:_ 1-element string array

_Valid values:_ Name of a worker group specified in the schema
