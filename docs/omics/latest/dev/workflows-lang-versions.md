# Version support for HealthOmics workflow definition languages

HealthOmics supports workflow definition files written in Nextflow, WDL, or CWL.
The following sections provide information about HealthOmics version support for these languages.

###### Topics

- [WDL version support](#workflows-lang-versions-WDL "#workflows-lang-versions-WDL")
- [CWL version support](#workflows-lang-versions-CWL "#workflows-lang-versions-CWL")
- [Nextflow version support](#workflows-lang-versions-nextflow "#workflows-lang-versions-nextflow")

## WDL version support

HealthOmics supports versions 1.0, 1.1, and the development version of the WDL specification.

Every WDL document must include a version statement to specify which version (major and minor) of the
specification it adheres to. For more information about versions, see [WDL versioning](https://github.com/openwdl/wdl/blob/wdl-1.1/SPEC.md#versioning "https://github.com/openwdl/wdl/blob/wdl-1.1/SPEC.md#versioning")

Versions 1.0 and 1.1 of the WDL specification do not support the `Directory` type.
To use the `Directory` type for inputs or outputs, set the version to **development**
in the first line of the file:

```
version development  # first line of .wdl file
     ... remainder of the file ...
```

## CWL version support

HealthOmics supports versions 1.0, 1.1, and 1.2 of the CWL language.

You can specify the language version in the CWL workflow definition file. For more information about CWL,
see the [CWL user guide](https://github.com/common-workflow-language/user_guide "https://github.com/common-workflow-language/user_guide")

## Nextflow version support

HealthOmics supports three Nextflow stable versions. Nextflow typically releases a stable version every six months.
HealthOmics doesn't support the monthly “edge” releases.

HealthOmics supports released features in each version, but not preview features.

### Supported versions

HealthOmics supports the following Nextflow versions:

- Nextflow v22.04.01 DSL 1 and DSL 2
- Nextflow v23.10.0 DSL 2 (default)
- Nextflow v24.10.8 DSL 2

To migrate your workflow to the latest supported version (v24.10.8), follow the [Nextflow upgrade guide](https://nextflow.io/docs/latest/migrations/24-10.html "https://nextflow.io/docs/latest/migrations/24-10.html").

There are some breaking changes when migrating from Nextflow v23 to v24, as described in the following
sections of the Nextflow migration guide:

- [Breaking changes in 24.04](https://www.nextflow.io/docs/latest/migrations/24-04.html#breaking-changes "https://www.nextflow.io/docs/latest/migrations/24-04.html#breaking-changes")
- [Breaking changes in 24.10](https://www.nextflow.io/docs/latest/migrations/24-10.html#breaking-changes "https://www.nextflow.io/docs/latest/migrations/24-10.html#breaking-changes")

### Detect and process Nextflow versions

HealthOmics detects the DSL version and Nextflow version that you specify. It automatically determines the best
Nextflow version to run based on these inputs.

#### DSL version

HealthOmics detects the requested DSL version in your workflow definition file. For example, you can specify:
`nextflow.enable.dsl=2`.

HealthOmics supports DSL 2 by default. It provides backwards compatibility with DSL 1, if specified in your
workflow definition file.

- If you specify DSL 2, HealthOmics runs Nextflow v23.10.0, unless you specify Nextflow v22.04.0 or v24.10.8.
- If you specify DSL 1, HealthOmics runs Nextflow v22.04 DSL1 (the only supported version that runs DSL
  1).
- If you don't specify a DSL version, or if HealthOmics can’t parse the DSL information for any reason (such
  as syntax errors in your workflow definition file), HealthOmics defaults to DSL 2 and runs Nextflow v23.10.0.
- To upgrade your workflow from DSL 1 to DSL 2 to take advantage of the latest Nextflow versions and
  software features, see [Migrating from DSL
  1](https://nextflow.io/docs/latest/dsl1.html "https://nextflow.io/docs/latest/dsl1.html").

#### Nextflow versions

HealthOmics detects the requested Nextflow version in the Nextflow configuration file (nextflow.config), if you
provide this file. We recommend that you add the `nextflowVersion` clause at the end of the file to
avoid any unexpected overrides from included configs. For more information, see [Nextflow configuration](https://nextflow.io/docs/latest/config.html "https://nextflow.io/docs/latest/config.html").

You can specify a Nextflow version or a range of versions using the following syntax:

```
   // exact match
   manifest.nextflowVersion = '1.2.3'

   // 1.2 or later (excluding 2 and later)
   manifest.nextflowVersion = '1.2+'

   // 1.2 or later
   manifest.nextflowVersion = '>=1.2'

   // any version in the range 1.2 to 1.5
   manifest.nextflowVersion = '>=1.2, <=1.5'

   // use the "!" prefix to stop execution if the current version
   // doesn't match the required version.
   manifest.nextflowVersion = '!>=1.2'
```

HealthOmics processes the Nextflow version information as follows:

- If you use **=** to specify an exact version that HealthOmics supports, HealthOmics uses that
  version.
- If you use **!** to specify an exact version or a range of versions that are not
  supported, HealthOmics raises an exception and fails the run. Consider using this option if you want to be strict
  with version requests and fail quickly if the request includes unsupported versions.
- If you specify a range of versions, HealthOmics uses the latest supported version in that range, unless the
  range includes v24.10.8. In this case, HealthOmics gives preference to an earlier version. For example, if the
  range covers both v23.10.0 and v24.10.8, HealthOmics chooses v23.10.0.
- If there is no requested version, or if the requested versions aren't valid or can’t be parsed for
  any reason:
  - If you specified DSL 1, HealthOmics runs Nextflow v22.04.
  - Otherwise, HealthOmics runs Nextflow v23.10.0.

You can retrieve the following information about the Nextflow version that HealthOmics used for each run:

- The run logs contain information about the actual Nextflow version that HealthOmics used for the run.
- HealthOmics adds warnings in the run logs if there isn't a direct match with your requested version or
  if it needed to use a different version than you specified.
- The response to the **GetRun** API operation includes a field
  (`engineVersion`) with the actual Nextflow version that HealthOmics used for the run. For
  example:

```
"engineVersion":"22.04.0"
```
