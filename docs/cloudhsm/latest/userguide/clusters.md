# AWS CloudHSM clusters

Making individual HSMs work together in a synchronized, redundant, and highly-available way can be difficult,
but AWS CloudHSM does the heavy lifting for you by providing hardware security modules (HSMs) in _clusters_. A cluster
is a collection of individual HSMs that AWS CloudHSM keeps in sync. When you perform a task or operation on one HSM in a cluster, the other HSMs in
that cluster are automatically kept up to date.

AWS CloudHSM offers clusters in two modes: _FIPS_ and _non-FIPS_. In FIPS mode, only Federal Information Processing Standard (FIPS) validated keys and algorithms can be used.
Non-FIPS mode offers all the keys and algorithms that are supported by AWS CloudHSM, regardless of FIPS approval. AWS CloudHSM also offers two types of HSMs: _hsm1.medium_ and _hsm2m.medium_.
For details on the differences between each HSM type and cluster mode, see [AWS CloudHSM cluster modes](cluster-hsm-types.md "cluster-hsm-types.md"). The _hsm1.medium_ HSM type is reaching end of support so new clusters cannot be created with this type. For more information, see [Deprecation
notifications](compliance-dep-notif.md#hsm-dep-1 "compliance-dep-notif.md#hsm-dep-1") for details.

To meet your availability, durability, and scalability goals, you set the number of HSMs in your cluster across multiple availability zones. You can create a cluster that has 1 to 28 HSMs (the [default
limit](limits.md "limits.md") is 6 HSMs per AWS account per [AWS Region](regions.md "regions.md")). You can place the HSMs in different [Availability Zones](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.az.en.html "https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.az.en.html")
in an AWS region. Adding more HSMs to a cluster provides higher performance. Spreading clusters across Availability Zones provides redundancy and high availability.

For more information about clusters, see [Clusters in AWS CloudHSM](manage-clusters.md "manage-clusters.md").

To create a cluster, see [Getting started](getting-started.md "getting-started.md").
