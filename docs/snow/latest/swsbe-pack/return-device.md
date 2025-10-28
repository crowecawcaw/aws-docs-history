# Returning the device

The prepaid shipping label on the E Ink display contains the
correct address to return the Snowball Edge.

The device is delivered to an AWS sorting facility and forwarded
to the AWS data center. The carrier automatically reports back a tracking number for
your job to the AWS Snow Family Management Console. You can access that tracking number, and also a link to
the tracking website, by viewing the job's status details in the console, or by making
calls to the job management API.

###### Important

Unless personally instructed otherwise by AWS, never affix a separate shipping
label to the device. Always use the shipping label that is on the E Ink
display.

In addition, you can track the status changes of your job through the
AWS Snow Family Management Console. You can use Amazon SNS notifications if you selected that option during job
creation, or you can make calls to the job management API. For more information about
this API, see [AWS Snowball Edge API Reference](../../../snowball/latest/api-reference/api-reference.md "../../../snowball/latest/api-reference/api-reference.md").

The hardware security module must also be returned. Before returning it, decommission it to remove the cryptographic information used to secure it. See [Decomission the hardware security module](#decom-hsm "#decom-hsm"). Then, contact Support for instructions to return it.

## Decomission the hardware security module

1. Use secure shell to connect to the device.
2. Use the `/usr/safenet/lunaclient/bin/lunacm` command to access the device's command line utility. Then, use the `hsm login` command to log in to the device.
3. Use the `/usr/safenet/lunaclient/bin/lunacm` command to access the device's command line utility., Then, use the `hsm factoryRestore` command to restore the unit to default settings.
4. Use secure shell to connect to the device again.
5. Use the `ssh -i default_key ksadmin@HSM_IP` command to use the default key.
6. Use the `/usr/safenet/lunaclient/bin/lunacm` command to access the device's command line utility. Then, use the `hsm system factory-reset` to reset the device.

###### Important

The `system factory-reset` command totally wipes the hardware security module. After running the command, you will not be able to access any Snow devices bound to it and the data on them will be lost. 7. After the device is reset, power it off, disconnect cables, and remove it from the rack.

## Disconnecting the device

Disconnect the Snowball Edge cables. Secure the device's power cable into the
cable nook beneath the top door on the device.

Pull out and close the front and back doors. When they close completely, you hear
an audible click. When the return shipping label appears on the E Ink display on top
of the device, it's ready to be returned.
