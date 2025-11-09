#

Troubleshoot contacts that received no data

It is possible for a contact to appear successful, but still did not receive any data. This may
mean that you receive PCAP files that are empty, or no PCAP files at all if you are using S3
data delivery. This can happen for a number of reasons. The following discusses some of the
causes, and how to address them.

##

Incorrect downlink config

Each contact that receives data from a satellite will have an associated
[Antenna Downlink Config](how-it-works.md#how-it-works.config-antenna-downlink "how-it-works.md#how-it-works.config-antenna-downlink")
or [Antenna Downlink Demod
Decode Config](how-it-works.md#how-it-works.config-antenna-downlink-demod-decode "how-it-works.md#how-it-works.config-antenna-downlink-demod-decode") . If the configuration
specified does not agree with the signal being transmitted by a satellite, AWS Ground Station will not be
able to receive the transmitted signal. This will result in no data being received by AWS Ground Station.

To fix this, please verify that the configs you are using agree with the signal being
transmitted by your satellite. For example, verify that you've set the correct center
frequency, bandwidth, polarization, and if needed, demodulation and decoding parameters.

##

Satellite maneuver

There are times that a satellite may perform a maneuver which temporarily disables some of its
communication systems. The maneuver may also significantly change the location of the
satellite in the sky. AWS Ground Station will not be able to receive a signal from a satellite that is not
transmitting a signal, or if the ephemeris being used causes the AWS Ground Station antenna to point at a
location in the sky where the satellite is not present.

If you are trying to communicate with a public broadcast satellite operated by NOAA, you may
be able to find a message describing an outage or maneuver on the NOAA
[Satellite Alert Messages](https://www.ospo.noaa.gov/Operations/messages.html "https://www.ospo.noaa.gov/Operations/messages.html") page. The message may include a timeline of when data transmission is expected to
resume, or this may be posted in a subsequent message.

If you are communicating with your own satellites, it's your responsibility to understand your
satellite operations, and how this might impact communicating with AWS Ground Station. If you are
performing a maneuver that will impact the satellite trajectory, this may include providing
updated custom ephemeris data. For more information on providing custom ephemeris data, see
[Understand how AWS Ground Station uses ephemerides](ephemeris.md "ephemeris.md").

## AWS Ground Station outage

If AWS Ground Station causes a contact to fail, or cancels it, AWS Ground Station will set the contact status
to _AWS_FAILED_, or _AWS_CANCELLED_. For more
information on contact lifecycle, see
[Understand contact lifecycle](contacts.md "contacts.md"). In some cases, AWS Ground Station
may have a failure that prevents data from being delivered to your account, but doesn't result
in the contact being in an _AWS_FAILED_ or
_AWS_CANCELLED_ status. When this happens, AWS Ground Station should post an
account-specific event to your AWS Health dashboard. For more information about the AWS
Health dashboard, see
[AWS Health User Guide](../../../health/latest/ug.md "../../../health/latest/ug.md") .
