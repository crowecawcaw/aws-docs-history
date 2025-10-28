# How Amazon Q works

with Confluence (Cloud) access and refresh tokens

The following are important points to note about using Confluence (Cloud) access
and refresh tokens with Amazon Q:

- If a Confluence (Cloud) access token-refresh token pair you use to connect
  to Amazon Q are expired or invalid, the Amazon Q sync
  process fails. If this happens, you need to generate and provide a new pair
  of tokens.
- If your access token is valid but you have an invalid refresh token,
  Amazon Q will sync data until the access token expires (up to
  1 hour). After the access token expires, you won't be able to re-generate an
  access token-refresh token pair using the expired refresh token. When both
  access token and refresh token expire, the Amazon Q
  Confluence (Cloud) data source connector stops syncing.
- If an access token expires during the Confluence (Cloud) connector sync
  process, the connector internally regenerates a new pair of tokens using the
  existing refresh token (if the provided refresh token is valid). After
  regenerating the new pair of tokens, the old pair is invalidated by
  Confluence (Cloud) and can't be re-used. To sync documents again after the
  connector auto-regenerates tokens, you must provide a new access
  token-refresh token pair.
- If you use OAuth, select **Rotate secret** if you want
  Amazon Q to rotate the secret automatically so that you don’t have to
  manually update the secret every time before you sync.
- As a best practice, use Confluence (Cloud) OAuth and the **Rotate
  secret** feature for the Amazon Q connector.
