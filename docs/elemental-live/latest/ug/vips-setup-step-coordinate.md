# Step 1: Coordinate with the POIS operator

Talk to the POIS operator, and agree on the values for this
data:

- The label for each input. This value must be identical, and it is
  case sensitive.
- The acquisition ID for the Elemental Live node. The POIS must have a
  different acquisition ID for each Elemental Live node that it works
  with.
- The zone ID for the specific event.

The combination of acquisition ID and zone ID must be unique in the
Elemental Live event.

- The URL for the signal conditioner endpoint on the POIS. This
  endpoint handles the input switching communications with
  Elemental Live.
- The URL for the alternate signal conditioner endpoint on the POIS, if
  this exists.
- The preroll that is the number of seconds between when Elemental Live
  receives the request from the POIS and when Elemental Live inserts any
  SCTE-35 messages in the content. This preroll isn't required if the
  messages that the POIS sends include a start time for the input
  switch,
  Make a note of all of this data. You will need it to set up on Elemental Live.
