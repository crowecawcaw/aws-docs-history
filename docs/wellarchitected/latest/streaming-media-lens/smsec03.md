

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

## Maturity levels
<a name="smsec03-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | No watermarking or session traceability. Leaked content can't be traced to a source. | 
| 2 | Emerging | Visible watermarks are applied but no invisible forensic marking exists. Traceability is limited to broad user cohorts. | 
| 3 | Defined | Invisible forensic watermarks are embedded per session with a maintained mapping between watermark IDs and playback sessions. | 
| 4 | Proactive | Active piracy monitoring scans for leaked content and correlates findings back to specific sessions using the forensic watermark database. | 
| 5 | Optimized | Full-path forensic tracing covers all distribution channels. Detection-to-action time is measured and continuously reduced through automation. | 

## Common issues to watch for
<a name="smsec03-issues"></a>
+ No watermarking capability at all.
+ Single shared watermark ID rather than per-session identifiers.
+ Only visible watermarks without invisible forensic ones.
+ No active piracy monitoring to detect when leaked content surfaces.