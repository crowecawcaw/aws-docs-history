# Enable Amazon Connect quick responses in a custom Contact Control Panel

(CCP)

To enable your agents to use quick responses for an embedded or custom CCP, you use the
[Amazon Connect Streams
library](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams") on GitHub to call the [SearchQuickResponse](../../../amazon-q-connect/latest/APIReference/API_SearchQuickResponses.md "../../../amazon-q-connect/latest/APIReference/API_SearchQuickResponses.md") API and return a list of quick response search results to CCP. For
more information, see [Amazon Connect Streams Documentation](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#quick-responses-apis "https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#quick-responses-apis") on Github.

###### Note

To prevent search API misuse, we implemented default values for the following request
parameters:

- `debounceTime` – 250ms between subsequent
  `SearchQuickResponse` API calls
- `maxSearchResults` – 25
- Search priority order:

      1. `shortcut key`
      2. `name`
      3. `content`
      4. `description`

  For information about the agent's experience using quick responses, see [Search for quick responses to
  customers](search-qr-ccp.md "search-qr-ccp.md").
