# Update Dashboards

## Update Dashboards

###### Important

We recommend customers updating both cid-cmd tool and CID Cloud Formation stack to a version 4.2.3 or more recent.

We always improve Cloud Intelligence Dashboards by adding new actionable
insights and recommendations. All new dashboard versions announced in
our
[Changelog](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/changes "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/changes").
You can find your current dashboard version on About tab of each of the
dashboards.

To pull the latest version of the dashboard from the public template
please use the following steps.

### Simple Update

1. Open [CloudShell](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home") in the account where you have deployed the Cloud Intelligence Dashboards
2. Install cid-cmd tool. Run the following command and make sure you hit enter :

```
pip3 install --upgrade cid-cmd
```

1. Start update. Run the following command and choose the dashboard to
   update :

```
cid-cmd update
```

###### Note

After update QuickSight
datasets will be refreshed automatically. During the refresh process you
may see "Dataset changed too much" error which should disappear once
datasets are fully refreshed

### Recursive Update

In some cases the update of underlying
QuickSight Datasets and views is required. This can be useful also to
reset dashboards to factory settings if any issue. Please note that it
might impact customizations you did on the dashboards. The tool will
provide you an interactive prompt when it will detect the difference and
you can accept the changes or keep existing.

```
cid-cmd update --force --recursive
```

### Update from CUDOS v4 to v5

If you are looking to update to CUDOS v5 from a previous CUDOS version,
please refer to the guide in the [FAQs](faq.md "faq.md")

### Update Demo
