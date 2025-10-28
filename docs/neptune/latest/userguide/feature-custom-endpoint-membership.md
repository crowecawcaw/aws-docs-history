# Working with custom endpoints in Neptune

When you add a DB instance to a custom endpoint or remove it from a custom endpoint, any existing
connections to that DB instance remain active.

You can define a list of DB instances to include in a custom endpoint (the
_static_ list), or one to exclude from the custom endpoint (the.
_exclusion_ list). You can use the inclusion/exclusion mechanism
to subdivide the DB instances into groups and make sure that the custom endpoints
covers all the DB instances in the cluster. Each custom endpoint can contain
only one of these list types.

In the AWS Management Console, the choice is represented by the check box **Attach
future instances added to this cluster**. When you keep check box clear,
the custom endpoint uses a static list containing only the DB instances specified
in the dialog. When you check the check box, the custom endpoint uses an exclusion
list. In that case, the custom endpoint represents all DB instances in the cluster
(including any that you add in the future) except the ones left unselected in the
dialog.

Neptune doesn't change the DB instances specified in the static or exclusion
lists when DB instances change roles between primary instance and Neptune Replica
because of failover or promotion.

You can associate a DB instance with more than one custom endpoint. For example,
suppose you add a new DB instance to a cluster. In that case the DB instance is added
to all custom endpoints for which it is eligible. The static
or exclusion list defined for it determines which DB instance can be added to it.

If an endpoint includes a static list of DB instances, newly added Neptune
Replicas aren't added to it. Conversely, if the endpoint has an exclusion list,
newly added Neptune Replicas are added to it provided that they aren't named
in the exclusion list.

If a Neptune Replica becomes unavailable, it remains associated with its
custom endpoints. This is true whether it is unhealthy, stopped, rebooting,
or unavailable for another reason. However, as long as it remains unavailable
you can't connect to it through any endpoint.

Because newly created Neptune clusters have no custom endpoints, you must create
and manage them yourself. This is also true for Neptune clusters restored from snapshots,
because custom endpoints are not included in the snapshot. You have create them again after
restoring, and choose new endpoint names if the restored cluster is in the same region as
the original one.

## Creating a custom endpoint

Manage custom endpoints using the Neptune console. Do this by navigating to the
details page for your Neptune cluster and use the controls in the **Custom
Endpoints** section.

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Navigate to the cluster detail page.
3. Choose the `Create custom endpoint` action in the
   **Endpoints** section.
4. Choose a name for the custom endpoint that is unique for your user ID
   and region. The name must be 63 characters or less in length and take the
   following form:

``endpointName`.cluster-custom-`customerDnsIdentifier`.`dnsSuffix``

Because custom endpoint names don't include the name of your cluster,
you don't have to change those names if you rename a cluster. However, you
can't reuse the same custom endpoint name for more than one cluster in the
same region. Give each custom endpoint a name that is unique across the
clusters owned by your user ID within a particular region. 5. To choose a list of DB instances that remains the same even as
the cluster expands, keep the check box **Attach future instances
added to this cluster** clear. When that check box is checked, the custom
endpoint dynamically adds any new instances as that are added to the cluster.

## Viewing custom endpoints

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Navigate to the cluster detail page of your DB cluster.
3. The **Endpoints** section only contains
   information about custom endpoints (details about the built-in endpoints are
   listed in the main **Details** section). To see details for
   a specific custom endpoint, select its name to bring up the detail page for
   that endpoint.

## Editing a custom endpoint

You can edit the properties of a custom endpoint to change which DB instances
are associated with it. You can also switch between a static list and an exclusion
list.

You can't connect to or use a custom endpoint while the changes from an edit
action are in progress. It might take some minutes after you make a change before
the endpoint status returns to **Available** and you can connect
again.

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Navigate to the cluster detail page.
3. In the **Endpoints** section, choose
   the name of the custom endpoint you want to edit.
4. In the detail page for that endpoint, choose the
   **Edit** action.

## Deleting a custom endpoint

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Navigate to the cluster detail page.
3. In the **Endpoints** section, choose
   the name of the custom endpoint you want to delete.
4. In the detail page for that endpoint, choose the
   **Delete** action.
