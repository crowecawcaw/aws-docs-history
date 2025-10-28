# Creating a transport stream (TS) file input

This section describes how to set up to ingest transport stream (TS) content that is
stored as a file.

###### To create a TS file input

1.  You should have already arranged with the video content provider to set up the
    upstream system for your content. Make sure that the operator of the upstream
    system gives you the following information:
    - The full URLs of the locations where MediaLive will pull the TS files
      from. For example:

    `s3ssl://amzn-s3-demo-bucket/filler-videos/main/oceanwaves.ts`

    `s3ssl://amzn-s3-demo-bucket/filler-videos/redundant/oceanwaves.m2ts`

2.  If this input is being used in a multiple-input channel, you should have
    decided whether to set it up as a static input or a [dynamic input](dynamic-inputs.md "dynamic-inputs.md"). You might need to modify the
    URLs you obtained from the upstream system:
    - If the input is a static input, don't modify the URLs.
    - If the input is a dynamic input, set up the URL as an optional
      absolute portion and a required variable portion ($urlPath$). For
      examples, see the table after this procedure.

    We recommend that you use the format <protocol>/$urlPath$.

3.  Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
4.  In the navigation pane, choose **Inputs**. On the
    **Inputs** page, choose **Create
    input**.
5.  Complete the **Input details** section:
    - **Input** name – enter a name.
    - **Input type** – choose
      **TS**.

6.  In the **Input class** section, choose the class for this
    input:
    - STANDARD_INPUT
    - SINGLE_INPUT

7.  In the **Input sources** section, enter the URLs you
    previously obtained:

        * If the input is a standard-class input, complete both fields, to
         provide two URLs.
        * If the input is a single-class input, complete the first field with
         the URL that you obtained and leave the second field empty.

    If the upstream system requires that you provide user credentials, you must
    also enter the user name and password key for accessing the location. These
    credentials are stored on the Systems Manager Parameter Store. For more information, see
    [About the feature for creating password
    parameters](requirements-for-EC2.md#about-EC2Password "requirements-for-EC2.md#about-EC2Password").

8.  In the **Tags** section, create tags if you want to associate
    tags with this input. For more information, see [Tagging resources](tagging.md "tagging.md").
9.  Choose **Create**.

MediaLive creates the input and adds it to the list of inputs. The input specifies
either one or two sources. The sources don't appear in the list, but if you
choose the **Name** link, the details page shows them.

When you start the channel, MediaLive will connect to the upstream system at this
source location or locations and pull the content:

    * For a standard channel, MediaLive expects the upstream system to provide
     two sources and will therefore attempt to pull from both source
     locations.
    * For a single-pipeline channel, MediaLive expects the upstream system to
     provide one source and will therefore attempt to pull from one source
     location.

## Formats for the URL in a dynamic

input

The following table describes the different formats for the URL in a dynamic
input.

| Format                        | Description                                           | Example                                                                       | Example of the $urlPath$                |
| ----------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------- |
| <protocol>/$urlPath$          | URL has only the protocol in the absolute portion     | s3ssl://$urlPath$                                                             | amzn-s3-demo-bucket/my-movie.ts         |
| <protocol and path>/$urlPath$ | URL has the protocol and path in the absolute portion | mediastoressl://f31z.data.mediastore.us-west-2.amazonaws.com/movies/$urlPath$ | my-movie.ts                             |
| $urlPath$                     | URL has only the variable portion                     | $urlPath$                                                                     | s3ssl://amzn-s3-demo-bucket/my-movie.ts |
