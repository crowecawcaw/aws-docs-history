# Filters to choose which repositories are scanned in Amazon ECR

When you configure image scanning for your private registry, you can use filters to
choose which repositories are scanned.

When **basic** scanning is used, you may specify scan on push filters
to specify which repositories are set to do an image scan when new images are pushed.
Any repositories not matching a basic scanning scan on push filter will be set to the **manual** scan frequency which means to perform a scan, you must manually
trigger the scan.

When **enhanced** scanning is used, you may specify separate filters
for scan on push and continuous scanning. Any repositories not matching an enhanced
scanning filter will have scanning disabled. If you are using enhanced scanning and
specify separate filters for scan on push and continuous scanning where multiple filters
match the same repository, then Amazon ECR enforces the continuous scanning filter over the
scan on push filter for that repository.

## Filter wildcards

When a filter is specified, a filter with no wildcard will match all repository
names that contain the filter. A filter with a wildcard (`*`) matches on
any repository name where the wildcard replaces zero or more characters in the
repository name.

The following table provides examples where repository names are expressed on the
horizontal axis and example filters are specified on the vertical axis.

|            | prod | repo-prod | prod-repo | repo-prod-repo | prodrepo |
| ---------- | ---- | --------- | --------- | -------------- | -------- |
| prod       | Yes  | Yes       | Yes       | Yes            | Yes      |
| \*prod     | Yes  | Yes       | No        | No             | No       |
| prod\*     | Yes  | No        | Yes       | No             | Yes      |
| \*prod\*   | Yes  | Yes       | Yes       | Yes            | Yes      |
| prod\*repo | No   | No        | Yes       | No             | Yes      |
