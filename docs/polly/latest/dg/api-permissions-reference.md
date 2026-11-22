

# Amazon Polly API Permissions: Actions, Permissions, and Resources Reference

When you're setting up a permissions policy that you can attach to an IAM identity (identity-based policies), you can use the following table as a reference. The table lists each Amazon Polly API operation, the corresponding actions for which you can grant permissions to perform the action, and the AWS resource for which you can grant the permissions. You specify the actions in the policy's `Action` field, and you specify the resource value in the policy's `Resource` field. 

You can use AWS-wide condition keys in your Amazon Polly policies to express conditions. For a complete list of AWS-wide keys, see [available keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*. 

**Note**  
To specify an action, use the `polly` prefix followed by the API operation name (for example, `polly:GetLexicon`).

Use the scroll bars to see the rest of the table.




**Amazon Polly API and Required Permissions for Actions**  

| Amazon Polly API Operations | Required Permissions (API Actions) | Resources | 
| --- | --- | --- | 
| [CreateVoice](API_CreateVoice.html) | `polly:CreateVoice`<br />If the request includes `Tags`, also `polly:TagResource`. | `arn:aws:polly:{{region}}:{{account-id}}:voice/*` | 
| [DeleteLexicon](API_DeleteLexicon.html) | `polly:DeleteLexicon` | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}` | 
| [DeleteVoice](API_DeleteVoice.html) | `polly:DeleteVoice` | `arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}` | 
| [DescribeVoices](API_DescribeVoices.html) | `polly:DescribeVoices` | `*` | 
| [GetLexicon](API_GetLexicon.html) |  polly:GetLexicon  | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}` | 
| [GetVoice](API_GetVoice.html) | `polly:GetVoice` | `arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}` | 
| [ListLexicons](API_ListLexicons.html) | `polly:ListLexicons` | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/*` | 
| [ListTagsForResource](API_ListTagsForResource.html) | `polly:ListTagsForResource` | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}`<br />`arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}` | 
| [PutLexicon](API_PutLexicon.html) | `polly:PutLexicon`<br />If the request includes `Tags`, also `polly:TagResource`. | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}` | 
| [SynthesizeSpeech](API_SynthesizeSpeech.html) | `polly:SynthesizeSpeech` | `*`, or `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}` (if lexicons are specified in the request)<br />Authorized against each lexicon in `LexiconNames`. A request without lexicons isn't associated with a lexicon resource, so a statement that is scoped to lexicon ARNs doesn't match it. The same applies to `StartSpeechSynthesisTask` and `StartSpeechSynthesisStream`.<br />`arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}` (if `VoiceId` is a custom voice). A statement that is scoped only to lexicon ARNs doesn't allow synthesis with a custom voice. The same applies to `StartSpeechSynthesisTask` and `StartSpeechSynthesisStream`. | 
| [TagResource](API_TagResource.html) | `polly:TagResource` | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}`<br />`arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}` | 
| [UntagResource](API_UntagResource.html) | `polly:UntagResource` | `arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}`<br />`arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}` | 

Amazon Polly supports Identity-based policies for actions at the resource-level. Therefore, the `Resource` value is indicated by the ARN. For example: `arn:aws:polly:{{us-east-2}}:{{account-id}}:lexicon/*` as the `Resource` value specifies permissions on all owned lexicons within the `us-east-2` Region.

Because Amazon Polly doesn't support permissions for actions at the resource-level, most policies specify a wildcard character (\*) as the `Resource` value. However, if it is necessary to limit permissions to a specific Region this wildcard character is replaced with the appropriate ARN: `arn:aws:polly:{{region}}:{{account-id}}:lexicon/*. ` 

