# Known limitations for the Drupal connector

Amazon Q Business Drupal connector has the following known
limitations:

- Drupal APIs have no official throttling limits.
- Java SDKs are not available for Drupal.
- Drupal data can be fetched only using native JSON API’s.
- Content types not associated with any Drupal
  **View** cannot be crawled.
- You need administrator access to crawl data from Drupal
  **Blocks**.
- There is no JSON API available to create the user defined content type using
  HTTP verbs.
- The document body and comments for **Articles**,
  **Basic pages**, **Basic blocks**, user
  defined content type, and user defined block type, are displayed in HTML format.
  If the HTML content is not well-formed, then the HTML related tags will appear
  in the document body and comments and will be visible in Amazon Kendra
  search results.
- Content types and **Block** types without description or body
  will not be ingested into Amazon Q. Only
  **Comments** and **Attachments** of such
  **Content** or **Block** types will be
  ingested into your Amazon Q index.
