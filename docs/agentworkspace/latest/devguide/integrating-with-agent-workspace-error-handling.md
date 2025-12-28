# Handle application

errors in Amazon Connect Agent Workspace

Applications can communicate errors back to the Amazon Connect agent workspace by either
calling `sendError` or `sendFatalError` on the `AmazonConnectApp`
object. The agent workspace will shutdown an app if it sends a fatal error meaning that
the app has reached an unrecoverable state and isn’t functional. When an app sends a
fatal error the agent workspace won’t attempt to go through the destroy lifecycle
handshake and will immediately remove the iframe from the DOM. Apps should do any clean
up required prior to sending fatal errors.
