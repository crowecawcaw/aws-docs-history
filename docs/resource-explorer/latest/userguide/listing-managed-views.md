# Listing managed views

You can see which managed views you have access to on the **Views** page
in the Resource Explorer console. You can also run AWS CLI commands or their equivalent API operations in
an AWS SDK to list the managed views you have access to in your currently selected
AWS Region and retrieve view details.

To run these commands, you must have the following permissions:

- **Action**:
  `resource-explorer-2:GetManagedView`

**Resource**: The ARN of the specified view.

- **Action**:
  `resource-explorer-2:ListManagedViews`

**Resource**: The ARN of the specified view.
**To list your available managed views**

Run the following command to list managed views in the specified AWS Region:

```
aws resource-explorer-2 list-managed-views  --region `region`
```

The command output is a list of ARNs.

```
{
  "ManagedViews": [
    "arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ManagedViewNameA/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
    "arn:aws:resource-explorer-2:us-east-1:444455556666:managed-view/ManagedViewNameB/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222"
  ]
}
```

**To retrieve managed view details**

Run the following command to retrieve details about a specified managed view using the
view's ARN:

```
aws resource-explorer-2 get-managed-view \
    --managed-view-arn `arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ManagedViewNameA/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111`
```

The command output provides details about the specified managed view, similar to the
following:

```
{
  "ManagedView": {
    "ManagedViewArn": "arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ManagedViewNameA/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
    "ManagedViewName": "ManagedViewNameA",
    "TrustedService": "sampleservice.amazonaws.com",
    "LastUpdatedAt": "2024-01-01T01:01:01.100000+00:00",
    "Owner": "111111111111",
    "Scope": "arn:aws:iam::111111111111:root",
    "Filters": {
      "FilterString": ""
    },
    "IncludedProperties": [
      {
        "Name": "tags"
      }
    ],
    "ResourcePolicy": "{\"Version\":\"`YYYY-MM-DD`\",\"Statement\":[{\"Sid\":\"EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111_ACCESS_TO_SERVICE_PRINCIPAL\",\"Effect\":\"Allow\",\"PrincipalGroup\":{\"AWS\":\"sservicea.amazonaws.com\"},\"Action\":[\"resource-explorer-2:GetManagedView\",\"resource-explorer-2:DeleteManagedView\",\"resource-explorer-2:Search\"],\"Resource\":\"arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ExampleManagedViewName/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"}}},{\"Sid\":\"EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111_DENY_ACCESS_TO_NON_SERVICE_PRINCIPAL\",\"Effect\":\"Deny\",\"Principal\":\"*\",\"NotAction\":\"resource-explorer-2:GetManagedView\",\"Resource\":\"arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ExampleManagedViewName/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111\",\"Condition\":{\"ForAllValues:StringNotEquals\":{\"aws:PrincipalServiceNamesList\":\"servicea.amazonaws.com\"}}}]}",
    "Version": "1"
  }
}
```
