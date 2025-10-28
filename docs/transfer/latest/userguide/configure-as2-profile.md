# Create AS2 profiles

This topic discusses how to create profiles for use in the AS2 process.
A _local profile_ defines the local (AS2-enabled
Transfer Family server) organization or "party." Similarly, a _partner
profile_ defines the remote partner organization, external to Transfer Family.

1. [Import AS2 certificates](managing-as2-partners.md#configure-as2-certificate "managing-as2-partners.md#configure-as2-certificate")
2. Create AS2 profiles
3. [Create an AS2 server](create-as2-transfer-server.md "create-as2-transfer-server.md")
4. [Create an AS2 agreement](create-as2-transfer-server.md#as2-agreements "create-as2-transfer-server.md#as2-agreements")
5. [Configure AS2 connectors](configure-as2-connector.md "configure-as2-connector.md")
   Use this procedure to create both local and partner profiles. This procedure explains
   how to create AS2 profiles by using the Transfer Family console. If you want to use the AWS CLI
   instead, see [Step 3: Create profiles for you and
   your trading partner](as2-example-tutorial.md#as2-create-profiles-example "as2-example-tutorial.md#as2-create-profiles-example").

###### To create an AS2 profile

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, under **AS2 Trading Partners**,
   choose **Profiles**, then choose **Create
   profile**.
3. In the **Profile configuration** section, enter the AS2 ID
   for the profile. This value is used for the AS2 protocol-specific HTTP headers
   `as2-from` and `as2-to` to identify the trading
   partnership, which determines the certificates to use, and so on.
4. In the **Profile type** section, choose **Local
   profile** or **Partner profile**.
5. In the **Certificates** section, choose one or more
   certificates from the dropdown menu.

**Tip:** If you want to import a certificate that
is not listed in the dropdown menu, select **Import a new
Certificate**. This opens a new browser window at the
**Import certificate** screen. For the procedure about
importing certificates see [Import AS2 certificates](managing-as2-partners.md#configure-as2-certificate "managing-as2-partners.md#configure-as2-certificate"). 6. (Optional) In the **Tags** section, specify one or more
key-value pairs to help identify this profile. 7. Choose **Create profile** to complete the process and save
the new profile.
