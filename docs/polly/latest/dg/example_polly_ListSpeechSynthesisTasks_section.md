# Use `ListSpeechSynthesisTasks` with an AWS SDK or CLI

The following code examples show how to use `ListSpeechSynthesisTasks`.

CLI

**AWS CLI**

**To list your speech synthesis tasks**

The following `list-speech-synthesis-tasks` example lists your speech synthesis tasks.

```
`aws polly list-speech-synthesis-tasks`

```

Output:

```
{
    "SynthesisTasks": [
        {
            "TaskId": "70b61c0f-57ce-4715-a247-cae8729dcce9",
            "TaskStatus": "completed",
            "OutputUri": "https://s3.us-west-2.amazonaws.com/amzn-s3-demo-bucket/70b61c0f-57ce-4715-a247-cae8729dcce9.mp3",
            "CreationTime": 1603911042.689,
            "RequestCharacters": 1311,
            "OutputFormat": "mp3",
            "TextType": "text",
            "VoiceId": "Joanna"
        }
    ]
}
```

For more information, see [Creating long audio files](longer-cli.md "longer-cli.md") in the _Amazon Polly Developer Guide_.

- For API details, see
  [ListSpeechSynthesisTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-speech-synthesis-tasks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-speech-synthesis-tasks.html")
  in _AWS CLI Command Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ply#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ply#code-examples").

```
    TRY.
        " Only pass optional parameters if they have values
        IF iv_max_results IS NOT INITIAL AND iv_status IS NOT INITIAL.
          oo_result = lo_ply->listspeechsynthesistasks(
            iv_maxresults = iv_max_results
            iv_status = iv_status ).
        ELSEIF iv_max_results IS NOT INITIAL.
          oo_result = lo_ply->listspeechsynthesistasks(
            iv_maxresults = iv_max_results ).
        ELSEIF iv_status IS NOT INITIAL.
          oo_result = lo_ply->listspeechsynthesistasks(
            iv_status = iv_status ).
        ELSE.
          oo_result = lo_ply->listspeechsynthesistasks( ).
        ENDIF.
        DATA(lt_tasks) = oo_result->get_synthesistasks( ).
        DATA(lv_count) = lines( lt_tasks ).
        MESSAGE |Found { lv_count } synthesis tasks| TYPE 'I'.
      CATCH /aws1/cx_plyinvalidnexttokenex.
        MESSAGE 'Invalid NextToken.' TYPE 'E'.
      CATCH /aws1/cx_plyservicefailureex.
        MESSAGE 'Service failure occurred.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [ListSpeechSynthesisTasks](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Polly with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
