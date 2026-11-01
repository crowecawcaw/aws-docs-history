

# Validating workflow definitions locally
<a name="workflows-validate-local"></a>

You can validate a workflow definition with the workflow language's own tooling before you call `CreateWorkflow` or `CreateWorkflowVersion`. It catches problems such as syntax errors and references that don't resolve.

Local validation checks your definition against the workflow language, not against HealthOmics requirements. For the linters that HealthOmics runs during workflow creation, see [Workflow linters in HealthOmics](workflows-linter.md).

## Installing a validator
<a name="workflows-validate-local-install"></a>

The validators are third-party software that AWS doesn't maintain.
+ **WDL** – Install [miniwdl](https://miniwdl.readthedocs.io/en/latest/getting_started.html), a local runner and developer toolkit for WDL.
+ **Nextflow** – Install [Nextflow](https://docs.seqera.io/nextflow/install) v25.10 or later. Earlier versions either don't have the `nextflow lint` command or report no warnings.
+ **CWL** – Install [cwltool](https://cwltool.readthedocs.io/en/latest/), the reference implementation of the CWL standards.

**Note**  
Your run can use an older Nextflow version than the one you lint with. The `nextflow lint` command parses with the strict syntax, which your run might not use. So before you rewrite a definition to satisfy a syntax finding, check which syntax version your run uses, described in [Specify the Nextflow syntax version](workflow-definition-nextflow.md#nextflow-syntax-version). For how HealthOmics selects the Nextflow version for a run, see [Nextflow versions](workflows-lang-versions.md#workflows-versions-p2).

## Running the validator
<a name="workflows-validate-local-run"></a>

Run the validator against the main definition file, or for Nextflow, against the directory that contains it.

------
#### [ WDL ]

```
miniwdl check {{main-file}}
```

------
#### [ Nextflow ]

```
nextflow lint {{definition-directory}}
```

------
#### [ CWL ]

```
cwltool --validate {{main-file}}
```

------

For a multi-file bundle, lay the files out on disk with the same relative paths that they have in the ZIP archive you upload to HealthOmics. References resolve relative to the file that declares them, not to the directory you run the command from. For the main file requirements, see [HealthOmics workflow definition requirements](workflow-defn-requirements.md).

Pass `nextflow lint` the directory rather than the main file, so that it also checks `nextflow.config`, which it doesn't reach from the main file.

**Note**  
When you pass `-format`, `nextflow lint` rewrites the definition files that have no errors. Formatting with v25.10 or later can produce syntax that earlier Nextflow versions reject, so don't format unless your run uses the version you format with.

## Reading the validation results
<a name="workflows-validate-local-results"></a>

miniwdl and `nextflow lint` exit with a non-zero status when they report an error, but with a zero status when they report only warnings, so read the output rather than relying on the exit status.
+ **WDL** – miniwdl reports either the first error it can't recover from, or an outline of every document it loaded with any lint findings inline.
+ **Nextflow** – Nextflow reports each error and warning with its file, line, and column, and quotes the offending line. It ends with a count of the files that had errors and a count of those that had none, so a file with a warning but no error is counted as having none. To change the report format, pass `-o`, for example `-o json`.
+ **CWL** – cwltool reports either that the file is valid CWL, or a validation failure with the file, line, and column of each problem.

**Note**  
Nextflow versions differ in how much they report. Nextflow v26.04 counts warnings in its summary and includes them in `-o json` output. Nextflow v25.10 prints warnings in the default output only, and reports none in either its summary or its `-o json` output.