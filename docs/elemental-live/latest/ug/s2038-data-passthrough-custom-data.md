# Setting up the

event to pass through custom data

After you have enabled SMPTE 2038, you can identify the custom data
to extract, and then set up to include that data in your SMPTE 2110
outputs.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating an event.

###### To pass through custom data

1. Decide which custom data you want to pass through to the SMPTE
   2110 outputs. Make a note of the DID/SDID values.
2. On the Elemental Live web interface, display the details for
   the event that you want to set up.
3. In the **Input** section of the web
   interface, find the input that contains the SMPTE 2038. Find the
   **Add Custom DID/SDID Pair** button below the
   **Prefer SMPTE 2038** field. The button
   appears only if you selected the **Prefer**
   field.
4. Click the button and enter the appropriate values in the DID
   and SDID fields that appear. Repeat to add more pairs.
5. In the web interface, find the SMPTE 2110 output where you
   want to pass through the custom data. Find the ancillary output
   for that output. If you are not sure how to set up an ancillary
   output for SMPTE 2110, see [Step 3: Create SMPTE 2110 output group](config-output-2110.md "config-output-2110.md").
6. In the **Ancillary Data Settings** section,
   select **SMPTE 2038**.

Elemental Live will extract each custom data pair that you
identified in the input, convert it to a SMPTE 291 packet, and
include it in the ancillary data stream of the SMPTE 2110 output.
