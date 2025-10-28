# CircleCI limitations

The following are limitations or notes for CircleCI:

- CircleCI does not support either field based or record based partitioning.
- Filter fields containing '-' (hyphen) will work only if they are wrapped within backticks. For example: `workflow-name` = "abc"
- The GitLab VCS type cannot be supported as there is no programmatic way to retrieve the 'Project ID' required for the GitLab VCS entity path.
