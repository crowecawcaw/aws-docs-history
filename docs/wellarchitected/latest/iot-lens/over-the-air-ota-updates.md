# Over-the-air (OTA) updates

OTA updates enable IoT devices to receive and install software
or configuration updates without the need for physical access
to the devices.  This mechanism is supported across a variety
of embedded operating systems, including embedded Linux and
FreeRTOS, and can be powered by
the [AWS IoT Jobs](../../../iot/latest/developerguide/iot-jobs.md "../../../iot/latest/developerguide/iot-jobs.md") agent and cloud service .

The OTA update mechanism for IoT devices must be resilient,
reliable, and secure in order to help prevent a failed update
from requiring a truck roll to fix the device. There are
several techniques that device makers can use to build a
resilient OTA mechanism.

OTA updates may encounter errors or failures during the update
process, such as network errors, data corruption, or other
issues. The device's firmware should have error handling and
recovery mechanisms in place to detect and recover from
potential errors, such as checksum verification, error
correction codes (ECC), redundancy, or other suitable
techniques to support data integrity and reliability.

Atomic updates are updates that are either fully applied or
fully rolled back, without leaving the system in an
inconsistent state. This can be achieved by storing a new
version of the firmware on an inactive partition and then
swapping it with the active firmware partition upon successful
completion.  This approach also supports safe roll-back in
case the new firmware encounters errors.

Once an OTA update is installed and running correctly, the
device must help prevent it from being rolled back to a
previous vulnerable version. This can be achieved through
mechanisms such as secure bootloaders, cryptographic
signatures, or other techniques that help prevent the device
from reverting to older, potentially less secure
firmware/software versions.

OTA updates can also be used for certificate rotation when
there is a security incident or to renew an expiring
certificate. A certificate rotation mechanism extends the
device's lifetime without the need to use long-lived
certificates and allows the device to benefit from
improvements in security algorithms and ciphers that might not
have been available at the time the device was manufactured.  

Devices on networks such as LoRaWAN and NB-IoT face additional
challenges. These networks are constrained in bandwidth,
making OTA updates power inefficient for large file transfers.
Sending large files over the air is also problematic for
battery-powered devices connected to more power-hungry Wi-Fi
and cellular networks.   To overcome this issue, instead of
sending the entire firmware image to a device, send only the
portions of the image that have actually changed, reducing
communication and processing required, and reducing power
consumption. 
The [Delta
Over the Air Updates](https://www.freertos.org/2022/01/delta-over-the-air-updates.html "https://www.freertos.org/2022/01/delta-over-the-air-updates.html") feature supported by FreeRTOS uses
this approach.
