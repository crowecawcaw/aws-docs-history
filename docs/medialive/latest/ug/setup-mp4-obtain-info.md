# Obtain information

Obtain the following information from the operator at the upstream system:

- The URLs on the upstream system for the source file or files.

There are two URLs for a standard-class input, or one URL for a
single-class input. For information about input classes and their uses, see
[Choosing the channel class and input
class](class-channel-input.md "class-channel-input.md").

See the table later in this section for the URL format and for
examples.

Make a note of the full URLs.

- The user name and password to access the upstream system, if the upstream
  system requires authenticated requests. Note that these user credentials
  relate to user authentication, not to the protocol. User authentication is
  about whether the upstream system will accept your request. The protocol is
  about whether the request is sent over a secure connection.
  The following tables show the format of the URLs on the different types of
  upstream systems that MediaLive supports for MP4 input.

**Upstream server is an HTTP or HTTPS server**

|               |                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| Format of URL | ``<protocol>`//:`<hostname>`/`<filename>`.mp4`                                                          |
| Example       | `https://203.0.113.13/filler-videos/oceanwaves.mp4``https://198.51.100.54/filler-videos/oceanwaves.mp4` |

**Upstream server is AWS Elemental MediaStore**

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Format of URL | `mediastoressl://`<data endpoint for<br>container>`/`<path>`/`<filename>.`mp4`                                                                                                                                                                                                                                                                                                                                                    |
| Example       | Assume that the data endpoint for the container for one of the<br>content sources is the following:<br>`f31z.data.mediastore.us-west-2.amazonaws.com`.<br>Assume that the file is called<br>`oceanwaves.mp4`,<br>and it is stored in the container, in the path<br>`filler-video`.<br>The URL for one of the source files would be:<br>`mediastoressl://f31z.data.mediastore.us-west-2.amazonaws.com/filler-video/oceanwaves.mp4` |

**Upstream server is Amazon S3**

| Upstream server | Format of URL                                                                                                                                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Format of URL   | `s3ssl://`<bucket>`/`<path>`/`<filename>`.mp4`                                                                                                                                                                                                                                    |
| Example         | `s3ssl://amzn-s3-demo-bucket/filler-videos/main/oceanwaves.mp4`<br>`s3ssl://amzn-s3-demo-bucket/filler-videos/redundant/oceanwaves.mp4`<br>With MediaLive, the S3 bucket name must not use dot<br>notation,<br>which means it mustn't use . (dot) between the words in a<br>name. |
