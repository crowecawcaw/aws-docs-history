As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# About full repository analysis and

incremental code reviews

There are three different kinds of code reviews that CodeGuru Reviewer can do to provide
recommendations.

- _Incremental code reviews_ are created automatically when you
  create a pull request from your repository context on an associated repository. These code
  reviews scan the changed code in a pull request.
- _Full repository analysis code reviews_ are done when you create a
  full repository analysis code review in the CodeGuru Reviewer console. These code reviews scan all
  the code in a specified branch.

###### Note

Your first full repository analysis is created for you when you associate your
repository.

- _Full repository analysis code reviews for CI/CD workflows_ scan
  all the source code in your CI/CD workflow. For more information, see [Create
  code reviews with GitHub Actions](working-with-cicd.md "working-with-cicd.md").
  You can receive recommendations in code reviews by creating a full repository analysis or
  submitting a pull request. After you associate a repository, CodeGuru Reviewer automatically creates a
  full repository analysis code review, and every pull request in that repository creates an
  incremental code review. You can also choose to create additional full repository analysis
  code reviews.

| Type of code review                            | Is the review automatic after I associate the repository?                                                                                                                                                                        | Where can I see recommendations?                                                                                            | What code is reviewed?                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Full repository analysis                       | Your first full repository analysis is done automatically when you associate<br>your repository. After that, you must request a full repository analysis in the CodeGuru Reviewer<br>console or by using the AWS CLI or AWS SDK. | In the CodeGuru Reviewer console, or by using the AWS CLI or AWS SDK.                                                       | All the code in the branch is reviewed.                                   |
| Incremental code review                        | Yes. After associating the repository, every time you do a pull request there<br>is a code review.                                                                                                                               | In the CodeGuru Reviewer console, in the AWS CLI or AWS SDK, or in pull request comments in the repository source provider. | The code that is changed in the pull request is reviewed.                 |
| GitHub Actions code review in a CI/CD workflow | Yes. After enabling CodeGuru Reviewer on your GitHub repository, for every push, pull, or scheduled<br>repository scan there is a code review.                                                                                   | In the GitHub \*_Security_<br>• tab.                                                                                        | The code that is changed in the push, pull, or scheduled repository scan. |
