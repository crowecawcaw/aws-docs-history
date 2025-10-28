# Handle application

errors in Amazon Connect Agent Workspace

Apps in Amazon Connect Agent Workspace can communicate errors back to the workspace by either calling
`sendError` or `sendFatalError` on the
`AmazonConnectApp` object. The workspace will shutdown an app if it sends
a fatal error meaning that the app has reached an unrecoverable state and isn’t
functional. When an app sends a fatal error the workspace won’t attempt to go through
the destroy lifecycle handshake and will immediately remove the iframe from the DOM.
Apps should do any clean up required prior to sending fatal errors.
