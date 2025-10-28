End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Domains

You provide a name for a set of configuration properties for a domain. The launch setting
for apps in a domain determines the type of domain:

- `launch_apps_via_start_app_call` – custom domain
- `launch_apps_by_partitioning_strategy` – spatial domain
- `launch_apps_per_worker` (not included in the sample application) – service
  domain

###### Important

SimSpace Weaver supports up to 5 domains for
each simulation. This includes all spatial, custom, and service domains.

```

domains:
  MyViewDomain:
    launch_apps_via_start_app_call: {}
    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MyViewApp.zip"
      launch_command: ["MyViewApp"]
      required_resource_units:
        compute: 1
      endpoint_config:
        ingress_ports:
          - 7000
  MySpatialDomain:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "MyGridPartitioning"
      grid_partition:
        x: 2
        y: 2
    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MySpatialApp.zip"
      launch_command: ["MySpatialApp"]
      required_resource_units:
        compute: 1

```

###### Note

SimSpace Weaver app SDK
version 1.12.x projects use separate buckets for the app .zip files
and the schema:

- weaver-`lowercase-project-name`-`account-number`-app-zips-`region`
- weaver-`lowercase-project-name`-`account-number`-schemas-`region`

###### Topics

- [App configuration](working-with_configuring-simulation_domains_app-config.md "working-with_configuring-simulation_domains_app-config.md")
- [Configuring spatial domains](working-with_configuring-simulation_domains_spatial.md "working-with_configuring-simulation_domains_spatial.md")
- [Network endpoints](working-with_configuring-simulation_domains_endpoints.md "working-with_configuring-simulation_domains_endpoints.md")
- [Configuring service domains](working-with_configuring-simulation_domains_service-domains.md "working-with_configuring-simulation_domains_service-domains.md")
