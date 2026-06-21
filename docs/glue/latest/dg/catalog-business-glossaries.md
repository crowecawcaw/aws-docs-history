# Business glossaries for AWS Glue Data Catalog

###### Note

Business context and semantic search is in preview for AWS Glue and is subject to change.

A business glossary is a container for controlled vocabulary terms that define business
concepts within your organization. Associate glossary terms with Data Catalog assets to enrich
them with business meaning and improve discoverability through semantic search.

## Creating a glossary

Use `CreateGlossary` to create a business glossary.

```
aws glue create-glossary \
    --name "Finance Data Definitions" \
    --description "Standardized financial terms used across reporting and analytics"
```

Example output:

```
{
    "Id": "gl-c9vq7sh2fk4t2h",
    "Name": "Finance Data Definitions"
}
```

## Creating glossary terms

Use `CreateGlossaryTerm` to add terms to a glossary.

```
aws glue create-glossary-term \
    --glossary-identifier `glossary-id` \
    --name "Active User" \
    --short-description "A user with at least one login in the last 30 days" \
    --long-description "An account that has logged in at least once within the trailing 30-day window. Used as the standard engagement metric across all product teams."
```

Example output:

```
{
    "Id": "gt-d7xm3np5rk2w9j",
    "GlossaryId": "gl-c9vq7sh2fk4t2h",
    "Name": "Active User"
}
```

## Associating glossary terms with assets

Use `AssociateGlossaryTerms` to associate terms with Data Catalog assets.

###### Note

During preview, you can associate a maximum of 10 glossary terms per asset.

```
aws glue associate-glossary-terms \
    --identifier `asset-id` \
    --glossary-term-identifiers '["`term-id-1`", "`term-id-2`"]'
```

Example output:

```
{
    "Identifier": "c2fymbu18rtsx5",
    "GlossaryTerms": [
        {"Id": "gt-d7xm3np5rk2w9j", "Name": "Active User"},
        {"Id": "gt-h4kp9wt6mq3v2n", "Name": "PII"}
    ]
}
```

## Removing glossary term associations

Use `DisassociateGlossaryTerms` to remove term associations from an asset.

```
aws glue disassociate-glossary-terms \
    --identifier `asset-id` \
    --glossary-term-identifiers '["`term-id`"]'
```

## Updating glossaries and terms

Updates take effect immediately and are reflected in search results.

###### To update a glossary

Use `UpdateGlossary`:

```
aws glue update-glossary \
    --identifier `glossary-id` \
    --name "Enterprise Finance Glossary" \
    --description "Updated standardized financial terms for enterprise reporting"
```

###### To update a glossary term

Use `UpdateGlossaryTerm`:

```
aws glue update-glossary-term \
    --identifier `term-id` \
    --name "Monthly Active User" \
    --short-description "A user with at least one login in the last 30 days"
```

## Deleting glossaries and terms

You must delete all terms from a glossary before you can delete the glossary.

###### To delete a glossary term

Use `DeleteGlossaryTerm`:

```
aws glue delete-glossary-term \
    --identifier `term-id`
```

###### To delete a glossary

Use `DeleteGlossary` after removing all terms:

```
aws glue delete-glossary \
    --identifier `glossary-id`
```

## Listing glossaries and terms

Both `ListGlossaries` and `ListGlossaryTerms` support pagination
with `MaxResults` and `NextToken`.

###### To list all glossaries

Run the following command:

```
aws glue list-glossaries \
    --max-results 10
```

Example output:

```
{
    "Items": [
        {"Id": "gl-c9vq7sh2fk4t2h", "Name": "Finance Data Definitions"},
        {"Id": "gl-f8yn2bx7jl5r4k", "Name": "Marketing Glossary"}
    ]
}
```

###### To list terms in a glossary

Run the following command:

```
aws glue list-glossary-terms \
    --glossary-identifier `glossary-id` \
    --max-results 10
```

Example output:

```
{
    "GlossaryId": "gl-c9vq7sh2fk4t2h",
    "Items": [
        {"Id": "gt-d7xm3np5rk2w9j", "Name": "Active User"},
        {"Id": "gt-j6rm4xv9np8w3t", "Name": "EBITDA"}
    ]
}
```

## Retrieving glossary and term details

###### To retrieve a glossary

Run the following command:

```
aws glue get-glossary \
    --identifier `glossary-id`
```

###### To retrieve a glossary term

Run the following command:

```
aws glue get-glossary-term \
    --identifier `term-id`
```
