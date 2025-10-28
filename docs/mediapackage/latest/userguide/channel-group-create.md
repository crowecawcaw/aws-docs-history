# Creating a channel group in AWS Elemental MediaPackage

This guide shows how to create a channel group as a holder for your channels and
origin endpoints. You can provide high-level information about your channel group and
can add a certain number of channel groups for each account. After you create a channel
group, you can add channels to the channel group.

You can use the MediaPackage console, MediaPackage API, or AWS Command Line Interface (AWS CLI) to create a channel group.
When you're creating a channel group, don't put sensitive identifying information like
customer account numbers into free-form fields such as the name or description field.
MediaPackage doesn’t require that you supply any customer data. This includes when you work
with MediaPackage using the MediaPackage console, MediaPackage API, AWS CLI, or AWS SDKs. Any data that you
enter into MediaPackage might get picked up for inclusion in diagnostic logs or Amazon CloudWatch Events.

###### To create a channel group

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Choose **Create channel group** from the **Channel groups** list.
3. For **Name**, enter a name
   that describes the channel group. This is the name that you use for API and
   console interactions. The name is the primary identifier for the channel group, and must be unique for your
   account in the AWS Region. Supported characters are **A-Z**, **a-z**, **0-9**, **\_** (underscore), and
   **-** (hyphen) with a length of 1–256
   characters. You can't use spaces in the name, and you can't change the name
   after you create the channel group.
4. (Optional) For **Description**, enter any descriptive text that helps you to identify the channel group.
5. Choose **Create**.

MediaPackage displays the new channel group's details page.

After you create a channel group, MediaPackage provides an egress domain URL that is
fixed for the lifetime of the channel
group. This domain remains regardless of any failures or upgrades that might
happen over time.

All channels and origin endpoints that belong to this channel group will use
the same domain URL. For stream delivery from MediaPackage, direct your CDNs to this domain.

When you create a channel group, if you exceed the quotas on the account,
you'll receive an error. The error will be similar to **`Too many
 requests, please try again. Resource limit exceeded`**. This error
means that either you exceeded the API request quotas, or that you reached the
maximum number of channel groups that your account permits.
You can add channels to a channel group to do the following:

- Permit a live content stream from a source such as AWS Elemental MediaLive or
  another encoder.
- Permit downstream video players and content delivery networks (CDNs)
  to start requesting content playback.
  For instructions on adding channels to a channel group from the MediaPackage console, see
  [Working with channels in AWS Elemental MediaPackage](channels.md "channels.md").
