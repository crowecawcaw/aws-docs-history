

# Troubleshooting ambient documentation
<a name="al-troubleshooting"></a>

**Topics**
+ [Session start and configuration](#al-troubleshooting-session-start)
+ [Streaming](#al-troubleshooting-streaming)

## Session start and configuration
<a name="al-troubleshooting-session-start"></a>

The following errors can occur when you start a session or configure its inputs.


| Error | Likely cause | What to do | 
| --- | --- | --- | 
|  `ValidationException` (HTTP 400) | An input violated a limit — an unsupported character in `unstructuredContext` or a `sectionInstruction`, encounter context over its 20 KB limit, a section instruction over its 15 KB limit, more than 20 section instructions, a non-alphanumeric `sectionHeader`, or `PHYSICAL_SOAP` used as a custom `templateType`. | Validate every input against the character pattern and size limits before you send. Check the section count (1–20) and section headers (alphanumeric only). Use `PHYSICAL_SOAP` only as a managed template. | 
|  `AccessDeniedException` (HTTP 401) | Missing or invalid credentials, or the caller lacks permission. | Ensure the caller is granted the `health-agent:StartMedicalScribeListeningSession` action and that credentials are valid. | 
|  `ResourceNotFoundException` (HTTP 404) | The domain, subscription, or session referenced doesn’t exist. | Verify the domain ID, subscription ID, and session ID are correct and active. | 
|  `ServiceQuotaExceededException` (HTTP 402) | The request exceeds a service quota. | Review your service quotas for the service. To request an increase, open the Service Quotas console or create a case in the AWS Support Center. | 
|  `ThrottlingException` (HTTP 429) | You exceeded the allowed request rate. | Back off and retry with exponential backoff. | 
|  `InternalServerException` (HTTP 500) | A transient service-side error. | Retry the request. | 

## Streaming
<a name="al-troubleshooting-streaming"></a>

The following symptoms can occur while a session is streaming audio. `InvalidSignatureException` is the most common failure — check it first if a stream terminates unexpectedly.


| Symptom | Likely cause | What to do | 
| --- | --- | --- | 
|  `InvalidSignatureException` and the stream terminates under load | Audio is being delivered in large bursts, so signed messages back up in the buffer and their signatures expire (older than 5 minutes) before they’re read. | Reduce to \~1 second of audio per message and lower the chunk size to ≤ 30,720 bytes. Pace sends at \~500–1000 ms. This is the most common streaming failure — check it first. | 
| A single audio event is rejected | The chunk exceeded the 32,000-byte maximum. | Split audio on 30,720-byte boundaries. | 
| The presigned WebSocket URL is rejected | The presigned URL expired. | WebSocket presigned URLs allow `X-Amz-Expires` up to 60 seconds; connect promptly after generating the URL. | 
| Long silences don’t produce output | Expected — the note is generated from the conversation. | Ensure audio is actually flowing and that channels are defined correctly. | 