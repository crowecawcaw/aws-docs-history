

# How the playground works

The playground runs every job in your own AWS account. Both kinds of jobs use two resources there, and the console sets up both for you:
+ An IAM service role named `ElementalInferencePlaygroundServiceRole`. You create it once, from the **Create job** page, and it applies to every AWS Region. For more information, see [Permissions](playground-permissions.md).
+ An MediaConvert queue named `ElementalInferencePlaygroundQueue`. The console creates it the first time that you run a job in a Region. The queue lets its jobs use only one Elemental Inference feed at a time, so Smart Cropping jobs run one at a time and use at most one feed from your Elemental Inference quota. Don't delete this queue. The playground lists its jobs from it.

A Smart Cropping job uses a feed that MediaConvert creates and deletes. A preview creates its own temporary feed in your account, streams the clip to it from your browser, and deletes it when the preview ends.

A preview saves its clip segments and results in a folder named `ei-preview-{{run-id}}/` in your output location, so that you can reopen it later without running it again.