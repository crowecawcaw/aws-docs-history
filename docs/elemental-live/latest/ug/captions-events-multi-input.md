# Captions in events with

multiple inputs

If your event includes multiple inputs, these rules apply to
Elemental Live handling of captions:

- The captions formats in one input can be different from the
  captions formats in another input. For example, 608 embedded
  captions might be in one input and teletext might be in
  another.
- There is no requirement for all the inputs to have captions that
  are capable of producing the specified captions in any given output.

If the captions from an input cannot produce the specified
captions in one of the outputs, the captions will be omitted for the
course of that input. The event will not fail. When the event
switches to a different input, the captions will be included again
if the captions from that input can produce the specified captions
in that output.
