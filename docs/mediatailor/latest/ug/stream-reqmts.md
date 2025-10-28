# Input source requirements for MediaTailor ad insertion

A input source must meet the following requirements to work with MediaTailor:

- Use Apple HLS (HTTP Live Streaming) or MPEG DASH (Dynamic Adaptive Streaming over
  HTTP)
- Use live streaming or video on demand (VOD)
- Be accessible on the public internet and have a public IP address
- Use standard HTTP ports (port 80) or HTTPS ports (port 443). MediaTailor does not support
  custom ports for origin server communication.
- Contain ad markers in one of the formats described in the [Getting started with MediaTailor ad insertion
  tutorial](getting-started-ad-insertion.md#getting-started-prep-stream "getting-started-ad-insertion.md#getting-started-prep-stream")
