# Create an

account-level transformer policy

Use the steps in this section to create a transformer policy that applies to all
log groups in the account, or to multiple log groups that have log group names that
start with the same string (prefix). You can have as many as 20 account-level
transformer policies in a Region.

You can't create two transformer policies in the same Region that use the same
prefix or have one prefix contained within another. For example, if you create one
transformer policy for the string prefix `/aws/lambda`, you can't create
another with the prefix `/aws`. But you could have one transformer for
`/aws/lambda` and another for `/aws/waf`

###### To create an account-level transformer policy

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Settings** and then
   choose the **Logs** tab.
3. In the **Transformer policy for account** section, choose
   **Create transformer policy**.
4. For **Transformer policy name**, enter a name for your
   new poiicy.
5. For **Select log groups**, do one of the
   following:
   - Choose **All standard log groups** to have the
     transformer policy apply to all Standard Class log groups in the
     account.
   - choose **Log groups by prefix match** to apply
     the policy to a subset of log groups that all have names that start
     with the same string. Then, enter the prefix for these log groups in
     **Selection criteria**.

6. In the **Select parsers** area, use
   **Parsers** to select a parser to include in your
   transformer.

If it is a pre-configured parser for a type of AWS vended log, you don't
have to specify any configuration for it.

If it is a different parser, you need to specify its configuration. For
more information, see the information for that processor in [Configurable
parser-type processors](CloudWatch-Logs-Transformation-Processors.md#CloudWatch-Logs-Transformation-Configurable "CloudWatch-Logs-Transformation-Processors.md#CloudWatch-Logs-Transformation-Configurable"). 7. To add another processor, choose **Select processor**.
Then select the processor that you want in the
**Processor** box, and fill in the configuration
parameters. For information about the configuration parameters, see the
section for that processor in [Processors that you can
use](CloudWatch-Logs-Transformation-Processors.md "CloudWatch-Logs-Transformation-Processors.md").

Remember that processors operate on the log events in the order that you
add them to the transformer. 8. (Optional) To add additional processors, choose **+
Processor** and repeat the previous step. 9. (Optional) At any time, you can test the transformer that you have built
so far on a sample log event. To do so, do one of the following in the
**Transformer preview** section:

    * Select as many as five log groups in **Select log
     groups** and then choose **Load latest log
     events**. Then choose **Test
     transformer**.
    * Copy log events directly into **Sample log
     events** and then choose **Test
     transformer**.The transformed version of the log then appears.

10. When you are finished adding processors and satisfied with the tests on
    sample logs, choose **Save**.
11. When you have finished, choose **Create**.
