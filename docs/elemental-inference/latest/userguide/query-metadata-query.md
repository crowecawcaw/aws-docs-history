# Step D: Query the metadata

Use the Elemental Inference GetEndpoint operation to obtain the metadata that Elemental Inference
generates.

For example, the following CURL code shows how to use the POST command to query for
the metadata for the output named `testOutput`. The query is for the first
second of metadata. This one second span is identified by the start PTS of 0 and the end
PTS of 1001.

```
# Query the first second of metadata
$ awscurl --service "elemental-inference" --region <`region`> \
  -X POST 'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "testOutput", "timeSpecification": { "ptsBased":
//{ "startPts":0, "endPts": 1001, "timescale": 1000 } }, "parameters": {"smartCropping":
//{"frameRate": { "numerator": 24, "denominator": 1}}}}'
```

For information about the metadata returned for each feature, see the following
topics.

###### Topics

- [Metadata for smart crop](#query-metadata-smart-crop "#query-metadata-smart-crop")
- [Metadata for smart subtitles](#query-metadata-smart-subtitles "#query-metadata-smart-subtitles")

## Metadata for smart crop

The following CURL code shows the query command plus the results when the output
`testOutput` is a smart crop output.

```
# Query the first second of metadata
$ awscurl --service "elemental-inference" --region <`region`> \
  -X POST 'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/metadata' \
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

For smart crop, Elemental Inference identifies a _region of
interest_ in each frame. Elemental Inference then generates metadata that
identifies the centerpoint in that region. You can develop a solution that uses
this metadata to crop and scale the video. The centerpoint provides you with a
reference point for the cropping and scaling algorithms that you develop.

The centerpoint is identified using three pieces of data:

- scale is a reference for calculating the positions as a percentage.
- X position is the position of the centerpoint on the X-axis, from the
  top left corner of the video frame. Always a positive number.
- Y position is the position of the centerpoint on the Y-axis, from the
  top left corner of the video frame. Always a positive number.

You can use this data to calculate the centerpoint pixel position in output
video of any resolution. The formulas for finding the centerpoint are:

(_X position_) x width of output video /
_scale_

(_Y position_) x height of output video /
_scale_

**Example 1**

For example, if the output video is 1920 x 1080, then the following applies to
the first piece of data in the metadata example:

- The X pixel position is 2176 x 1920 / 10000 = pixel 417.792 or 418
  rounded up
- The Y pixel position is 6250 x 1080 / 10000 = pixel 675

**Example 2**

Or if the output video is 1280 x 720, then the following applies:

- The X pixel position is 2176 x 1280 / 10000 = pixel 278.528 or 279
  rounded up
- The Y pixel position is 6250 x 720 / 10000= pixel 450

## Metadata for smart subtitles

For smart subtitles, Elemental Inference returns the metadata as a TTML (Timed Text Markup
Language) document encapsulated in the JSON response. The TTML contains the
transcribed text with timing information that corresponds to the requested time
range.

The following `awscurl` command shows how to query for smart subtitles metadata:

```
# Query the first 5 seconds of subtitles metadata
$ awscurl --service "elemental-inference" --region <`region`> \
  -X POST 'https://<`data-endpoint`>/v1/feed/<`feed-id`>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "subtitles", "timeSpecification": { "ptsBased": { "startPts": 0, "endPts": 5000, "timescale": 1000 }}}'
```

The response contains a TTML document with subtitle cues timed to the requested
range. Each subtitle cue includes a start time, end time, and the transcribed
text.

### Using the metadata

The TTML subtitles returned by Elemental Inference can be used in the following
ways:

- Embed the subtitles directly into your video player as a subtitle
  track.
- Convert the TTML to other subtitle formats such as WebVTT or SRT for
  compatibility with different players and platforms.
- Use the timed text for downstream processing such as search indexing
  or content analysis.
