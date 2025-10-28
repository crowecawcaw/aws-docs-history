# 2 Hardware

An AWS IoT ExpressLink qualified module is generally composed of the following elements:
(see block diagram)

- a module processor (MCU), that handles the AT command parser and manages the network
  connectivity protocols (ethernet, Wi-Fi, cellular)
- a minimum of six I/Os
- a pre-provisioned secure element or equivalent secure enclave that provides crypto
  hardware acceleration, random number generation and secure key storage
- a non-volatile memory that provides bulk storage sufficient to support the module's
  own over-the-air updates (OTA) and host processor OTA (HOTA)

## 2.1 Block diagram

![Figure 1 - Simplified block diagram](images/image1.png)

Figure 1 - Simplified block diagram

## 2.2 Pin definitions

`2.2.1`   GND (input) – Ground

`2.2.2`   VCC (input) – 3.3v

`2.2.3`   TXD (output) – Serial interface
Universal Asynchronous Receiver the Transmitter (UART) TX from module

UART output to the host processor/application processor.

`2.2.4`   RXD (input) – Serial interface
Universal Asynchronous Receiver the Transmitter (UART) RX to module

UART input to the ExpressLink, from the host processor/application processor.

`2.2.5`   RST (input) – holds module in reset

When asserted (low), the ExpressLink module is held in reset (low power,
disconnected, all queues emptied and error conditions cleared).

`2.2.6`   WAKE (input) – low-power sleep mode wakeup

When not asserted (high), the ExpressLink module is allowed to enter
a low power sleep mode. If in low power sleep mode and asserted (low),
this will awake the ExpressLink module.

`2.2.7`   Event (output) – Asynchronous Event Flag

When asserted, the ExpressLink module indicates to the host processor that
an event has occurred (disconnect error or message received on a subscribed topic)
and a notification is available in the event queue waiting to be delivered. It is
de-asserted when the event queue is emptied. A host processor can connect an
interrupt input to this signal (rising edge) or can poll the event queue at
regular intervals (see [8.2.1 EVENT?   »Request the next event in the queue«](elpg-event-handling.md#elpg-eventq-command "elpg-event-handling.md#elpg-eventq-command")).
