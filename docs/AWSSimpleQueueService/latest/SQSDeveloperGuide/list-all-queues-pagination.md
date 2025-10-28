# Amazon SQS list queue pagination

The [`listQueues`](../APIReference/API_ListQueues.md "../APIReference/API_ListQueues.md") and
[`listDeadLetterQueues`](../APIReference/API_ListDeadLetterSourceQueues.md "../APIReference/API_ListDeadLetterSourceQueues.md") API methods support optional pagination
controls. By default, these API methods return up to 1000 queues in the response message.
You can set the `MaxResults` parameter to return fewer results in each response.

Set parameter `MaxResults` in the `listQueues` or
`listDeadLetterQueues` request to specify the maximum number of results to be
returned in the response. If you do not set `MaxResults`, the response includes a
maximum of 1,000 results and the `NextToken` value in the response is null.

If you set `MaxResults`, the response includes a value for
`NextToken` if there are additional results to display. Use
`NextToken` as a parameter in your next request to `listQueues` to
receive the next page of results. If there are no additional results to display, the
`NextToken` value in the response is null.
