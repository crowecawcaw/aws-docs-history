

# Viewing dependency insights
<a name="next-gen-viewing-insights"></a>

After insights are generated, they are stored with the service and remain available until you regenerate them. The console displays the summary in the **Dependencies** section, along with the time the summary was last generated so that you can gauge whether it is stale.

To retrieve the stored insights using the AWS CLI, use the following command.

```
aws resiliencehubv2 get-dependency-insights \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123"
```

The response includes an overview, a list of individual insights, the generation status, and the time the summary was last created.

```
{
  "status": "COMPLETED",
  "lastCreatedAt": "2026-09-15T10:00:00Z",
  "overview": "...",
  "insights": [
    {
      "category": "CROSS_REGION",
      "description": "..."
    },
    {
      "category": "NEW_DEPENDENCY",
      "description": "..."
    }
  ]
}
```

The following table describes the fields in the response.


| Field | Type | Description | 
| --- | --- | --- | 
| status | String | The state of insights generation: IN\_PROGRESS, COMPLETED, or FAILED. | 
| overview | String | A short narrative summary of the most significant patterns across your dependencies. Empty while status is IN\_PROGRESS or FAILED. | 
| insights | List | A list of individual insights, each with a category and a description. Empty while status is IN\_PROGRESS or FAILED. | 
| lastCreatedAt | Timestamp | When the summary was last successfully generated. | 

Each insight is assigned one of the following categories.


| Category | Description | 
| --- | --- | 
| CROSS\_REGION | A dependency that resolves in a different AWS Region than the caller. | 
| NEW\_DEPENDENCY | A dependency that first appeared in the last 7 days. | 
| THIRD\_PARTY | A non-AWS dependency. | 
| UNEVEN\_USAGE | A dependency with an irregular usage pattern. | 