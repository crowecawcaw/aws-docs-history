

# Technical reference
<a name="techref"></a>

In the W3C WebDriver model, the feature operates as an intermediary node. It provides a means to start, end, and manage sessions. 

 Here is the functional flow for using the feature: 

1. Use the `createTestGridProject` API to create a project. 

1. Use the `createTestGridUrl` API to create a signed WebDriver hub URL. 

1. Pass the WebDriver URL to your Selenium `RemoteWebDriver` configuration.

1. Run your tests.

1. Use the `listTestGridSessions` API to retrieve the sessions created in the running of your tests.

1. Use the `listTestGridSessionArtifacts` API to collect any artifacts such as Selenium logs or video.