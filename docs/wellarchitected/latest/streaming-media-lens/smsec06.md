

# Data protection
<a name="smsec06"></a>

High-value content requires protection through Digital Rights Management (DRM) and encryption. The protection scheme must balance security requirements with device coverage and operational complexity.


| SMSEC06: How do you protect content at-rest and in-transit to avoid unauthorized distribution? | 
| --- | 
| [SMSEC06-BP01 Collaborate with business and legal stakeholders to align on content protection requirements](smsec06-bp01.md) | 
| [SMSEC06-BP02 Select a content protection scheme that meets business objectives](smsec06-bp02.md) | 

## Capability intent
<a name="smsec06-intent"></a>
+ Content protection requirements are defined collaboratively with business and legal stakeholders.
+ The protection scheme meets licensing obligations across all target devices.
+ Architecture supports multiple DRM systems where device coverage requires it.
+ Protection decisions are revisited as content agreements and supported devices change.

## Common issues to watch for
<a name="smsec06-issues"></a>
+ DRM implemented without consulting legal on contractual requirements.
+ Single DRM chosen based on familiarity rather than device coverage analysis.
+ Keys stored alongside content rather than in a separate key management service.
+ Protection requirements never revisited as licensing agreements change.