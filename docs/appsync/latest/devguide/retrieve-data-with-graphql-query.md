# Using GraphQL queries to retrieve data

from a DynamoDB table in the AWS AppSync console

Now that a record exists in your database, you'll get results when you run a query. A query is one of the
other fundamental operations of GraphQL. It's used to parse and retrieve information from your data source. In
terms of REST APIs, this is similar to the `GET` operation. The main advantage of GraphQL queries is
the ability to specify your application's exact data requirements so that you fetch the relevant data at the
right time.

###### To query your data source

1. If you haven't already done so, sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
2. Choose your API from the table.
3. In the tab to the left, choose **Queries**.
4. In the **Explorer** tab to the left of the table, under
   `query`
   `listTodos`, expand the `getTodo` operation:

![Expanded getTodo operation showing fields id, description, name, when, and where.](images/explorer-example-4.png) 5. In the code editor, you should see the operation code:

```
query listTodos {
  getTodo(id: "") {
    description
    id
    name
    when
    where
  }
```

In `(id:"")`, fill in the value that you saved in the result from the mutation operation.
In our example, this would be:

```
query listTodos {
  getTodo(id: "`abcdefgh-1234-1234-1234-abcdefghijkl`") {
    description
    id
    name
    when
    where
  }
```

6. Choose **Run**, then **listTodos**. The
   result will appear to the right of the editor. Our example looked like this:

```
{
  "data": {
    "getTodo": {
      "description": "I need to buy eggs",
      "id": "abcdefgh-1234-1234-1234-abcdefghijkl",
      "name": "Shopping List",
      "when": "Friday",
      "where": "Home"
    }
  }
}
```

###### Note

Queries only return the fields you specify. You can deselect the fields you don't need by deleting
them from the return field:

```
{
    description
    id
    name
    when
    where
  }
```

You can also uncheck the box in the **Explorer** tab next to the field
you want to delete. 7. You can also try the `listTodos` operation by repeating the steps to create an entry in
your data source, then repeating the query steps with the `listTodos` operation. Here's an
example where we added a second task:

```
{
  "createtodoinput": {
    "name": "Second Task",
    "when": "Monday",
    "where": "Home",
    "description": "I need to mow the lawn"
  }
}
```

By calling the `listTodos` operation, it returned both the old and new entries:

```
{
  "data": {
    "listTodos": {
      "items": [
        {
          "id": "abcdefgh-1234-1234-1234-abcdefghijkl",
          "name": "Shopping List",
          "when": "Friday",
          "where": "Home",
          "description": "I need to buy eggs"
        },
        {
          "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
          "name": "Second Task",
          "when": "Monday",
          "where": "Home",
          "description": "I need to mow the lawn"
        }
      ]
    }
  }
}
```
