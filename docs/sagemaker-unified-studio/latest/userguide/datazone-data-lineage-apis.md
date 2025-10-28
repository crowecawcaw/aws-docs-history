# Publishing data lineage

programmatically

You can also publish data lineage programmatically using [PostLineageEvent](../../../datazone/latest/APIReference/API_PostLineageEvent.md "../../../datazone/latest/APIReference/API_PostLineageEvent.md") API. The API takes in open lineage run event as the
payload. Additionally, the following APIs support lineage events and traversing
lineage graph: [GetLineageEvent](../../../datazone/latest/APIReference/API_GetLineageEvent.md "../../../datazone/latest/APIReference/API_GetLineageEvent.md"), [ListLineageEvents](../../../datazone/latest/APIReference/API_ListLineageEvents.md "../../../datazone/latest/APIReference/API_ListLineageEvents.md"), [GetLineageNode](../../../datazone/latest/APIReference/API_GetLineageNode.md "../../../datazone/latest/APIReference/API_GetLineageNode.md"), and [ListLineageNodeHistory](../../../datazone/latest/APIReference/API_ListLineageNodeHistory.md "../../../datazone/latest/APIReference/API_ListLineageNodeHistory.md").

The following is a sample PostLineageEvent operation payload:

```

{
  "producer": "https://github.com/OpenLineage/OpenLineage",
  "schemaURL": "https://openlineage.io/spec/2-0-0/OpenLineage.json#/definitions/RunEvent",
  "eventType": "COMPLETE",
  "eventTime": "2024-05-04T10:15:30Z",
  "run": {
    "runId": "d2e7c111-8f3c-4f5b-9ebd-cb1d7995082a"
  },
  "job": {
    "namespace": "xyz.analytics",
    "name": "transform_sales_data"
  },
  "inputs": [
    {
      "namespace": "xyz.analytics",
      "name": "raw_sales",
      "facets": {
        "schema": {
          "_producer": "https://github.com/OpenLineage/OpenLineage",
          "_schemaURL": "https://openlineage.io/spec/facets/schema_dataset.json",
          "fields": [
            { "name": "region", "type": "string" },
            { "name": "year", "type": "int" },
            { "name": "created_at", "type": "timestamp" }
          ]
        }
      }
    }
  ],
  "outputs": [
    {
      "namespace": "xyz.analytics",
      "name": "clean_sales",
      "facets": {
        "schema": {
          "_producer": "https://github.com/OpenLineage/OpenLineage",
          "_schemaURL": "https://openlineage.io/spec/facets/schema_dataset.json",
          "fields": [
            { "name": "region", "type": "string" },
            { "name": "year", "type": "int" },
            { "name": "created_at", "type": "timestamp" }

          ]
        },
        "columnLineage": {
          "_producer": "https://github.com/OpenLineage/OpenLineage",
          "_schemaURL": "https://openlineage.io/spec/facets/columnLineage" + "DatasetFacet.json",
          "fields": {
            "id": {
              "inputFields": [
                {
                  "namespace": "xyz.analytics",
                  "name": "raw_sales",
                  "field": "id"
                }
              ]
            },
            "year": {
              "inputFields": [
                {
                  "namespace": "xyz.analytics",
                  "name": "raw_sales",
                  "field": "year"
                }
              ]
            },
            "created_at": {
              "inputFields": [
                {
                  "namespace": "xyz.analytics",
                  "name": "raw_sales",
                  "field": "created_at"
                }
              ]
            }
          }
        }
      }
    }
  ]
}

```
