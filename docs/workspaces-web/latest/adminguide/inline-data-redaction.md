# Inline data redaction in Amazon WorkSpaces Secure Browser

By adding inline data redaction to a portal, you can automatically predict and redact
certain data from a string of text displayed in web pages. You can create redaction policies by
choosing from built-in patterns (such as social security numbers or credit card numbers), or
create their own custom data types using regular expression and keywords. Policies include
configurable levels of enforcement and controls for the URLs where redaction should be enforced.

The following components determine when data is redacted:

- **Data Protection Settings** - Data Protection Settings is the name of
  the resource that includes your data types and enforcement criteria. To use this resource,
  first create your settings, then associate them to a portal. When users launch a session, your
  settings are enforced during the session.
- **In-session browser extension** - When you associate redaction settings
  with your portal, the session browser will launch with a system-enforced browser extension
  that enforces your settings. Data Protection Settings enforce redaction through pattern
  matching (Regular Expressions) and keyword searching following your confidence level and URL
  enforcement configuration. Content is predicted from text strings and redacted before
  displayed on the screen. The extension also sets related browser policies that govern users'
  ability to bypass redaction (such as disabled private browsing, access to developer tools, and
  network inspection).
  The following Chrome browser policy changes are enforced by the in-session browser
  extension. For more information, see [Chrome Enterprise policy list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/").

- Enforce browser policy to prevent users from viewing the session without
  redaction:
  - [IncognitoModeAvailability](https://chromeenterprise.google/policies/#IncognitoModeAvailability "https://chromeenterprise.google/policies/#IncognitoModeAvailability") = 1
  - [DeveloperToolsAvailability](https://chromeenterprise.google/policies/#DeveloperToolsAvailability "https://chromeenterprise.google/policies/#DeveloperToolsAvailability") = 2
  - [BrowserAddPersonEnabled](https://chromeenterprise.google/policies/#BrowserAddPersonEnabled "https://chromeenterprise.google/policies/#BrowserAddPersonEnabled") = false
  - [BrowserGuestModeEnabled](https://chromeenterprise.google/policies/#BrowserGuestModeEnabled "https://chromeenterprise.google/policies/#BrowserGuestModeEnabled") = false

- The extension also prevents users from downloading HTML files from URLs that are
  enforcing data protection settings by canceling the download event.
  In general, you should use redaction with private, structured websites (such as your
  customer management tools, ticketing systems, or wikis), and not for unstructured public
  browsing (such as Facebook or Google). You can choose from built-in data types (see below for
  the full list), or define custom data types using your own regular expression values and
  keywords. Administrators are responsible for testing and validating that each data type,
  confidence level, and URL enforcement are working as expected. AWS cannot guarantee
  compatibility with custom websites or applications provided by third parties.

WorkSpaces Secure Browser does not currently support redaction of supported or custom data types in non-text
formats, including text in the following formats:

- Images, such as JPEG, PNG, or GIF
- Web pages that enable users to use dynamic word processing or editing, such as Google
  Docs or Sheets
- Audio or video streams accessed in the browser, such as a YouTube videos
- PDFs viewed by the Chrome browser
  Do not use redaction for content in an unsupported format. Administrators are responsible
  for validating site and content compatibility prior to granting users access to content they
  intend to be redacted.
