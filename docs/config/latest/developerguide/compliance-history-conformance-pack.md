# Viewing the Compliance History Timeline for

Conformance Packs for AWS Config

AWS Config supports storing compliance state changes to your conformance packs. This allows you
to view the history of compliance state changes. These compliance state changes are
presented as a timeline. The timeline captures changes as `ConfigurationItems`
over a period of time. You can also use
this
feature to find specific rules within a conformance pack that are
noncompliant.

You can opt in or out to record all resource types in AWS Config. If you have opted to record
all resource types, AWS Config automatically begins recording the conformance pack compliance
history as evaluated by AWS Config Rules. By default, AWS Config records the configuration changes for
all supported resources. You can also select only the specific conformance pack compliance
history resource type: `AWS::Config::ConformancePackCompliance`. Recording for
the `AWS::Config::ConformancePackCompliance` resource type is available at no
additional charge. For more information, see [Recording AWS Resources](select-resources.md#select-resources-console "select-resources.md#select-resources-console").

A conformance pack is compliant if all of the rules in a conformance packs are compliant.
It is noncompliant if any of the rules are not compliant. The compliance status of a
conformance pack is INSUFFICIENT_DATA only if all rules within a conformance pack cannot be
evaluated due to insufficient data. If some of the rules in a conformance pack are compliant
but the compliance status of other rules in that same conformance pack is INSUFFICIENT_DATA,
the conformance pack shows compliant. Compliance for a conformance pack is not evaluated all
at one time. Some rules may take a longer time to evaluate than others. Compliance is evaluated
for groups of rules at a time, continuing in stages until all the rules in a conformance
pack have been evaluated.

## Viewing the Compliance

Timeline

Access the compliance timeline by selecting a specific conformance pack from the
**Conformance pack** main page.

1. Navigate to the **Conformance Pack** page.
2. On the **Conformance Pack** main page, choose a
   specific conformance pack and then choose **Conformance pack
   timeline** .

###### Note

Alternatively, you can use the compliance timeline from the conformance
pack's details page. Choose a conformance pack and choose **View
details** in the **Actions** dropdown. From
this page, choose **Conformance pack
timeline**.

The timeline shows you the history of compliance state changes for a conformance pack.
You can do the following:

1. Expand a compliance change to view the line-by-line compliance status of each
   rule within a conformance pack.
2. From the expanded view, choose a specific rule to view its details
   page.
