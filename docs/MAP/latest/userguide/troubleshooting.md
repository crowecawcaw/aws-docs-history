# Troubleshooting

## Verify and Fix map-migrated cost-allocation tag

The Migration Acceleration Program requires that you tag resources with the
`map-migrated` tag. The `map-migrated` tag is automatically activated for
you as a cost-allocation tag. For a very small set of dated migration project plans, the
`map-migrated` tag is not automatically activated and requires a manual setup.
Following provides you steps on how to verify that the `map-migrated` tag is activated
and if it isn't activated, how to manually set it up.

###### Verify that the `map-migrated` tag is activated as a cost-allocation tag

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost allocation tags**.
3. To filter, copy the following tag key and enter it in the search box.

```
map-migrated
```

4. The status of the tag must appear as **Active**.
5. If the `map-migrated` tag is not found, or tag status is not
   **Active**, perform the following manual setup.

###### Manually set up the `map-migrated` tag and activate it as a cost-allocation tag

1. In the AWS Billing and Cost Management console, log in to the management (payer) account(s) listed in your
   Migration Plan.
2. Create an empty Amazon S3 bucket.
3. Copy the following tag key and tag the resource with it. The tag value can be
   empty.

```
map-migrated
```

4. Wait 24 hours.

###### Note

It might take up to 24 hours for the cost allocations to appear available in the system.
Therefore, if you don't see the [MAP tag](tag-key.md "tag-key.md"), wait for 24 hours, and then refresh
the cost allocation tag screen. 5. After waiting 24 hours, log in to the management (payer) account(s) listed in your
Migration Plan to activate the cost allocation tags that apply to your workload. 6. In the AWS Management Console, choose **Services**. 7. Choose **Billing** from the Services menu. 8. Choose **Cost allocation tags** from the navigation panel. 9. To filter for MAP-migrated resources, enter the [MAP tag](tag-key.md "tag-key.md") key in the
search box. 10. Choose the **check boxes** for the tags created for the [MAP tag](tag-key.md "tag-key.md"). 11. Choose **Activate**.

The status of the tags should now appear as **Active**.

### Next step

[Tagging Resources](getting-started-step2.md "getting-started-step2.md")
