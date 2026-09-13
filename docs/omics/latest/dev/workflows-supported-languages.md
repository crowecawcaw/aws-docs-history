

# Supported workflow languages for HealthOmics
<a name="workflows-supported-languages"></a>

HealthOmics Private Workflows support workflow definitions written in three workflow languages. Each language has its own syntax, capabilities, and version support on HealthOmics.

## Workflow engines at a glance
<a name="workflows-supported-languages-overview"></a>

The following table summarizes the supported workflow languages, versions, and key characteristics. In the table, DSL refers to the domain-specific language version that each engine supports.


| Engine | Supported versions | DSL / Spec versions | Key characteristics | 
| --- | --- | --- | --- | 
| Nextflow | v22.04, v23.10, v24.10, v25.10, v26.04 | DSL 1 (v22.04 only), DSL 2 | Groovy-based dataflow language with channel-driven parallelism. Widely adopted in genomics through the nf-core community. Supports plugins (nf-schema, nf-prov, nf-fgbio, nf-core-utils). | 
| WDL | — | Language spec 1.0, 1.1, development | Task-oriented language with explicit input/output typing. Two engine modes: WDL (strict spec compliance) and WDL lenient (Cromwell-compatible with implicit type casting). | 
| CWL | — | Language spec 1.0, 1.1, 1.2 | Standards-based, YAML-defined workflow language maintained by the Common Workflow Language community. Portable across multiple execution platforms. | 

## Choosing a workflow language
<a name="workflows-choosing-language"></a>

All three languages are fully supported on HealthOmics and can access the same compute, storage, and networking capabilities. The following considerations might help inform your choice:
+ **Existing pipelines** – If your organization already maintains pipelines in one language, you can use them on HealthOmics without rewriting. HealthOmics supports all three languages with the same underlying compute, storage, and networking infrastructure.
+ **Language characteristics** – Nextflow uses a Groovy-based dataflow model with channel-driven parallelism and supports plugins. WDL uses explicit input/output typing with a task-oriented structure. CWL uses a declarative YAML-based approach designed for cross-platform portability.
+ **Open-source ecosystem** – Each language has an active open-source community with publicly available pipelines and tools. For more information, see the specifications for [WDL](https://github.com/openwdl/wdl), [Nextflow](https://www.nextflow.io/), or [CWL](https://www.commonwl.org/).

## Version details by language
<a name="workflows-version-details-by-language"></a>

For detailed version support, language-specific features, and configuration guidance, see the following pages:
+ [Version support for HealthOmics workflow definition languages](workflows-lang-versions.md) – Complete version matrix for all three languages, including how HealthOmics detects and selects versions.
+ [Nextflow workflow definition specifics](workflow-definition-nextflow.md) – Nextflow DSL syntax, directives, plugins, profiles, execution reports, and engine settings.
+ [Nextflow version release notes for HealthOmics](nextflow-version-release-notes.md) – Release notes for each supported Nextflow version on HealthOmics.
+ [WDL workflow definition specifics](workflow-languages-wdl.md) – WDL version support, type coercion, WDL lenient mode, and struct handling.
+ [CWL workflow definition specifics](workflow-languages-cwl.md) – CWL version support, input formats, and Docker requirements.

## Nextflow engine version lifecycle
<a name="workflows-nextflow-version-lifecycle"></a>

HealthOmics maintains a regular cadence for supporting new Nextflow engine versions. Nextflow typically releases a stable version every six months, and HealthOmics adds support for these versions on an ongoing basis. For the full Nextflow version lifecycle policy, including deprecation timelines and Extended Version Availability pricing, see the following page:
+ [Nextflow version retention policy](nextflow-version-retention-policy.md) – Supported versions, how long they remain available, deprecation phases, Extended Version Availability pricing, plugin management, and testing guidance.

## Related topics
<a name="workflows-supported-languages-related"></a>
+ [Workflow definition files in HealthOmics](workflow-definition-files.md) – How to structure your workflow definition ZIP, requirements, and examples.
+ [Creating private workflows in HealthOmics](workflows-setup.md) – End-to-end guide for creating a workflow on HealthOmics.
+ [Start a run in HealthOmics](starting-a-run.md) – How to start a workflow run, including engine settings.

**Topics**
+ [Workflow engines at a glance](#workflows-supported-languages-overview)
+ [Choosing a workflow language](#workflows-choosing-language)
+ [Version details by language](#workflows-version-details-by-language)
+ [Nextflow engine version lifecycle](#workflows-nextflow-version-lifecycle)
+ [Related topics](#workflows-supported-languages-related)
+ [Nextflow version retention policy](nextflow-version-retention-policy.md)
+ [Nextflow version release notes for HealthOmics](nextflow-version-release-notes.md)