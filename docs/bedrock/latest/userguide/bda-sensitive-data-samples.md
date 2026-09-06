

# Sensitive data detection and redaction sample outputs
<a name="bda-sensitive-data-samples"></a>

The following examples show excerpts of sensitive data detection and redaction for standard outputs. For the complete response format, see [InvokeDataAutomationAsync](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_InvokeDataAutomationAsync.html) in the API Reference.

## Document
<a name="bda-sensitive-data-sample-document"></a>

The following example shows redacted standard output for a document.

```
{
    "id": "5e9cc636-73be-4264-9284-e178da9d094a",
    "text": "- Full Name: [PII]",
    "confidence": 0.0099853515625,
    "reading_order": 2,
    "page_index": 0,
    "locations": [
        {
            "page_index": 0,
            "bounding_box": {
                "left": 0.08195127630357191,
                "top": 0.11714535522460938,
                "width": 0.28159839146295634,
                "height": 0.012292622884114576
            }
        }
    ]
},
{
    "id": "b84ee8f7-6081-45ff-a5a6-da61db7928a5",
    "text": "- Social Security Number: [PII]",
    "confidence": 0.0099853515625,
    "reading_order": 3,
    "page_index": 0,
    "locations": [
        {
            "page_index": 0,
            "bounding_box": {
                "left": 0.08195658199122695,
                "top": 0.13631119791666665,
                "width": 0.33843516892045605,
                "height": 0.015145751953125008
            }
        }
    ]
},
```

## Audio
<a name="bda-sensitive-data-sample-audio"></a>

The following example shows the standard output before redaction, with the detected entity identified.

```
"audio_segments": [{
    "start_timestamp_millis": 133190,
    "end_timestamp_millis": 136410,
    "segment_index": 7,
    "type": "TRANSCRIPT",
    "text": "Hi, my name is Mary Major.",
    "audio_item_indices": [389, 390, 391, 392, 393, 394, 395, 396],
    "language": "EN",
    "sensitive_data_detection": [{
        "index": 0,
        "entity_type": "NAME",
        "content": "Mary Major",
        "audio_item_indices": [394, 395],
        "start_timestamp_millis": 135540,
        "end_timestamp_millis": 136380,
        "start_character_offset": 15,
        "end_character_offset": 25
    }]
}]
```

The following example shows the same standard output after redaction.

```
"audio_segments": [{
    "start_timestamp_millis": 133190,
    "end_timestamp_millis": 136410,
    "segment_index": 7,
    "type": "TRANSCRIPT",
    "text": "Hi, my name is [NAME].",
    "audio_item_indices": [389, 390, 391, 392, 393, 394, 395, 396],
    "language": "EN",
    "sensitive_data_detection": [{
        "index": 0,
        "entity_type": "NAME",
        "content": "[NAME]",
        "audio_item_indices": [394, 395],
        "start_timestamp_millis": 135540,
        "end_timestamp_millis": 136380,
        "start_character_offset": 15,
        "end_character_offset": 21
    }]
}]
```

## Image
<a name="bda-sensitive-data-sample-image"></a>

The following example shows redacted standard output for an image.

```
"image": {
    "summary": "This image shows an illustration of two individuals engaged in a conversation. [NAME], wearing an orange shirt, is gesturing with her hand while speaking. [NAME], dressed in a blue shirt, is listening to her.",
    "sensitive_data_detection": {
        "image": {
            "summary": [{
                "id": 0,
                "sensitive_data_type": "PII",
                "entity_type": "NAME",
                "content": "[NAME]",
                "start_character_offset": 79,
                "end_character_offset": 85
            }, {
                "id": 1,
                "sensitive_data_type": "PII",
                "entity_type": "NAME",
                "content": "[NAME]",
                "start_character_offset": 155,
                "end_character_offset": 161
            }],
            "text_words": [],
            "text_lines": []
        }
    }
}
```

The following examples show sensitive data detection and redaction for custom outputs.

## Custom output
<a name="bda-sensitive-data-sample-custom"></a>

The following example shows the custom output before redaction, with the detected entities identified.

```
"blueprint_sensitive_data_detection": {
    "call_summary": {
        "value": "This is a podcast episode featuring Mary Major and John Stiles discussing various topics including Turkish soap operas, childhood lies, and John's career. No specific caller-agent interaction is present.",
        "sensitive_data_detection": [{
            "index": 0,
            "entity_type": "NAME",
            "content": "Mary Major",
            "start_character_offset": 36,
            "end_character_offset": 46
        }, {
            "index": 1,
            "entity_type": "NAME",
            "content": "John Stiles",
            "start_character_offset": 51,
            "end_character_offset": 62
        }, {
            "index": 2,
            "entity_type": "NAME",
            "content": "John",
            "start_character_offset": 140,
            "end_character_offset": 144
        }]
    }
}
```

The following example shows the same custom output after redaction.

```
"blueprint_sensitive_data_detection": {
    "call_summary": {
        "value": "This is a podcast episode featuring [NAME] and [NAME] discussing various topics including Turkish soap operas, childhood lies, and [NAME]'s career. No specific caller-agent interaction is present.",
        "sensitive_data_detection": [{
            "index": 0,
            "entity_type": "NAME",
            "content": "[NAME]",
            "start_character_offset": 36,
            "end_character_offset": 42
        }, {
            "index": 1,
            "entity_type": "NAME",
            "content": "[NAME]",
            "start_character_offset": 47,
            "end_character_offset": 53
        }, {
            "index": 2,
            "entity_type": "NAME",
            "content": "[NAME]",
            "start_character_offset": 131,
            "end_character_offset": 137
        }]
    }
}
```