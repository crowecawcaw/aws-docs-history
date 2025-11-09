# Supported capabilities, browsers, and platforms in Device Farm desktop browser

testing

This topic lists the supported configurations of browsers and operating systems. An exception is raised if you
request a browser and operating system combination that is not supported.

Values here are suitable for parametrized test suites.

## Supported browsers

The following browsers are supported:

| Name                      | `browserName` value | Supported platforms |
| ------------------------- | ------------------- | ------------------- |
| Google Chrome             | `chrome`            | `windows`           |
| Mozilla Firefox           | `firefox`           | `windows`           |
| Microsoft Edge (Chromium) | `MicrosoftEdge`     | `windows`           |

###### Note

AWS Device Farm no longer supports Microsoft Internet Explorer because Microsoft has stopped providing security updates and
technical support for older versions of Internet Explorer. For more information, see [Microsoft's announcement of
IE end of support](http://microsoft.com/en-us/microsoft-365/windows/end-of-ie-support "http://microsoft.com/en-us/microsoft-365/windows/end-of-ie-support").

## Supported capabilities

The desktop browser testing feature does not implement all capabilities outlined in the [W3C WebDriver documentation](https://w3c.github.io/webdriver/#capabilities "https://w3c.github.io/webdriver/#capabilities"). Extension
capabilities used by Device Farm desktop browser testing are prefixed with `aws:`. The following capabilities are used by
the Device Farm WebDriver node:

`browserName` (string, required, no default)

Name of the browser to use for the session. Must be one of the [supported browsers](#techref-support-browsers "#techref-support-browsers"). _This
value is always lowercase._

`browserVersion` (string, required)

Version of the browser to launch; one of `latest`, `latest-1`,
`latest-2`

###### Note

Device Farm desktop browser testing does not support requesting specific releases of browsers.

`platform` (string, optional, defaults to `windows`)

Platform (operating system) to use when creating the session. Must be one of the [supported platforms](#techref-support-platforms "#techref-support-platforms").

`aws:maxDurationSecs` (integer, optional, defaults to `900`)

Maximum duration of the session before it is forcibly closed, in seconds. Range:
`180` to `2400`.

`aws:idleTimeoutSecs` (integer, optional, defaults to `120`)

Maximum delay between WebDriver commands before the session is forcibly closed. Range:
`30` to `900`

The following are not allowed:

`w3c` (in Chrome)

Setting this capability to `false` will result in an error.

`binary`

Setting this capability will result in an error.

`args`

The following browser command line parameters are not allowed:

- `--headless` (Chrome)
- `-headless` (Firefox)
- `--user-data-dir`
- `--no-sandbox` (Chrome and Firefox)

All other capabilities are passed directly to the target browser-specific WebDriver. These arguments are
not officially supported by Device Farm. Their use might result in unexpected behavior.

## Supported platforms

The following platforms are supported:

| Name              | `platform` value |
| ----------------- | ---------------- |
| Microsoft Windows | `windows`        |
