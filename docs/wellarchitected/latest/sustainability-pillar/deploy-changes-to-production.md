# Deploy changes to production

Implement tested, validated, and approved improvements to
production. Implement using limited deployments, confirm the
functionality of your workload, test the actual reduction in
provisioned resources and resources consumed per unit of work
within the limited deployment, and check for unintended
consequences of the change. Proceed with full deployments after
successful testing.

Revert changes if tests fail or you encounter unacceptable
unintended consequences of your change.

Applying this step to the [Example scenario](improvement-process.md#example-scenario "improvement-process.md#example-scenario"), you take the following actions.

You implement the changes in production using a limited deployment
through a blue-green deployment methodology. Functionality tests
against the newly deployed instances are successful. You see a 26%
average reduction in provisioned storage for original and
manipulated image files. You don’t see any evidence of an increase
in compute load compressing new files.

You notice an unanticipated decrease in the elapsed time to
compress image files, and you attribute this to the highly
optimized code for the new compression algorithm.

You proceed with full deployment of the new version.
