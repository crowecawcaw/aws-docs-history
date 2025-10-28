# Enabling blanking

Follow this procedure if you want to enable the ad avail blanking feature in a
MediaLive channel.

###### To enable blanking

1. In the channel that you are creating, in the navigation pane, choose
   **General settings**.
2. Set the ad avail mode, if you have not already done so. See [Getting ready: Set the SCTE 35
   source—segments or manifest](scte35-getting-ready-source.md "scte35-getting-ready-source.md"). The mode identifies which of
   all possible events are treated as triggers for blanking, which determines
   [when video is
   blanked](triggers-for-ad-avail-blanking.md "triggers-for-ad-avail-blanking.md").
3. Still in
   **General settings**, in **Avail
   blanking**, in **State**, choose
   **Enabled**.
4. In **Avail blanking image**, choose the appropriate
   value:
   - Disable: To use a plain black image for blanking.
   - Avail blanking image: To use a special image for blanking. In the
     **URL** field, type the path to a file in an S3
     bucket. For integration with MediaLive, the bucket name mustn't use dot
     notation. For example, `mycompany-videos` is
     acceptable but `mycompany.videos` isn't. The file
     must be of type .bmp or .png. Also enter the user name and Systems Manager
     password parameter for accessing the S3 bucket. See [About the feature for creating password
     parameters](requirements-for-EC2.md#about-EC2Password "requirements-for-EC2.md#about-EC2Password").
