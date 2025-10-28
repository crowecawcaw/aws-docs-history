# Archive

procedure

You enable or disable passthrough at the output level: only in
outputs that have an MPEG-2 TS container.

1. In the Profile or Event screen, go to the Output Groups section at the bottom
   of the screen and display the tab for Archive Output Group.
2. In the output that has the MPEG-2 TS container, open the PID Control section.
   Complete the following fields:
   - SCTE-35: Click to
     select.
   - SCTE-35 PID: Enter the ID of the PID where you want the SCTE-35 messages
     to go.

###### Result

All SCTE-35 messages from the input are included in the data stream of this
output.
