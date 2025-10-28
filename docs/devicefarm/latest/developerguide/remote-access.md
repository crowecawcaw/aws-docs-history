# Remote access in AWS Device Farm

Remote access allows you to swipe, gesture, and interact with a device through your web browser in real time
to test functionality and reproduce customer issues. You interact with a specific device by creating a remote
access session with that device.

A session in Device Farm is a real-time interaction with an actual, physical device hosted in a web browser. A session displays the single device you select when you start the session. A user can
start more than one session at a time with the total number of simultaneous devices limited by the number of
device slots you have. You can purchase device slots based on the device family (Android or iOS devices). For
more information, see [Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/ "https://aws.amazon.com/device-farm/pricing/").

Device Farm currently offers a subset of devices for remote access testing. New devices are added to the device pool
all the time.

Device Farm captures video of each remote access session and generates logs of activity during the session. These
results include any information you provide during a session.

###### Note

For security reasons, we recommend that you avoid providing or entering sensitive information, such as
account numbers, personal login information, and other details during a remote access session. If possible,
use alternatives developed specifically for testing, such as test accounts.

###### Topics

- [Creating a remote access session in AWS Device Farm](how-to-create-session.md "how-to-create-session.md")
- [Using a remote access session in AWS Device Farm](how-to-use-session.md "how-to-use-session.md")
- [Retrieving the results of a remote access session in AWS Device Farm](how-to-access-session-results.md "how-to-access-session-results.md")
