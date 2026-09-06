

# Customer Profiles standard web analytics object fields
<a name="standard-web-analytics-object-fields"></a>


**WebAnalytics Standard Object Schema**  

<table>
<thead>
  <tr><th>Field</th><th>Type</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="3">Event Attributes</td></tr>
  <tr><td>EventId</td><td>String</td><td>Unique identifier for a web analytics event.</td></tr>
  <tr><td>EventType</td><td>String</td><td>Type of the web analytics event, like - Page View, form submission, button choose, sPull up mainline<br />\u0000<br />earch bar interaction, app error prompts, cart interactions, purchases, scrolls.</td></tr>
  <tr><td>EventTimestamp</td><td>Number</td><td>Epoch millisecond timestamp of the event.</td></tr>
  <tr><td>EventDuration</td><td>Number</td><td>EventDuration represents the amount of time a user spent during a particular interaction, measured in seconds. Common use cases include: Time spent viewing a product, Length of a browsing session on a particular page, Time spent on a feature.</td></tr>
  <tr><td>EventValue</td><td>Number</td><td>EventValue is a numerical attribute that represents the value or importance of an interaction event. Common use cases include: Purchase amount for transaction events, Rating values for product ratings, Percentage completion for video views.</td></tr>
  <tr><td colspan="3">Session Attributes</td></tr>
  <tr><td>Session.Id</td><td>String</td><td>Unique identifier for the session.</td></tr>
  <tr><td>Session.StartTimestamp</td><td>Number</td><td>Epoch millisecond indicating the start timestamp of the session.</td></tr>
  <tr><td colspan="3">Page/Screen Attributes</td></tr>
  <tr><td>Page.Title</td><td>String</td><td>Title of a Web App/Screen Name for a mobile app.</td></tr>
  <tr><td>Page.Location</td><td>String</td><td>URL of a Web page. For mobile, it could be deep link or route to the screen.</td></tr>
  <tr><td>Page.Referrer</td><td>String</td><td>Previous screen/page.</td></tr>
  <tr><td>Page.Category</td><td>String</td><td>Logical grouping of a screen/page. Might be useful to group nested URLs/app locations.</td></tr>
  <tr><td colspan="3">HTML/DOM Elements</td></tr>
  <tr><td>Element.Id</td><td>String</td><td>HTML Element Id</td></tr>
  <tr><td>Element.Type</td><td>String</td><td>Element Type - Button, Anchor Links, Etc.</td></tr>
  <tr><td>Element.Classes</td><td>String</td><td>CSS Styling Classes of the Element</td></tr>
  <tr><td>Element.Text</td><td>String</td><td>Element text (Useful for buttons, input fields placeholders, etc).</td></tr>
  <tr><td>Element.AltText</td><td>String</td><td>AltText of a HTML element (generally used for images).</td></tr>
  <tr><td>Element.Source</td><td>String</td><td>Source of an video, image.</td></tr>
  <tr><td colspan="3">Form</td></tr>
  <tr><td>Form.Id</td><td>String</td><td>Unique Identifier for an input form</td></tr>
  <tr><td>Form.Name</td><td>String</td><td>Name of the Form</td></tr>
  <tr><td>Form.Length</td><td>String</td><td>Number of input fields in a form.</td></tr>
  <tr><td>Form.ValidationErrors</td><td>Number</td><td>Number of validation errors in the form.</td></tr>
  <tr><td>Form.FieldsCompleted</td><td>Number</td><td>Number of fields completed.</td></tr>
  <tr><td>Form.FieldsRequired</td><td>Number</td><td>Number of fields required.</td></tr>
  <tr><td colspan="3">Search</td></tr>
  <tr><td>Search.Query</td><td>String</td><td>Query string used in the input</td></tr>
  <tr><td>Search.TotalMatchingResults</td><td>Number</td><td>Total number of search results.</td></tr>
  <tr><td>Search.ResultsPerPage</td><td>Number</td><td>Number of results shown per page.</td></tr>
  <tr><td>Search.CurrentResultsPage</td><td>Number</td><td>Current results page that the user is viewing.</td></tr>
  <tr><td>Search.FilterExpression</td><td>String</td><td>Any additional filter expressions used.</td></tr>
  <tr><td>Search.SortCriteria</td><td>String</td><td>Criteria for sorting the search result. For example - Relevance, Price.</td></tr>
  <tr><td>Search.SortOrder</td><td>String</td><td>Sort order for Search results - Ascending/Descending.</td></tr>
  <tr><td colspan="3">Item/Item List</td></tr>
  <tr><td>Item</td><td>Item</td><td>Focused item in an event, indicating, the item added to a cart, item viewed.</td></tr>
  <tr><td>ItemsList</td><td>List&lt;Item&gt;</td><td>Focused list of items in an event, indicating, items purchased, items in a cart, item search results.</td></tr>
  <tr><td colspan="3">Item Impressions</td></tr>
  <tr><td>AdditionalItemImpressions</td><td>List&lt;Item&gt;</td><td>Additional Item impressions list</td></tr>
  <tr><td colspan="3">Cart</td></tr>
  <tr><td>Cart.Id</td><td>String</td><td>Unique identifier for a cart.</td></tr>
  <tr><td>Cart.ItemsCount</td><td>Number</td><td>Number of items in the cart.</td></tr>
  <tr><td>Cart.Currency</td><td>String</td><td>Currency for cart value.</td></tr>
  <tr><td>Cart.Value</td><td>Number</td><td>Monetary value of items in the cart.</td></tr>
  <tr><td colspan="3">Order Information</td></tr>
  <tr><td>OrderId</td><td>String</td><td>Unique identifier for a order. We will only store the order identifier here, other information related to the order will be stored in the standard order object.</td></tr>
  <tr><td colspan="3">Device</td></tr>
  <tr><td>DeviceId</td><td>String</td><td>Unique identifier of the user's device.</td></tr>
  <tr><td colspan="3">Scroll Attributes</td></tr>
  <tr><td>Scroll.DepthPercentage</td><td>String</td><td>Vertical Scroll depth percentage. This helps understand how far a users scroll through a web page.</td></tr>
  <tr><td>Scroll.PositionX</td><td>Number</td><td>Horizontal Scroll position in pixels from the left.</td></tr>
  <tr><td>Scroll.PositionY</td><td>Number</td><td>Vertical Scroll position in pixels from the top.</td></tr>
  <tr><td colspan="3">Error</td></tr>
  <tr><td>Error.Description</td><td>String</td><td>A short description of the error.</td></tr>
  <tr><td>Error.Type</td><td>String</td><td>User Input Error/Server Error.</td></tr>
  <tr><td colspan="3">User</td></tr>
  <tr><td>User.Id</td><td>String</td><td>Unique identifier of the user</td></tr>
  <tr><td>User.AnonymousId</td><td>String</td><td>Anonymous UserId. This would be a uniqueId assigned to a user when they are not logged in.</td></tr>
  <tr><td>User.IsReturning</td><td>String</td><td>A Boolean value indicating if a user is revisiting.</td></tr>
  <tr><td>User.IsLoggedIn</td><td>String</td><td>A Boolean value indicating if a user is logged in.</td></tr>
  <tr><td colspan="3">Activity Location</td></tr>
  <tr><td>Location.Country</td><td>String</td><td>User activity country.</td></tr>
  <tr><td>Location.State</td><td>String</td><td>User activity state.</td></tr>
  <tr><td>Location.Province</td><td>String</td><td>User activity province.</td></tr>
  <tr><td>Location.County</td><td>String</td><td>User activity county.</td></tr>
  <tr><td>Location.City</td><td>String</td><td>User activity city.</td></tr>
  <tr><td>Location.Latitude</td><td>String</td><td>User activity location coordinates</td></tr>
  <tr><td>Location.Longitude</td><td>String</td><td>User activity location coordinates</td></tr>
  <tr><td colspan="3">Application Attributes</td></tr>
  <tr><td>Application.Name</td><td>String</td><td>The name of the application.</td></tr>
  <tr><td>Application.Version</td><td>String</td><td>If the device is Mobile, we can capture the Application Version here. User could also consider using this for population A/B testing or experimentation attributes.</td></tr>
  <tr><td>Application.Environment</td><td>String</td><td>Application environments, like - Beta, Gamma, Prod.</td></tr>
  <tr><td colspan="3">Custom Attributes</td></tr>
  <tr><td>Attributes</td><td>Map&lt;String, String&gt;</td><td>Any custom attributes or metadata to add to the event.</td></tr>
