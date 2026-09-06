

# Enable Connect Customer quick responses in a custom Contact Control Panel (CCP)
<a name="enable-qr-search"></a>

To enable your agents to use quick responses for an embedded or custom CCP, you use the [ Connect Customer Streams library](https://github.com/amazon-connect/amazon-connect-streams) on GitHub to call the [SearchQuickResponse](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SearchQuickResponses.html) API and return a list of quick response search results to CCP. For more information, see [Connect Customer Streams Documentation](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#quick-responses-apis) on Github.

**Note**  
To prevent search API misuse, we implemented default values for the following request parameters:  
`debounceTime` – 250ms between subsequent `SearchQuickResponse` API calls
`maxSearchResults` – 25
Search priority order:  
`shortcut key`
`name`
`content`
`description`

For information about the agent's experience using quick responses, see [Search for quick responses to customers](search-qr-ccp.md).