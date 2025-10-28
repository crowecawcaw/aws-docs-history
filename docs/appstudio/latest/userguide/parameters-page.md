# Page parameters

Page parameters are a way to send information between pages and are often used when
navigating from one page to another within an App Studio app to maintain context or pass data.
Page parameters typically consist of a name and a value.

## Page parameter use cases

Page parameters are used for passing data between different pages and components within your App Studio applications.
They are particularly helpful for the following use cases:

1. **Searching and filtering**: When users search on your app's homepage, the search terms can be
   passed as parameters to the results page, allowing it to display only the relevant filtered items. For example, if a user searches for
   `noise-cancelling headphones`, the parameter with the value `noise-cancelling headphones` can be
   passed to the product listing page.
2. **Viewing item details**: If a user clicks on a listing, such as a product, the unique
   identifier of that item can be passed as a parameter to the details page. This allows the details page to display all the information about the specific item.
   For example, when a user clicks on a headphone product, the product's unique ID is passed as a parameter to the product details page.
3. **Passing user context in page navigation**: As users navigate between pages, parameters can pass along important context,
   such as the user's location, preferred product categories, shopping cart contents, and other settings. For example, as a user
   browses through different product categories on your app, their location and preferred categories are retained as parameters, providing a personalized and consistent experience.
4. **Deep links**: Use page parameters to share or bookmark a link to a specific page within the app.
5. **Data actions**: You can create data actions that accept parameter values to filter and query your data sources based on the passed parameters.
   For example, on the product listing page, you can create a data action that accepts `category` parameters to fetch the relevant products.

## Page parameter security considerations

While page parameters provide a powerful way to pass data between pages, you must use them with caution, as they can potentially expose
sensitive information if not used properly. Here is an important security considerations to keep in mind:

1. **Avoid exposing sensitive data in URLs**
   1. **Risk**: URLs, including data action parameters, are often visible in server logs, browser history, and other places. As such, it's essential to
      avoid exposing sensitive data, such as user credentials, personal identifiable information (PII), or any other confidential data, in page parameter values.
   2. **Mitigation**: Consider using identifiers that can be securely mapped to the sensitive data. For example, instead of passing a user's name or email
      address as a parameter, you could pass a random unique identifier that can be used to fetch the user's name or email.
