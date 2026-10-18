

# Forensics
<a name="smsec03"></a>

When content is distributed without consent, forensic controls help trace leaked material back to its source. This covers watermarking and session-level traceability.


| SMSEC03: How do you monitor unauthorized re-distribution of your content? | 
| --- | 
| [SMSEC03-BP01 Implement content or sessions forensics](smsec03-bp01.md) | 

## Capability intent
<a name="smsec03-intent"></a>
+ Leaked content can be traced to the specific session or user that captured it.
+ Forensic watermarking is applied invisibly across all distribution channels.
+ A mapping between watermark identifiers and playback sessions is maintained.

## Common issues to watch for
<a name="smsec03-issues"></a>
+ No watermarking capability at all.
+ Single shared watermark ID rather than per-session identifiers.
+ Only visible watermarks without invisible forensic ones.
+ No active piracy monitoring to detect when leaked content surfaces.