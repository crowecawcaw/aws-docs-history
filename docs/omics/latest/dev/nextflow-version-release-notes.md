

# Nextflow version release notes for HealthOmics
<a name="nextflow-version-release-notes"></a>

This page contains release notes for each supported Nextflow version on HealthOmics. Each section summarizes new features, enhancements, and deprecations for a specific Nextflow version.

## Nextflow v26.10 release notes
<a name="nextflow-v26-10-release-notes"></a>

The following tables summarize HealthOmics support for new features, enhancements, breaking changes, and deprecations released in Nextflow version 26.10.

### New features and enhancements
<a name="nextflow-v26-10-new-features"></a>


| Feature | From version | HealthOmics support | Notes | 
| --- | --- | --- | --- | 
| Static typing | 26.10 (preview in 25.10 and 26.04) | Yes | Generally available from v26.10. Enable it per script with nextflow.enable.types = true. For more information, see [Static typing](https://docs.seqera.io/nextflow/static-typing) in the Seqera Nextflow documentation. | 
| Auto-load collection params from files | 26.04 | Yes | Requires static typing, so it is supported from v26.10. Pass a CSV, JSON, or YAML file as the value of a Channel<R> parameter, where R is a record type. Keep the file in the same Region as the run. | 
| Report directory option | 26.10 | Yes | The report, timeline, trace, and dag scopes accept a relative directory inside the workflow output directory. HealthOmics exports these files with the run outputs. For more information, see [Generate Nextflow execution reports](workflow-definition-nextflow.md#nextflow-execution-reports). | 
| Call-cache keys for eval outputs | 26.10 | Yes | The cache key for eval outputs is now stable across runs. Tasks with eval outputs re-run once on their first v26.10 run. | 
| Workflow modules (Nextflow Registry) | 26.10 | No | HealthOmics workflows run in an isolated network with no outbound internet access. Include modules directly in your workflow ZIP archive. | 
| Pipeline composition | 26.10 | Yes | Include a pipeline and call it as a workflow. Both the calling script and the included pipeline must enable static typing. | 
| Global cache | 26.10 | N/A | Requires Seqera Platform. Use HealthOmics call caching instead. | 
| Agents (preview) | 26.10 | No | HealthOmics does not support preview features. | 
| Run a named workflow or process directly | 26.10 | No | Requires nextflow module run, which HealthOmics does not expose. | 
| manifest.diagram | 26.10 | N/A | Accepted and ignored. HealthOmics does not render it. | 

### Breaking changes
<a name="nextflow-v26-10-breaking-changes"></a>


| Change | From version | What happens | What to do | 
| --- | --- | --- | --- | 
| echo process directive removed | 26.10 | Fails to compile with either syntax parser. The lint report flags it. | Replace echo true with debug true. | 
| Aliased type includes rejected | 26.10 | Including a record or enum type under another name fails to compile. | Include the type under its own name. | 

### Deprecations
<a name="nextflow-v26-10-deprecations"></a>


| Deprecated item | From version | Impact | Recommended action | 
| --- | --- | --- | --- | 
| storeDir process directive | 26.10 | Still works. No deprecation warning appears in the run log or the lint report. | Reuse intermediate outputs in workflow logic instead. See the [Nextflow 26.10 migration notes](https://docs.seqera.io/nextflow/migrations/26-10). | 
| when: process section | 26.10 | Still works. For workflows that declare v26.10, reported as a lint warning at workflow creation. | Move the condition into the workflow logic. | 

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