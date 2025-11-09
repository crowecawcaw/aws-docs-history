# Scope of blackout of SCTE-35

messages

All SCTE-35 messages that are “Other type” are blanked out as follows:

| SCTE-35 segmentation type | Blanking   |
| ------------------------- | ---------- |
| Programs                  | Always     |
| Chapters                  | Always     |
| Unscheduled events        | Always     |
| Network                   | See below. |

###### How Network End Blackout Differs from Other Events

Network end blackout is different from the other events that trigger a blackout
because:

- With Network, blanking starts when the "Network End" instruction is encountered
  and ends when the "Network Start" instruction is encountered.
- With other events, blanking starts when the “event start” instruction is
  encountered and ends when the “event end” instruction is encountered.
