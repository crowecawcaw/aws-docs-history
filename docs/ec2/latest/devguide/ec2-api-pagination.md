# Pagination in the Amazon EC2 API

We recommend that you use pagination when calling describe actions that can potentially
return a large number of results, such as `DescribeInstances`. Using pagination
bounds the number of items returned by a describe call and the time it takes for the call to
return. If you have a large number of resources, unpaginated calls might be throttled and
could time out. Therefore, overall latency is better with paginated calls than with
unpaginated calls because paginated calls are consistently successful.

For more information, see [Pagination](../../../AWSEC2/latest/APIReference/Query-Requests.md#api-pagination "../../../AWSEC2/latest/APIReference/Query-Requests.md#api-pagination") in the _Amazon EC2 API Reference_.

## Best practices

Where possible, specify a list of resource IDs in your describe calls. This is the fastest
way to describe a large number of resources. Note that you should not specify more than
1,000 IDs in a single call. The following is an example.

```
private List<Reservation> describeMyInstances(List<String> ids){
    if (ids == null || ids.isEmpty()) {
        return ImmutableList.of();
    }

    final DescribeInstancesRequest request = new DescribeInstancesRequest()
            .withInstanceIds(ids);

    return ec2.describeInstances(request).getReservations();
}
```

If you can't specify resource IDs in your describe calls, we strongly recommend using
pagination. The following is an example.

```
private List<Reservation> describeMyInstances(final Collection<Filter> filters){
    final DescribeInstancesRequest request = new DescribeInstancesRequest()
            .withFilters(filters)
            .withMaxResults(1000);

    List<Reservation> reservations = new ArrayList<>();
    String nextToken = null;
    do {
        request.setNextToken(nextToken);
        final DescribeInstancesResult response = ec2.describeInstances(request);
        reservations.addAll(response.getReservations());
        nextToken = response.getNextToken();
    } while (nextToken != null);

    return reservations;
}
```

If you need to retry a paginated call, use [exponential back-off
with jitter](ec2-api-throttling.md#api-backoff "ec2-api-throttling.md#api-backoff").

## Common issues

The following are examples of code that inadvertently makes unpaginated calls.

###### Example issue: Passing an empty list of resource IDs

The following code uses a list of IDs. However, if the list is empty, the result is an
unpaginated call.

```
private List<Reservation> describeMyInstances(List<String> ids){
    final DescribeInstancesRequest request = new DescribeInstancesRequest()
            .withInstanceIds(ids);

    return ec2.describeInstances(request).getReservations();
}
```

To correct this issue, ensure that the list is not empty before making the describe
call.

```
private List<Reservation> describeMyInstances(List<String> ids){
    if (ids == null || ids.isEmpty()) {
        return ImmutableList.of();
        // OR
        return Lists.newArrayList();
        // OR
        return new ArrayList<>();
    }

    final DescribeInstancesRequest request = new DescribeInstancesRequest()
            .withInstanceIds(ids);

    return ec2.describeInstances(request).getReservations();
}
```

###### Example issue: Not setting MaxResults

The following code checks and uses `nextToken`, but does not set
`MaxResults`.

```
private List<Reservation> describeMyInstances(final Collection<Filter> filters){
    final DescribeInstancesRequest request = new DescribeInstancesRequest()
            .withFilters(filters);

    List<Reservation> reservations = new ArrayList<>();
    String nextToken = null;
    do {
        request.setNextToken(nextToken);
        final DescribeInstancesResult response = ec2.describeInstances(request);
        reservations.addAll(response.getReservations());
        nextToken = response.getNextToken();
    } while (nextToken != null);

    return reservations;
}
```

To correct this issue, add `withMaxResults` as follows.

```
private List<Reservation> describeMyInstances(final Collection<Filter> filters){
    final DescribeInstancesRequest request = new DescribeInstancesRequest()
            .withFilters(filters)
            .withMaxResults(1000);

    List<Reservation> reservations = new ArrayList<>();
    String nextToken = null;
    do {
        request.setNextToken(nextToken);
        final DescribeInstancesResult response = ec2.describeInstances(request);
        reservations.addAll(response.getReservations());
        nextToken = response.getNextToken();
    } while (nextToken != null);

    return reservations;
}
```
