# AWS IoT secure tunneling tutorials

AWS IoT secure tunneling helps customers establish bidirectional communication to remote
devices that are behind a firewall over a secure connection managed by AWS IoT.

To demo AWS IoT secure tunneling, use our [AWS IoT secure tunneling
demo on GitHub](https://github.com/aws-samples/iot-secure-tunneling-demo "https://github.com/aws-samples/iot-secure-tunneling-demo").

The following tutorials will help you learn how to get started and use secure tunneling.
You'll learn how to:

1. Create a secure tunnel using the quick setup and manual setup methods for
   accessing the remote device.
2. Configure the local proxy when using the manual setup method and connect to the
   tunnel to access the destination device.
3. SSH into the remote device from a browser without having to configure the local
   proxy.
4. Convert a tunnel created using the AWS CLI or using the manual setup method to use the
   quick setup method.

## Tutorials in this section

The tutorials in this section focus on creating a tunnel using the AWS Management Console and the
AWS IoT API Reference. In the AWS IoT console, you can create a tunnel from the [Tunnels
hub](https://console.aws.amazon.com/iot/home#/tunnels "https://console.aws.amazon.com/iot/home#/tunnels") page or from the details page of a thing that you created. For more information,
see [Tunnel creation methods in AWS IoT console](secure-tunneling-tutorial-open-tunnel.md#tunneling-tutorial-flows "secure-tunneling-tutorial-open-tunnel.md#tunneling-tutorial-flows").

Following shows the tutorials in this section:

- ###### [Open a tunnel and use browser-based
  SSH to access remote device](tunneling-tutorial-quick-setup.md "tunneling-tutorial-quick-setup.md")

This tutorial shows how to open a tunnel from the [Tunnels
hub](https://console.aws.amazon.com/iot/home#/tunnels "https://console.aws.amazon.com/iot/home#/tunnels") page using the quick setup method. You'll also learn how to use browser-based SSH to access the remote device
using an in-context command line interface within the AWS IoT console.

- ###### [Open a tunnel using manual setup and
  connect to remote device](tunneling-tutorial-manual-setup.md "tunneling-tutorial-manual-setup.md")

This tutorial shows how to open a tunnel from the [Tunnels
hub](https://console.aws.amazon.com/iot/home#/tunnels "https://console.aws.amazon.com/iot/home#/tunnels") page using the manual setup method. You'll also learn how to configure and start the local proxy
from a terminal in your source device and connect to the tunnel.

- ###### [Open a tunnel for remote device and
  use browser-based SSH](tunneling-tutorial-existing-tunnel.md "tunneling-tutorial-existing-tunnel.md")

This tutorial shows how to open a tunnel from the details page of a thing that you created. You'll learn
how to create a new tunnel and use an existing tunnel. The existing tunnel corresponds to the most recent, open tunnel
that was created for the device. You can also use the browser-based SSH to access the remote device.

###### AWS IoT secure tunneling tutorials

- [Open a tunnel and start
  SSH session to remote device](secure-tunneling-tutorial-open-tunnel.md "secure-tunneling-tutorial-open-tunnel.md")
- [Open a tunnel for remote device and
  use browser-based SSH](tunneling-tutorial-existing-tunnel.md "tunneling-tutorial-existing-tunnel.md")
