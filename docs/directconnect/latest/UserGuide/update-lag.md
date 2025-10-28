# Update a LAG at an AWS Direct Connect endpoint

You can update the following link aggregation group (LAG) attributes using either the AWS Direct Connect console or using the command line or API:

- The name of the LAG.
- The value for the minimum number of connections that must be operational for
  the LAG itself to be operational.
- The LAG's MACsec encryption mode.

MACsec is only available on dedicated connections.

AWS assigns this value to each connection that is part of the LAG.

The valid values are:

    + `should_encrypt`
    + `must_encrypt`


    When you set the encryption mode to this value, the connections go
     down when the encryption is down.
    + `no_encrypt`

- The tags.

###### Note

If you adjust the threshold value for the minimum number of operational
connections, ensure that the new value does not cause the LAG to fall below the
threshold and become non-operational.

###### To update a LAG

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **LAGs**.
3. Select the LAG, and then choose **Edit**.
4. Modify the LAG

[Change the
name] For **LAG Name**, enter a new LAG name.

[Adjust the minimum number of connections] For **Minimum Links**,
enter minimum number of operational connections.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key
     value.[Remove a tag] Next to the tag, choose **Remove tag**.

5. Choose **Edit LAG**.

###### To update a LAG using the command line or API

- [update-lag](../../../cli/latest/reference/directconnect/update-lag.md "../../../cli/latest/reference/directconnect/update-lag.md")
  (AWS CLI)
- [UpdateLag](../APIReference/API_UpdateLag.md "../APIReference/API_UpdateLag.md") (AWS Direct Connect
  API)
