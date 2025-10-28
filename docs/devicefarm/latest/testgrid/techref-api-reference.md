# Device Farm desktop browser testing API

The [Device Farm API Reference](../APIReference.md "../APIReference.md") includes a
`CreateProject` action and a `CreateTestGridProject` action. For desktop browser and
Selenium testing, the following API calls are used:

###### Project Management APIs

[`CreateTestGridProject`](../APIReference/API_CreateTestGridProject.md "../APIReference/API_CreateTestGridProject.md")

Creates a desktop browser testing project.

[`DeleteTestGridProject`](../APIReference/API_DeleteTestGridProject.md "../APIReference/API_DeleteTestGridProject.md")

Deletes a desktop browser testing project.

[`GetTestGridProject`](../APIReference/API_GetTestGridProject.md "../APIReference/API_GetTestGridProject.md")

Gets information about a desktop browser testing project.

[`UpdateTestGridProject`](../APIReference/API_UpdateTestGridProject.md "../APIReference/API_UpdateTestGridProject.md")

Updates attributes (name, description) of a desktop browser testing project.

[`ListTestGridProjects`](../APIReference/API_ListTestGridProjects.md "../APIReference/API_ListTestGridProjects.md")

Lists desktop browser testing projects, including ARNs, names, and descriptions.

###### Session Management APIs

[`CreateTestGridUrl`](../APIReference/API_CreateTestGridUrl.md "../APIReference/API_CreateTestGridUrl.md")

Creates a limited-time desktop browser testing WebDriver path for creating sessions.

[`ListTestGridSessions`](../APIReference/API_ListTestGridSessions.md "../APIReference/API_ListTestGridSessions.md")

Lists your desktop browser testing sessions.

[`GetTestGridSession`](../APIReference/API_GetTestGridSession.md "../APIReference/API_GetTestGridSession.md")

Gets a desktop browser testing session.

[`ListTestGridSessionActions`](../APIReference/API_ListTestGridSessionActions.md "../APIReference/API_ListTestGridSessionActions.md")

Gets a list of the actions performed during a session.

[`ListTestGridSessionArtifacts`](../APIReference/API_ListTestGridSessionArtifacts.md "../APIReference/API_ListTestGridSessionArtifacts.md")

Lists the artifacts (video, Selenium logs, and so on) associated with a session.
