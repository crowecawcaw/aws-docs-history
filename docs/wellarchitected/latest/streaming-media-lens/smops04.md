

# Operational procedures
<a name="smops04"></a>

Streaming systems are susceptible to encoding failures, delivery issues, and quality degradation. Documented, repeatable response procedures reduce resolution time and limit viewer impact during incidents.


| SMOPS04: How do you document and automate responses to operational events in your streaming video workflow? | 
| --- | 
| [SMOPS04-BP01 Create runbooks for common streaming video operational events](smops04-bp01.md) | 

## Capability intent
<a name="smops04-intent"></a>
+ Common operational events have documented runbooks with clear response steps.
+ Responses are consistent regardless of which operator is on call.
+ Resolution time is minimized through pre-approved actions and automation.

## Maturity levels
<a name="smops04-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Incident response depends on individual expertise. No runbooks or documented procedures exist. | 
| 2 | Emerging | Runbooks exist for some common scenarios but are incomplete or outdated. Response quality varies by operator. | 
| 3 | Defined | All common operational events have tested runbooks. Responses are consistent regardless of who is on call. | 
| 4 | Proactive | Routine recovery actions are automated. Runbooks are validated periodically through drills and updated after every incident. | 
| 5 | Optimized | Automation handles the majority of known failure modes. Humans focus on novel incidents, and post-incident analysis feeds back into procedure and automation improvements. | 

## Common issues to watch for
<a name="smops04-issues"></a>
+ Tribal knowledge as the primary incident response mechanism.
+ Runbooks that exist but are not tested or updated as the system evolves.
+ No automation of routine recovery actions that operators perform manually every time.