# Create an MP4 input

After you have obtained information from the upstream system, you can create an
MP4 input.

###### To create an MP4 pull input

1.  Make sure that you have the information from [step 1](setup-mp4-obtain-info.md "setup-mp4-obtain-info.md").
2.  If this input is being used in a multiple-input channel, you should have
    decided whether to set it up as a static input or a [dynamic input](dynamic-inputs.md "dynamic-inputs.md"). You might need to modify
    the URLs you obtained from the upstream system:
    - If the input is a static input, don't modify the URLs.
    - If the input is a dynamic input, set up the URL as an optional
      absolute portion and a required variable portion ($urlPath$). For
      examples, see the table after this procedure.

    We recommend that you use the format
    <protocol>/$urlPath$.

3.  Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
4.  In the navigation pane, choose **Inputs**. On the
    **Inputs** page, choose **Create
    input**.
5.  Complete the **Input details** section:
    - **Input** name – enter a name.
    - **Input type** – choose
      **MP4**.

6.  In the **Input class** section, choose the class for this
    input:
    - STANDARD_INPUT
    - SINGLE_INPUT

7.  In the **Input sources** section, enter the URLs you
    previously obtained:

        * If the input is a standard-class input, complete both fields, to
         provide two URLs.
        * If the input is a single-class input, complete the first field
         with the URL that you obtained and leave the second field
         empty.

    If the upstream system requires that you provide user credentials, you
    must also enter the user name and password key for accessing the location.
    These credentials are stored on the Systems Manager Parameter Store. For more
    information, see [About the feature for creating password
    parameters](requirements-for-EC2.md#about-EC2Password "requirements-for-EC2.md#about-EC2Password").

8.  In the **Tags** section, create tags if you want to
    associate tags with this input. For more information, see [Tagging resources](tagging.md "tagging.md").
9.  Choose **Create**.

MediaLive creates the input and adds it to the list of inputs. The input
specifies either one or two sources. The sources don't appear in the list,
but if you choose the **Name** link, the details page shows
them.

## Formats for the URL in a dynamic

input

The following table describes the different formats for the URL in a dynamic
input.

| Format                        | Description                                           | Example                                                                       | Example of the $urlPath$                 |
| ----------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------- |
| <protocol>/$urlPath$          | URL has only the protocol in the absolute portion     | s3ssl://$urlPath$                                                             | amzn-s3-demo-bucket/my-movie.mp4         |
| <protocol and path>/$urlPath$ | URL has the protocol and path in the absolute portion | mediastoressl://f31z.data.mediastore.us-west-2.amazonaws.com/movies/$urlPath$ | my-movie.mp4                             |
| $urlPath$                     | URL has only the variable portion                     | $urlPath$                                                                     | s3ssl://amzn-s3-demo-bucket/my-movie.mp4 |
