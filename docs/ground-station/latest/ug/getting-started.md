# Create configs

By this step you have identified the satellite, the communication paths, and the IAM, Amazon EC2,
and Amazon S3 resources as needed. In this step you will create AWS Ground Station
_configs_ that store their respective parameters.

## Data delivery configs

The first configs to create relate to where and how you want data delivered. Using the
information from the previous step you will construct many of the following configuration
types.

- **[Amazon S3 Recording Config](how-it-works.md#how-it-works.config-s3-recording "how-it-works.md#how-it-works.config-s3-recording")** - Deliver data to your Amazon S3 bucket.
- **[Dataflow Endpoint Config](how-it-works.md#how-it-works.core-config-dfe "how-it-works.md#how-it-works.core-config-dfe")** - Deliver data to your Amazon EC2 instance.

## Satellite configs

The satellite configs relate how AWS Ground Station can communicate with your satellite. You will reference
the information you gathered in [Onboard satellite](getting-started.md "getting-started.md").

- **[Tracking Config](how-it-works.md#how-it-works.config-tracking "how-it-works.md#how-it-works.config-tracking")** - Sets preference for how your vehicle is physically tracked during a contact. This is required for mission profile construction.
- **[Antenna Downlink Config](how-it-works.md#how-it-works.config-antenna-downlink "how-it-works.md#how-it-works.config-antenna-downlink")** - Deliver digitized radio frequency data.
- **[Antenna Downlink Demod
  Decode Config](how-it-works.md#how-it-works.config-antenna-downlink-demod-decode "how-it-works.md#how-it-works.config-antenna-downlink-demod-decode")** - Deliver demodulated and decoded radio frequency data.
- **[Antenna Uplink Config](how-it-works.md#how-it-works.config-antenna-uplink "how-it-works.md#how-it-works.config-antenna-uplink")** - Uplink data to your satellite.
- **[Antenna Uplink Echo Config](how-it-works.md#how-it-works.config-antenna-uplink-echo "how-it-works.md#how-it-works.config-antenna-uplink-echo")** - Deliver an echo of your uplink signal data.
