# Security and access control for the SageMaker Data Agent

###### Topics

- [Required IAM permissions to use SageMaker Data Agent](#data-agent-control-actions "#data-agent-control-actions")

## Required IAM permissions to use SageMaker Data Agent

To use the SageMaker Data Agent in Notebooks or Query Editor, your project role needs
the required IAM permissions. Your role must have the permissions to invoke the following
Amazon DataZone APIs: SendMessage, GenerateCode, StartConversation, GetConversation, and
ListConversations.
