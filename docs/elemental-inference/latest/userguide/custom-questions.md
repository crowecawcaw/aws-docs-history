

# Customer decisions for contextual metadata in Elemental Inference

With customer decisions, Elemental Inference makes your own decisions about each shot, each scene, or both, in a contextual metadata output. You write each decision as a question in a *question set*, and then you attach the question set to the contextual metadata output of a feed. In the API, a feed references the question set in its `customQuestions` setting.

Elemental Inference answers the questions with scores. The answers appear in a `customQuestions` object on the contextual metadata items that the `GetMetadata` operation returns. They appear alongside the built-in classifications, such as the Interactive Advertising Bureau (IAB) categories, Global Alliance for Responsible Media (GARM) ratings, labels, and mood. For more information about contextual metadata, see [Configuring contextual metadata](create-feed-outputs.md#create-feed-console-contextual-metadata).

You manage question sets with the Elemental Inference API, the AWS CLI, or an AWS SDK. The examples in this chapter use the AWS CLI.

**Topics**
+ [Use cases for customer decisions](custom-questions-use-cases.md)
+ [Concepts for customer decisions](custom-questions-concepts.md)
+ [Limits and text rules for question sets](custom-questions-limits.md)
+ [Requirements for the contextual metadata output](custom-questions-output-requirements.md)
+ [Creating a question set](custom-questions-create.md)
+ [Updating the DRAFT of a question set](custom-questions-update.md)
+ [Publishing a question set version](custom-questions-publish.md)
+ [Listing question sets and versions](custom-questions-list.md)
+ [Adding customer decisions to a feed](custom-questions-attach.md)
+ [Getting the answers with GetMetadata](custom-questions-results.md)
+ [Interpreting the answers](custom-questions-interpret.md)
+ [Deleting question set versions and question sets](custom-questions-delete.md)
+ [Tagging and access control for question sets](custom-questions-access.md)