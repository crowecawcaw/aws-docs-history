

# Step D: Query the metadata
<a name="query-metadata-query"></a>

Use the Elemental Inference GetEndpoint operation to obtain the metadata that Elemental Inference generates.

For example, the following CURL code shows how to use the POST command to query for the metadata for the output named `testOutput`. The query is for the first second of metadata. This one second span is identified by the start PTS of 0 and the end PTS of 1001.

```
# Query the first second of metadata
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "testOutput", "timeSpecification": { "ptsBased":
{ "startPts":0, "endPts": 1001, "timescale": 1000 } }, "parameters": {"smartCropping":
{"frameRate": { "numerator": 24, "denominator": 1}}}}'
```

For information about the metadata returned for each feature, see the following topics.

**Topics**
+ [Metadata for smart crop](#query-metadata-smart-crop)
+ [Metadata for smart subtitles](#query-metadata-smart-subtitles)
+ [Querying contextual metadata](#query-metadata-contextual)

## Metadata for smart crop
<a name="query-metadata-smart-crop"></a>

The following CURL code shows the query command plus the results when the output `testOutput` is a smart crop output.



```
# Query the first second of metadata
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "testOutput", "timeSpecification": { "ptsBased": { "startPts":0, "endPts": 1001, "timescale": 1000 } }, "parameters": {"smartCropping": {"frameRate": { "numerator": 24, "denominator": 1}}}}'
{
    "items": [
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2176,
                            "yPosition": 6250
                        }
                    }
                }
            },
            "pts": 0,
            "timecode": null
        },
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2176,
                            "yPosition": 6250
                        }
                    }
                }
            },
            "pts": 41,
            "timecode": null
        },
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2208,
                            "yPosition": 6238
                        }
                    }
                }
            },
            "pts": 83,
            "timecode": null
        },
.
.
.
        {
            "metadata": {
                "smartCropping": {
                    "crop": {
                        "centerPoint": {
                            "scale": 10000,
                            "xPosition": 2873,
                            "yPosition": 5781
                        }
                    }
                }
            },
            "pts": 1000,
            "timecode": null
        }
    ]
}
```

### Using the metadata
<a name="query-metadata-smart-crop-usage"></a>

For smart crop, Elemental Inference identifies a *region of interest* in each frame. Elemental Inference then generates metadata that identifies the centerpoint in that region. You can develop a solution that uses this metadata to crop and scale the video. The centerpoint provides you with a reference point for the cropping and scaling algorithms that you develop. 

The centerpoint is identified using three pieces of data:
+  scale is a reference for calculating the positions as a percentage. 
+  X position is the position of the centerpoint on the X-axis, from the top left corner of the video frame. Always a positive number. 
+ Y position is the position of the centerpoint on the Y-axis, from the top left corner of the video frame. Always a positive number.

You can use this data to calculate the centerpoint pixel position in output video of any resolution. The formulas for finding the centerpoint are:

(*X position*) x width of output video / *scale*

(*Y position*) x height of output video / *scale*

**Example 1**

For example, if the output video is 1920 x 1080, then the following applies to the first piece of data in the metadata example:
+ The X pixel position is 2176 x 1920 / 10000 = pixel 417.792 or 418 rounded up
+ The Y pixel position is 6250 x 1080 / 10000 = pixel 675 

**Example 2**

Or if the output video is 1280 x 720, then the following applies:
+ The X pixel position is 2176 x 1280 / 10000 = pixel 278.528 or 279 rounded up
+ The Y pixel position is 6250 x 720 / 10000= pixel 450

### Metadata for graphic composition
<a name="query-metadata-smart-crop-graphics"></a>

When you configure graphic composition on a smart crop output (see [Configuring smart crop](create-feed-outputs.md#create-feed-console-smart-crop)), the smart crop metadata includes a `graphics` list in addition to the crop `centerPoint`. The list contains one entry for each template group that Elemental Inference evaluated for the frame.

Each graphic reports whether it is present in the frame. When `isPresent` is `true`, the entry also includes the bounding box that locates the graphic within the frame. When `isPresent` is `false`, Elemental Inference omits the position and size fields.

The following table describes the fields in each graphic composition entry.


| Field | Always present | Description | 
| --- | --- | --- | 
| name | Yes | The name of the template group. This matches the name you configured, so that you can identify which graphic was detected. | 
| isPresent | Yes | Whether the graphic was detected in this frame. When this value is false, the position and size fields are omitted. | 
| xPosition | No | The X position of the top-left corner of the bounding box, measured from the top-left corner of the video frame and normalized against scale. Always a positive number. | 
| yPosition | No | The Y position of the top-left corner of the bounding box, measured from the top-left corner of the video frame and normalized against scale. Always a positive number. | 
| width | No | The width of the bounding box, as a fraction of the frame width, normalized against scale. | 
| height | No | The height of the bounding box, as a fraction of the frame height, normalized against scale. | 
| scale | No | The reference value used to normalize the position and size fields, so that you can calculate them as a percentage of the frame dimensions. | 

The following example shows smart crop metadata in which Elemental Inference detected a scoreboard graphic:

```
{
    "metadata": {
        "smartCropping": {
            "crop": {
                "centerPoint": {
                    "scale": 10000,
                    "xPosition": 2176,
                    "yPosition": 6250
                }
            },
            "graphics": [
                {
                    "name": "scoreboard",
                    "isPresent": true,
                    "xPosition": 1602,
                    "yPosition": 1201,
                    "width": 2250,
                    "height": 1264,
                    "scale": 10000
                }
            ]
        }
    },
    "pts": 0,
    "timecode": null
}
```

Use the returned `name` to identify the graphic and to look up the action that your downstream encoder or application must take for it. Use the bounding box to locate the graphic within the frame.

`xPosition` and `yPosition` give the top-left corner of the bounding box. You calculate pixel values from the normalized values by multiplying by the output video dimension and dividing by `scale`. For an output video that is *W* pixels wide and *H* pixels high:
+ Left edge (pixels) = *xPosition* x *W* / *scale*
+ Top edge (pixels) = *yPosition* x *H* / *scale*
+ Width (pixels) = *width* x *W* / *scale*, and height (pixels) = *height* x *H* / *scale*

## Metadata for smart subtitles
<a name="query-metadata-smart-subtitles"></a>

For smart subtitles, Elemental Inference returns the metadata as a TTML (Timed Text Markup Language) document encapsulated in the JSON response. The TTML contains the transcribed text with timing information that corresponds to the requested time range.

The following `awscurl` command shows how to query for smart subtitles metadata:

```
# Query the first 5 seconds of subtitles metadata
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "subtitles", "timeSpecification": { "ptsBased": { "startPts": 0, "endPts": 5000, "timescale": 1000 }}, "parameters": { "subtitling": { "format": "TTML" }}}'
```

The response contains a TTML document with subtitle cues timed to the requested range. Each subtitle cue includes a start time, end time, and the transcribed text.

### Using the metadata
<a name="query-metadata-smart-subtitles-usage"></a>

The TTML subtitles returned by Elemental Inference can be used in the following ways:
+ Embed the subtitles directly into your video player as a subtitle track.
+ Convert the TTML to other subtitle formats such as WebVTT or SRT for compatibility with different players and platforms.
+ Use the timed text for downstream processing such as search indexing or content analysis.

## Querying contextual metadata
<a name="query-metadata-contextual"></a>

For contextual metadata, Elemental Inference returns content classifications that include IAB Content Taxonomy v3.1 category IDs and GARM brand safety ratings. The response contains one item for each shot and each scene that overlaps the requested time range, ordered by presentation timestamp (PTS).

The following `awscurl` command shows how to query for contextual metadata. The `parameters` field is required, and must contain a `contextualMetadata` object that matches the type of the output that you name in `outputName`.

```
# Query contextual metadata
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "contextual-metadata", "timeSpecification": { "ptsBased": { "startPts": 0, "endPts": 5000, "timescale": 1000 }}, "parameters": { "contextualMetadata": {}}}'
```

The response contains contextual classification results. The following example shows one shot-level item and one scene-level item, for a feed that has summary generation enabled, so the items include the `summary` field:

```
{
  "items": [
    {
      "pts": 1800,
      "metadata": {
        "contextualMetadata": {
          "type": "SHOT",
          "startPts": 1800,
          "domain": "Sports",
          "iabTaxonomy": {
            "version": "V3_1",
            "categories": [
              {"uniqueId": "547", "path": ["Sports", "Basketball"]}
            ]
          },
          "garm": {
            "suitability": {
              "categories": [
                {"category": "ARMS_AMMUNITION", "flagged": false},
                {"category": "CRIME_HARMFUL_ACTS", "flagged": false},
                {"category": "DRUGS_ALCOHOL_TOBACCO", "flagged": false},
                {"category": "ADULT_EXPLICIT", "flagged": false}
              ]
            }
          },
          "objects": ["basketball", "hoop", "scoreboard"],
          "actions": ["jumping", "rebounding"],
          "summary": "Two players contest a rebound under the basket."
        }
      }
    },
    {
      "pts": 1800,
      "metadata": {
        "contextualMetadata": {
          "type": "SCENE",
          "startPts": 1710,
          "domain": "Sports",
          "iabTaxonomy": {
            "version": "V3_1",
            "categories": [
              {"uniqueId": "547", "path": ["Sports", "Basketball"]},
              {"uniqueId": "640", "path": ["Entertainment", "Television"]}
            ]
          },
          "garm": {
            "suitability": {
              "categories": [
                {"category": "ARMS_AMMUNITION", "flagged": false},
                {"category": "CRIME_HARMFUL_ACTS", "flagged": false},
                {"category": "DRUGS_ALCOHOL_TOBACCO", "flagged": true, "risk": "LOW"},
                {"category": "ADULT_EXPLICIT", "flagged": false}
              ]
            }
          },
          "objects": ["basketball", "hoop", "scoreboard", "arena signage"],
          "actions": ["jumping", "rebounding", "cheering"],
          "summary": "A close fourth-quarter sequence, with a beer commercial visible on the arena signage."
        }
      }
    }
  ]
}
```

**Note**  
The preceding example shows a subset of the GARM categories. Elemental Inference returns a result for each of the GARM categories.

### Using the metadata
<a name="query-metadata-contextual-usage"></a>

Contextual metadata provides content classifications that you can use for contextual ad targeting. The response contains the following structure:
+ `pts` – The presentation timestamp of the metadata item, in the timebase of the media.
+ `timecode` – The timecode of the metadata item, when the source media carries timecode information.
+ **contextualMetadata** – The top-level object containing classification results.
  + `type` – The granularity of the classification. `SHOT` for a single continuous camera take, or `SCENE` for a group of related consecutive shots. Elemental Inference returns both shot-level and scene-level items for a time range, so a shot item and the scene item that contains it can both appear in the response.
  + `startPts` – The presentation timestamp at which the shot or scene begins. For a scene, this value can be earlier than the `pts` of the item and earlier than the start of the requested time range.
  + `domain` – The high-level content category of the video, such as `Sports`, `News`, or `Entertainment`.
  + **iabTaxonomy** – IAB Content Taxonomy classifications. This field is omitted when Elemental Inference does not match any category.
    + `version` – The taxonomy version used (currently `V3_1`).
    + `categories` – An array of matched content categories. Each category includes:
      + `path` – The hierarchical category path (for example, `["Sports", "Basketball"]`).
      + `uniqueId` – The IAB taxonomy unique identifier for the category.
  + **garm** – GARM (Global Alliance for Responsible Media) brand safety classifications.
    + `suitability` – Brand suitability assessment.
      + `categories` – An array of GARM brand safety categories. Each category includes:
        + `category` – The GARM category name (for example, `ARMS_AMMUNITION`, `HATE_SPEECH`, `ADULT_EXPLICIT`).
        + `flagged` – Whether the content is flagged for this category (`true` or `false`).
        + `risk` – The risk level for the category (`FLOOR`, `HIGH`, `MEDIUM`, or `LOW`). Elemental Inference includes this field only when `flagged` is `true`.
  + `objects` – Labels for the notable objects that Elemental Inference detects in the shot or scene, such as `basketball` or `scoreboard`. For a scene, the list is the union of the labels from the shots in the scene. Elemental Inference omits this field when it detects no objects.
  + `actions` – Labels for the notable actions that Elemental Inference detects in the shot or scene, such as `jumping` or `cheering`. For a scene, the list is the union of the labels from the shots in the scene. Elemental Inference omits this field when it detects no actions.
  + `summary` – A short natural-language description of what happens in the shot or scene. Elemental Inference returns this field only when the output is configured with `summaryGeneration` set to `ENABLED`. For more information, see [Configuring contextual metadata](create-feed-outputs.md#create-feed-console-contextual-metadata).

The 11 GARM brand safety categories are: `ARMS_AMMUNITION`, `CRIME_HARMFUL_ACTS`, `DEATH_INJURY_MILITARY`, `ONLINE_PIRACY`, `HATE_SPEECH`, `OBSCENITY`, `DRUGS_ALCOHOL_TOBACCO`, `SPAM_MALWARE`, `TERRORISM`, `DEBATED_SENSITIVE`, and `ADULT_EXPLICIT`.

#### Integration with AWS Elemental MediaTailor
<a name="query-metadata-contextual-emt-integration"></a>

You can integrate Elemental Inference contextual metadata with AWS Elemental MediaTailor to enrich ad requests with content classifications. Your ad-decision server can then target ads based on what is happening in the content.

This integration uses a MediaTailor Function of type `AWS_SERVICE_REQUEST` to call the Elemental Inference `GetMetadata` API during ad breaks. AWS Elemental MediaLive decorates SCTE-35 markers with Elemental Inference query parameters, and MediaTailor parses these markers to construct authenticated requests to Elemental Inference.

##### How it works
<a name="query-metadata-contextual-emt-flow"></a>

1. Elemental Inference analyzes your content and produces shot-level and scene-level IAB Content Taxonomy and GARM brand safety classifications.

1. AWS Elemental MediaLive decorates SCTE-35 ad break markers with Elemental Inference query parameters (feed endpoint, region, and timing information).

1. At each ad break, MediaTailor triggers the configured Function, which sends an authenticated request to `GetMetadata` to retrieve classifications for the content window.

1. The Function output expressions extract IAB and GARM signals and pass them to the ad-decision server.

##### Prerequisites
<a name="query-metadata-contextual-emt-prerequisites"></a>

Before you configure this integration, you need the following:
+ An Elemental Inference feed with a contextual metadata output enabled.
+ A resource-based policy on the feed that grants MediaTailor permission to call `GetMetadata`. For more information, see [Managing feed policies](feed-policies.md).
+ An AWS Elemental MediaLive channel with contextual metadata enrichment enabled and associated with the feed.

##### Configuring MediaTailor
<a name="query-metadata-contextual-emt-configure"></a>

For complete instructions on creating the `AWS_SERVICE_REQUEST` Function, attaching it to a playback configuration, and configuring output expressions, see [Contextual ad targeting with Elemental Inference](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-elemental-inference-integration.html) in the *AWS Elemental MediaTailor User Guide*.

If the `GetMetadata` request fails or times out, MediaTailor proceeds with the ad request without contextual metadata. The ad-decision server falls back to its default targeting logic.