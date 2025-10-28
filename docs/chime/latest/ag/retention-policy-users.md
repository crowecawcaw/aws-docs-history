**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# How retention policies affect Amazon Chime

users

The retention policies that Enterprise account administrators set affect Amazon Chime
users differently, depending on whether the users are part of the same Enterprise
account, a different Enterprise account, a Team account, or whether the users are
not members of any account.

###### Enterprise member chat conversations

The following table shows how retention policies affect chat conversations for
Enterprise account members.

| If the chat conversation includes...                        | The retention policy is...                    |
| ----------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Only other members of the user’s Enterprise account         | Set by the user’s administrator               |
| Anyone outside of the user’s Enterprise account             | Automatically set to 90 days                  | ###### Enterprise member chat rooms The following table shows how retention policies affect chat rooms for Enterprise account members.                                                                                                                                                                                                                                                                                                             |
| If the chat room is created by...                           | The retention policy is...                    |
| ---                                                         | ---                                           |
| A member of the user’s Enterprise account                   | Set by the user’s administrator               |
| Another Enterprise account member                           | Set by the other account’s administrator      |
| A non-Enterprise account member                             | Not applicable                                | ###### Team member chat conversations The following table shows how retention policies affect chat conversations for Team account members.                                                                                                                                                                                                                                                                                                         |
| If the chat conversation includes...                        | The retention policy is...                    |
| ---                                                         | ---                                           |
| Only users who are not members of an Enterprise account     | Not applicable                                |
| At least one member of an Enterprise account                | Automatically set to 90 days                  | ###### Team member chat rooms The following table shows how retention policies affect chat rooms for Team account members.                                                                                                                                                                                                                                                                                                                         |
| If the chat room is created by ...                          | The retention policy is...                    |
| ---                                                         | ---                                           |
| A Team account user                                         | Not applicable                                |
| Anyone who is not an Enterprise account member              | Not applicable                                |
| A member of an Enterprise account                           | Set by the Enterprise account’s administrator | Amazon Chime users who are not members of an Enterprise or Team account are only subject to chat room retention policies in chat rooms that are created by a member of an Enterprise account. ###### Chat conversations with recipients who do not belong to an Enterprise or Team account The following table shows how retention policies affect chat conversations for users who are not members of an Amazon Chime Enterprise or Team account. |
| If the chat conversation includes...                        | The retention policy is...                    |
| ---                                                         | ---                                           |
| Only users who are not members of an Enterprise account     | Not applicable                                |
| At least one member of an Enterprise account                | Automatically set to 90 days                  | ###### Chat rooms created by users who do not belong to an Enterprise or Team account The following table shows how retention policies affect chat rooms for users who are not members of an Amazon Chime Enterprise or Team account.                                                                                                                                                                                                              |
| If the chat room is created by ...                          | The retention policy is...                    |
| ---                                                         | ---                                           |
| A user who is not a member of an Enterprise or Team account | Not applicable                                |
| A Team account user                                         | Not applicable                                |
| A member of an Enterprise account                           | Set by the Enterprise account’s administrator |
