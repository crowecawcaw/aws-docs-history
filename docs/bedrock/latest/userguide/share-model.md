# Share a model for another account to use

By default, models are only available in the Region and account in which they were created. Amazon Bedrock provides you the ability to share custom models with other accounts so that they can use them. The general process to share a model with another account is as follows:

1. Sign up for an AWS Organizations account, create an organization, and add the account that will share the model and the account that will receive the model to the organization.
2. Set up IAM permissions for the following:
   - The account that will share the model.
   - The model that will be shared.

3. Share the model with the help of AWS Resource Access Manager.
4. The recipient account copies the model to the Region in which they want to use it.

###### Topics

- [Supported Regions and models for model sharing](share-model-support.md "share-model-support.md")
- [Fulfill prerequisites to share models](share-model-prereq.md "share-model-prereq.md")
- [Share a model with another account](share-model-share.md "share-model-share.md")
- [View information about shared models](share-model-view.md "share-model-view.md")
- [Update access to a shared model](share-model-edit.md "share-model-edit.md")
- [Revoke access to a shared model](share-model-revoke.md "share-model-revoke.md")
