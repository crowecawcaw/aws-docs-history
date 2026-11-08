

# Mappings and index templates
<a name="optimized-log-analytics-mappings"></a>

This topic shows how to model logs, OpenTelemetry data, and security findings for the Optimized engine. The core choice is straightforward: use `object` for one structured value, `nested` for a list of objects whose fields must stay correlated, `multi_value` for a list of scalar values, and `flat_object` for an open-ended key/value bag.

**Note**  
The Optimized engine mapping behavior and index-template patterns described in this topic require OpenSearch 3.7.

## Choose the mapping from the data shape
<a name="optimized-log-analytics-mappings-shape"></a>

Choose a mapping from the shape of the data. This distinction keeps the physical schema predictable and makes query semantics explicit.


| Data shape | Mapping | Example | 
| --- | --- | --- | 
| One scalar | Scalar type | status\_code: integer | 
| A list of scalar values | Scalar type with multi\_value: true | tags: ["prod", "checkout"] | 
| One structured object | object | status: {code, message} | 
| A list of objects needing per-element correlation | nested | span events[], correlated items[], resource collections | 
| An open set of scalar key/value attributes | flat\_object | OpenTelemetry attributes, labels, and resource metadata | 

## Scalar arrays with multi\_value
<a name="optimized-log-analytics-mappings-multivalue"></a>

A scalar field is single-valued by default. Add `multi_value: true` when a field can contain zero, one, or many scalar values.

```
"host.ip": { "type": "ip", "multi_value": true },
"tags":    { "type": "keyword", "multi_value": true }
```

When producers can vary between scalar and array forms, declare the intended shape in an index template. Explicit `multi_value: true` and `multi_value: false` both appear in the mapping. An omitted value is not serialized.

## Dynamic mapping and dynamic templates
<a name="optimized-log-analytics-mappings-dynamic"></a>

OpenSearch 3.7 can infer columnar field shapes from the first document that introduces a field. This is useful for evolving log and telemetry payloads, whereas dynamic templates provide a stable contract for fields whose shape is known in advance.


| First observed value | Inferred mapping on an Optimized index | 
| --- | --- | 
| Root string | text, without an automatic .keyword sub-field | 
| String inside a nested element | keyword | 
| Scalar number, date, IP, or boolean | Matching scalar type on the columnar path | 
| Scalar array, including a one-element array | Matching scalar type with multi\_value: true | 
| One object | object | 
| Array of objects | nested | 
| Object array inside another object array | Nested collection at each array boundary | 

The first observed shape establishes the mapping. A field first seen as a scalar stays scalar; declare `multi_value: true` in a template when later documents might send a list. A field first seen as one object stays an object; declare it as `nested` when the field represents an object list.

### Use templates to make producer intent explicit
<a name="optimized-log-analytics-mappings-dynamic-templates"></a>

Dynamic templates are evaluated before automatic inference. They can pin a known scalar list, keep an identifier scalar, map a known object collection as `nested`, or apply `low_cardinality` to string dimensions.

```
PUT _index_template/observability-dynamic-shapes
{
  "index_patterns": ["observability-*"],
  "template": {
    "mappings": {
      "dynamic": true,
      "dynamic_templates": [
        {
          "tag_lists": {
            "path_match": "tags",
            "match_mapping_type": "string",
            "mapping": {
              "type": "keyword",
              "multi_value": true
            }
          }
        },
        {
          "scalar_identifiers": {
            "path_match": "*.id",
            "match_mapping_type": "string",
            "mapping": {
              "type": "keyword",
              "multi_value": false
            }
          }
        },
        {
          "event_collections": {
            "match": "events",
            "match_mapping_type": "object",
            "mapping": {
              "type": "nested"
            }
          }
        },
        {
          "string_dimensions": {
            "match_mapping_type": "string",
            "mapping": {
              "type": "keyword",
              "low_cardinality": true
            }
          }
        }
      ]
    }
  }
}
```

Use `dynamic: true` for the evolving portion of a payload, templates for known field families, and `dynamic: strict` when the schema is a fixed contract. Simulate a template before rollout so incompatible combinations are reported before the first production index is created.

## object and nested
<a name="optimized-log-analytics-mappings-object-nested"></a>

Use `object` when the document contains one structured value. Use `nested` when it contains an array of objects and predicates on several child fields must match the same element. Given the following events array:

```
"events": [
  { "name": "exception", "type": "TimeoutException" },
  { "name": "retry", "type": "none" }
]
```

A correlated predicate such as `events.name = 'retry' AND events.type = 'TimeoutException'` must not combine values from different events. Mapping `events` as `nested` preserves that boundary.

