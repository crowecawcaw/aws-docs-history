# Skill assets for AI agents

###### Note

Business context and semantic search is in preview for AWS Glue and is subject to
change.

## What are skill assets

Skill assets are catalog assets that point to a URI location containing context
that AI agents use when working with your data. The URI can reference an accessible
location—such as a markdown file in Amazon S3, a document in a git repository, or a
wiki page—where you store organizational and domain knowledge, references, and instructions specific to one or more datasets.

Common uses for skill content include:

- Organizational context (for example, which teams own which data domains,
  how teams define key metrics, and what business processes produce the data)
- Data usage rules and constraints specific to your organization
- Common query patterns and SQL examples for your datasets

You associate skills with data assets using the `amazon::RelatedTo` form.
When an agent retrieves an asset, it finds the associated skill IDs, fetches the skill,
and loads the URI content into its reasoning context.

There are two kinds of skills:

- **Custom skills** – Created by you, searchable
  via the Search API. Identifiers must not begin with `amazon.`
- **Built-in skills** – Amazon-owned, immutable,
  accessed by ID directly (for example, `amazon.skill::querying-aws-s3`).

## Creating and associating a skill

### Step 1: Create the skill

```
aws glue put-asset \
    --asset-type-id "amazon::Skill" \
    --identifier "sales-table-skill" \
    --name "sales-table-skill" \
    --forms '{"amazon::Skill":{"FormTypeId":"amazon::Skill","Content":"{\"uri\": \"s3://my-bucket/skills/sales-table-skill.md\"}"}}'
```

### Step 2: Associate the skill with a table

```
aws glue put-attachment \
    --asset-identifier "arn:aws:glue:us-east-1:123456789012:table/mydb/sales_transactions" \
    --attachment-name relatedTo \
    --form-type-id "amazon::RelatedTo" \
    --content '{"assetIdentifiers":["sales-table-skill"]}'
```

## How relationships are defined

Relationships use the built-in `amazon::RelatedTo` form. A relation
declared on either asset surfaces symmetrically for both in relationship-based search.

```
{ "assetIdentifiers": ["<related-asset-id>"] }
```

Attach inline when creating the asset (`PutAsset --forms`) or afterward
(`PutAttachment`).

## Searching for skill assets

```
aws glue search \
    --filter-clause '{"AttributeFilter":{"Attribute":"type","Operator":"equals","Value":{"StringValue":"amazon::Skill"}}}' \
    --max-results 20
```

## Built-in skills

Reference the following Amazon-owned skills by ID:

- `amazon.skill::querying-aws-s3`
- `amazon.skill::querying-aws-cloudwatch`
- `amazon.skill::querying-aws-sagemaker-catalog`

## Deleting a skill asset

```
aws glue delete-asset \
    --identifier `skill-asset-id`
```

###### Note

Deleting a skill asset does not delete the content at the referenced URI.

## Considerations

- Review skill content when you rename columns, deprecate tables, or modify metrics.
- During preview, access is managed through IAM roles with no asset-level access control.
- Agents must have access to the skill URI (for example, `s3:GetObject` for Amazon S3 URIs).
- Keep skill content concise to minimize context window usage.
