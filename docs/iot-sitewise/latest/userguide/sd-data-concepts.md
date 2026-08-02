# Data concepts in Scenario Discovery

Before you manage your workflow, take a moment to understand the key data concepts in this
section. Understanding these concepts and the reasoning behind them enables you to use the system
more efficiently. In the previous sections, you learned about the Account and Workspace data
entities. This section takes you deeper into the data entities in the system.

## Datasets

Datasets serve as the fundamental logical grouping of data. A dataset contains (or
references) the actual data you ingest, store, and index in Scenario Discovery through the
onboarding process. Data types in datasets include video (MPEG-4, H.264 encoding), OpenLABEL
annotations, and telemetry data captured as Parquet files. There are two fundamental types
of datasets, each with its own function in the system.

### Session dataset

Session datasets represent a complete collection (videos, annotations, and telemetry)
captured from a particular data collection event. In automotive ADAS applications, this
typically represents a single driving session for an instrumented vehicle set up to capture
multi-modal driving data. For the purposes of Scenario Discovery, a session dataset
represents the system-ingested parts of the original recordings in the formats the system
specifies (MPEG-4 H.264, OpenLABEL, and Parquet) derived from the actual raw data gathered
on the vehicle.

### Curated dataset

Curated datasets are a collection of video snippets (and possibly other
time-synchronous multi-modal data such as telemetry and annotations) that have been curated
within the system. Curation occurs through manual curation, where you prompt the system and
judge or choose the relevant results, or through Agentic Curation, where the system
leverages your intent expressed in natural language to derive a curated set of related
results. Curated datasets contain all the information needed to identify where in the
original data the scenes or snippets of interest are located. Curated datasets also define
how Scenario Discovery extracts the curated results from the original session datasets for
delivery to your downstream applications (annotation tools, simulation tools, or model
training tools).

## Timeseries and aliases

Scenario Discovery uses the concept of timeseries. You can reference a timeseries in two
ways: by an internally generated unique alphanumeric ID, or by a (recommended) human-readable
alias associated with that ID. Timeseries are unique at the account level by system-generated
identifier; aliases are unique at the workspace level. This means that in Workspace A you can
have a timeseries alias called "/test\_vehicle\_02/left\_front\_camera" associated with a UUID of
abc123. In Workspace B, you can also have a timeseries alias called
"/test\_vehicle\_02/left\_front\_camera," but the UUID will be different (for example, zxy987)
because the system creates it with the data you load into that workspace. A timeseries
conceptually represents the data contained in one physical sensor across datasets and across
time. This sensor can be a camera, in-vehicle network signals, or an annotation file.
Scenario Discovery stores three types of timeseries data, discussed in the following
subsections.

### Understanding aliases

An alias (propertyAlias) is a customer-defined, human-readable string that uniquely
names a data stream (timeseries) within a workspace. Every piece of data you ingest —
whether it's a video recording, a telemetry stream, or an annotation file — is identified
by an alias that you choose.

Think of it like a filesystem path for your data:

```
/fleet-7/truck-42/front_camera
/fleet-7/truck-42/lidar_top
/route-A/session-2026-06-15/rear_cam_rainy
```

The system also assigns an opaque timeSeriesId (UUID), but the alias is what you
interact with day-to-day.

#### Why aliases matter

| Purpose                   | Explanation                                                   |
| ------------------------- | ------------------------------------------------------------- |
| Human readability         | Name your data logically instead of tracking UUIDs            |
| Cross-API identifier      | Used across ingestion, enrichment, listing, and querying APIs |
| Stable reference          | You control the name; it doesn't change unless you do         |
| Filtering and diagnostics | List segments by alias to find specific recordings quickly    |

#### Where you provide an alias (ingestion)

When calling `CreateBulkImportJob`, you specify the alias differently
depending on the file format.

##### MP4 video files

Alias is required per file, along with `startTime`:

```
{
  "files": [
    {
      "alias": "/fleet-7/truck-42/front_camera",
      "bucket": "my-data-bucket",
      "key": "recordings/2026-06-15/front_cam.mp4",
      "startTime": {"timeInSeconds": 1718452800, "offsetInNanos": 0}
    }
  ],
  "jobConfiguration": { "fileFormat": { "mp4": {} } }
}
```

##### Annotation (OpenLABEL) files

Alias is required per file. Timestamps are derived from frame data inside the
file:

```
{
  "files": [
    {
      "alias": "/fleet-7/truck-42/front_camera_annotations",
      "bucket": "my-data-bucket",
      "key": "labels/pedestrian_events.json"
    }
  ],
  "jobConfiguration": { "fileFormat": { "annotation": {} } }
}
```

##### Parquet telemetry files

Alias is a required column inside the Parquet schema itself — each row declares
which timeseries it belongs to:

