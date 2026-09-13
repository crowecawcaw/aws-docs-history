

# Nextflow version retention policy
<a name="nextflow-version-retention-policy"></a>

## Supported Nextflow engine versions
<a name="nf-retention-supported-versions"></a>

HealthOmics supports multiple stable releases of the Nextflow engine. Each release supports one or more domain-specific language (DSL) versions. The following table shows the currently supported versions.


| Version | DSL support | HealthOmics release date | Status | 
| --- | --- | --- | --- | 
| v22.04 | DSL 1 & DSL 2 | November 2022 | Scheduled for deprecation on November 30, 2026 | 
| v23.10 | DSL 2 | October 2024 | Scheduled for deprecation on November 30, 2027 | 
| v24.10 | DSL 2 | August 2025 | Supported through at least November 2027 | 
| v25.10 | DSL 2 | April 2026 | Supported through at least October 2028 | 
| v26.04 | DSL 2 | June 2026 | Latest, supported through at least April 2029 | 

HealthOmics doesn't support the monthly "edge" releases. HealthOmics supports released features in each version, but not preview features.

A version can remain **available** to run workflows after it stops being **supported**. Supported versions (the current calendar year plus the two prior years) receive new features and compatibility improvements. Deprecated-but-available versions receive only security patches.

## How long Nextflow engine versions remain available
<a name="nf-retention-availability-window"></a>

HealthOmics supports Nextflow versions released within the current calendar year, plus versions released within the two prior years. Only these supported versions receive feature releases and backward compatibility improvements. In practice:
+ In 2026: Supported year families are 26.x, 25.x, and 24.x.
+ In 2027: When 27.04 is released, supported year families shift to 27.x, 26.x, and 25.x.

When the first stable release of a new calendar year becomes generally available on HealthOmics, the oldest year family is eligible for deprecation.

After a version receives a deprecation notice (enters the T–12 to T–0 notice period), maintenance is limited to security patches only. New features are not added to deprecated versions.

## Deprecation lifecycle
<a name="nf-retention-deprecation-lifecycle"></a>

When a Nextflow version is scheduled for deprecation on HealthOmics, you receive a minimum 12-month notice period. This is followed by up to 24 months of Extended Version Availability, across three distinct phases.


| Phase | Timeline | Version availability | Maintenance | Pricing | Workflow creation | Starting a run | Your action | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Phase 1: Notice Period | T–12 to T–0 | Fully functional for existing workflows at standard pricing | Security patches only | Standard rate (no change) | Not available on deprecated versions | Fully functional for existing workflows | Migrate to avoid Extended Version Availability pricing | 
| Phase 2: Extended Version Availability | T–0 to T\+24 months | Fully functional for existing workflows at Extended Version Availability pricing | Security patches only | 2x (months 0–12), 4x (months 12–24) | Not available on deprecated versions | Fully functional for existing workflows, subject to Extended Version Availability pricing | Start new runs on supported versions or upgrade workflow default version to exit Extended Version Availability pricing | 
| Phase 3: End of Life | After T\+24 months | Removed from service | None | N/A – runs fail | Not available on deprecated versions | Runs fail on unsupported (or retired) versions | You must upgrade to resume runs or start new runs on supported versions | 

### Phase 1: Notice Period (T–12 to T–0)
<a name="nf-retention-phase1"></a>

During the notice period:
+ If you are using the deprecated version, you receive communication about the timeline and impacted workflows through email, AWS Health Dashboard, and in-console banners.
+ The version remains functional for existing workflows at standard pricing.
+ You cannot create new workflows on deprecated versions, but you can start new runs on existing workflows at standard pricing.
+ Only security patches are applied. No new features or bug fixes are provided for the deprecated version.
+ We recommend that you test and migrate to a newer supported version.
+ You receive reminders to migrate workflows that use the deprecated version.

### Phase 2: Extended Version Availability (T–0 to T\+24 months)
<a name="nf-retention-phase2"></a>

After the deprecation date (T):
+ Any new runs started with deprecated versions incur Extended Version Availability pricing. You can avoid this pricing by starting new runs on supported versions or upgrading your workflow to use a supported version.
+ You cannot create new workflows on the deprecated versions.
+ Only security patches are applied. No new features or bug fixes are provided for the deprecated version.
+ You receive notifications about Extended Version Availability pricing if your workflows continue to use deprecated versions. Extended Version Availability pricing is applied only if new runs are started with deprecated versions during this phase.
+ To start a run on supported versions, see Nextflow engine version pinning in [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings).

The following table summarizes Extended Version Availability pricing.


| Period | Pricing | 
| --- | --- | 
| T–0 to T\+12 months | 2x base rate for new runs on unsupported versions | 
| T\+12 to T\+24 months | 4x base rate for new runs on unsupported versions | 

### Phase 3: End of Life (after T\+24 months)
<a name="nf-retention-phase3"></a>

After the Extended Version Availability period ends:
+ You receive final notification of the version retirement if any workflow is still using the retired version.
+ The version is fully removed from the service. You cannot create new workflows or start new runs on the retired version.
+ Existing workflow definitions remain accessible but fail to run on the retired version.
+ You must upgrade your workflow to use a supported engine version or pin a supported version in `StartRun`. For more information on version pinning at run start time, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings).

**Version locking for active runs**  
A workflow run always completes on the engine version and plugin versions it started with. This applies to all version transitions, including patch updates, version retirement, and plugin updates. Version changes apply only to new runs initiated after the update, never to runs already in progress.

