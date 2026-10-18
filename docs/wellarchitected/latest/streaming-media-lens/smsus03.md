

# Encoding and delivery
<a name="smsus03"></a>

Every avoidable bit in an encode is multiplied across millions of viewing sessions in network transfer and client decode energy.


| SMSUS03: How do you optimize your streaming software and architecture for sustainability? | 
| --- | 
| [SMSUS03-BP01 Implement efficient encoding and delivery mechanisms](smsus03-bp01.md) | 

## Capability intent
<a name="smsus03-intent"></a>
+ Bit rate is allocated based on content complexity and measured viewing demand, not a fixed profile.
+ Renditions that are not requested are not produced or stored.
+ Codec and packaging choices are made per content tier, weighing compression gains against encode cost and device reach.
+ Lightweight delivery logic runs at the edge rather than generating origin round-trips.
+ Encoding efficiency is measured through resource proxies and reviewed regularly.

## Common issues to watch for
<a name="smsus03-issues"></a>
+ A single fixed bit rate ladder applied to all content regardless of complexity.
+ Pre-encoding every rendition for the full catalog, including titles that are rarely watched.
+ Adopting a newer codec across the whole catalog without confirming device decode support.
+ No measurement of bytes delivered per viewing session or encode compute per title.