# Deleting Evaluation Results from AWS Config

Rules

After AWS Config evaluates your rule, you can see the evaluation results on the
**Rules** page or the **Rules details** page for the
rule. If the evaluation results are incorrect or if you want to evaluate again, you can
delete the current evaluation results for the rule. For example, if your rule was
incorrectly evaluating your resources or you recently deleted resources from your account,
you can delete the evaluation results and then run a new evaluation.

Deleting Evaluation Results (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the AWS Management Console menu, verify that the Region selector is set to an
   AWS Region that supports AWS Config rules. For the list of supported
   Regions, see [AWS Config
   Regions and Endpoints](../../../general/latest/gr/rande.md#awsconfig_region "../../../general/latest/gr/rande.md#awsconfig_region") in the
   _Amazon Web Services General Reference_.
3. In the navigation pane, choose **Rules**. The
   **Rules** page shows the name, associated
   remediation action, and compliance status of each rule.
4. Choose a rule from the table.
5. From the **Actions** dropdown list, choose
   **Delete results**.
6. When prompted, type **Delete** (this
   entry is case sensitive), and then choose **Delete**.
   After you delete an evaluation, you cannot retrieve it.
7. After the evaluation results are deleted, you can manually start a new
   evaluation.

Deleting Evaluation Results (CLI)

- Use the **delete-evaluation-results** command.

```
$ **aws configservice delete-evaluation-results --config-rule-name `ConfigRuleName`**
```

AWS Config deletes the evaluation results for the rule.

Deleting Evaluation Results (API)
Use the [DeleteEvaluationResults](../APIReference/API_DeleteEvaluationResults.md "../APIReference/API_DeleteEvaluationResults.md") action.
