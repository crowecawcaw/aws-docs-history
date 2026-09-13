

# Nextflow version release notes for HealthOmics
<a name="nextflow-version-release-notes"></a>

This page contains release notes for each supported Nextflow version on HealthOmics. Each section summarizes new features, enhancements, and deprecations for a specific Nextflow version.

## Nextflow v26.04 release notes
<a name="nextflow-v26-release-notes"></a>

The following tables summarize HealthOmics support for new features, enhancements, and deprecations released in Nextflow version 26.04.

### New features and enhancements
<a name="nextflow-v26-new-features"></a>


| Feature | From version | HealthOmics support | Notes | 
| --- | --- | --- | --- | 
| Strict syntax parser (default) | 26.04 | Yes | Enabled by default from v26.04. Legacy parser available via syntaxVersion: "v1" in engine settings. | 
| Record types | 26.04 | Yes | For more information, see [Records](https://docs.seqera.io/nextflow/script#records) in the Seqera Nextflow documentation. | 
| Workflow output summaries | 26.04 | Yes | Prints a summary of workflow outputs on run completion. Output format configurable via outputFormat in engine settings. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings). | 
| Agent logging mode | 26.04 | Yes | Configurable via agentMode in engine settings. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings). | 
| Module system (Nextflow Registry) | 26.04 | No | HealthOmics workflows run in an isolated network with no outbound internet access. You can include modules directly in your workflow zip. | 
| Static typing (preview) | 26.04 | No | HealthOmics does not support preview features. | 
| Auto-load collection params from files | 26.04 | No | Requires static typing (preview), which HealthOmics does not support. | 
| Multi-revision pipelines checkout | 26.04 | N/A | Not applicable. HealthOmics does not use Git-based pipeline checkout. | 

### Deprecations
<a name="nextflow-v26-deprecations"></a>


| Deprecated item | From version | Impact | Recommended action | 
| --- | --- | --- | --- | 
| listFiles() method | 26.04 | Deprecation warning | Replace with listDirectory(). | 
| nextflow.enable.strict flag | 26.04 | No longer needed | Remove from config. Strict mode is now the default. | 
| manifest.defaultBranch | 26.04 | No longer needed | Remove from config. HealthOmics does not use Git-based pipeline checkout and has never supported this option. | 