

# Lessons and shared transformation definitions

Continual learning works differently for shared TDs. Lessons for a shared TD always belong to the owner's TD.


| Situation | Lessons the run uses | Lessons the run creates | 
| --- | --- | --- | 
| The consumer runs with Execute permission | None | None | 
| The consumer runs with ExecuteWithLearnings or ExecuteWithLearningsAndPackageDownload | The owner's current lessons for the TD | None | 
| The consumer runs with ExecuteWithLearningsAndContribution and doesn't opt in | The owner's current lessons | None | 
| The consumer runs with ExecuteWithLearningsAndContribution and opts in with --share-learnings | The owner's current lessons | Added to the owner's TD, where they help future runs in every account that uses the owner's lessons | 

A run of a shared TD never adds lessons to the consumer account. A consumer that needs its own lessons can download the TD (if allowed), publish its own TD, and run that.

## Contribute lessons to the owner
<a name="custom-sharing-lessons-contribute"></a>

Contributing is off by default. To contribute lessons from one run, add `--share-learnings`.

```bash
atx custom def exec \
  -n arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade \
  -p ./my-repo --share-learnings
```

Contribution is turned on only by `--share-learnings`, for one run at a time. No setting or environment variable turns it on.

How it works:
+ Before the run, the CLI checks that the share's permission allows contribution and that your IAM principal allows `transform-custom:ContributeKnowledgeItems` on the TD. If either doesn't, the run doesn't start, and the CLI shows an error. For the messages, see [Troubleshooting shared transformation definitions](custom-sharing-troubleshooting.md). To run without contributing, run again without `--share-learnings`.
+ When the check passes, the CLI shows `Learnings from this run will be saved to the owner's account ({{owner-account-id}}).`
+ The service checks the permission again during the run.
+ After the run, continual learning extracts lessons from your run and adds them to the owner's TD. Your repository and run transcripts aren't shared with the owner. The lessons themselves can describe patterns from your code and fixes, and the owner can read, archive, or delete them.
+ Contributed lessons go through the same continual learning processing as every other lesson. It checks them for duplicates, conflicts with existing lessons, unsafe content, and sensitive data.
+ Each contribution is recorded in the owner's AWS CloudTrail log as a `ContributeKnowledgeItems` call on the TD.
+ `--share-learnings` applies only to shared TDs. For your own TDs, the CLI ignores it and shows `--share-learnings only applies to transformation definitions shared with you.`
+ You can't combine `--share-learnings` with `--do-not-learn` (`-d`). The CLI shows `--share-learnings can't be used with --do-not-learn.` and exits before the run.
+ `--do-not-learn` has no other effect on shared TDs, because their runs never add lessons to your account.

Contribution for accounts in the same organization isn't automatic in this release. Each run needs the opt-in.

A contributed lesson doesn't record which account contributed it. You can't tell a contributed lesson apart from one that your own runs created. To see which accounts contributed to your TD, and when, look for `ContributeKnowledgeItems` events in AWS CloudTrail in your account.

**Note**  
**For administrators:** To stop accounts in your organization from contributing lessons to TDs owned outside the organization, use a service control policy (SCP) that denies `transform-custom:ContributeKnowledgeItems` unless the TD belongs to your organization. For more information, see [Identity-based policy examples for sharing](custom-sharing-policy-examples.md).

## Owner's lessons
<a name="custom-sharing-lessons-owner"></a>

As the owner, you manage all of the TD's lessons with `atx custom def learnings`, including lessons that consumers contributed. If you archive a lesson, no runs in any account use it. If you choose a permission that includes lessons, consumers' runs use your current lessons and any lessons that you add later. For more information, see [Continual Learning](custom-workflows.md#custom-continual-learning).