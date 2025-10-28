# Update an AWS Direct Connect connection

You can update the following connection attribute using either the AWS Direct Connect console or using the command line or API.

- The name of the connection.
- The connection's MACsec encryption mode.

###### Note

While you cannot directly modify MACSec properties on hosted connections,
partners can enable MACSec on their own interconnects to provide secure hosted
connections to their customers.

The valid values are:

    + `should_encrypt`
    + `must_encrypt`


    When you set the encryption mode to this value, the connection goes
     down when the encryption is down.
    + `no_encrypt`

###### To update a connection

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Connections**.
3. Select the connection, and then choose **Edit**.
4. Modify the connection:

[Change the name] For **Name**, enter a new connection
name.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.[Remove a tag] Next to the tag, choose **Remove tag**.

5. Choose **Edit connection**.

###### To update a connection using the command line or API

- [update-connection](../../../cli/latest/reference/directconnect/update-connection.md "../../../cli/latest/reference/directconnect/update-connection.md") (AWS CLI)
- [UpdateConnection](../APIReference/API_UpdateConnection.md "../APIReference/API_UpdateConnection.md") (AWS Direct Connect API)
