# Enabling blackout

Follow this procedure if you want to enable the blackout feature in a MediaLive
channel.

###### To enable blackout

1. In the channel that you are creating, in the navigation pane, choose
   **General settings**.
2. Set the ad avail mode, if you have not already done so. See [Getting ready: Set the SCTE 35
   source—segments or manifest](scte35-getting-ready-source.md "scte35-getting-ready-source.md"). The mode identifies which of
   all possible events are treated as triggers for blackouts, which determines
   [when video is blacked out](triggers-for-blackout.md "triggers-for-blackout.md").
3. Still in
   **General settings**, in **Blackout
   slate**, in **State**, choose
   **Enabled**.
4. For **Blackout slate image**, choose the appropriate
   value:
   - **Disable**: To use a plain black image for
     blackout.
   - **Avail blanking image**: To use a special image
     for blackout. In the **URL** field, enter the path
     to a file in an Amazon S3 bucket. For integration with MediaLive, the
     bucket name mustn't use dot notation, which means it mustn't use .
     (dot) between the words in the bucket name. The file must be of type
     .bmp or .png. Also enter the user name and Systems Manager password parameter
     for accessing the S3 bucket. For information about this key, see
     [About the feature for creating password
     parameters](requirements-for-EC2.md#about-EC2Password "requirements-for-EC2.md#about-EC2Password").

5. If you want to enable network end blackout (in other words, black out
   content when network transmission has ended and remove blackout only when
   network transmission resumes), continue reading. If you don't want to enable
   it, you have now finished setting up.
6. For **Network end blackout**, choose
   **Enabled**.
7. For **Network end blackout image**, choose the
   appropriate value:
   - **Disable**: To use a plain black image for
     blackout.
   - **Network end blackout image**: To use a special
     image for network end blackout. In the **URL**
     field, enter the path to a file in an Amazon S3 bucket. For
     integration with MediaLive, the bucket name mustn't use dot notation,
     which means it mustn't use . (dot) between the words in the bucket
     name. The file must be of type .bmp or .png. Also enter the user
     name and Systems Manager password for accessing the S3 bucket. See [About the feature for creating password
     parameters](requirements-for-EC2.md#about-EC2Password "requirements-for-EC2.md#about-EC2Password").

8. For **Additional settings**, in **Network
   ID**, type the EIDR ID of the network in the format
   10.nnnn/xxxx- xxxx- xxxx- xxxx-xxxx-c (case insensitive). Only network end
   events with this ID will trigger blackout.
