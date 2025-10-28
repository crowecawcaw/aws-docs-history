# Advanced workflow concepts in Amazon SWF

The e-commerce example in the section represents a
simplified workflow scenario. In reality, you are likely to want your workflow to do concurrent tasks (send an order
confirmation email while authorizing a credit card), record major events (all items are packed), update the order
with changes (add or remove an item), and make other more advanced decisions as part of your workflow execution. This
section describes advanced workflow concepts that you can use to construct your workflows.

###### Advanced concepts

- [Versioning](swf-dev-adv-versioning.md "swf-dev-adv-versioning.md")
- [Signals](swf-dev-adv-signals.md "swf-dev-adv-signals.md")
- [Child workflows](swf-dev-adv-child-workflows.md "swf-dev-adv-child-workflows.md")
- [Markers](swf-dev-adv-markers.md "swf-dev-adv-markers.md")
- [Tags](swf-dev-adv-tags.md "swf-dev-adv-tags.md")
- [Exclusive choice](swf-dg-exclusive-choice.md "swf-dg-exclusive-choice.md")
- [Timers](swf-dg-timers.md "swf-dg-timers.md")
- [Cancelling activity tasks](swf-dg-task-cancellation.md "swf-dg-task-cancellation.md")
