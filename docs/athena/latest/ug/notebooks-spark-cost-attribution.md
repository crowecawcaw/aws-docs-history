# Session level cost attribution

From Apache Spark version 3.5 release version onward, Athena allows tracking costs for each session. You can define cost allocation tags when starting a session and the reported costs for a session will appear in Cost Explorer or on AWS Billing cost allocation reports. You can also apply cost allocation tags at the Workgroup level and those get copied over to any sessions started on that workgroup.

## Using Session Level Cost Attribution

By default, any cost allocation tags specified at the workgroup level is copied over to interactive sessions started on that workgroup.

To disable tags to be copied from the Workgroup when starting an interactive session from the AWS CLI:

```
aws athena start-session \
  --region "REGION" \
  --work-group "WORKGROUP" \
  --tags '[
    {
      "Key": "tag_key",
      "Value": "tag_value"
    }
  ]' \
  --no-copy-work-group-tags
```

To enable tags to be copied from the Workgroup when starting an interactive session from the AWS CLI:

```
aws athena start-session \
  --region "REGION" \
  --work-group "WORKGROUP" \
  --copy-work-group-tags
```

## Considerations and Limitations

- Session tags overrides workgroup tags with the same keys.
