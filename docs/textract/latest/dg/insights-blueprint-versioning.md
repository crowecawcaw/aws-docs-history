

# Blueprint versioning

A blueprint has one mutable current schema and up to a quota of immutable numbered versions (see [Limits and quotas](insights-quotas.md)). Use versions to freeze a schema you have validated so that changes to the current schema do not affect jobs already in production.

## Current schema versus numbered versions
<a name="insights-current-versus-numbered"></a>
+ **Current schema** — the working schema of the blueprint. `CreateBlueprint` sets it, and `UpdateBlueprint` replaces it. It is mutable: each update overwrites the previous current schema.
+ **Numbered versions** — immutable snapshots created with `CreateBlueprintVersion`. Versions are numbered "1", "2", and so on. After it is created, a version never changes.

A typical workflow is to iterate on the current schema until extraction looks right, call `CreateBlueprintVersion` to snapshot it, and then pin that version in your projects. You can keep editing the current schema afterward without disturbing pinned jobs.

## Create a version
<a name="insights-create-a-version"></a>

`CreateBlueprintVersion` snapshots the current schema as the next numbered version.

```
aws textract create-blueprint-version \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --region us-east-1
```

### When you reach the version quota
<a name="insights-version-quota"></a>

Each blueprint can hold a limited number of numbered versions. When the blueprint already has the maximum, `CreateBlueprintVersion` fails with `LimitExceededException`. To create another version, either delete a version you no longer use (see [Delete ordering](#insights-delete-ordering)), or request a quota increase for **Versions per blueprint** in Service Quotas. Deleted version numbers are not reused: if you delete version 2 of a blueprint that has versions 1 to 10, the next version you create is 11. For the default value, see [Limits and quotas](insights-quotas.md).

## Get a specific version
<a name="insights-get-a-specific-version"></a>

`GetBlueprint` without a version returns the current schema. Pass `--blueprint-version` to return the snapshot of that numbered version instead.

```
aws textract get-blueprint \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --blueprint-version "1" \
  --region us-east-1
```

## Pin a version in a project
<a name="insights-pin-a-version"></a>

In a project's custom configuration, each blueprint entry carries a `BlueprintArn` and an optional `BlueprintVersion`. Set `BlueprintVersion` to pin a specific numbered version; omit it to use the current schema. An unpinned blueprint uses whatever the current schema is when each job runs, so a later `UpdateBlueprint` changes the output of every job that follows. Pin a version for production workloads, and leave it unpinned only while you develop the schema.

```json
{
  "Blueprints": [
    {
      "BlueprintArn": "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint",
      "BlueprintVersion": "1"
    }
  ]
}
```

Pinning a version means that later edits to the current schema do not change how the project processes documents. See [Working with projects](insights-working-with-projects.md) for how to set a project's custom configuration.

## List versions
<a name="insights-list-versions"></a>

`ListBlueprints` with `--blueprint-arn` lists the versions of a single blueprint.

```
aws textract list-blueprints \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --region us-east-1
```

## Delete ordering
<a name="insights-delete-ordering"></a>

`DeleteBlueprint` with `--blueprint-version` deletes that single version. `DeleteBlueprint` without a version deletes the whole blueprint, but only after all of its numbered versions are gone. If versions still exist, the call fails:

```
ValidationException: The blueprint cannot be deleted because one or more versions still exist
```

Delete each numbered version first, then delete the blueprint.

```
# Delete version 1
aws textract delete-blueprint \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --blueprint-version "1" \
  --region us-east-1
# After all versions are deleted, delete the blueprint
aws textract delete-blueprint \
  --blueprint-arn "arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint" \
  --region us-east-1
```

Deletion is also blocked while a project references the blueprint. In that case the call fails with `ValidationException`; remove the blueprint from the project first.

Find the referencing project:

```
aws textract list-projects \
  --blueprint-filter '{"BlueprintArn":"arn:aws:textract:us-east-1:111122223333:blueprint/my-invoice-blueprint","BlueprintVersion":"1"}' \
  --max-items 10 \
  --region us-east-1
```

For request parameters and errors, see the Amazon Textract Insights API Reference.