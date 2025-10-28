# Bulk analysis output manifests

The bulk analysis job generates an output manifest file that contains the job results,
as well as a manifest summary which contains statistics and details on any errors when
processing the input manifest entries.

If duplicated entries were included in the input manifest, the job won’t attempt to
filter out unique inputs, and will instead process all provided entries.

The output manifest file is formatted as follows:

```
// Output manifest for content moderation
{"source-ref":"s3://foo/bar/1.jpg", "detect-moderation-labels": {"ModerationLabels":[],"ModerationModelVersion":"7.0","ContentTypes":[{"Confidence":72.7257,"Name":"Animated"}]}}
```

The output manifest summary is formatted as follows:

```
{
    "version": "1.0",                # Schema version, 1.0 for GA.
    "statistics": {
        "total-json-lines": Number,  # Total number json lines (images) in the input manifest.
        "valid-json-lines": Number,  # Total number of JSON Lines (images) that contain references to valid images.
        "invalid-json-lines": Number # Total number of invalid JSON Lines. These lines were not handled.
    },
    "errors": [
        {
            "line-numer": Number,   # The number of the line in the manifest where the error occured.
            "source-ref": "String", # Optional. Name of the file if was parsed.
            "code": "String",       # Error code.
            "message": "String"     # Description of the error.
        }
     ]
}
```
