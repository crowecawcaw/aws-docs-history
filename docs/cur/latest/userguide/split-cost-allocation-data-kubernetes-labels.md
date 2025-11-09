# Using Kubernetes

labels for cost allocation in EKS

Split cost allocation data supports Kubernetes labels as cost allocation tags for
Amazon EKS clusters. While these labels are automatically imported as user-defined cost
allocation tags, they require activation at the management account level. Once
activated, you can use them to attribute pod-level costs in your Cost and Usage Reports (CUR)
using custom attributes such as cost center, application, business unit, and
environment.

This feature helps organizations accurately track and allocate costs in shared EKS
environments across teams, projects, or departments. Using Kubernetes labels, you
can allocate your Kubernetes costs based on your specific business requirements and
organizational design.

## Prerequisites

As prerequisites for using Kubernetes labels with split cost allocation
data:

- You need to enable split cost allocation data in the AWS Billing and
  Cost Management console. This must be enabled at the management account
  level. For details, see [Enabling split cost allocation
  data](enabling-split-cost-allocation-data.md "enabling-split-cost-allocation-data.md").
- You need an EKS cluster for which you want to track split cost
  allocation data. This can be an existing cluster, or you can create a
  new one. For more information, see [Create an Amazon EKS cluster](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") in the _Amazon EKS User
  Guide_.
- You must have labels assigned to your pods in the EKS cluster. For
  more information on how to create labels in Kubernetes, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ "https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/") in the _Kubernetes Documentation_.

## Working with Kubernetes labels in

EKS

Split cost allocation data supports up to 50 Kubernetes labels per pod, which
are sorted alphabetically before being imported as cost allocation tags. Any
labels beyond the first 50 are automatically discarded. If you need to add a new
cost allocation tag after reaching the 50-label limit, you must first remove an
existing label and ensure your new label falls within the first 50 when
alphabetically sorted.

###### Note

Some AWS managed services automatically add labels to EKS pods. These
labels count toward the 50-label limit per pod and will appear on your cost
allocation tags page.

While Kubernetes labels have no size restrictions, cost allocation tags
have specific character limits: 128 characters for tag keys and 256
characters for tag values. Labels that exceed these character limits will be
discarded and not presented as cost allocation tags. It's recommended to
create labels that follow these character limits for cost allocation
purposes.

The imported Kubernetes labels appear as cost allocation tags and must be
activated at the payer account level. For more information on cost allocation
tags and activation, see [Using user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md"). The following cost
allocation tag limits apply: 50 user-defined tags per resource and 500
user-defined tags per payer account. System-generated tags do not count toward
these limits.

###### Note

After you create and apply user-defined tags to your resources, it can
take up to 24 hours for the tag keys to appear on your cost allocation tags
page. Once you activate the tags, it can take an additional 24 hours for
them to become active.

## Managing Kubernetes labels and cost

allocation tags

You can add, delete, and edit Kubernetes labels in EKS, as well as deactivate
the associated cost allocation tags. The following describes the expected
behavior for each action.

**Adding a new label**

You can add a new Kubernetes label to a pod. If the label limit of 50 has not
been reached, the new label will be imported and offered as a cost allocation
tag, which can then be activated. However, if the limit of 50 has been reached,
the new label will not be imported even if it falls within the alphabetical sort
order of first 50 labels. You must first deactivate an existing cost allocation
tag to import a new label.

**Editing a label**

Kubernetes does not allow you to edit a label key. To change a label key, you
must remove it and add a new label. However, you can edit label values, which
will be reflected in your next CUR.

**Deleting a label**

You can remove a label from EKS pods. Note that removing a label does not
automatically deactivate its associated cost allocation tag. Split cost
allocation data will continue to populate in CUR until you explicitly deactivate
the cost allocation tag.

**Deactivating a cost allocation tag**

You can deactivate any cost allocation tag created from Kubernetes labels.
Once deactivated, data will no longer populate in the respective columns, and
the column will be deleted from the next month’s CUR.

## Best practices for managing

Kubernetes labels for cost allocation

Kubernetes labels provide significant flexibility in shared cost allocation
modeling. To maximize the potential of this capability, we recommend following
these best practices to optimize your cost management approach.

**Understanding label limits**

The 50-label-per-pod limit is based on alphabetical sorting. Only the first 50
alphabetically ordered labels will be imported for cost allocation. To ensure
critical labels are included, carefully plan your label naming to ensure
important labels appear within the first 50 when alphabetically sorted.

**Following character constraints**

AWS cost allocation tags have the following character limits:

- Tag keys: 128 characters
- Tag values: 256 characters

While Kubernetes allows longer labels, any labels exceeding these limits will
not be imported. Design your labels within these limits to ensure successful
cost allocation tracking.

**Adding new labels when at capacity**

When a pod has reached the 50-label limit and you need to add a new cost
allocation label, follow these steps:

1. Review existing labels and identify a cost allocation tag to
   deactivate.
2. Deactivate the selected tag.
3. Add the new cost allocation label.
4. Verify the new label falls within the first 50 alphabetically sorted
   labels.

###### Note

Remember that only the first 50 alphabetically sorted labels are used for
cost allocation.
