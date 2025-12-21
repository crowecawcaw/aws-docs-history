# Example mission profile configurations

The examples provided show how to take a public broadcast satellite and create a mission
profile that supports it. The resulting templates are provided to help you take a public
broadcast satellite contact and to help you make decisions about your satellites.

###### Topics

- [JPSS-1 - Public broadcast satellite (PBS) -
  Evaluation](#examples.pbs-definition "#examples.pbs-definition")
- [Public broadcast satellite utilizing Amazon S3 data delivery](examples.md "examples.md")
- [Public broadcast satellite utilizing a dataflow endpoint (narrowband)](examples.md "examples.md")
- [Public broadcast satellite utilizing a dataflow endpoint (demodulated and decoded)](examples.md "examples.md")
- [Public broadcast satellite utilizing AWS Ground Station Agent (wideband)](examples.md "examples.md")

## JPSS-1 - Public broadcast satellite (PBS) -

Evaluation

This example section matches the [Customer onboarding process overview](getting-started.md#customer-onboarding-process "getting-started.md#customer-onboarding-process"). It provides a brief compatibility analysis
with AWS Ground Station and sets the stage for the specific examples that follow.

As mentioned in the
[Public broadcast satellites](getting-started.md#public-broadcast-satellites "getting-started.md#public-broadcast-satellites")
section, you can utilize select satellites, or communication paths of a satellite, that are
publicly available. In this section we describe [JPSS-1](https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system "https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system") in the AWS Ground Station terms. For reference, we utilize the [Joint Polar Satellite System 1 (JPSS-1) Spacecraft High Rate Data (HRD) to Direct Broadcast
Stations (DBS) Radio Frequency (RF) Interface Control Document (ICD)](https://www.nesdis.noaa.gov/s3/2022-03/JPSS-1SCHRDtoDBSRFICDRevA-470-REF-00184February9,2015.pdf "https://www.nesdis.noaa.gov/s3/2022-03/JPSS-1SCHRDtoDBSRFICDRevA-470-REF-00184February9,2015.pdf") to complete the example. Also, worth noting that JPSS-1 is associated to the NORAD ID 43013.

The JPSS-1 satellite offers one uplink and three direct downlink communication paths, as seen
in Figure 1-1 of the ICD. Of these four communication paths, only the single High Rate Data
(HRD) downlink communication path is available for public consumption. Based on this, you'll
see this path will have much more specific data associated with it as well. The four paths are
as follows:

- Command path (uplink) at 2067.27 MHz center frequency with a data rate of 2-128 kbps.
  This path is not publicly accessible.
- Telemetry path (downlink) at 2247.5 MHz center frequency with a data rate of 1-524
  kbps. This path is not publicly accessible.
- SMD path (downlink) at 26.7034 GHz center frequency with a data rate of 150-300 Mbps.
  This path is not publicly accessible.
- The RF for the HRD path (downlink) at 7812 MHz center frequency with a data rate of
  15 Mbps. It has a 30 MHz bandwidth, and is right-hand-circular-polarized. When you onboard
  JPSS-1 with AWS Ground Station, this is the communication path you get access to. This communication
  path contains instrument science data, instrument engineering data, instrument telemetry
  data, and real-time spacecraft housekeeping data.

As we compare the potential data paths, we see that the command (uplink), telemetry
(downlink), and HRD (downlink) paths meet the frequency, bandwidth, and multi-channel
concurrent use capabilities of AWS Ground Station.
The SMD path is not compatible as the center frequency is out of range of the existing
receivers.
For more information about the supported capabilities, see
[AWS Ground Station Site Capabilities](locations.md "locations.md").

###### Note

As the SMD path is not compatible with AWS Ground Station it will not be represented in the example
configurations.

###### Note

As the command (uplink) and telemetry (downlink) paths are not defined in the ICD, nor
are they available for public use, the values provided when used are notional.