**Nextflow version pinning at start run recommended**  
We strongly recommend that you pin an exact Nextflow version at runtime and test on newer versions well in advance of any deprecation date. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings).

## Expedited engine version retirement
<a name="nf-retention-expedited-retirement"></a>

AWS reserves the right to initiate an expedited retirement of a Nextflow engine version in rare cases where a version cannot be maintained consistent with AWS security and operational standards.

In such cases:
+ If you are using affected versions, you are notified immediately upon determination of expedited retirement.
+ A compressed retirement timeline applies, with a minimum notice period of 90 days wherever operationally feasible.
+ HealthOmics provides migration guidance and, where possible, automated upgrade tooling to assist you.

## Patch engine versions
<a name="nf-retention-patch-versions"></a>

Patch versions (for example, v24.10.0 to v24.10.8) are upgraded transparently by HealthOmics as part of routine service maintenance. Patch releases contain security fixes, bug fixes, and dependency updates. They do not introduce breaking changes.

No customer notification or retirement process applies to patch upgrades. You always run the latest secure patch within your selected version.

## DSL specification versions
<a name="nf-retention-dsl-versions"></a>

Because Nextflow bundles the specification language and engine into one application, DSL version support is tied directly to engine version support:
+ **DSL 1** – Supported exclusively on v22.04. When v22.04 is retired, DSL 1 support ends. You must migrate to DSL 2.
+ **DSL 2 – Legacy Parser (Syntax V1)** – Supported on v22.04 through v26.04. On v26.04, the legacy parser requires explicit opt-in through `engineSettings.syntaxVersion = v1`.
+ **DSL 2 – Strict Parser (Syntax V2)** – Default on v26.04 and all future versions.

## Testing before upgrading
<a name="nf-retention-testing"></a>

Before upgrading to a newer Nextflow version, we recommend that you:
+ You can use HealthOmics MCP servers to upgrade and validate your workflows against a newer version, including checking for breaking changes and version compatibility. You can use the MCP servers through [Kiro CLI](https://docs.aws.amazon.com/kiro/latest/userguide/what-is.html), Claude Code, or any other MCP-compatible agentic endpoint.
+ Use the `engineSettings.engineVersion` parameter in `StartRun` to test workflows against a newer version without changing your workflow definition. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings).
+ Review the [Nextflow migration guides](https://www.nextflow.io/docs/latest/migrations/index.html) for breaking changes between versions.
+ For workflows moving from v25.10 or earlier to v26.04, test compatibility with the Strict Parser (V2) or explicitly set `syntaxVersion` to `v1`.
+ For workflows on DSL 1 (v22.04), follow the [Migrating from DSL 1](https://nextflow.io/docs/latest/dsl1.html) guide before upgrading.

## Nextflow plugin versions
<a name="nf-retention-plugins"></a>

HealthOmics pre-installs a curated set of Nextflow plugins for each supported engine version. The plugin set is specific to each engine version and cannot be modified.


| Engine version | Pre-installed plugins | 
| --- | --- | 
| v22.04 | No plugin support | 
| v23.10 | nf-schema@2.3.0, nf-validation@1.1.1 | 
| v24.10 | nf-schema@2.3.0 | 
| v25.10 | nf-schema@2.6.1, nf-core-utils@0.4.0, nf-prov@1.7.0, nf-fgbio@1.0.1 | 
| v26.04 | nf-schema@2.7.2, nf-core-utils@0.4.0, nf-prov@1.7.0, nf-fgbio@1.0.1 | 

**Note**  
For Nextflow v24.10 and higher, nf-schema replaces the deprecated nf-validation plugin. You can use nf-validation only on v23.10.

### How Nextflow plugin versions are managed
<a name="nf-retention-plugin-management"></a>

HealthOmics maintains one plugin version per engine version:
+ **Single version per plugin per engine** – Only the pre-installed version listed in the preceding table is available.
+ **Only pre-installed plugins are supported** – HealthOmics supports only the plugins listed in the preceding table for each engine version. Plugin declarations in your `nextflow.config` that reference plugins not pre-installed for your engine version are not supported.
+ **Automatic updates** – When HealthOmics updates the pre-installed plugin version for an engine, all workflows on that engine use the updated version on their next run.
+ **No opt-in or opt-out** – Plugin updates are applied uniformly. There is no mechanism to remain on a prior plugin version and no Extended Version Availability option for plugins.
+ **Version locking for active runs** – A workflow run that starts on a given plugin version completes on that version, even if the plugin is updated during the run. Updates apply only to new runs initiated after the update.

### What happens when a plugin version updates
<a name="nf-retention-plugin-updates"></a>

**Major version changes** (for example, nf-schema 2.x to 3.x):
+ A minimum 30-day advance notice is provided before the major version is applied.
+ During the 30-day grace period, the prior major version remains in use. Your workflows continue to use the prior version until the grace period ends.
+ After the grace period, the new major version replaces the prior version for all workflows.
+ Advance notice is communicated through email, AWS Health Dashboard, and in-console banners.

**Minor and patch updates** (for example, nf-schema 2.3.0 to 2.7.2): Applied automatically without advance notice. These updates do not introduce breaking changes.

#### Testing plugin changes
<a name="nf-retention-testing-plugins"></a>

When a major plugin version change is announced (30-day grace period), we recommend the following:
+ Review the plugin release notes for breaking changes and migration guidance.
+ Test your workflows against the new plugin version before the grace period ends.
+ For nf-schema major changes, verify that your pipeline's parameter validation definitions are compatible with the new version's schema format.