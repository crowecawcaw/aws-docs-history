End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Configuring your simulation

A **simulation schema** (or **schema**)
is a YAML-formatted text file that specifies the configuration for a simulation. You can use the
same schema to start multiple simulations. The schema file is located in the project folder
for your simulation. You can use any text editor to edit the file. SimSpace Weaver only reads your schema
when it starts the simulation. Any edits that you make to a schema file only affect new simulations
that you start after the edits.

To configure your simulation, edit your simulation schema file (use the appropriate path separator for your operating system):

```
`project-folder`\tools\`project-name`-schema.yaml
```

You upload the simulation schema when you create a new simulation. The
quick start helper script for your project will upload the schema as part of
its process to build your simulation:

```
`project-folder`\tools\windows\quick-start.py
```

For more information about running the quick-start script, see the [Detailed tutorial](getting-started_detailed.md "getting-started_detailed.md") in the [Getting started](getting-started.md "getting-started.md") chapter of this guide.

## Simulation configuration parameters

The simulation schema contains bootstrapping information, including:

- Simulation properties – SDK version and compute configuration
  (type and number of [workers](w2aac51.md#glossary_worker "w2aac51.md#glossary_worker"))
- Clocks – tick rate and tolerances
- Spatial partitioning strategies – spatial topology (such as a grid),
  bounds, and placement groups (spatial partition grouping on workers)
- Domains and their apps – app bucket, path, and launch command(s)

SimSpace Weaver uses your schema configuration to configure and arrange spatial partitions, launch apps,
and advance the simulation at your specified tick rate.

###### Note

The create-project script in the SimSpace Weaver app SDK will automatically generate a
simulation schema for you, based on the sample application.

The following topics describe the parameters in the simulation schema.
For a full description of the simulation schema, see [SimSpace Weaver simulation schema reference](schema-reference.md "schema-reference.md").

###### Topics

- [SDK version](working-with_configuring-simulation_sdk-version.md "working-with_configuring-simulation_sdk-version.md")
- [Simulation properties](working-with_configuring-simulation_simulation-properties.md "working-with_configuring-simulation_simulation-properties.md")
- [Workers](working-with_configuring-simulation_workers.md "working-with_configuring-simulation_workers.md")
- [Clock](working-with_configuring-simulation_clock.md "working-with_configuring-simulation_clock.md")
- [Partitioning strategies](working-with_configuring-simulation_partitioning-strategies.md "working-with_configuring-simulation_partitioning-strategies.md")
- [Domains](working-with_configuring-simulation_domains.md "working-with_configuring-simulation_domains.md")
