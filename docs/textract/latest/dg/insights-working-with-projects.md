

# Working with projects

A project holds the reusable configuration that your analysis jobs share. This page covers creating, reading, updating, listing, and deleting projects, and the rules that govern each operation.

## Create a project
<a name="insights-working-with-projects-create"></a>

`CreateProject` is synchronous. You must supply `ExtractionConfiguration`; every other configuration block is optional. `ExtractionConfiguration` must set `BoundingBox` and a non-empty `Granularity.Types`, so extraction cannot be turned off on a project.

The following example creates a project with a minimal extraction configuration and a public blueprint for custom extraction:

```
aws textract create-project \
  --region us-east-1 \
  --project-name "my-custom-output-project" \
  --custom-configuration '{"Blueprints": [{"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-w2-form"}]}' \
  --extraction-configuration '{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}'
```

The call returns the project ARN and a status:

```json
{
  "ProjectArn": "arn:aws:textract:us-east-1:111122223333:project/abcdef123456",
  "Status": "COMPLETED"
}
```

### Minimal versus richer extraction
<a name="insights-working-with-projects-extraction-levels"></a>

Because `ExtractionConfiguration` is required, choose a configuration that matches what you need:
+ **Minimal.** When you care only about custom extraction, pass `'{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}'`. This produces a lightweight, page-level extraction with no bounding-box coordinates. It does not suppress the extraction result entirely.
+ **Richer.** To get fuller extraction results, enable `BoundingBox`, add the `Granularity` types you need (`PAGE`, `LINE`, `WORD`, `ELEMENT`, `DOCUMENT`), and an optional output format. Each added granularity type produces an additional section and increases output size and latency. See [Extraction results](insights-extraction-results.md).

`ProjectName` must match `[a-zA-Z0-9-_]+`. `ProjectName` and `ProjectDescription` both have length limits. For all limits, see [Limits and quotas](insights-quotas.md).

To tag a project when you create it, add `--tags`, for example `--tags '{"Team": "finance"}'`. `UpdateProject` doesn't change tags. To add or remove tags later, use `TagResource` and `UntagResource`. See [Tagging Amazon Textract Insights resources](insights-tagging.md).

## Read a project
<a name="insights-working-with-projects-read"></a>

`GetProject` returns a project's current configuration. Use it to confirm which capabilities are enabled before you submit a job:

```
aws textract get-project \
  --region us-east-1 \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcdef123456"
```

## Update a project
<a name="insights-working-with-projects-update"></a>

`UpdateProject` updates top-level configuration blocks independently. A block you omit is left unchanged. A block you include is replaced in full, so send the complete block, including its required members. Members you leave out of an included block are cleared or reset to their defaults.

To turn a feature off, send its block with the off value: `DetectionMode: DISABLED` for sensitive data, `State: DISABLED` for generative output and splitting, or `Blueprints: []` to clear custom extraction.

`EncryptionConfiguration` is the exception: an omitted `KmsKeyId` or `KmsEncryptionContext` keeps the stored value. Send `KmsKeyId` as an empty string to return to the service-managed key.

`ProjectName` is immutable—you cannot rename a project. To use a different name, create a new project.

```
aws textract update-project \
  --region us-east-1 \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcdef123456" \
  --sensitive-data-configuration '{"DetectionMode": "DETECTION", "PiiEntitiesConfiguration": {"PiiEntityTypes": ["ALL"]}}'
```

This example adds a sensitive-data configuration while leaving the extraction and custom configurations unchanged.

## List projects
<a name="insights-working-with-projects-list"></a>

`ListProjects` returns the projects in your account. You can filter the list by a blueprint to find the projects that reference it:

```
aws textract list-projects \
  --region us-east-1 \
  --blueprint-filter '{"BlueprintArn": "arn:aws:textract:us-east-1:111122223333:blueprint/abcdef123456"}'
```

## Delete a project
<a name="insights-working-with-projects-delete"></a>

`DeleteProject` removes a project:

```
aws textract delete-project \
  --region us-east-1 \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcdef123456"
```

A blueprint cannot be deleted while a project references it, so delete or update the referencing projects first when you want to remove a blueprint. See [Blueprint versioning](insights-blueprint-versioning.md).

## Next steps
<a name="insights-working-with-projects-next-steps"></a>

To continue, see the following topics:
+ Attach custom extraction schemas in [Custom extraction with blueprints](insights-custom-extraction.md).
+ Configure extraction in [Extraction results](insights-extraction-results.md) and [Output formats for LLM and RAG workflows](insights-output-formats.md).