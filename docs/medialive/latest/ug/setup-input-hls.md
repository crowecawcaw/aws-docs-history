# Create an HLS input

After you have obtained information from the upstream system, you can create an
HLS input.

###### To create an HLS pull input

1. Make sure that you have the information from [step 1](setup-input-link-obtain-info.md "setup-input-link-obtain-info.md").
2. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
3. In the navigation pane, choose **Inputs**. On the
   **Inputs** page, choose **Create
   input**.
4. Complete the **Input details** section:
   - **Input** name – enter a name.
   - **Input type** – choose
     **HLS**.

5. In the **Input class** section, choose the class for this
   input:
   - STANDARD_INPUT
   - SINGLE_INPUT

6. In the **Input sources** section, enter the URLs you
   previously obtained:
   - If the input is a standard-class input, complete both fields, to
     provide two URLs.
   - If the input is a single-class input, complete the first field
     with the URL that you obtained and leave the second field
     empty.

7. If the upstream system and/or the license server (if the HLS source is
   encrypted) requires that you provide user credentials, you must also enter
   the user name and password key for accessing the location. These credentials
   are stored on the Systems Manager Parameter Store. For more information, see [About the feature for creating password
   parameters](requirements-for-EC2.md#about-EC2Password "requirements-for-EC2.md#about-EC2Password").

If one of the servers (upstream system or license server) requires
credentials and the other doesn't, MediaLive presents them to both. But the
server that doesn't need them simply ignores them. 8. In the **Tags** section, create tags if you want to
associate tags with this input. For more information, see [Tagging resources](tagging.md "tagging.md"). 9. Choose **Create**.

MediaLive creates the input and adds it to the list of inputs. The input
specifies either one or two sources. The sources don't appear in the list,
but if you choose the **Name** link, the details page shows
them.
