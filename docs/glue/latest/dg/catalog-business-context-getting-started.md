# Getting started with business context in the Data Catalog

###### Note

Business context and semantic search is in preview for AWS Glue and is subject to change.

This tutorial walks you through creating a glossary, tagging assets, and using
semantic search to discover data by meaning.

## Prerequisites

- An AWS account with the AWS Glue Data Catalog configured in a supported Region.
- The AWS CLI installed and configured.
- At least one table registered in the Data Catalog.
- An IAM role or user with permissions for AWS Glue Data Catalog actions.

Attach the following IAM policy to grant the required permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "glue:SearchAssets", "glue:PutAsset", "glue:GetAsset", "glue:DeleteAsset",
            "glue:PutAssetType", "glue:GetAssetType", "glue:DeleteAssetType", "glue:ListAssetTypes",
            "glue:CreateGlossary", "glue:UpdateGlossary", "glue:GetGlossary", "glue:ListGlossaries", "glue:DeleteGlossary",
            "glue:CreateGlossaryTerm", "glue:UpdateGlossaryTerm", "glue:GetGlossaryTerm", "glue:ListGlossaryTerms", "glue:DeleteGlossaryTerm",
            "glue:AssociateGlossaryTerms", "glue:DisassociateGlossaryTerms",
            "glue:PutFormType", "glue:GetFormType", "glue:DeleteFormType", "glue:ListFormTypes",
            "glue:PutAttachment", "glue:DeleteAttachment",
            "glue:ListIterableForms", "glue:BatchGetIterableForms"
        ],
        "Resource": "*"
    }]
}
```

## Step 1: Create a glossary and tag an asset

###### To create a glossary

Run the following command:

```
aws glue create-glossary \
  --name "Enterprise Data Glossary" \
  --description "Standardized business definitions for enterprise data assets."
```

Example output:

```
{
    "Id": "d7xm3np5rk2w9j",
    "Name": "Enterprise Data Glossary"
}
```

###### To create a glossary term

Replace the glossary identifier with the `Id` from the preceding output.

```
aws glue create-glossary-term \
  --glossary-identifier "d7xm3np5rk2w9j" \
  --name "Active User" \
  --short-description "A user with at least one login in the last 30 days." \
  --long-description "An account that has logged in at least once within the trailing 30-day window."
```

Example output:

```
{
    "Id": "c2fymbu18rtsx5",
    "GlossaryId": "d7xm3np5rk2w9j",
    "Name": "Active User"
}
```

###### To associate the term with an asset

Run the following command:

```
aws glue associate-glossary-terms \
  --asset-identifier "arn:aws:glue:us-east-1:123456789012:table/mydb/sales_transactions" \
  --glossary-term-identifiers "c2fymbu18rtsx5"
```

## Step 2: Search for data using business context

Use the `SearchAssets` API to find assets by business meaning.

```
aws glue search-assets \
  --search-text "active users"
```

Example output:

```
{
    "Items": [
        {"Id": "c9vq7sh2fk4t2h", "AssetName": "Customer Sales Transactions", "AssetTypeId": "Table"}
    ]
}
```

To filter results by asset type:

```
aws glue search-assets \
  --search-text "active users" \
  --filter-clause '{"AttributeFilter":{"Attribute":"type","Operator":"equals","Value":{"StringValue":"Table"}}}' \
  --max-results 10
```

To filter to only AWS Glue tables (excluding tables from other source systems):

```
aws glue search-assets \
  --search-text "active users" \
  --filter-clause '{"AndAllFilters":[{"AttributeFilter":{"Attribute":"type","Operator":"equals","Value":{"StringValue":"Table"}}},{"AttributeFilter":{"Attribute":"namespace","Operator":"equals","Value":{"StringValue":"amazon.glue"}}}]}' \
  --max-results 10
```

## Using AI agents with the catalog

MCP-compatible AI agents can discover catalog assets, retrieve business context,
and load skill content using skills from the AWS Agent Toolkit. You can get
catalog skills in the following ways:

- **Bundled with a plugin** –
  Install the `aws-data-analytics` plugin, which includes a curated
  set of catalog skills available to the agent immediately after installation.
  For instructions, see [Installing plugins](../../../agent-toolkit/latest/userguide/plugins.md#installing-plugins "../../../agent-toolkit/latest/userguide/plugins.md#installing-plugins") in the AWS Agent Toolkit User Guide.
- **Installed locally** –
  Download individual skills from the Agent Toolkit for AWS repository on
  GitHub and add them to your agent's skills directory. The following skills
  support catalog workflows:

  - [exploring-data-catalog](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/exploring-data-catalog "https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/exploring-data-catalog")
  - [finding-data-lake-assets](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/finding-data-lake-assets "https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/finding-data-lake-assets")

## Next steps

- Attach forms to standardize metadata fields such as data residency or retention policy.
- Create skill assets that provide AI agents with domain context for your data.
