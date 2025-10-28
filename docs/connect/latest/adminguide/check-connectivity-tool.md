# Validate connectivity to Amazon Connect with the

Endpoint Test Utility

To validate connectivity to Amazon Connect, or when your agents are
experiencing problems with the Contact Control Panel (CCP), we recommend using the
[Amazon Connect Endpoint Test
Utility](https://tools.connect.aws/endpoint-test/ "https://tools.connect.aws/endpoint-test/").

The Amazon Connect Endpoint Test Utility performs the following checks:

- Validates that the browser being used supports WebRTC.
- Determines if the browser has appropriate access to media devices (microphone,
  speakers, etc).
- Performs latency tests for all active Amazon Connect Regions.
- Performs latency tests to a specific Amazon Connect instance, if provided.
- Validates network connectivity across required ports for media streams.
  The complete results are available for download as a JSON file. You can copy the
  results to include in a support ticket. You can also load the results file into the tool
  by selecting the **Load previous results** option. This option displays
  the contents of the file visually and makes it easier to analyze the results.
  Additionally, you can download a bookmark specifically for the provided instance to make
  future tests easier to run.

## Parameters to customize the

Endpoint Test Utility

You can use the Endpoint Test Utility as is without any customizations. However,
if you want to customize it, use the following URL parameters:

- **lng**: Change the language of the tool. Currently
  supported languages are English, Spanish, and French. It accepts the
  following values:
  - en (default)
  - es
  - fr

- **autoRun**: Run the tool automatically. It accepts the
  following values:
  - true
  - false (default)

- **connectInstanceUrl**: Not used by default. You can
  specify the Amazon Connect instance in the URL. It must start with
  **https**.
- **regions**: A comma-separated list of region codes for
  the AWS Regions that you want to test. For example
  `regions=us-east-1,us-west-2`.

Example customized URL:

`https://tools.connect.aws/endpoint-test/?lng=es&autoRun=true&connectInstanceUrl=https://myinstance.awsapps.com&regions=us-east-1,us-west-2`
