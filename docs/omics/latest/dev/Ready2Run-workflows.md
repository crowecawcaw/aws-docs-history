AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Ready2Run workflows in HealthOmics

Ready2Run workflows are preconfigured workflows published by third-party publishers. Some publishers, such as
Sentieon Inc, offer subscription-based workflows. Other Ready2Run workflows don't require a subscription, and some
workflows are open source, such as the NF-Core workflows.

Ready2Run workflows are well-suited to the following scenarios:

- You want to focus on the analysis of pipeline output and generating results, without the need to set up the
  underlying infrastructure.
- You want to replicate your results using established workflows.
- As a software developer, you want to integrate your application directly with the HealthOmics SDK.
  HealthOmics supports versioning for Ready2Run workflows. For a Ready2Run workflow that offers versions, you can specify
  the version name when you start a run.

All Ready2Run workflows provide logs, including CloudWatch logs, that you can use for troubleshooting.

###### Note

Sentieon Ready2Run workflows are subscription-based. When you run a Sentieon Ready2Run workflow for the first
time in an account, Sentieon automatically creates a two-week evaluation license for your AWS account. The
license is valid for all Sentieon Ready2Run workflows. After the evaluation period ends, you can request a
permanent license or request an extension to the evaluation license. See
**Subscribing to Sentieon Ready2Run workflows** for details.

###### Topics

- [Available Ready2Run workflows in HealthOmics](workflows-r2r-table.md "workflows-r2r-table.md")
- [Subscribing to Sentieon Ready2Run workflows](Ready2Run-workflows-subscribe.md "Ready2Run-workflows-subscribe.md")
- [Starting HealthOmics Ready2Run workflows using the console](Ready2Run-workflows-console.md "Ready2Run-workflows-console.md")
- [Starting HealthOmics Ready2Run workflows using the API](Ready2Run-workflows-API.md "Ready2Run-workflows-API.md")
