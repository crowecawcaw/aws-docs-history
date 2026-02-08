Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Troubleshooting Wi-Fi gateway

detection

When you add a gateway to your project or site, as soon as you choose
**Add gateway** the Amazon Monitron mobile app starts scanning to find
it. If the mobile app can't find the gateway, try the following troubleshooting
tips.

![Smartphone connected to AWS service via Bluetooth, represented by icons and symbols.](images/gs-gateway-bluetooth.png)

- **Make sure that the gateway is turned on.**
  Check the LED lights—the two small orange and blue lights next to the
  Amazon symbol on the top of the gateway. If they're on, the gateway has
  power. If the gateway has no power, check the following:
  - Is the power cord firmly attached to both the back of the gateway
    and the power outlet?
  - Is the power outlet functioning properly?
  - Is the gateway power cable working? To test this, try using the
    cable with another gateway.
  - Is the outlet where the cable plugs into the gateway clean, with
    no debris stuck inside? Be sure to check both the outlet in the
    gateway and the connecting end of the cable.

- **Make sure that the gateway is in commissioning
  mode.** The Amazon Monitron mobile app finds a new gateway only when it's
  in commissioning mode. When you turn a gateway on, the LED lights blink
  slowly, alternating orange and blue. When you press the button on the side
  of the gateway and enter commissioning mode, they blink rapidly, also
  alternating orange and blue. If the LEDs show any sequence other than slow
  blinking before you press the button, the gateway might not go into
  commissioning mode. In this case, perform a factory reset of the gateway by
  turning the power off, then pressing and holding down the commissioning
  button (located on the side) while you turn the power back on.

![Orange device with smiley face being touched by a finger, connected to a power source.](/images/Monitron/latest/user-guide/images/gs-gateway-turnon.png)

- **Make sure your smartphone's Bluetooth is
  working.** The gateway connects to your smartphone using
  Bluetooth.
  - Is you smartphone's Bluetooth on and working? Try switching it off
    and on. If that doesn't help, restart your phone and check
    again.
  - Are you within your smartphone's Bluetooth range? Bluetooth range
    is relatively short, usually less than 10 meters and its reliability
    can vary dramatically.
  - Is there anything that might be interfering electronically with
    the Bluetooth signal?

- **Make sure the gateway is not already commissioned to
  any of your projects.** The devide must be deleted from all
  existing projects before commissioning.
  If none of these actions resolves the issue, try the following:

- View and copy your gateway MAC address and get in touch with your IT
  admin. See [Retrieving MAC address details](mac-address-wifi-gateway.md "mac-address-wifi-gateway.md").
- Log out of the mobile app and restart it.
- Do a factory reset of the gateway by turning the power off, then pressing
  and holding down the commissioning button on the side while you turn the
  power back on.
