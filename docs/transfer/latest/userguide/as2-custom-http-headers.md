# Customize HTTP headers for AS2 messages

When sending AS2 messages to trading partners, you may need to customize the HTTP headers
to meet specific requirements or enhance compatibility with your partner's AS2 server
configuration. This CloudFormation template creates an infrastructure to enable customized HTTP
headers for AS2 messages sent through AWS Transfer Family. It sets up an Amazon API Gateway and Lambda function
to act as a proxy, allowing dynamic modification of headers required by trading partners'
AS2 servers.

Use this template to do the following:

- Add custom HTTP headers to outbound AS2 messages
- Override default header values with custom values

###### Important

Be careful when overriding default header values, as it can cause send
failures: some AS2 headers are required.

- Ensure compatibility with trading partners that have specific header
  requirements

## Template Overview

The template creates the following main components:

- A Lambda function that processes and forwards AS2 messages
- An Amazon API Gateway to expose the Lambda function
- IAM roles and permissions for the Lambda function
- Conditional resources for HTTPS support

The template file is available here: [Dynamic HTTP headers template](https://s3.amazonaws.com/aws-transfer-resources/as2-templates/dynamic-http-headers.template.yml "https://s3.amazonaws.com/aws-transfer-resources/as2-templates/dynamic-http-headers.template.yml").

## How It Works

1. The Amazon API Gateway receives incoming AS2 messages from AWS Transfer Family.
2. The request is forwarded to the Lambda function.
3. The Lambda function processes the request, adding or modifying headers as
   needed.
4. The modified request is then forwarded to the partner's AS2 server.
5. The response from the partner's server is returned through the Lambda and
   Amazon API Gateway back to AWS Transfer Family.

## Key Features

- _Dynamic Header Modification:_ Allows customization of the
  Subject header and addition of other required headers.
- _Protocol Support:_ Works with both HTTP and HTTPS
  protocols.
- _Flexible Configuration:_ Allows specification of partner
  host, port, and path.

## Implementation Details

The template implements the following key components:

### Lambda Function

The core of the solution is a Node.js Lambda function that:

- Receives requests from the Amazon API Gateway
- Modifies headers based on configuration and incoming request data
- Forwards the modified request to the partner's AS2 server
- Handles both HTTP and HTTPS protocols
- Includes error handling and logging

### Amazon API Gateway

An HTTP API is set up to:

- Receive incoming AS2 messages
- Route requests to the Lambda function
- Return responses back to AWS Transfer Family

### Template parameters

Enter information for the template parameters as follows. Note that all of these
parameters are strings.

- `Environment`: this parameter is used to name the resources
  that the template creates: whether they are intended for a development or
  production environment. Valid values are **dev** and
  **prod**.
- `PartnerHost`: the IP address or hostname of the AS2 partner
  server.
- `PartnerPort`: the port number for the AS2 partner server. If
  not specified, defaults to 80 for HTTP and 443 for HTTPS.
- `PartnerPath`: the path to the AS2 endpoint on the partner
  server
- `ProtocolType`: the protocol to use for the AS2 communication:
  valid values are **HTTP** and
  **HTTPS**.

### Conditional Resources

For HTTPS support, the template conditionally creates:

- A Lambda Layer for CA certificates
- HTTPS-specific configuration in the Lambda function

## Deployment and Usage

###### To customize AS2 HTTP headers using a CloudFormation template

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the left navigation pane, choose **Stacks**.
3. Choose **Create stack**, and then choose **With new
   resources (standard)**.
4. In the **Prerequisite - Prepare template** section, choose
   **Choose an existing template**.
5. Copy this link, [Dynamic HTTP headers template](https://s3.amazonaws.com/aws-transfer-resources/as2-templates/dynamic-http-headers.template.yml "https://s3.amazonaws.com/aws-transfer-resources/as2-templates/dynamic-http-headers.template.yml"), and paste it into the **Amazon S3
   URL** field.
6. Choose **Next**.
7. Fill in the parameter details with your information. These are detailed in
   [Template parameters](#as2-header-template-parameter-details "#as2-header-template-parameter-details").
8. Choose **Next**. On the **Configure stack
   options** page, choose **Next** again.
9. Review the details for the stack that you're creating, and then choose
   **Create stack**.

###### Note

At the bottom of the page, under **Capabilities**, you
must acknowledge that CloudFormation might create AWS Identity and Access Management (IAM) resources.

After deploying this CloudFormation stack:

1. Note the Amazon API Gateway endpoint URL provided in the stack outputs.
2. Update your existing AWS Transfer Family Connector to use this new Amazon API Gateway
   endpoint.
3. The solution will now handle AS2 messages, adding or modifying headers as
   configured.

###### Warning

Only modify the Subject header or add headers that your partner explicitly
expects. Changing other headers may cause transfer failures.
