# Overview

The POIS must be set up with the following information:

- A tag for the Elemental Live input. Each input must be unique in the
  Elemental Live event.
- The acquisition point ID and zone for the Elemental Live event.
  In Elemental Live, you set up the event with the following
  information:

- Acquisition point ID. This ID is how the POIS identifies the
  Elemental Live node. The POIS provides you with this ID.
- Zone. This ID is how the POIS identifies the specific event. The POIS
  provides you with this ID.
- These two fields set up Elemental Live and the POIS to have a common identifier for the
  event.
  In the event, you set up the inputs with the following
  information:

- Input ID. This is the standard ID that Elemental Live generates and
  assigns when you save an event.
- The URL for the input.
- Label. This tag has the same value as the label (in Elemental Live).
  In this way, both Elemental Live and the POIS have a common identifier for
  each input.
- A virtual tag. This identifies the input as one that the POIS knows
  about. Typically, you set up all the inputs in an event as virtual.

## Number of nodes and number of POIS

- Each Elemental Live node can communicate with only one POIS. All the
  events on the Elemental Live node must be configured for the same
  POIS.
- One POIS can communicate with several Elemental Live nodes. The POIS
  uses the POIS AcquisitionPointID and ZoneID parameter to uniquely
  identify each Elemental Live node.

## Number and type of inputs

With asynchronous input switching, the inputs can be any of the
following:

- Programs in one MPTS. You can set up a maximum of 11
  programs.
- Any type of input that Elemental Live considers to be a file input.
  See [Supported upstream systems
  for file inputs](supported-inputs-file-types.md "supported-inputs-file-types.md").

There is no limit to the number of inputs of this type.

With SCTE-35-triggered input switching, the inputs can be any of the
following:

- Programs in one MPTS. You can set up a maximum of 11
  programs.
