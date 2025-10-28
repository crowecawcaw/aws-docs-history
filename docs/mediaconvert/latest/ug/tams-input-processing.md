# How MediaConvert processes TAMS content

When you submit a job with TAMS inputs, MediaConvert automatically handles the complexity of
retrieving and processing your content. MediaConvert constructs the proper API endpoints by
appending paths like `/sources/{sourceId}` and
`/flows/{flowId}/segments` to your base TAMS server URL.

MediaConvert first connects to your TAMS server and retrieves information about the specified source. The source must be a multi-format source that contains references to individual flows. MediaConvert then discovers all flows associated with the source and automatically selects the highest quality flows based on bitrate, resolution, and other quality metrics.

For content with separate audio and video flows, MediaConvert selects the highest bitrate video flow and the highest bitrate audio flow. For content with combined audio-video flows, MediaConvert selects the highest quality multi flow. If a selected flow contains no segments, MediaConvert automatically attempts to retrieve segments from parent flows when available.

During processing, MediaConvert generates HLS manifests for the content and applies your specified gap handling approach. Finally, MediaConvert calculates precise clipping parameters to ensure your output contains exactly the content within your specified time range.

###### Note

MediaConvert processes segments in the order they appear in the TAMS server response and maintains timing accuracy throughout the workflow.
