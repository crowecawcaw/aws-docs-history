# Apple HLS

passthrough procedure

Passthrough is enabled or disabled individually for each output, which means it can
be applied differently for different outputs in the same group.

1. If you have not already set up for manifest decoration, do so now; see [Procedure to enable
   manifest decoration](manifest-decoration.md#procedure-to-enable-decoration "manifest-decoration.md#procedure-to-enable-decoration").
2. In the Profile or Event screen, go to the Output Groups section at the bottom
   of the screen and display the tab for **Apple HLS Output
   Group**.
   1. In each output, open the PID Control section. You
      will note that the SCTE-35 field is automatically
      selected
      (because you set up for manifest decoration) and you
      cannot
      clear
      it .
   2. Complete the following field:
      - SCTE-35 PID field: Enter the ID of the PID where you want the
        SCTE-35 messages to go.

###### Result

All SCTE-35 messages from the input are included in the data stream of the
relevant output.
