# Artifacts in Device Farm desktop browser testing

Artifacts are created automatically in Device Farm when your tests perform actions like opening or closing a
session.

The following kinds of artifacts are produced:

- Video recording of your test. Recording starts when your session starts and ends when your session
  times out or is closed.

###### Note

For long-running test sessions, videos are split at even intervals. Even test runs that go just
over one of these intervals are still split.

- Selenium logs produced by the Selenium WebDriver.
  Session artifacts have the following properties:

- Type (video, log, other).
- File name.
- Limited lifetime S3-signed URL that can be used to retrieve the artifact.
  A new URL is generated whenever the artifact is requested as a part of an API request. This URL expires after
  an hour.