```
"events": {
  "type": "nested",
  "properties": {
    "name": { "type": "keyword" },
    "type": { "type": "keyword" }
  }
}
```

Inside a nested element, you can use plain objects, dotted field names, `flat_object`, scalar fields, keyword multi-fields, and scalar fields with `multi_value: true`. Declare a scalar leaf as multi-value when one nested element can itself contain a scalar list.

For strings inside `nested`, use `keyword`. Put free text that needs `match` or `match_phrase` at the document root as `text` or `match_only_text`.

## flat\_object
<a name="optimized-log-analytics-mappings-flatobject"></a>

Use `flat_object` for attributes whose keys are not known when the template is created.

```
"attributes": { "type": "flat_object" }
```

Each key holds one scalar string value inside each object or nested element. Access a key using its dotted path, for example `attributes.http.method`. Cast the value when a numeric comparison is needed.

If one key can contain several values, promote it to a dedicated field with `multi_value: true`. Promote frequently grouped, sorted, or joined keys to dedicated `keyword` or numeric fields. Query joins, unions, grouping, and sorting on those dedicated fields or individual keys rather than carrying the whole `flat_object` value.

## OpenTelemetry logs index template
<a name="optimized-log-analytics-mappings-otel-logs"></a>

The following template keeps free-text log content at the root, models repeated addresses and tags as scalar lists, promotes commonly filtered dimensions, and leaves the long tail of attributes flexible.

```
PUT _index_template/otel-logs-optimized
{
  "index_patterns": ["otel-logs-*"],
  "template": {
    "settings": {
      "index.sort.field": ["service.name", "@timestamp"],
      "index.sort.order": ["asc", "desc"],
      "index.parquet.bloom_filter_enabled.field": ["trace_id"],
      "index.parquet.bloom_filter_enabled.value": [true]
    },
    "mappings": {
      "dynamic": true,
      "properties": {
        "@timestamp":          { "type": "date_nanos" },
        "observed_timestamp":  { "type": "date_nanos" },
        "body":                { "type": "text" },
        "severity.text":       { "type": "keyword", "low_cardinality": true },
        "severity.number":     { "type": "integer" },
        "trace_id":            { "type": "keyword" },
        "span_id":             { "type": "keyword" },
        "service.name":        { "type": "keyword", "low_cardinality": true },
        "service.version":     { "type": "keyword" },
        "host.name":           { "type": "keyword", "low_cardinality": true },
        "host.ip":             { "type": "ip", "multi_value": true },
        "k8s.namespace.name":  { "type": "keyword", "low_cardinality": true },
        "k8s.pod.name":        { "type": "keyword" },
        "http.request.method": { "type": "keyword", "low_cardinality": true },
        "http.response.status_code": { "type": "integer" },
        "http.route":          { "type": "keyword" },
        "tags":                { "type": "keyword", "multi_value": true },
        "resource.attributes": { "type": "flat_object" },
        "attributes":          { "type": "flat_object" },
        "scope.name":          { "type": "keyword" },
        "scope.version":       { "type": "keyword" }
      }
    }
  }
}
```

## OpenTelemetry traces index template
<a name="optimized-log-analytics-mappings-otel-traces"></a>

A span contains lists of event and link objects, so both fields are `nested`. Their string leaves are `keyword`, and each element's open-ended attributes remain a `flat_object`.

```
PUT _index_template/otel-traces-optimized
{
  "index_patterns": ["otel-traces-*"],
  "template": {
    "settings": {
      "index.sort.field": ["service.name", "start_time"],
      "index.sort.order": ["asc", "desc"],
      "index.parquet.bloom_filter_enabled.field": ["trace_id", "duration_nanos"],
      "index.parquet.bloom_filter_enabled.value": [true, false]
    },
    "mappings": {
      "dynamic": true,
      "properties": {
        "trace_id":        { "type": "keyword" },
        "span_id":         { "type": "keyword" },
        "parent_span_id":  { "type": "keyword" },
        "trace_state":     { "type": "keyword" },
        "name":            { "type": "keyword" },
        "kind":            { "type": "keyword", "low_cardinality": true },
        "start_time":      { "type": "date_nanos" },
        "end_time":        { "type": "date_nanos" },
        "duration_nanos":  { "type": "long" },
        "status.code":     { "type": "keyword", "low_cardinality": true },
        "status.message":  { "type": "keyword" },
        "service.name":    { "type": "keyword", "low_cardinality": true },
        "service.version": { "type": "keyword" },
        "host.name":       { "type": "keyword", "low_cardinality": true },
        "resource.attributes": { "type": "flat_object" },
        "attributes":          { "type": "flat_object" },
        "events": {
          "type": "nested",
          "properties": {
            "time":       { "type": "date_nanos" },
            "name":       { "type": "keyword" },
            "attributes": { "type": "flat_object" },
            "dropped_attributes_count": { "type": "integer" }
          }
        },
        "links": {
          "type": "nested",
          "properties": {
            "trace_id":    { "type": "keyword" },
            "span_id":     { "type": "keyword" },
            "trace_state": { "type": "keyword" },
            "attributes":  { "type": "flat_object" }
          }
        }
      }
    }
  }
}
```

