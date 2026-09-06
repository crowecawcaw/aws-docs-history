

# Lambda event source mapping execution block sample policy
<a name="security_iam_region_switch_lambda_esm"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Lambda event source mappings. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:GetEventSourceMapping",
        "lambda:UpdateEventSourceMapping"
      ],
      "Resource": "arn:aws:lambda:{{region}}:{{account-id}}:event-source-mapping:{{uuid}}"
    },
    {
      "Effect": "Allow",
      "Action": [
        "lambda:GetFunction"
      ],
      "Resource": "arn:aws:lambda:{{region}}:{{account-id}}:function:{{function-name}}"
    }
  ]
}
```