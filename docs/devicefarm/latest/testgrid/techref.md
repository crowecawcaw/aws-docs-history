# Technical reference

In the W3C WebDriver model, the feature operates as an intermediary node. It provides a means to start, end, and
manage sessions.

Here is the functional flow for using the feature:

1. Use the `createTestGridProject` API to create a project.
2. Use the `createTestGridUrl` API to create a signed WebDriver hub URL.
3. Pass the WebDriver URL to your Selenium `RemoteWebDriver` configuration.
4. Run your tests.
5. Use the `listTestGridSessions` API to retrieve the sessions created in the running of your
   tests.
6. Use the `listTestGridSessionArtifacts` API to collect any artifacts such as Selenium logs or
   video.
