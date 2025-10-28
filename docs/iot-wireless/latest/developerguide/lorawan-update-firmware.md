# Update gateway firmware using CUPS service

with AWS IoT Core for LoRaWAN

The [LoRa Basics Station](https://doc.sm.tc/station/ "https://doc.sm.tc/station/") software that
runs on your gateway provides credential management and firmware update interface using
the Configuration and Update Server (CUPS) protocol. The CUPS protocol is an efficient
mechanism that provides secure firmware update delivery with ECDSA signatures. It
enables over-the-air (OTA) firmware updates, allowing you to remotely manage and upgrade
the software on your LoRaWAN gateways without physically accessing them.

You'll have to frequently update your gateway's firmware. You can use the CUPS service
with AWS IoT Core for LoRaWAN to provide firmware updates to the gateway where the updates can also
be signed. To update the gateway's firmware, you can use the SDK, CLI, or the console.
With CUPS, you can upload the firmware file to an Amazon Simple Storage Service bucket, sign them with a
private key, and schedule the updates to be delivered to your gateways with
AWS IoT Core for LoRaWAN.

## Pre-requisites

Before you can update the firmware of your LoRaWAN gateway, your gateway must have
established a CUPS connection to the cloud. If you had previously connected your
gateway, verify that your gateway is still connected before updating the gateway
firmware. For information about onboarding and connecting your LoRaWAN gateway to
AWS IoT Core for LoRaWAN, see [Onboard your gateways to
AWS IoT Core for LoRaWAN](lorawan-onboard-gateways.md "lorawan-onboard-gateways.md").

## Firmware update process

The firmware update process involves the following steps.

1. Upload the firmware file to an Amazon Simple Storage Service (S3) bucket.
2. Generate a signature key pair and sign the firmware update file with the
   private key.

###### Note

To perform this step, make sure that the private key is present in the
gateway. 3. Schedule the firmware update job, specifying the signed firmware file, the
devices to be updated, and other configuration options.

The firmware update is then securely delivered to the targeted gateways using the
CUPS protocol. If the update was signed, the gateways can then verify the
authenticity and integrity of the update using the provided signature, which ensures
a secure and reliable firmware update process.

The update process takes about 45 minutes to complete. It can take longer if
you're setting up your gateway for the first time to connect to
AWS IoT Core for LoRaWAN.

Gateway manufacturers usually provide their own firmware update files and
signatures so you can use that for the firmware update. If you don't have the
firmware update files, see [(Optional) Generate the firmware
update file and signature](lorawan-script-fwupdate-sigkey.md "lorawan-script-fwupdate-sigkey.md") for an example that you can use
to adapt to your application.

- If you're using the AWS Management Console to schedule and run the firmware update,
  proceed to [Schedule and run gateway firmware
  update task](lorawan-schedule-firmware-update.md "lorawan-schedule-firmware-update.md").
- If you're using the AWS CLI to schedule and run the firmware update, first
  proceed to [Upload the firmware file to an
  Amazon S3 bucket and add an IAM role](lorawan-upload-firmware-s3bucket.md "lorawan-upload-firmware-s3bucket.md") to upload your
  firmware file to Amazon S3 and grant AWS IoT Core for LoRaWAN permissions to access the file
  on your behalf.

###### To perform your gateway's firmware update:

- [(Optional) Generate the firmware
  update file and signature](lorawan-script-fwupdate-sigkey.md "lorawan-script-fwupdate-sigkey.md")
- [Upload the firmware file to an
  Amazon S3 bucket and add an IAM role](lorawan-upload-firmware-s3bucket.md "lorawan-upload-firmware-s3bucket.md")
- [Schedule and run gateway firmware
  update task](lorawan-schedule-firmware-update.md "lorawan-schedule-firmware-update.md")
