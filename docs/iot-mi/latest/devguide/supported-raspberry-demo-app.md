# Managed integrations demo application

###### Note

This implementation of AWS IoT Hub SDK on Raspberry Pi is a demonstration project
intended for learning and testing purposes only and is not intended to be used in production environments.
For the purposes of this demo, set the following configurations for development ease:

**AWS credentials storage**: For demo purposes only, credentials and certificates are
stored in an accessible location for easier testing and development.
Production environments must use secure storage solutions like AWS Secrets Manager, or
Systems Manager Parameter Store. They must implement encryption at rest, and follow AWS IoT security guidelines.

**Container privileges**: The demo runs with elevated privileges to allow unrestricted access to host resources
and simplify development workflows. In production, containers should operate with minimal required privileges.

**Network bridge configuration**: The demo uses a network bridge configuration that exposes internal network traffic
for easier debugging and monitoring. In production environments, implement proper network isolation and segmentation to
prevent unauthorized access to internal network traffic.

**USB device permissions**: Unrestricted USB device access is enabled to facilitate easy
connection of development peripherals and testing devices. For production, implement strict USB device controls and validation to prevent device spoofing attacks.

These configurations enable straightforward testing and must notcbe used in production environments. When deploying to production,
please follow security best practices to prevent host system compromise and unauthorized access to credentials.

The demo application is a React-based demo application showcasing Managed integrations capabilities for smart home device management.
This application demonstrates device onboarding, control, and monitoring for Z-Wave and Zigbee devices through a modern web interface.

## Prerequisites

- [Sign up for an AWS account](setting-up.md#sign-up-for-aws "setting-up.md#sign-up-for-aws").
- [Create a credential locker](managedintegrations-sdk-v2-cookbook-ss.md#managedintegrations-sdk-v2-cookbook-credential-locker "managedintegrations-sdk-v2-cookbook-ss.md#managedintegrations-sdk-v2-cookbook-credential-locker")
  and

  [add the credential locker to your hub](managedintegrations-sdk-v2-cookbook-ss.md#managedintegrations-sdk-v2-cookbook-add-to-hub "managedintegrations-sdk-v2-cookbook-ss.md#managedintegrations-sdk-v2-cookbook-add-to-hub")
  .

- Complete
  [Hub onboarding setup](managedintegrations-sdk-v2-cookbook-hubsetup.md "managedintegrations-sdk-v2-cookbook-hubsetup.md").
- [Node.js 18+ and npm](https://nodejs.org/en/download "https://nodejs.org/en/download").
- Install the latest version of
  [AWS CLI from the Managed integrations AWS CLI Command Reference](../../../cli/latest/reference/iot-managed-integrations.md "../../../cli/latest/reference/iot-managed-integrations.md").
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Install and configure the Application

1. Download [Managed integrations demo application](https://d2no7dt1utuyzo.cloudfront.net/IotMI-HubSDK-DemoApp/1.0.0/IotMI-HubSDK-DemoApp-v1.0.0.tar.gz "https://d2no7dt1utuyzo.cloudfront.net/IotMI-HubSDK-DemoApp/1.0.0/IotMI-HubSDK-DemoApp-v1.0.0.tar.gz").
2. Extract the package:

```
cd ~/Downloads
tar -xzf IotMI-HubSDK-DemoApp-v1.0.0.tar.gz
cd IotManagedIntegrations-DemoApp
```

3. Install dependencies:

```
npm install
```

4. Create a `.env` file in the root directory:

```
# AWS Configuration
REACT_APP_AWS_REGION=your_region
REACT_APP_AWS_ACCESS_KEY_ID=your_access_key
REACT_APP_AWS_SECRET_ACCESS_KEY=your_secret_key
REACT_APP_AWS_SESSION_TOKEN=your_session_token

# IoT Managed Integrations Endpoint
REACT_APP_IOT_ENDPOINT=https://your-iot-endpoint.amazonaws.com

# Hub Configuration
REACT_APP_HUB_MANAGED_THING_ID=your_hub_id
REACT_APP_CREDENTIAL_LOCKER_ID=your_credential_locker_id
```

5. Build and start the application:

```
npm start
```

6. Access the application at:

```
http://localhost:3000
```

For pricing information, refer to [Managed integrations section on the AWS IoT Device Management pricing page](https://aws.amazon.com/iot-device-management/pricing/ "https://aws.amazon.com/iot-device-management/pricing/").
