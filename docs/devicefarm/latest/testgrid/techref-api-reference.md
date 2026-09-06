

# Device Farm desktop browser testing API
<a name="techref-api-reference"></a>

The [Device Farm API Reference](https://docs.aws.amazon.com/devicefarm/latest/APIReference/) includes a `CreateProject` action and a `CreateTestGridProject` action. For desktop browser and Selenium testing, the following API calls are used:Project Management APIs

[`CreateTestGridProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateTestGridProject.html)  
Creates a desktop browser testing project.

[`DeleteTestGridProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteTestGridProject.html)  
Deletes a desktop browser testing project.

[`GetTestGridProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetTestGridProject.html)  
Gets information about a desktop browser testing project.

[`UpdateTestGridProject`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateTestGridProject.html)  
Updates attributes (name, description) of a desktop browser testing project.

[`ListTestGridProjects`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridProjects.html)  
Lists desktop browser testing projects, including ARNs, names, and descriptions.Session Management APIs

[`CreateTestGridUrl`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateTestGridUrl.html)  
Creates a limited-time desktop browser testing WebDriver path for creating sessions.

[`ListTestGridSessions`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessions.html)  
Lists your desktop browser testing sessions.

[`GetTestGridSession`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetTestGridSession.html)  
Gets a desktop browser testing session.

[`ListTestGridSessionActions`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionActions.html)  
Gets a list of the actions performed during a session.

[`ListTestGridSessionArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionArtifacts.html)  
Lists the artifacts (video, Selenium logs, and so on) associated with a session.