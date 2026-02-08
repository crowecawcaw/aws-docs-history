# Create an SRT Listener input

After you have obtained the necessary information from the upstream system and
created an input security group, you can create the SRT Listener input.

###### To set up an SRT Listener input

1. Make sure that you have the information that you [obtained from the upstream
   system](input-listener-srt-prereqs.md "input-listener-srt-prereqs.md").
2. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
3. In the navigation pane, choose **Inputs**. On the
   **Inputs** page, choose **Create
   input**. Then choose **SRT Listener**.
4. In the **Input class** section, choose the class for this
   input:
   - STANDARD_INPUT: MediaLive allocates two IP addresses for redundancy.
   - SINGLE_INPUT: MediaLive allocates one IP address.

5. In the **Input security group** section, select the input
   security group that you created or identified earlier. This security group must
   include the IP address of the upstream system that will push content to this
   input.
6. In the **SRT Listener settings** section, complete the
   following fields:
   - **Minimum latency**: Enter the latency value in
     milliseconds that you agreed on with the upstream system. The valid
     range is 120 to 15000 milliseconds. SRT will choose the maximum of
     the values proposed by the sender and receiver.
   - **Stream ID**: Optional. Enter the stream ID if
     the upstream system uses this identifier.

7. Complete the **Decryption** fields. Encryption is required
   for SRT Listener inputs:
   - **Algorithm**: Select the encryption algorithm that
     you agreed on with the upstream system: AES 128, AES 192, or AES 256.
     Encryption always uses AES, but the algorithm length can be negotiated
     between you and the sender. If you don't know what length to use, enter
     the lowest value. If the sender negotiates to use a longer length,
     MediaLive will always agree to that higher length.
   - **Passphrase secret ARN**: If the list of ARNs is
     populated, select the ARN of the passphrase that you [created earlier](input-listener-srt-prereqs.md "input-listener-srt-prereqs.md"). If the
     list is empty, type the ARN into the entry field.

8. In the **Tags** section, create tags if you want to
   associate tags with this input. For more information, see [Tagging resources](tagging.md "tagging.md").
9. Choose **Create**. MediaLive creates the input and allocates
   one or two IP addresses (depending on the input class). The input appears in
   the list of inputs with the allocated IP addresses and port 5050.
