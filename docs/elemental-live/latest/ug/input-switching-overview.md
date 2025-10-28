# Input switching

You can configure an Elemental Live event with multiple inputs, and then
implement an input switching mechanism to switch from ingesting one of those
inputs to ingesting another.

There are several ways to set up for input switching.

## Dynamic input switching

The dynamic input switching feature lets use REST API commands to switch
inputs in an event. This input switching feature has two key
characteristics:

- The switching control (the REST API) is built into Elemental Live. You
  don't need an external server to control switching.
- You can optionally modify the playlist of inputs without stopping the
  event. This ability to dynamically change at runtime the playlist is
  particularly useful when you can't identify in advance (before starting the
  For more information about dynamic input switching, see [Dynamic input
  switching](dynamic-content-switching.md "dynamic-content-switching.md").

## Virtual input switching

The virtual input switching feature lets you set up so that a POIS
controls switching from one input to another. This feature has these key
switching methods:

- Virtual input switching via SCTE-35 messages

This type of input switching works with SCTE-35 messages that are in
the input. We also refer to this switching as SCTE-35-triggered input
switching.

Virtual input switching via asynchronous ESAM messages that the POIS
sends.

This type of input switching is based only on decisions from the POIS.
It doesn't rely on messages that are in the input. We also refer to this
switching as asynchronous input switching.

For more information about virtual input switching, see [Virtual input switching](feature-vips.md "feature-vips.md").

## Automatic input switching

This type of switching is applicable when an event contains file inputs
that aren't set up to loop.

If Elemental Live gets to the end of a file input that isn't set up to
loop, then Elemental Live switches to the next input in the list of inputs in
the event.

We don't recommend relying on automatic switching.

## Combining different input switching features

We strongly recommend against implementing a combination of these input
switching features. You shouldn't give control of the input switching logic
to both a POIS and a REST-based application. There should be only one
mechanism controlling the input switching.
