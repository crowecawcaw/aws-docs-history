# Creating a CMAF packaging configuration

Create a packaging configuration that formats content for devices that support
Apple HLS fragmented MP4 (fMP4).

###### To create a CMAF packaging configuration (console)

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. In the navigation pane, under **Video on demand**, choose
   **Packaging groups**.
3. On the **Packaging groups** page, choose the
   group that will contain the configuration that you're creating.
4. On the details page for the packaging group, under **Packaging
   configurations**, choose **Manage
   configurations**.
5. On the **Manage packaging configurations** page, under
   **Packaging configurations**, choose
   **Add** and select **New
   config**.
6. Complete the fields as described in the following topics:
   - [General settings fields](cfigs-cmaf-new.md "cfigs-cmaf-new.md")
   - [Manifest settings fields](cfigs-cmaf-manset.md "cfigs-cmaf-manset.md")
   - [Stream selection fields](cfigs-cmaf-include-streams.md "cfigs-cmaf-include-streams.md")
   - [Encryption fields](cfigs-cmaf-encryption.md "cfigs-cmaf-encryption.md")

7. Choose **Save**.
   If you exceed the quotas for your account when you're creating a packaging
   configuration, you get an error. If you get an error similar to **`Too many
 requests, please try again. Resource limit exceeded`**, either you have
   exceeded the API request quotas, or you have already reached the maximum number of
   packaging groups allowed on your account. If this is your first group, or if you
   think you mistakenly received this error, use the Service Quotas console to
   [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediapackage/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediapackage/quotas"). For more information
   about quotas in MediaPackage, see [Quotas in AWS Elemental MediaPackage](quotas.md "quotas.md").
