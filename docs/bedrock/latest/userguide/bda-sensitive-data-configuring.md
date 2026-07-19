# Configuring sensitive data settings

You configure sensitive data settings within an Amazon Bedrock Data Automation (BDA) project.
For more information about creating a project, see [Bedrock Data Automation projects](bda-projects.md "bda-projects.md").

Specify the sensitive data settings for a project within
`overrideConfiguration`, which provides customized settings for each modality. The
following example enables PII for the audio and document modalities, enables video processing
without PII detection, and disables image processing entirely. Replace the values with your own
configuration.

```
"overrideConfiguration": {
    "audio": {
        "sensitiveDataConfiguration": {
            "detectionMode": "DETECTION_AND_REDACTION",
            "detectionScope": ["STANDARD", "CUSTOM"],
            "piiEntitiesConfiguration": {
                "piiEntityTypes": ["ALL"],
                "redactionMaskMode": "ENTITY_TYPE"
            }
        }
    },
    "video": {
        "modalityProcessing": {
            "state": "ENABLED"
        }
    },
    "image": {
        "modalityProcessing": {
            "state": "DISABLED"
        }
    },
    "document": {
        "modalityProcessing": {
            "state": "ENABLED"
        },
        "sensitiveDataConfiguration": {
            "detectionMode": "DETECTION",
            "detectionScope": ["STANDARD"],
            "piiEntitiesConfiguration": {
                "piiEntityTypes": ["NAME", "ADDRESS", "EMAIL"]
            }
        }
    }
}
```
