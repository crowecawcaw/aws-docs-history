

# $nin
<a name="nin"></a>

The `$nin` operator is used to match values that are not in the specified array. It is the inverse of the `$in` operator, which matches values that are in the specified array.

Planner version 2.0 added index support for `$nin`.

**Parameters**
+ `field`: The field to check.
+ `array`: The array of values to check against.

 

**Dollar (`$`) in field names**

See [Dollar($) and dot(.) in field names](functional-differences.md#functional-differences-dollardot) for limitations regarding querying `$` prefixed fields in `$nin` in nested objects.

## Example (MongoDB Shell)
<a name="nin-examples"></a>

The following example demonstrates how to use the `$nin` operator to find documents where the `category` field is not equal to "Fiction" or "Mystery".

**Create sample documents**

```
db.books.insertMany([
  { title: "The Great Gatsby", author: "F. Scott Fitzgerald", category: "Fiction" },
  { title: "To Kill a Mockingbird", author: "Harper Lee", category: "Fiction" },
  { title: "The Girl on the Train", author: "Paula Hawkins", category: "Mystery" },
  { title: "The Martian", author: "Andy Weir", category: "Science Fiction" },
  { title: "The Alchemist", author: "Paulo Coelho", category: "Philosophy" }
])
```

**Query example**

```
db.books.find({
  category: {
    $nin: ["Fiction", "Mystery"]
  }
})
```

**Output**

```
[
  {
    _id: ObjectId('...'),
    title: 'The Martian',
    author: 'Andy Weir',
    category: 'Science Fiction'
  },
  {
    _id: ObjectId('...'),
    title: 'The Alchemist',
    author: 'Paulo Coelho',
    category: 'Philosophy'
  }
]
```

## Code examples
<a name="nin-code"></a>

To view a code example for using the `$nin` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findBooksNotInCategories(categories) {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const books = await db.collection('books').find({
    category: {
      $nin: categories
    }
  }).toArray();
  console.log(books);
  client.close();
}

findBooksNotInCategories(['Fiction', 'Mystery']);
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_books_not_in_categories(categories):
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    books = list(db.books.find({
        'category': {
            '$nin': categories
        }
    }))
    print(books)
    client.close()

find_books_not_in_categories(['Fiction', 'Mystery'])
```

------