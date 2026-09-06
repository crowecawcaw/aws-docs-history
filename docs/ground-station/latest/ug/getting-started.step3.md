

# Create configs
<a name="getting-started.step3"></a>

 By this step you have identified the satellite, the communication paths, and the IAM, Amazon EC2, and Amazon S3 resources as needed. In this step you will create AWS Ground Station *configs* that store their respective parameters. 

## Data delivery configs
<a name="getting-started.step3.data-delivery-configs"></a>

 The first configs to create relate to where and how you want data delivered. Using the information from the previous step you will construct many of the following configuration types. 
+ **[Amazon S3 Recording Config](how-it-works.config.md#how-it-works.config-s3-recording)** - Deliver data to your Amazon S3 bucket.
+ **[Dataflow Endpoint Config](how-it-works.config.md#how-it-works.core-config-dfe)** - Deliver data to your Amazon EC2 instance.

## Telemetry config (optional)
<a name="getting-started.step3.telemetry-config"></a>

 If you want to receive near real-time telemetry during your contacts, you can create a TelemetrySinkConfig. This config is optional and specifies where AWS Ground Station will deliver telemetry data. 
+  **[Telemetry Sink Config](how-it-works.config.md#how-it-works.config-telemetry-sink)** - Deliver telemetry data to your account. 

 For detailed setup instructions, see [Set up telemetry](telemetry.setup.md). 

## Satellite configs
<a name="getting-started.step3.satellite-configs"></a>

 The satellite configs relate how AWS Ground Station can communicate with your satellite. You will reference the information you gathered in [Onboard satellite](getting-started.step1.md). 
+ **[Tracking Config](how-it-works.config.md#how-it-works.config-tracking)** - Sets preference for how your vehicle is physically tracked during a contact. This is required for mission profile construction.
+ **[Antenna Downlink Config](how-it-works.config.md#how-it-works.config-antenna-downlink)** - Deliver digitized radio frequency data.
+ **[Antenna Downlink Demod Decode Config](how-it-works.config.md#how-it-works.config-antenna-downlink-demod-decode)** - Deliver demodulated and decoded radio frequency data.
+ **[Antenna Uplink Config](how-it-works.config.md#how-it-works.config-antenna-uplink)** - Uplink data to your satellite.
+ **[Antenna Uplink Echo Config](how-it-works.config.md#how-it-works.config-antenna-uplink-echo)** - Deliver an echo of your uplink signal data.