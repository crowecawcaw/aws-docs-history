# Tag-based Policies

Amazon SWF supports policies based on tags. For instance, you could restrict Amazon SWF domains
that include a tag with the key `environment` and the value
`production` with the following condition:

```
"Condition": {
    "StringEquals": {"aws:ResourceTag/environment": "production"}
}
```

For more information on tagging, see:

- [Tags in Amazon SWF](swf-dev-adv-tags.md "swf-dev-adv-tags.md")
- [Controlling Access Using IAM
  Tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md")
