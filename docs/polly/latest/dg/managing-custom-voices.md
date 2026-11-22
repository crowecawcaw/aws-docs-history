

# Managing custom voices

You can list, view, and delete your custom voices.

## Custom voice statuses and IDs
<a name="managing-custom-voices-ids"></a>

When you create a custom voice, Amazon Polly returns it in `pending` status and then creates it.

A custom voice has one of the following statuses:

pending  
Amazon Polly is creating the voice. You can't use or delete the voice yet.

active  
The voice is ready. You can use it to synthesize speech.

failed  
Amazon Polly couldn't create the voice. The `StatusReason` field of the voice contains information about the failure. You can delete the voice and create it again.

Each custom voice has an ID and an Amazon Resource Name (ARN). Amazon Polly assigns the ID. It consists of `vc-` followed by hexadecimal characters, for example `vc-9a8fa85dd3`. You use the ID as the `VoiceId` in synthesis requests and in the `GetVoice` and `DeleteVoice` operations. You can't use the ARN in these requests. You use the ARN to tag the voice. The ARN has the following format:

```
arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}
```

The name that you give a voice is a label. It doesn't need to be unique, and you can't use it to identify the voice in a request.

## Listing and viewing custom voices
<a name="managing-custom-voices-list"></a>

To list and view custom voices, you must have the `polly:DescribeVoices` and `polly:GetVoice` permissions.

The `DescribeVoices` operation returns your custom voices in every status, together with the voices that Amazon Polly provides. Your custom voices have `Origin` set to `customer`.

------
#### [ Console ]<a name="managing-custom-voices-list-console"></a>

**To view your custom voices (console)**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Voice Cloning** tab. The tab lists your custom voices in the current Region.

1. (Optional) To filter the list, enter a name, voice ID, status, or locale in the search box.

1. To view the details of a voice, do one of the following:
   + Choose its **Voice ID** to open the voice details page.
   + Select the check box next to its name to show the details in a split panel.

------
#### [ AWS CLI ]

The following AWS CLI command lists only your custom voices:

```
aws polly describe-voices \
--region us-east-1 \
--query "Voices[?Origin=='customer']"
```

------

For each custom voice, `DescribeVoices` returns the origin, ID, name, status, language, supported engines, and creation time. To see all the details of a voice, use `GetVoice`. The details include the ARN, the recordings, the key, and information about a failure. `GetVoice` doesn't return the audio of the recordings. To see the tags of a voice, use `ListTagsForResource`.

## Deleting a custom voice
<a name="managing-custom-voices-delete"></a>

To delete a voice, you must have the `polly:DeleteVoice` permission.

You can delete a voice in `active` or `failed` status. You can't delete a voice in `pending` status. Wait until creation ends.

------
#### [ Console - list of voices ]<a name="managing-custom-voices-delete-console"></a>

**To delete custom voices from the list of voices**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Voice Cloning** tab.

1. Select the check box next to each voice that you want to delete.

1. Choose **Delete**.

1. Enter the confirmation text and then choose **Delete** to delete the voices, or **Cancel** to keep them.

------
#### [ Console - voice details page ]<a name="managing-custom-voices-delete-console-details"></a>

**To delete a custom voice from the voice details page**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Voice Cloning** tab.

1. In the list of voices, choose the **Voice ID** of the voice that you want to delete. The voice details page opens.

1. Choose **Delete**.

1. Enter the confirmation text and then choose **Delete** to delete the voice, or **Cancel** to keep it.

------
#### [ AWS CLI ]

The following AWS CLI command deletes a custom voice. It prints nothing when it succeeds.

```
aws polly delete-voice \
--region us-east-1 \
--voice-id {{vc-9a8fa85dd3}}
```

------

Amazon Polly deletes the voice immediately. You can't restore a deleted voice. After you delete it, requests that use its ID fail with `ResourceNotFoundException`. You can delete a voice even if its AWS KMS key is disabled, scheduled for deletion, or deleted.