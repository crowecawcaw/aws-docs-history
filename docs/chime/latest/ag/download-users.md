**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Downloading user lists

The following example shows how to download a list of users associated with your Amazon Chime
administrative account in `.csv` format.

```
BufferedWriter writer = Files.newBufferedWriter(Paths.get("/path/to/csv"));
CSVPrinter printer = new CSVPrinter(writer, CSVFormat.DEFAULT.withHeader("userId", "email"));

ListUsersRequest listUsersRequest = new ListUsersRequest()
    .withAccountId(accountId)
    .withMaxResults(1);

boolean done = false;
while (!done) {
    ListUsersResult listUsersResult = chime.listUsers(listUsersRequest);
    for (User user: listUsersResult.getUsers()) {
        printer.printRecord(user.getUserId(), user.getPrimaryEmail());
    }

    if (listUsersResult.getNextToken() == null) {
        done = true;
    }

    listUsersRequest = new ListUsersRequest()
        .withAccountId(accountId)
        .withNextToken(listUsersResult.getNextToken());
}

printer.close();
```
