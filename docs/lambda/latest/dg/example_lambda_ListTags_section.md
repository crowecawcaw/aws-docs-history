# Use `ListTags` with a CLI

The following code examples show how to use `ListTags`.

CLI

**AWS CLI**

**To retrieve the list of tags for a Lambda function**

The following `list-tags` example displays the tags attached to the `my-function` Lambda function.

```
`aws lambda list-tags \
 --resource `arn:aws:lambda:us-west-2:123456789012:function:my-function``

```

Output:

```
{
    "Tags": {
        "Category": "Web Tools",
        "Department": "Sales"
    }
}
```

For more information, see [Tagging Lambda Functions](tagging.md "tagging.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-tags.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-tags.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Retrieves the tags and their values currently set on the specified function.**

```
Get-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"

```

**Output:**

```
Key        Value
---        -----
California Sacramento
Oregon     Salem
Washington Olympia
```

- For API details, see
  [ListTags](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Retrieves the tags and their values currently set on the specified function.**

```
Get-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"

```

**Output:**

```
Key        Value
---        -----
California Sacramento
Oregon     Salem
Washington Olympia
```

- For API details, see
  [ListTags](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
