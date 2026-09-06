

# Managed Integrations demo application
<a name="supported-raspberry-demo-app"></a>

**Note**  
 This implementation of AWS IoT Hub SDK on Raspberry Pi is a demonstration project intended for learning and testing purposes only and is not intended to be used in production environments. For the purposes of this demo, set the following configurations for development ease:   
 **AWS credentials storage**: For demo purposes only, credentials and certificates are stored in an accessible location for easier testing and development. Production environments must use secure storage solutions like AWS Secrets Manager, or Systems Manager Parameter Store. They must implement encryption at rest, and follow AWS IoT security guidelines.   
 **Container privileges**: The demo runs with elevated privileges to allow unrestricted access to host resources and simplify development workflows. In production, containers should operate with minimal required privileges.   
 **Network bridge configuration**: The demo uses a network bridge configuration that exposes internal network traffic for easier debugging and monitoring. In production environments, implement proper network isolation and segmentation to prevent unauthorized access to internal network traffic.   
 **USB device permissions**: Unrestricted USB device access is enabled to facilitate easy connection of development peripherals and testing devices. For production, implement strict USB device controls and validation to prevent device spoofing attacks.   
 These configurations enable straightforward testing and must notcbe used in production environments. When deploying to production, please follow security best practices to prevent host system compromise and unauthorized access to credentials. 

 The demo application is a React-based demo application showcasing Managed Integrations capabilities for smart home device management. This application demonstrates device onboarding, control, and monitoring for Z-Wave and Zigbee devices through a modern web interface. 

## Prerequisites
<a name="prerequisites-demo-app"></a>
+ [Sign up for an AWS account](https://docs.aws.amazon.com/iot-mi/latest/devguide/setting-up.html#sign-up-for-aws).
+  [Create a credential locker](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-ss.html#managedintegrations-sdk-v2-cookbook-credential-locker) and [ add the credential locker to your hub](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-ss.html#managedintegrations-sdk-v2-cookbook-add-to-hub) .
+ Complete [ Hub onboarding setup](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-hubsetup.html).
+ [Node.js 18\+ and npm](https://nodejs.org/en/download).
+ Install the latest version of [AWS CLI from the Managed Integrations AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/).
+ Modern web browser (Chrome, Firefox, Safari, Edge)

## Install and configure the Application
<a name="installation-demo"></a>

1. Download [ Managed Integrations demo application](https://d2no7dt1utuyzo.cloudfront.net/IotMI-HubSDK-DemoApp/1.0.0/IotMI-HubSDK-DemoApp-v1.0.0.tar.gz).

1. Extract the package:

   ```
   cd ~/Downloads
   tar -xzf IotMI-HubSDK-DemoApp-v1.0.0.tar.gz
   cd IotManagedIntegrations-DemoApp
   ```

1. Install dependencies:

   ```
   npm install
   ```

1. Create a `.env` file in the root directory:

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

1. Build and start the application:

   ```
   npm start
   ```

1. Access the application at:

   ```
   http://localhost:3000
   ```

For pricing information, refer to [Managed Integrations section on the AWS IoT Device Management pricing page](https://aws.amazon.com/iot-device-management/pricing/).