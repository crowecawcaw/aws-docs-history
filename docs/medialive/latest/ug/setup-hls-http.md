# Obtain information

Obtain the following information from the operator at the upstream system:

- The locations (URLs) on the upstream server where the M3U8 manifest files
  are stored.

There are two URLs for a standard-class input, or one URL for a
single-class input. For information about input classes and their uses, see
[Choosing the channel class and input
class](class-channel-input.md "class-channel-input.md").

See the tables later in this section for the URL format and for examples.

Make a note of the full URLs.

- The user name and password (credentials) to access the upstream server, if
  the upstream system requires authenticated requests, and to access the
  license server, if the [HLS source is
  encrypted](uss-obtain-info.md "uss-obtain-info.md"). You might need credentials for the upstream system, or
  for the license server, or both.

If you need credentials for both, the credentials must be identical for
both servers. When you [discussed any encryption requirements](planning-hls-input-encrypted.md "planning-hls-input-encrypted.md") with the upstream system,
you should have made sure that the license server uses the same credentials
as the upstream system.

Note that these user credentials relate to user authentication, not to the
protocol. User authentication is about whether the upstream system or
license server will accept your request. The protocol is about whether the
request is sent over a secure connection.
**Upstream server is an HTTP or HTTPS server**

|               |                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| Format of URL | `http//:<web<br>server>[:port]/<path>/<file>.m3u8`or`https//:<web<br>server>[:port]/<path>/<file>.m3u8` |
| Example       | `https://203.0.113.13/sports/curling.m3u8`<br>and`https://198.51.100.54/sports/curling.m3u8`            |

**Upstream server is AWS Elemental MediaStore**

|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Format of URL | `mediastoressl://<data endpoint for<br>container>/<path>/<file>.m3u8`                                                                                                                                                                                                                                                                                                                                                                          |
| Example       | Assume that the data endpoint for the container for one of the<br>content sources is the following:<br>`eri39n.data.mediastore.us-west-2.amazonaws.com`.<br>Assume that the `M3U8` file is called<br>`curling.m3u8`,<br>and it is stored in the container, in the path<br>`sports/canada`.<br>The URL for one of the content sources would be:<br>`mediastoressl://eri39n.data.mediastore.us-west-2.amazonaws.com/sports/canada/curling.m3u8`. |

**Upstream server is Amazon S3**

| Upstream server | Format of URL                                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Format of URL   | `s3ssl://<bucket>/<path>/<file>.m3u8`                                                                                   |
| Example         | `s3ssl://amzn-s3-demo-bucket/movies/main/mlaw.m3u8`<br>and<br>`s3ssl://amzn-s3-demo-bucket1/movies/redundant/mlaw.m3u8` |
