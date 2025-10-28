# Using lenses in AWS WA Tool

In AWS Well-Architected Tool, you can use lenses to consistently measure your architectures against best
practices and identify areas for improvement. The **AWS Well-Architected Framework
Lens** is automatically applied when a workload is defined.

A workload can have one or more lenses applied. Each lens has its own set of questions,
best practices, notes, and improvement plan.

There are two kinds of lenses that can be applied to your workloads: **Lens Catalog** lenses and **Custom lenses**.

- **[Lens Catalog](lens-catalog.md "lens-catalog.md"):** Official lenses that are created and maintained by AWS. The Lens Catalog is available to all users and does not require any additional installation to use.
- **[Custom lenses](lenses-custom.md "lenses-custom.md"):** User-defined lenses that are not AWS official content. You can [create custom lenses](lenses-create.md "lenses-create.md") with your own pillars, questions, best practices, and
  improvement plans, as well as [share custom lenses](lenses-sharing.md "lenses-sharing.md") with other AWS accounts.
  Five lenses can be added at a time to a workload, with a maximum of 20 lenses applied to one workload.

If a lens is removed from a workload, the data associated with the lens is retained. The
data is restored if you add the lens back to the workload.
