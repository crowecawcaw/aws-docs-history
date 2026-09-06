# Metadata Object

The `metadata` object is optional organizational metadata used to categorize and group resources within your workspace. It does not affect runtime behavior it is purely for organization and filtering in the agentic CX designer workspace.

| Field  | Type     | Required | Description                                                                                                                                  |
| ------ | -------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `path` | string   | No       | A folder-like path for organizing resources in the agentic CX designer workspace (e.g., `/support/tags`, `/production`). Max 512 characters. |
| `tags` | string[] | No       | Classification labels for filtering and grouping (max 5 tags, each max 256 characters).                                                      |

## Example

```
{
  "metadata": {
    "path": "/customer-support/sentiment",
    "tags": ["production", "support"]
  }
}
```
