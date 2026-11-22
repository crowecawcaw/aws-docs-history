

# Limitations and notes for the Bitbucket connector

The following are limitations and notes for the Bitbucket connector:
+ Bitbucket is supported as a source only. Writing to Bitbucket is not supported.
+ Without a `state` filter, the `pull-requests` entity returns only open pull requests, because that is the Bitbucket default. To read merged, declined, or superseded pull requests, filter on `state`, for example `state = 'MERGED'`.
+ Job bookmarks are not supported.