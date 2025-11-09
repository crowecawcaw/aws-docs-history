# Adding K8s Pods Labels or Amazon ECS Tasks Tags to the Dashboard

## Introduction

When creating pods in Kubernetes (K8s) clusters or tasks in ECS clusters, you can also apply K8s labels (pods) or AWS tags (ECS tasks) to them.
This is useful for purpose of cost allocation, and can help you identify costs of your EKS/ECS workloads by definitions which are relevant to your organization.
SCAD supports K8s pods labels and ECS tasks tags as user-defined cost allocation tags, and you can use these labels/tags in the dashboard, to visualize you costs based on them. Please follow the below instructions to add K8s pods labels/ECS tasks tags to the dashboard.

## Adding Labels/Tags

Follow the below process to add cost allocation tags to the dashboard.

### Activating Cost Allocation Tags

[Activate the user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") that represent the K8s pods labels or the ECS tasks tags that you wish to add to the dashboard.

### Adding Cost Allocation Tags to the Athena View

###### Note

The Athena view already includes the [Kubernetes Recommended Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/ "https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/"), and the labels `app`, `chart`, `release`, `version`, `component`, `type` and `created-by`.
The dashboard also already inclueds these labels, in the "Workloads Explorer" sheet (as group-by dimensions and as filters) and in the "Labels/Tags Explorer" sheet.
If you’d like to use them in the dashboard, there’s no need for any additional action except for activating the respective cost allocation tags.
If you have other labels or tags you’d like to use, please continue reading the below, to learn how to add them to the Athena view.

- In Athena, open the `scad_cca_summary_view` Athena view by clicking "Show/edit query"
- Add the label/tag to the left table in the view. The easiest way is to find an existing cost allocation tag and add yours below it.
  For example, find the following line:

```
, COALESCE("resource_tags"['user_created_by'], 'No K8s label/AWS tag key: created-by') "cat_created_by"
```

Add your cost allocation tag below it. Here’s an example, assuming your cost allocation tag is `business_unit`:

```
, COALESCE("resource_tags"['user_business_unit'], 'No K8s label/AWS tag key: business_unit') "cat_business_unit"
```

- Bump the number in the `GROUP BY` clause of the left table. For example, if the `GROUP BY` looks like this:

```
GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47
```

You should add the number 48 at the end, like this:

```
GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48
```

- Repeat the same process in the `UNION ALL` section - find the last existing cost allocation tag line, add your cost allocation tag below it, and bump the `GROUP BY` numbers shown as above
- Run the query, it should quickly complete
- Log into QuickSight, edit the `scad_cca_summary_view` dataset, click `Save & publish` on the top right, and wait for the dataset to finish refreshing

Once the QuickSight dataset refresh is completed successfully, the new cost allocation tag column will be available in the QuickSight analysis, for you to add to visuals.
You may now save the dashboard as analysis and create visuals with the labels/tags, or continue to the [Total Cost of Ownership Using Kubernetes Labels and AWS Tags](scad-containers-dashboard-tco.md "scad-containers-dashboard-tco.md") chapter for 2 examples on using K8s pods labels/ECS tasks tags in the dashboard.
