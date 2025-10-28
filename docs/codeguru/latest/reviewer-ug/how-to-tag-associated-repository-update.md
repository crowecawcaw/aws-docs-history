Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Add or update tags for a

CodeGuru Reviewer associated repository

You can change the value for a tag associated with an associated repository or add a
new tag. Keep in mind that there are limits on the characters you can use in the key and
value fields. For more information, see [Limits](quotas.md#limits-tags "quotas.md#limits-tags").

###### Important

Updating the value of a tag for an associated repository can impact access to that
associated repository. Before you update the value of a tag for an associated
repository, make sure to review any IAM policies that might use the value to
control access to resources such as associated repositories. For examples of
tag-based access policies, see [Using tags to control access to
Amazon CodeGuru Reviewer associated repositories](auth-and-access-control-using-tags.md "auth-and-access-control-using-tags.md").

###### Topics

- [Add or update tags
  for a CodeGuru Reviewer associated repository (console)](how-to-tag-associated-repository-update-console.md "how-to-tag-associated-repository-update-console.md")
- [Add or update tags for
  a CodeGuru Reviewer associated repository (AWS CLI)](how-to-tag-associated-repository-update-cli.md "how-to-tag-associated-repository-update-cli.md")
