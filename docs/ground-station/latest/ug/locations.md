# AWS Ground Station site masks

Each AWS Ground Station [antenna location](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md") has associated site masks.
These masks block antennas at that location from transmitting or receiving when pointing in some directions,
typically close to the horizon. The masks may take into account:

- **Features of the geographic terrain surrounding the antenna** – For example,
  this includes things like mountains or buildings, that would block a radio frequency (RF) signal
  or prevent transmitting.
- **Radio Frequency Interference (RFI)** – This affects both the
  ability to receive (external RFI sources impacting a downlink signal into AWS Ground Station antennas)
  and transmit (the RF signal transmitted by AWS Ground Station antennas adversely impacting external receivers).
- **Legal authorizations** – Local site authorizations to operate AWS Ground Station
  in each region may include specific restrictions, such as a minimum elevation angle for transmitting.

These site masks may change over time. For example, new buildings could be constructed near an antenna location,
RFI sources may change, or legal authorization may be renewed with different restrictions.
The AWS Ground Station site masks are available to you under a non-disclosure agreement (NDA).

## Customer-specific masks

In addition to the AWS Ground Station site masks at each site, you may have additional masks
due to restrictions on your own legal authorization to communicate with your satellites in a given region.
Such masks can be configured in AWS Ground Station on a case-by-case basis to ensure compliance when using
AWS Ground Station to communicate with these satellites. Contact the AWS Ground Station team for details.

## Impact of site masks on available contact times

There are two kinds of site masks: uplink (transmit) site masks, and downlink (receive) site masks.

When listing available contact times using the ListContacts operation,
AWS Ground Station will return visibility times based on when your satellite will rise above and set below
the downlink mask. Available contact times are based on this downlink mask visibility window.
This ensures that you do not reserve time when your satellite is below the downlink mask.

Uplink site masks are _not_ applied to the available contact times, even if the Mission Profile includes an
[Antenna Uplink Config](how-it-works.md#how-it-works.config-antenna-uplink "how-it-works.md#how-it-works.config-antenna-uplink") in a dataflow edge. This allows you to use all available contact time
for downlink, even if uplink may not be available for portions of that time due to the uplink site mask.
However, the uplink signal may not be transmitted for some or all of the time reserved for a satellite contact.
You are responsible for accounting for the provided uplink mask when scheduling uplink transmissions.

The portion of a contact that is unavailable for uplink varies depending on the satellite trajectory during the contact,
relative to the uplink site mask at the antenna location. In regions where the uplink and downlink site masks are similar,
this duration will typically be short. In other regions, where the uplink mask may be considerably higher than the downlink site mask,
this could result in significant portions, or even all, of the contact duration being unavailable for uplink.
The full contact time is billed to you, even if portions of the reserved time are unavailable for uplink.
