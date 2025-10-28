# UDP/TS

procedure

Passthrough is enabled or disabled individually for each output,
which means it can be applied differently for different outputs in
the same group.

###### To enable passthrough

1. In the Profile or Event screen, go to the Output Groups section at the bottom
   of the screen and display the tab for UDP/TS Output Group.
2. In the output where you want to pass through SCTE-35 messages, open the PID
   Control section. Complete the following fields:
   - SCTE-35: Click to
     select.
   - SCTE-35 PID: Enter the ID of the PID where you want the SCTE-35 messages
     to go.

###### Result

All SCTE-35 messages from the input are included in the data stream of the
relevant output.
