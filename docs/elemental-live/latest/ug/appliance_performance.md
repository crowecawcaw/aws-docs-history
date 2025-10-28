# Performance of Elemental Live appliances

This section looks at the factors that affect the performance of an
AWS Elemental Live appliance, with particular emphasis on the newest appliances.
It provides guidance about how to maximize
performance while achieving the preferred balance between density, speed, and
quality.

- **Density** is the number of output
  encodes or events that you can run on an appliance.

The density is affected by the following:

    + The capabilities of the appliance.
    + The compute demands of the individual events, especially the demands
     to achieve the desired video quality in the outputs.

- **Speed** is the rate at which the
  workflow content can be processed or transmitted. With live events, there
  must be enough compute power applied to achieve real-time ingest of the
  input and real-time encoding of the output.
- **Quality** refers primarily to the video
  quality.
  This section describes how to obtain the balance that suits your
  requirements.

###### Topics

- [Recommended testing
  procedure](performance-recommended-procedure.md "performance-recommended-procedure.md")
- [Recommendation: Continually
  upgrade Elemental Live](performance-recommended-upgrade.md "performance-recommended-upgrade.md")
- [Assessing performance by
  measuring](performance-measures.md "performance-measures.md")
- [Assessing performance with logging messages](performance-via-logs.md "performance-via-logs.md")
- [Encoding parameters that affect
  performance](performance-encoding-params.md "performance-encoding-params.md")
- [Features that affect
  performance](performance-features.md "performance-features.md")
