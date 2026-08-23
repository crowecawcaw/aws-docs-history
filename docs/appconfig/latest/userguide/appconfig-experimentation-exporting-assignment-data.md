# Exporting experiment assignment data

To capture which entities are assigned to which treatments during an experiment run, configure AWS AppConfig Agent with the `EXPERIMENT_ASSIGNMENT_LOG_DESTINATION` option (on the Lambda extension, `AWS_APPCONFIG_EXTENSION_EXPERIMENT_ASSIGNMENT_LOG_DESTINATION`). A treatment assignment occurs when a request for the experiment flag is made on behalf of an entity that is currently exposed to the experiment. If you do not set this option, the agent does not emit assignment records.

###### Important

AWS AppConfig Agent writes the entity ID to assignment records exactly as your application provides it in the `Entity-Id` header. If your entity IDs contain sensitive data or personally identifiable information (PII), such as email addresses, consider hashing or pseudonymizing them before you pass them to the agent so that the values written to your logs are not sensitive.

The entity ID is the key you use to join assignment records to your metric (observations) data. If you obfuscate the entity ID, you must apply the same transformation to both data sets. If you obfuscate the entity ID in your assignment records but not in your metric data, or apply a different transformation to each, you will not be able to join the two.

**Emitting records to stderr**

When you set the destination to `stderr`, the agent emits each assignment as a single-line JSON record. Each record includes a `type` field so you can distinguish assignment records from the agent application logs, which also go to stderr by default.

```
{
  "type": "AWS.AppConfig.TreatmentAssignment",
  "timestamp": "2026-01-01T12:00:00Z",
  "region": "us-east-1",
  "accountId": "111122223333",
  "applicationId": "app1234",
  "experimentDefinitionId": "exp1234",
  "experimentRunNumber": "1",
  "treatmentKey": "t1",
  "entityId": "user123"
}
```

The `treatmentKey` field is the key that AWS AppConfig assigns to each treatment (`c` for the control, and `t1`, `t2`, and so on for treatments). This is the bare form of the key. In the agent flag response, the same treatment appears as a flag variant named with a double-underscore pattern (for example, `__t1__`); for more information, see [Retrieving experiment treatments](appconfig-integration-retrieving-experiment-treatments.md "appconfig-integration-retrieving-experiment-treatments.md").

**Writing records to disk**

When you set the destination to a value like `file:`path`/`, the agent writes assignment records to disk under the provided base directory. Records are stored in a file structure that uniquely identifies the experiment run. Each log file name includes a random salt to prevent collisions when files from multiple hosts are combined.

```
`path`/
  us-east-1/           # Region
    111122223333/      # account ID
      app1234/         # application ID
        exp1234/       # experiment definition ID
          1_a4b5.jsonl # log file: <run-number>_<salt>.jsonl
```

Each file contains newline-delimited JSON records:

```
{"timestamp":"2026-01-01T12:00:00Z","treatmentKey":"t1","entityId":"user123"}
```
