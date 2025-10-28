# Example channel identification output (batch)

Here's an output example for a batch transcription with channel identification enabled.

```
{
    "jobName": "my-first-transcription-job",
    "accountId": "111122223333",
    "results": {
        "transcripts": [
            {
                "transcript": "I've been on hold for an hour. Sorry about that."
            }
        ],
        "channel_labels": {
            "channels": [
                {
                    "channel_label": "ch_0",
                    "items": [
                        {
                            "channel_label": "ch_0",
                            "start_time": "4.86",
                            "end_time": "5.01",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "I've"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "start_time": "5.01",
                            "end_time": "5.16",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "been"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "start_time": "5.16",
                            "end_time": "5.28",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "on"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "start_time": "5.28",
                            "end_time": "5.62",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "hold"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "start_time": "5.62",
                            "end_time": "5.83",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "for"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "start_time": "6.1",
                            "end_time": "6.25",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "an"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "start_time": "6.25",
                            "end_time": "6.87",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "hour"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_0",
                            "language_code": "en-US",
                            "alternatives": [
                                {
                                    "confidence": "0.0",
                                    "content": "."
                                }
                            ],
                            "type": "punctuation"
                        }
                    ]
                },
                {
                "channel_label": "ch_1",
                    "items": [
                        {
                            "channel_label": "ch_1",
                            "start_time": "8.5",
                            "end_time": "8.89",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "Sorry"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_1",
                            "start_time": "8.89",
                            "end_time": "9.06",
                            "alternatives": [
                                {
                                    "confidence": "0.9176",
                                    "content": "about"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_1",
                            "start_time": "9.06",
                            "end_time": "9.25",
                            "alternatives": [
                                {
                                    "confidence": "1.0",
                                    "content": "that"
                                }
                            ],
                            "type": "pronunciation"
                        },
                        {
                            "channel_label": "ch_1",
                            "alternatives": [
                                {
                                    "confidence": "0.0",
                                    "content": "."
                                }
                            ],
                            "type": "punctuation"
                        }
                    ]
                }
            ],
            "number_of_channels": 2
        },
        "items": [
            {
                "id": 0,
                "channel_label": "ch_0",
                "start_time": "4.86",
                "end_time": "5.01",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "I've"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 1,
                "channel_label": "ch_0",
                "start_time": "5.01",
                "end_time": "5.16",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "been"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 2,
                "channel_label": "ch_0",
                "start_time": "5.16",
                "end_time": "5.28",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "on"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 3,
                "channel_label": "ch_0",
                "start_time": "5.28",
                "end_time": "5.62",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "hold"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 4,
                "channel_label": "ch_0",
                "start_time": "5.62",
                "end_time": "5.83",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "for"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 5,
                "channel_label": "ch_0",
                "start_time": "6.1",
                "end_time": "6.25",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "an"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 6,
                "channel_label": "ch_0",
                "start_time": "6.25",
                "end_time": "6.87",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "hour"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 7,
                "channel_label": "ch_0",
                "alternatives": [
                    {
                        "confidence": "0.0",
                        "content": "."
                    }
                ],
                "type": "punctuation"
            },
            {
                "id": 8,
                "channel_label": "ch_1",
                "start_time": "8.5",
                "end_time": "8.89",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "Sorry"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 9,
                "channel_label": "ch_1",
                "start_time": "8.89",
                "end_time": "9.06",
                "alternatives": [
                    {
                        "confidence": "0.9176",
                        "content": "about"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 10,
                "channel_label": "ch_1",
                "start_time": "9.06",
                "end_time": "9.25",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "that"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "id": 11,
                "channel_label": "ch_1",
                "alternatives": [
                    {
                        "confidence": "0.0",
                        "content": "."
                    }
                ],
                "type": "punctuation"
            }
        ],
        "audio_segments": [
            {
                "id": 0,
                "transcript": "I've been on hold for an hour.",
                "start_time": "4.86",
                "end_time": "6.87",
                "channel_label": "ch_0",
                "items": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ]
            },
            {
                "id": 1,
                "transcript": "Sorry about that.",
                "start_time": "8.5",
                "end_time": "9.25",
                "channel_label": "ch_1",
                "items": [
                    8,
                    9,
                    10,
                    11
                ]
            }
        ]
    },
    "status": "COMPLETED"
}
```