| Column         | Type              | Description                                            |
| -------------- | ----------------- | ------------------------------------------------------ |
| `alias`        | string, required  | Identifies the timeseries for this row                 |
| `timestamp_ns` | int64, required\* | Nanosecond-precision timestamp                         |
| `value`        | binary, required  | Data payload                                           |
| `data_type`    | string, required  | One of: JSON, BINARY, BOOLEAN, DOUBLE, STRING, INTEGER |

#### Where aliases appear after ingestion

##### ListDatasetDataSegments response

Every segment returned carries its alias:

```
{
  "alias": "/fleet-7/truck-42/front_camera",
  "dataType": "VIDEO",
  "timeSeriesId": "a1b2c3d4-...",
  "startTimestamp": {
    "timeInSeconds": 1778275007,
    "offsetInNanos": 0
  },
  "endTimestamp": {
    "timeInSeconds": 1778275307,
    "offsetInNanos": 0
  },
  "enrichment": { "status": "ENRICHED", "lastEnrichedAt": 1781933115.223 }
}
```

##### CLI example — list all video aliases and enrichment status

```
aws iotsitewise list-dataset-data-segments --region eu-west-1 \
  --workspace-name my-workspace --dataset-id my-dataset \
  --query "dataSegments[?dataType=='VIDEO'].{alias:alias,tsId:timeSeriesId,status:enrichment.status}"
```

#### How to use aliases for enrichment

`CreateEnrichmentJob` targets a single timeseries. Identify it using
either `propertyAlias` or `timeSeriesId` — never both. The API
rejects the request if you supply both.

```
{
  "workspaceName": "my-workspace",
  "jobConfiguration": {
    "eventDetection": {
      "datasetId": "dataset-abc123",
      "propertyAlias": "/fleet-7/truck-42/front_camera",
      "trimSettings": {
        "startTime": {
          "timeInSeconds": 1778275007,
          "offsetInNanos": 0
        },
        "endTime": {
          "timeInSeconds": 1778275307,
          "offsetInNanos": 0
        }
      }
    }
  }
}
```

This is where alias shines — you can target a video for enrichment by name without
needing to look up its UUID.

#### How to use aliases for diagnostics

When a dataset shows `PARTIALLY_ENRICHED`, use the alias to pinpoint
which videos still need enrichment:

```
# Step 1: Check dataset-level enrichment status
aws iotsitewise describe-dataset --region eu-west-1 \
  --workspace-name my-workspace --dataset-id my-dataset \
  --query 'enrichmentStatus'

# Step 2: Find the NOT_ENRICHED segments by alias
aws iotsitewise list-dataset-data-segments --region eu-west-1 \
  --workspace-name my-workspace --dataset-id my-dataset \
  --query "dataSegments[?enrichment.status=='NOT_ENRICHED'].alias"
```

#### Naming conventions (recommendations)

The alias is a freeform string (type AssetPropertyAlias). Common patterns:

| Pattern                             | Example                         |
| ----------------------------------- | ------------------------------- |
| /fleet/vehicle/camera\_position     | /fleet-7/truck-42/front\_camera |
| /route/session\_date/sensor         | /route-A/2026-06-15/lidar\_top  |
| /project/recording\_id/stream\_name | /adas-v2/rec-0042/stereo\_left  |

Use a consistent hierarchy so your team can filter and reason about data without
consulting a lookup table.

## Video

You typically gather videos on test vehicles over a set period as part of a broader
sensor suite deployed on the vehicle. You can manage video collection in different ways:
sometimes as one long video over a whole drive session or often segmented into many smaller
chunks. Since a single camera on a test vehicle can generate multiple videos over a single
drive session as well as over multiple drive sessions, use an alias unique to that test
vehicle and sensor (camera) to associate the many small chunks of video with the single
video timeseries. In a session-type dataset, you can see all videos uploaded to the session
dataset and their associated aliases. A single alias can (and usually does) contain multiple
video files.

## Annotations

You ingest annotations to Scenario Discovery using the OpenLABEL JSON format. The system
stores each annotation as its own individual timeseries, and there is a one-to-one
relationship between the number of annotation files you upload, and the number of annotations
shown in a dataset.

## Telemetry

Telemetry ingestion is designed to be flexible and capable of handling thousands of
different timestreams in one import. Since many types of signal data are captured as
time-value pairs, the standard format for telemetry ingestion consists of a single Parquet
file containing the timestamp, alias for each signal, and the value for each signal at a
given timestamp. Upon ingestion, the system generates a unique ID for each different alias
and includes it in the Parquet file.

###### Important

Once you understand these concepts, your next steps are to upload and ingest data and
manage tasks and pipelines. These are available through a combination of user interface,
SDK documentation and API documentation. For more in-depth SDK and API documentation, go
to the SDK Experience and API documentation sections.
