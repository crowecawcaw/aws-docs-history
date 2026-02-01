# Updating NDI configuration

Updating the flow NDI® configuration allows you to determine how this flow communicates with the rest
of your NDI environment.

###### Important

The NDI configuration is available only for **Large** flows.

## Prerequisites

- The following procedure assumes that you’ve already created a **Large**flow.

## Procedure

###### To update the NDI configuration of an existing flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow that you
   want to update.

The details page for that flow appears. 3. In the **NDI configuration** section, choose
**Edit**. 4. Set **Flow NDI support** to **Enabled** to enable NDI, or
**Disabled** to disable NDI. 5. Enter or update the NDI machine name.

    * This name is used as a prefix to help you identify this
     flow source as an NDI receiver in your network. For example,
     if you enter `MACHINENAME`, your flow
     source will appear to your NDI senders as
     `MACHINENAME (ProgramName)`.
    * If you don’t enter a name, MediaConnect generates a unique
     12-character ID from the flow's ARN.

6. Update the NDI discovery servers. You can add up to three discovery servers.
   For each discovery server, provide the following information:
   - Enter the discovery server IP address (IPv4 format).
   - Specify a port number if you’re not using the default
     (5959).
   - Select the appropriate VPC interface adapter.

7. Choose **Update**.
