# How Elemental Live

works

From the point of view of Elemental Live, a live streaming workflow that includes Elemental Live involves three systems:

- An Elemental Live _event_, which ingests and transcodes source content.
- One or more _upstream systems_ that provide the _source content_ (the
  video) to Elemental Live.

Examples of an upstream system are a streaming camera or appliance that is directly connected to the internet, or a contribution encoder
that is located in a sports stadium where a sports event is being held.

The source content is in a specific package format and protocol. For example, the source content might be available as streaming HLS or
streaming TS (transport stream). The source content contains video, audio, and optional captions streams that are in specific codecs or
formats.

- One or more _downstream systems_ that are the destinations for the output that Elemental Live produces.

A typical downstream system consists of an origin service or a packager that is connected to Elemental Live, a content distribution network
(CDN) that is downstream of the origin service or the packager, and a playback device or website where the users view the content.
.
To create an Elemental Live workflow, you create an event. Broadly speaking this event contains two sets of configuration information:

- A list of inputs (sources) and information about how to ingest those sources.

- A list of output groups that specifying packaging and encoding information.
  To start processing the content, you start the event. When the event is running, it ingests the source content from the upstream system that is
  identified by the input. The event then transcodes that video (and the related audio, captions, and metadata) and creates outputs. Elemental Live
  sends the outputs to the specified downstream systems.
