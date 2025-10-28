AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Updating a connector using Amazon Q Developer in chat applications

If you're publishing a new alias for a Amazon Bedrock, you must replace the connector to converse with this new version. Existing threads can no longer use the old agent alias. You may also need
to update the roles and policies for your channel to allow the new alias.

###### To update a connector

1. In your chat channel, run `@Amazon Q connector delete `connector_name``.
2. Run `@Amazon Q connector add `connector_name` arn:aws:bedrock:aws-region:111122223333:agent/`AgentID` `AliasID``.