</tbody>
</table>



**WebAnalytics Item Object Schema**  

| Field | Type | Description | 
| --- | --- | --- | 
| Id | String | Unique Identifier for the item. | 
| Title | String | Title of the Item. | 
| Category | String | Category of the item. | 
| Value | String | Monetary value of the item. | 
| Currency | String | Currency of the item. | 
| Quantity | Number | Quantity of the item. | 
| ImpressionType | String | String identifying the impression type for an event. For example - Featured, Sponsored, Top picks. | 
| ImpressionId | String | A string identifier for uniquely identifying an impression. | 


**Device Standard Object Schema**  

| Field | Type | Description | 
| --- | --- | --- | 
| DeviceId | String | A unique identifier for the device. | 
| Type | String | Type of device (for example, desktop, mobile) | 
| Model | String | Device model, like - Macbook Pro/Air, IPhone 16. | 
| Manufacturer | String | Manufacturer of the device. | 
| OperatingSystem | String | Indicates Windows, MacOs, IOS, Android. | 
| OperatingSystemVersion | String | OS Version | 
| ScreenWidth | Number | Width of the Screen ViewPort | 
| ScreenHeight | Number | Height of the Screen ViewPort | 
| Browser | String | Name of the Browser the user is interacting with. | 
| BrowserVersion | String | Version of the Browser | 
| Locale | String | Device or App locale. | 
| Attributes | Map<String, String> | Any Custom Attributes for a Device. | 