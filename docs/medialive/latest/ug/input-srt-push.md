# Channel input—SRT listener input

Follow these guidelines to verify that the input is set up correctly.

###### To verify the setup of the input

1.  Look at the **Input destinations** section. It shows the
    locations on MediaLive that the upstream system will push the source to when
    the channel is running. These locations were automatically generated when
    you created the input. The port is always 5050 for SRT listener inputs:

        * If the channel is set up as a standard channel, MediaLive allocated two
         IP addresses.
        * If the channel is set up as a single-pipeline channel, MediaLive allocated one
         IP address.

    For example:

**srt://54.123.45.67:5050**

**srt://54.123.45.68:5050** 2. Look at the **SRT listener settings** section. It shows
the configuration you specified when you created the input:

    * **Minimum latency**: The latency value in milliseconds
     (120 to 15000).
    * **Stream ID**: The stream ID if you specified one.
    * **Decryption**: The encryption algorithm (AES 128,
     AES 192, or AES 256) and the passphrase secret ARN.

3. Look again at the **Input destinations** section.
   - The section must have an **Input security group**
     with a number beside it. This security group controls which IP addresses
     are allowed to push content to this input. If the section doesn't have
     an input security group, the input isn't correctly set up.
