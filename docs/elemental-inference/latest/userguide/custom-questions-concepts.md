

# Concepts for customer decisions

The following concepts describe how question sets work.

Question set  
A named resource that contains your questions. Each question set has an ID of 19 lowercase letters and digits, and an ARN in the following format:  

```
arn:aws:elemental-inference:{{region}}:{{account-id}}:question-set/{{id}}
```
A question set has one editable working copy, called `DRAFT`, and any number of published versions, up to the limit. For more information, see [Limits and text rules for question sets](custom-questions-limits.md).

DRAFT  
The working copy of the question set. Elemental Inference creates `DRAFT` when you create the question set. You change `DRAFT` in place with the `UpdateQuestionSet` operation. You can't delete `DRAFT` by itself. Elemental Inference deletes it only when you delete the question set.

Published version  
An unchangeable copy of `DRAFT`. When you publish, Elemental Inference copies `DRAFT` into the next version number: 1, 2, 3, and so on. You can't change a published version. Elemental Inference never reuses a version number, even after you delete that version.

Latest version  
The `latestVersion` field contains the highest version number that you have published. It's absent until you publish the first version. If you delete the highest version, `latestVersion` doesn't change, so it can name a deleted version.

sha256  
A hash of 64 lowercase hexadecimal characters. Elemental Inference computes it from the name of the question set and its questions at that version. Identical content always has an identical `sha256` value. The `sha256` value appears in the responses of the question set operations and on every answer. Use it to tell which questions produced an answer.

Version description  
An optional description that you set when you publish a version. You can't change it later. `DRAFT` has no description. The description doesn't affect the `sha256` value.

References  
The `references` field lists the IDs of the feeds that use a specific version. It appears in the responses of the `GetQuestionSet`, `CreateQuestionSet`, `UpdateQuestionSet`, and `CreateQuestionSetVersion` operations.