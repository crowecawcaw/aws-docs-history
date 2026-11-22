

# Use VCF features on Amazon EVS

For VMware Cloud Foundation (VCF) features, follow the Broadcom documentation. For some features, Amazon Elastic VMware Service adds steps or conditions of its own.

## Check whether a feature is supported
<a name="operate-vcf-features-support"></a>

Before you use a VCF feature, check its row in [VCF feature support on Amazon EVS](vcf-feature-support.md). Each row gives the support status, the VCF versions, the instance types or storage model, any Amazon EVS conditions, and a link to the Broadcom documentation. Support can differ by VCF version, so check the row for the version that your environment runs.

## When a feature has its own page
<a name="operate-vcf-features-when"></a>

A feature gets a page in this section when one or more of the following is true:
+ Amazon EVS adds three or more steps of its own that the Broadcom documentation doesn’t give, such as console, API, CLI, IAM, network, or DNS actions.
+ Amazon EVS adds an API, CLI command, or AWS CloudFormation resource for the feature.
+ The Amazon EVS conditions for the feature need more than a short note, or a decision table.
+ A problem that happens only on Amazon EVS needs a troubleshooting entry.

Otherwise, the feature has only its row on the feature support page, and you follow the Broadcom documentation. When a feature has a page, its row links to the page. The page doesn’t repeat the support status, so the feature support page is the one place to check it.

Features that you decide on before deployment are in [Plan](plan-overview.md). Settings that you choose when you deploy are in [Deploy](deploy-overview.md). The following pages cover features that you use after deployment.

## Feature pages
<a name="operate-vcf-features-pages"></a>

The following feature has its own page.
+  [Set up NSX Federation](nsx-federation.md) 

**Topics**