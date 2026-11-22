

# How a feed uses a question set version

In a contextual metadata output, you name a question set and a version separately for shots and for scenes. The version is either `DRAFT` or a published version number. The shot and scene questions can come from different question sets, from different versions of the same set, or from the same version.

A feed that uses a published version always gets answers to the same questions, because a published version never changes. A feed that uses `DRAFT` picks up your edits to `DRAFT`, but not immediately. A running feed can keep answering with the earlier `DRAFT` questions for a while.

After a change, answers for a shot or scene that is already in progress might still come from the previous version until that shot or scene ends. This applies when you edit `DRAFT`, and when you update the feed to use a different version.

We recommend that you use a published version in production, for stable and reproducible answers. Use `DRAFT` while you develop and test your questions.