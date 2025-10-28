# Design the inputs

When you design a workflow that implements Elemental Live output
locking, you must obtain information about the sources.

###### Topics

- [Determine the
  resources](#opl-step-get-ready-resources "#opl-step-get-ready-resources")
- [Decide how to
  produce the sources](#opl-step-get-ready-produce-source "#opl-step-get-ready-produce-source")
- [Obtain information
  about the sources](#opl-step-get-ready-source-info "#opl-step-get-ready-source-info")

## Determine the

resources

Identify the number of sources, output encodes, and events that
you need.

**For output redundancy
workflows**

For output redundancy, you need two sources, two output encodes,
and two events. Each event uses one input and produces one output
encode.

**For distributed encoding
workflows**

For distributed encoding, calculate the numbers as follows:

- The number of output encodes: You need one output encode for
  each video rendition in the ABR stack.

- The number of events: Decide how many output encodes each Elemental Live appliance
  can handle, based on the density capabilities of the appliance. An appliance might be
  able to produce only one output encode if that encode is a 4K rendition. However, an
  appliance might be able to produce several lower-resolution output encodes
  (renditions).

When you know the number of appliances, you know the number of
events—one event per appliance.

- The number of sources: You need one source for each
  event.

## Decide how to

produce the sources

Decide how you will produce the sources:

- You might produce the streams for each event using a different
  contribution encoder for each event.
- Instead, you might produce the sources once, then use a video router upstream of
  Elemental Live to product identical streams.

Make sure that the [sources are
identical](output-locking-requirements.md#output-locking-input-requirements "output-locking-requirements.md#output-locking-input-requirements").

## Obtain information

about the sources

Obtain the following information:

- The characteristics of the video.
- The type of timecode that each source includes.
