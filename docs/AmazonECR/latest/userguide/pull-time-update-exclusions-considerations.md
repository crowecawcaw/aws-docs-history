# Considerations for pull-time update exclusions

Consider the following when using pull-time update exclusions:

- The default page size for listing exclusions is 100. You can use pagination with `maxResults` and `nextToken` parameters.
- Only valid IAM role ARNs in the correct ARN format are accepted.
- If you try to create an exclusion that already exists, you'll receive an `ExclusionAlreadyExistsException` error. If you try to delete an exclusion that doesn't exist, you'll receive an `ExclusionNotFoundException` error.
