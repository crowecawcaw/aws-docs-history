# Connecting to a Amazon DCV session using URI

Using a URI automatically opens a locally installed Amazon DCV client with information passed into
from the URI.

Within the URL field of your internet browser, enter the URI in this format: `dcv://hostname[:port]/[?authToken][#sessionId]`

###### Example

For example,
`dcv://203.0.113.1:8443/?authToken=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855#1234567890abcdef0`

Your locally installed client will open with the information prepopulated.

For more information, see [GetSessionConnectionData](../sm-dev/GetSessionConnectionData.md "../sm-dev/GetSessionConnectionData.md")
in the [Amazon DCV Session Manager Developer Guide](../sm-dev.md "../sm-dev.md")
