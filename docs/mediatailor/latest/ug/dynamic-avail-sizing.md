

# Dynamic avail sizing

Dynamic avail sizing (DAS) reduces how much slate or unpersonalized avail content viewers see when an ad avail underfills in a live HLS stream. *Unpersonalized avail content* is the avail's original content from the origin. The *underfill* is the part of an avail that MediaTailor can't fill with ads. When the content reserve can cover the underfill, MediaTailor *shortens* the avail by omitting the underfill, so that programming resumes earlier.

**Topics**
+ [How dynamic avail sizing works](das-how-it-works.md)
+ [Configuring dynamic avail sizing](das-enable.md)
+ [Examples](das-examples.md)
+ [Feature interactions](das-feature-interactions.md)
+ [Monitoring dynamic avail sizing](das-monitoring.md)