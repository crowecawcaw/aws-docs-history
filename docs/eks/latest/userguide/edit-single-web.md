**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Edit a single page from a web browser

You can easily edit a single page in the EKS User Guide directly through your web browser.

![View of GitHub web edit interface](images/contribute-web-edit.png)
If you want to edit multiple pages from your web browser, see [Edit multiple files from a web browser with the GitHub Web Editor](edit-web.md "edit-web.md").

## Prerequisites

- Docs page to change opened in web browser.
- Signed into GitHub.

## Procedure

1. Navigate to the page you want to edit in the Amazon EKS User Guide.
2. In the right pane, choose the **Edit this page on GitHub** link.
3. Once on GitHub, open the editor by either:
   - Pressing the `e` key on your keyboard.
   - Clicking the pencil icon and selecting **Edit in Place** from the dropdown menu.
   - If you don’t have the option to edit, you need to login to GitHub. Your GitHub account does not need any special permissions to suggest changes. However, internal Amazon contributors should link their GitHub profile.

4. Make your required changes to the content in the GitHub editor.
   - The editor provides syntax highlighting and preview capabilities.
   - You can use AsciiDoc markup to format your changes.
   - You can use `ctrl-f` to open a find/replace interface.

5. (Optional) Preview your changes.
   - Use the `preview` tab to preview your changes with rich formatting.
   - Use the `show diff` option to highlight changed sections. Removed sections have a red indicator in the left margin. New sections have a green indicator in the left margin.

6. When finished editing, click the **Commit changes…​** button at the top of the editor
7. In the commit dialog:
   - Verify your email address is correct.
   - Add a brief but descriptive commit message explaining your changes.
   - Optionally add a longer description if needed.
   - Select to create a new branch and pull request.

You have created a pull request including the proposed changes.

## Pull request overview

When you create a PR:

- Your changes are submitted for review by repository maintainers.
- Reviewers can comment on your changes and request modifications.
- Automated tests may run to validate your changes.
- Once approved, your changes can be merged into the main repository.

Pull requests help ensure quality and provide a way to discuss changes before they are integrated.

[Learn how pull requests are reviewed and approved in the GitHub Docs.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews")
