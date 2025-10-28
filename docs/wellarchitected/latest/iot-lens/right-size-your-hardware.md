# Right-size your hardware

The choices made in hardware component selection can greatly
influence the operational phase impact of devices and therefore
must be carefully considered. The use case should dictate the
required CPU/MCU, peripherals and communication modules on the
device.  When choosing the processor, amount of RAM, and amount
of flash storage, the designer must focus on resource
optimization; over-provisioning hardware can lead to choosing a
processor that has a large power draw but stays mostly idle or
has an excess of memory that never gets used, increasing the
overall carbon footprint of the device unnecessarily.
Under-sizing hardware can lead to long execution times or a lack
of extensibility necessary to insure the longevity of the
device.

Your design will typically fall into one of three broad classes
of devices – Microcontroller (MCU) class devices, Microprocessor
(MPU) class devices, and devices that use hardware acceleration
for machine learning use cases (which we refer to as "Inference
class" devices).
