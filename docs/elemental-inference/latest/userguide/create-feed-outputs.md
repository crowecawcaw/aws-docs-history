# Configuring each feature

Following are details about how to configure each feature (output) that you
include in a Elemental Inference feed.

## Configuring event clipping

In **Callback config**, you can enter a string that you want
Elemental Inference to always include in the event clipping metadata for this output. This
information is useful when you later work with Elemental Inference events in Amazon EventBridge. You
will be able to filter events using this information, in order to find the
events for one feed. The string might identify the sports event in the feed, for
example.

## Configuring smart crop

There is no specific configuration for smart crop.
