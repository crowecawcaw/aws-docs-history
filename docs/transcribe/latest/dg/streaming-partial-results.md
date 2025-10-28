# Streaming and partial results

Because streaming works in real time, transcripts are produced in
_partial results_. Amazon Transcribe breaks up the incoming audio stream
based on natural speech segments, such as a change in speaker or a pause in the audio. The
transcription is returned to your application in a stream of transcription events, with each response
containing more transcribed speech until an entire segment is transcribed.

An approximation of this is shown in the following code block. You can view this process in
action by signing into the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/"),
selecting **Real-time transcription**, and speaking into your microphone. Watch
the **Transcription output** pane as you speak.

In this example, each line is the partial result of an audio segment.

```
The
The Amazon.
The Amazon is
The Amazon is the law.
The Amazon is the largest
The Amazon is the largest ray
The Amazon is the largest rain for
The Amazon is the largest rainforest.
The Amazon is the largest rainforest on the
The Amazon is the largest rainforest on the planet.
```

These partial results are present in your transcription output within the
[`Results`](../APIReference/API_streaming_Result.md "../APIReference/API_streaming_Result.md") objects. Also in this
object block is an **IsPartial** field. If this field is true, your transcription
segment is not yet complete. You can view the difference between an incomplete and a
complete segment below:

```
`"IsPartial": true (incomplete segment)`

"Transcript": "The Amazon is the largest rainforest."

"EndTime": 4.545,
"IsPartial": true,
"ResultId": "12345a67-8bc9-0de1-2f34-a5b678c90d12",
"StartTime": 0.025


`"IsPartial": false (complete segment)`

"Transcript": "The Amazon is the largest rainforest on the planet."

"EndTime": 6.025,
"IsPartial": false,
"ResultId": "34567e89-0fa1-2bc3-4d56-78e90123456f",
"StartTime": 0.025
```

Each word within a _complete_ segment has an associated confidence
score, which is a value between `0` and `1`. A larger value indicates a
greater likelihood that the word is correctly transcribed.

###### Tip

The `StartTime` and `EndTime` of an audio segment can be
used to synchronize transcription output with video dialogue.

If you're running an application that requires low latency, you may want to use
[partial-result stabilization](#streaming-partial-result-stabilization "#streaming-partial-result-stabilization").

## Partial-result stabilization

Amazon Transcribe starts returning transcription results as soon as you start streaming your
audio. It returns these partial results incrementally until it generates a finished result at the level
of a natural speech segment. A natural speech segment is continuous speech that contains a
pause or a change in speaker.

Amazon Transcribe continues outputting partial results until it generates the final
transcription result for a speech segment. Because speech recognition may revise words as it
gains more context, streaming transcriptions can change slightly with each new partial result
output.

This process gives you two options for each speech segment:

- Wait for the finished segment
- Use the segment's partial results

Partial result stabilization changes how Amazon Transcribe produces the final
transcription result for each complete segment. When activated, only the last few words from the
partial results can change. Because of this, transcription accuracy may be affected. However,
your transcript is returned faster than without partial-results stabilization. This reduction in latency
may be beneficial when subtitling videos or generating captions for live streams.

The following examples show how the same audio stream is handled when partial-results
stabilization is not activated and when it is. Note that you can set the stability level
to low, medium, or high. Low stability provides the highest accuracy. High stability
transcribes faster, but with slightly lower accuracy.

| "Transcript":                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | "EndTime":                                                                            | "IsPartial":                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Partial-result stabilization not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                       | `The The The Amazon. The Amazon is The Amazon is the law. The Amazon is the largest The Amazon is the largest ray The Amazon is the largest rain for The Amazon is the largest rainforest. The Amazon is the largest rainforest on the The Amazon is the largest rainforest on the planet. The Amazon is the largest rainforest on the planet. The Amazon is the largest rainforest on the planet.` | `0.545 1.045 1.545 2.045 2.545 3.045 3.545 4.045 4.545 5.045 5.545 6.025 6.025`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `true true true true true true true true true true true true false`                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                       | Partial-result stabilization enabled (high stability)                                                                                                                                                                                                                                                                                                                                               |
| `The The The Amazon. The Amazon is The Amazon is the large The Amazon is the largest The Amazon is the largest rainfall. The Amazon is the largest rain forest. The Amazon is the largest rain forest on The Amazon is the largest rain forest on the planet. The Amazon is the largest rain forest on the planet. The Amazon is the largest rain forest on the planet. The Amazon is the largest rain forest on the planet. The Amazon is the largest rain forest on the planet.` | `0.515 1.015 1.515 2.015 2.515 3.015 3.515 4.015 4.515 5.015 5.515 6.015 6.335 6.335` | `true true true true true true true true true true true true true false`                                                                                                                                                                                                                                                                                                                            | When you activate partial-result stabilization, Amazon Transcribe uses a `Stable` field to indicate whether an item is stable, where 'item' refers to a transcribed word or punctuation mark. Values for `Stable` are `true` or `false`. Items flagged as `false` (not stable) are more likely to change as your segment is transcribed. Conversely, items flagged as `true` (stable) won't change. You can choose to render non-stable words so your captions align with speech. Even if captions change slightly as context is added, this is a better user experience than periodic text bursts, which may or may not align with speech. You can also choose to display non-stable words in a different format, such as italics, to indicate to viewers that these words may change. Displaying partial results limits the amount of text displayed at a given time. This can be important when you're dealing with space constraints, as with video captions. ###### Dive deeper with the AWS Machine Learning Blog To learn more about improving accuracy with real-time transcriptions, see: <br>• [Improve the streaming transcription experience with Amazon Transcribe partial results stabilization](https://aws.amazon.com/blogs/machine-learning/amazon-transcribe-now-supports-partial-results-stabilization-for-streaming-audio/ "https://aws.amazon.com/blogs/machine-learning/amazon-transcribe-now-supports-partial-results-stabilization-for-streaming-audio/") <br>• [“What was that?” Increasing subtitle accuracy for live broadcasts using Amazon Transcribe](https://aws.amazon.com/blogs/media/what-was-that-increasing-subtitle-accuracy-for-live-broadcasts-using-amazon-transcribe/ "https://aws.amazon.com/blogs/media/what-was-that-increasing-subtitle-accuracy-for-live-broadcasts-using-amazon-transcribe/") ### Partial-result stabilization example output The following example output shows `Stable` flags for an incomplete segment (`"IsPartial": true`). You can see that the words "_to_" and "_Amazon_" are not stable and therefore could change before the segment is finalized. `"Transcript": { "Results": [ { "Alternatives": [ { "Items": [ { "Content": "Welcome", "EndTime": 2.4225, "Stable": true, "StartTime": 1.65, "Type": "pronunciation", "VocabularyFilterMatch": false }, { "Content": "to", "EndTime": 2.8325, "Stable": false, "StartTime": 2.4225, "Type": "pronunciation", "VocabularyFilterMatch": false }, { "Content": "Amazon", "EndTime": 3.635, "Stable": false, "StartTime": 2.8325, "Type": "pronunciation", "VocabularyFilterMatch": false }, { "Content": ".", "EndTime": 3.635, "Stable": false, "StartTime": 3.635, "Type": "punctuation", "VocabularyFilterMatch": false } ], "Transcript": "Welcome to Amazon." } ], "EndTime": 4.165, "IsPartial": true, "ResultId": "12345a67-8bc9-0de1-2f34-a5b678c90d12", "StartTime": 1.65 } ] }` |
