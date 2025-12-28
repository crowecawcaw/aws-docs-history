# Check the Power LED on the Atlas 3.0. NSK

AWS Outposts supports two versions of NSK: Atlas 2.0 and Atlas 3.0. Both NSK versions have a RGB
**Status** LED. In addition, the Atlas 3.0 has a green
**Power** LED. This step is only for the Atlas 3.0 NSK.

The following image shows the location of the LEDs on the Atlas 2.0 and Atlas 3.0
NSKs:

![An image of the Atlas 2.0 and 3.0 NSKs with the RGB Status LED on each NSK and the green Power LED on the Atlas 3.0.](/images/outposts/latest/install-server/images/nsk-led-status.png)
If you have the Atlas 2.0 NSK, skip to the next step, [Step 5: Connect your Outposts server to your network](install-network.md "install-network.md") because this version of the NSK only has the RGB Status
LED which you must check after the Outposts server is provisioned and activated.

If you have the Atlas 3.0 NSK, check the green Power LED:

- If the green light is on, the NSK is correctly connected to the host and has power.
  You can proceed to the next step.
- If the green light is off, the NSK is not correctly connected to the host or/and has
  no power. Contact Support.
