# Creating an ID namespace source

(rule-based)

This topic describes the process of creating an ID namespace source using the
**rule-based** method. This method uses matching rules to translate
first-party data from a source to a target in an ID mapping workflow.

###### Note

If the input data is the source, then it must have a schema mapping and an associated
AWS Glue database.

###### To create an ID namespace source (rule-based)

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2. In the left navigation pane, under **Data preparation**, choose
   **ID namespaces**.
3. On the **ID namespaces** page, in the upper right corner, choose
   **Create ID namespace**.
4. For **Details**, do the following:
   1. For **ID namespace name**, enter a unique name.
   2. (Optional) For **Description**, enter an optional
      description.
   3. For **ID namespace type**, choose
      **Source**.

5. For the **ID namespace method**, choose
   **Rule-based**.
6. For **Data input**, choose the **Input type** that
   you want to use and then take the recommended actions.

| Input type                    | Recommended actions                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| An existing schema mapping    | 1. Choose **Schema mapping**.<br>2. Choose the **AWS Region**, **AWS Glue<br>database**, the **AWS Glue table**, and the<br>\*_Schema mapping_<br>• from the dropdown list.<br>You can add up to 19 data inputs.<br>NoteIf your data table has a DELETE column, the schema mapping's type must<br>be `String` and you can't have a `matchKey` and<br>`groupName`. |
| An existing matching workflow | 1. Choose the **Matching workflow**.<br>2. Choose the account that’s associated with the ID namespace: either<br>**Your AWS account\*<br>• or **Another<br>AWS account**.<br>3. Depending on the type of account, select the **Matching<br>workflow name\*<br>• or enter the **Matching workflow<br>ARN**.                                                        |

7. For **Rule parameters**, do the following.
   1. Specify the **Rule controls** by choosing one of the following
      options based on your goal.

   | Your goal                                                                               | Recommended option |
   | --------------------------------------------------------------------------------------- | ------------------ |
   | Allow rules from both the source and the target                                         | **No preference**  |
   | Choose whether a source, target, or both can provide rules in an ID<br>mapping workflow | **Limited rules**  |

   **Rule controls** must be compatible between the source and the
   target to be used in an ID mapping workflow. For example, if a source ID namespace
   limits rules to the target but the target ID namespace limits rules to the source,
   this results in an error. 2. Specify the **Matching rules** by choosing one of the following
   options based on your data input type.

   | Data input type       | Recommended action                                                                                                                           |
   | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Schema mapping**    | Choose **Add another rule\*<br>• to add a matching rule.<br>You can apply up to 25 **Matching rules\*<br>• to define<br>your match criteria. |
   | **Matching workflow** | Choose either **Use rules from matching workflow\*<br>• or<br>**Provide new rules\*<br>• to define your **Matching<br>rules**.               |

8. For **Comparison and matching parameters**, do the
   following.
   1. Specify the **Comparison type** by choosing one of the
      following options based on your goal.

   | Your goal                                                                                                                                                  | Recommended option        |
   | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
   | Allow any comparison type to be used when you create the ID mapping<br>workflow.                                                                           | **No preference**         |
   | Find any combination of matches across data stored in multiple input<br>fields, regardless of whether the data is in the same or different input<br>field. | **Multiple input fields** |
   | Limit comparison within a single input field, when similar data stored<br>across multiple input fields shouldn't be matched.                               | **Single input field**    |
   2. Specify the **Record matching type** by choosing one of the
      following options based on your goal.

   | Your goal                                                                                                                                                           | Recommended option                                                   |
   | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
   | Allow any comparison type to be used when you create the ID mapping<br>workflow.                                                                                    | **No preference**                                                    |
   | Limit the record matching type to store only one matching record in the<br>source for each matched record in the target when you create the ID mapping<br>workflow. | **Limited record matching**<br>and<br>**One source to one target**   |
   | Limit the record matching type to store all matching records in the<br>source for each matched record in the target when you create the ID mapping<br>workflow.     | **Limited record matching**<br>and<br>**Many sources to one target** |

   ###### Note

   You must specify compatible limitations for the source and target ID
   namespaces. For example, if a source ID namespace limits rules to the target but
   the target ID namespace limits rules to the source, this results in an
   error.

9. Specify the **Service access permissions** by choosing an
   **Existing service role name** from the dropdown list.
10. (Optional) To enable **Tags** for the resource, choose
    **Add new tag**, and then enter the **Key** and
    **Value** pair.
11. Choose **Create ID namespace**.
    The ID namespace source is created. You are now ready to [create an
    ID namespace target](create-id-namespace-target.md "create-id-namespace-target.md").
