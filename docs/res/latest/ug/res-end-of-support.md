

End of development notice: AWS is discontinuing development of Research and Engineering Studio on AWS (RES). 2026.09 is the final release, supported through September 30, 2027. RES remains open source and keeps running in your account. For more information, see [RES end of support](res-end-of-support.md).

# RES end of support
<a name="res-end-of-support"></a>

After careful consideration, AWS is ending development of Research and Engineering Studio on AWS (RES). RES 2026.09 is the final release. As of September 29, 2026, RES is no longer available for new adoption, and AWS does not provide support to customers who begin using it after this date. As an existing customer, you can continue to use RES, and because it is open-source software that runs in your own AWS account, your existing deployment keeps running even after AWS support ends. Nothing is switched off; only AWS development and support conclude.

## Service updates until end of support
<a name="res-end-of-support-service-updates"></a>

Effective immediately, no new features, versions, or enhancements will be made to RES. Under the [RES support policy](support-policy.md), AWS provides fixes for critical issues through patch releases for releases that have not reached their End of Support Life (EOSL) date. The final release, 2026.09, is supported through September 30, 2027. If you are running an earlier release, it remains supported until its own EOSL date. We encourage you to plan your path before September 30, 2027.

## Your options
<a name="res-end-of-support-options"></a>

The right path depends on your workload, how customized your environment is, and whether you prefer to self-manage or use a managed service.
+ Continue on RES, self-managed or with an AWS partner for support and development. RES remains available as open source under the Apache 2.0 license. After 2026.09's EOSL, AWS no longer provides fixes for critical issues or technical support; you or your partner take that on.
+ Move to an AWS managed service: [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) or [Amazon WorkSpaces Applications](https://aws.amazon.com/workspaces/applications/) (formerly AppStream 2.0) for virtual desktops, or login nodes with [Amazon DCV](https://aws.amazon.com/hpc/dcv/) in [AWS Parallel Computing Service (PCS)](https://aws.amazon.com/pcs/) for HPC access. These are not drop-in replacements for the RES portal, so plan for some change to your setup.
+ Move to an alternative product, such as NI-SP EF Portal, Open OnDemand, or [Engineering Development Hub (EDH)](https://github.com/awslabs/engineering-development-hub).

## Milestones
<a name="res-end-of-support-milestones"></a>


| Milestone | Date | 
| --- | --- | 
| Final release (2026.09) and announcement | September 29, 2026 | 
| End of support for 2026.09 (EOSL) | September 30, 2027 | 

## Getting help
<a name="res-end-of-support-getting-help"></a>

To plan a transition or engage a partner, contact your AWS account team or AWS Support.

## Frequently asked questions
<a name="res-end-of-support-faq"></a>

**What is changing?**  
AWS is discontinuing development of RES. 2026.09 is the final release; no new features or versions after it. The support policy is unchanged: each release, including 2026.09, is supported through its EOSL date.

**Why is AWS making this change?**  
This is a business decision to focus AWS investment on managed services and partner-delivered solutions. A capable ecosystem of AWS Partners and complementary AWS services is available to support these workloads.

**How long will AWS support RES?**  
Each release is supported through its End of Support Life (EOSL) date; the final release, 2026.09, is supported through September 30, 2027, the latest EOSL. We encourage you to plan your path before then.

**What happens to the earlier release I'm running?**  
Each release is supported through its own End of Support Life (EOSL) date, the last day of the release month one year later; see the [RES support policy](support-policy.md) for the full table. If your release is still before its EOSL, it remains fully supported until then. If it is already past EOSL, AWS no longer provides updates or technical support for it. To get the longest supported runway, you can move to the final release, 2026.09, which is supported through September 30, 2027. In all cases, because RES is open source and runs in your own account, your deployment keeps running after EOSL, and you or an AWS partner can continue to maintain it.

**Can I keep using RES after its EOSL?**  
Yes. It is open source and runs in your own account; your deployment keeps operating. Only AWS technical support and critical-issue fixes end. You, or an AWS partner, can continue to maintain and develop it.

**Who maintains it after AWS support ends?**  
You or your chosen partner. Today, you run RES in your own account; after EOSL there are no RES patches provided by AWS.

**Does this affect other AWS services I use with RES?**  
No, only RES. Amazon EC2, Amazon Elastic File System (Amazon EFS), Amazon FSx, and AWS Directory Service are unaffected, and Amazon DCV continues to be developed and supported.