## Generic structured finding example
<a name="optimized-log-analytics-mappings-finding"></a>

A finding-like record can combine one structured context, scalar lists, correlated item lists, and flexible resource attributes. This example keeps classification as one object, maps references as a scalar list, and maps scores, affected\_items, resources, and resource tags as `nested` because each element's fields belong together. The names and values are intentionally generic; the example illustrates structure rather than a particular product schema.

```
PUT _index_template/findings-optimized
{
  "index_patterns": ["findings-*"],
  "template": {
    "mappings": {
      "dynamic": "strict",
      "properties": {
        "finding_id":  { "type": "keyword" },
        "category":    { "type": "keyword", "low_cardinality": true },
        "status":      { "type": "keyword", "low_cardinality": true },
        "title":       { "type": "keyword" },
        "description": { "type": "keyword", "index": false },
        "first_seen":  { "type": "date" },
        "last_seen":   { "type": "date" },
        "classification": {
          "type": "object",
          "properties": {
            "reference_id": { "type": "keyword" },
            "references":   { "type": "keyword", "multi_value": true },
            "scores": {
              "type": "nested",
              "properties": {
                "scheme":  { "type": "keyword" },
                "value":   { "type": "double" },
                "version": { "type": "keyword" }
              }
            },
            "affected_items": {
              "type": "nested",
              "properties": {
                "name":     { "type": "keyword" },
                "version":  { "type": "keyword" },
                "item_type": { "type": "keyword", "low_cardinality": true },
                "path":     { "type": "keyword" }
              }
            }
          }
        },
        "resources": {
          "type": "nested",
          "properties": {
            "id":       { "type": "keyword" },
            "type":     { "type": "keyword", "low_cardinality": true },
            "location": { "type": "keyword", "low_cardinality": true },
            "tags": {
              "type": "nested",
              "properties": {
                "key":   { "type": "keyword" },
                "value": { "type": "keyword" }
              }
            },
            "attributes": { "type": "flat_object" }
          }
        }
      }
    }
  }
}
```

The following is a representative record for this template:

```
{
  "finding_id": "finding-001",
  "category": "CONFIGURATION",
  "status": "OPEN",
  "title": "Configuration requires review",
  "description": "Additional context retained for display.",
  "first_seen": "2026-10-01T08:15:30Z",
  "last_seen": "2026-10-21T18:02:11Z",
  "classification": {
    "reference_id": "REFERENCE-001",
    "references": ["REFERENCE-001", "REFERENCE-002"],
    "scores": [
      { "scheme": "scheme-a", "value": 7.5, "version": "1" },
      { "scheme": "scheme-b", "value": 5.5, "version": "2" }
    ],
    "affected_items": [
      { "name": "component-a", "version": "1.2.0", "item_type": "library", "path": "/components/a" },
      { "name": "component-b", "version": "2.1.0", "item_type": "service", "path": "/components/b" }
    ]
  },
  "resources": [
    {
      "id": "resource-001",
      "type": "service",
      "location": "location-a",
      "tags": [
        { "key": "team", "value": "team-a" },
        { "key": "environment", "value": "production" }
      ],
      "attributes": {
        "runtime": "example-runtime",
        "architecture": "example-architecture"
      }
    }
  ]
}
```

The following query requires `name` and `version` to come from the same affected-item element:

```
source=findings-*
| where classification.affected_items.name = 'component-a'
  and classification.affected_items.version = '1.2.0'
| fields finding_id, category, classification.reference_id
```

## Template checklist
<a name="optimized-log-analytics-mappings-checklist"></a>

Use the following checklist when you author an index template for the Optimized engine:
+ Declare scalar arrays with `multi_value: true`.
+ Declare object arrays needing correlation with `type: nested`.
+ Use `object` for a single structured value.
+ Use `keyword` for string leaves inside nested fields.
+ Keep root-level free text as `text` or `match_only_text`.
+ Use `flat_object` for flexible scalar attribute bags, and promote frequently queried keys.
+ Use `low_cardinality: true` for low-cardinality string dimensions used for exact filtering.
+ Put mappings and creation-time settings in an index template so rollovers remain consistent.