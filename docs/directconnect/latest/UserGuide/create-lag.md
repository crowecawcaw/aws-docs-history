# Create a LAG at an Direct Connect endpoint

You can create a LAG by provisioning new connections, or aggregating existing
connections.

You cannot create a LAG with new connections if this results in you exceeding the overall
connections limit for the Region.

To create a LAG from existing connections, the connections must be on the same AWS
device (terminate at the same Direct Connect endpoint). They must also use the same bandwidth.
You cannot migrate a connection from an existing LAG if removing the connection causes
the original LAG to fall below its setting for the minimum number of operational
connections.

###### Important

For existing connections, connectivity to AWS is interrupted during the creation
of the LAG.

###### To create a LAG with new connections

1.  Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  In the navigation pane, choose **LAGs**.
3.  Choose **Create LAG**.
4.  Under **Lag creation type**, choose **Request new
    connections**, and provide the following information:
    - **LAG name**: A name for the LAG.
    - **Location**: The location for the LAG.
    - **Port speed**: The port speed for the connections.
    - **Number of new connections**: The number of new connections to
      create. You can have a maximum of four connections when the
      port speed is 1G or 10G, or two when the port speed is 100
      Gbps or 400 Gbps.
    - (Optional) Configure MAC security (MACsec) for the connection. Under
      **Additional Settings**, select **Request a MACsec
      capable port**.

    MACsec is only available on dedicated connections.
    - (Optional) Add or remove a tag.

    [Add a tag] Choose **Add tag** and do the
    following:

        + For **Key**, enter the key name.
        + For **Value**, enter the key value.

    [Remove a tag] Next to the tag, choose **Remove
    tag**.

5.  Choose **Create LAG**.

###### To create a LAG from existing connections

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **LAGs**.
3. Choose **Create LAG**.
4. Under **Lag creation type**, choose **Use existing
   connections**, and provide the following information:
   - **LAG name**: A name for the LAG.
   - **Existing connections**: The Direct Connect connection to use for
     the LAG.
   - (Optional) **Number of new connections**: The number of new
     connections to create. You can have a maximum of four
     connections when the port speed is 1G or 10G, or two when
     the port speed 100 Gbps or 400 Gbps.

5. (Optional) Add or remove a tag.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.[Remove a tag] Next to the tag, choose **Remove tag**.

6. Choose **Create LAG**.

###### To create a LAG using the command line or API

- [create-lag](../../../cli/latest/reference/directconnect/create-lag.md "../../../cli/latest/reference/directconnect/create-lag.md") (AWS CLI)
- [CreateLag](../APIReference/API_CreateLag.md "../APIReference/API_CreateLag.md")
  (Direct Connect API)

###### To describe your LAGs using the command line or API

- [describe-lags](../../../cli/latest/reference/directconnect/describe-lags.md "../../../cli/latest/reference/directconnect/describe-lags.md") (AWS CLI)
- [DescribeLags](../APIReference/API_DescribeLags.md "../APIReference/API_DescribeLags.md") (Direct Connect API)

###### To download the LOA-CFA using the command line or API

- [describe-loa](../../../cli/latest/reference/directconnect/describe-loa.md "../../../cli/latest/reference/directconnect/describe-loa.md") (AWS CLI)
- [DescribeLoa](../APIReference/API_DescribeLoa.md "../APIReference/API_DescribeLoa.md") (Direct Connect API)
  After you create a LAG, you can associate or disassociate connections from it. For more
  information, see [Associate a connection with a LAG](associate-connection-with-lag.md "associate-connection-with-lag.md") and [Disassociate a connection from a LAG](disassociate-connection-from-lag.md "disassociate-connection-from-lag.md").
