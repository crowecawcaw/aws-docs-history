End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Simulation properties

The `simulation_properties` section of your schema specifies the logging configuration and
a data type for the index field (usually the spatial location) of entities.

```

simulation_properties:
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"
  default_entity_index_key_type: "Vector3<f32>"

```

The value of `log_destination_service` determines the interpretation of the value of
`log_destination_resource_name`. Currently, the only supported value is `logs`.
This means that the value of `log_destination_resource_name` is the name of a log group in
Amazon CloudWatch Logs

###### Note

Logging is optional. If you don't configure log destination properties then your simulation
won't produce logs.

The `default_entity_index_key_type` property is required. The only valid value is
`Vector3<f32>`.
