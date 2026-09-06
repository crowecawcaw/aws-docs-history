

# Mapping WebAnalytics-Clickstream objects to standard objects
<a name="web-analytics-clickstream-mapping"></a>

The WebAnalytics-Clickstream mapping template defines how clickstream event data is ingested into Customer Profiles. It maps source fields to the standard web analytics object, the standard order object, and the standard device object. 

**Mapping to the standard web analytics object**

The following table lists which fields are mapped from the WebAnalytics-Clickstream source to the standard web analytics object.


| WebAnalytics-Clickstream source field | Standard web analytics target field | 
| --- | --- | 
| EventId | Attributes.ClickstreamEventId | 
| Session.Id | Session.Id | 
| Session.StartTimestamp | Session.StartTimestamp | 
| Browser.Id | Browser.Id | 
| User.Id | User.Id | 
| User.AnonymousId | User.AnonymousId | 
| User.IsReturning | User.IsReturning | 
| User.IsLoggedIn | User.IsLoggedIn | 
| OrderId | OrderId | 
| DeviceId | DeviceId | 
| EventType | EventType | 
| EventTimestamp | EventTimestamp | 
| EventDuration | EventDuration | 
| EventValue | EventValue | 
| Page.Title | Page.Title | 
| Page.Location | Page.Location | 
| Page.Referrer | Page.Referrer | 
| Page.Category | Page.Category | 
| Element.Id | Element.Id | 
| Element.Type | Element.Type | 
| Element.Classes | Element.Classes | 
| Element.Text | Element.Text | 
| Element.AltText | Element.AltText | 
| Element.Source | Element.Source | 
| Search.Query | Search.Query | 
| Search.TotalMatchingResults | Search.TotalMatchingResults | 
| Search.ResultsPerPage | Search.ResultsPerPage | 
| Search.CurrentResultsPage | Search.CurrentResultsPage | 
| Search.FilterExpression | Search.FilterExpression | 
| Search.SortCriteria | Search.SortCriteria | 
| Search.SortOrder | Search.SortOrder | 
| Item.Id | Item.Id | 
| Item.Title | Item.Title | 
| Item.Category | Item.Category | 
| Item.Value | Item.Value | 
| Item.Currency | Item.Currency | 
| Item.Quantity | Item.Quantity | 
| Item.ImpressionId | Item.ImpressionId | 
| Item.ImpressionType | Item.ImpressionType | 
| ItemsList[].Id | ItemsList[].Id | 
| ItemsList[].Title | ItemsList[].Title | 
| ItemsList[].Category | ItemsList[].Category | 
| ItemsList[].Value | ItemsList[].Value | 
| ItemsList[].Currency | ItemsList[].Currency | 
| ItemsList[].Quantity | ItemsList[].Quantity | 
| ItemsList[].ImpressionType | ItemsList[].ImpressionType | 
| ItemsList[].ImpressionId | ItemsList[].ImpressionId | 
| AdditionalItemImpressions[].Title | AdditionalItemImpressions[].Title | 
| AdditionalItemImpressions[].Id | AdditionalItemImpressions[].Id | 
| AdditionalItemImpressions[].Category | AdditionalItemImpressions[].Category | 
| AdditionalItemImpressions[].Value | AdditionalItemImpressions[].Value | 
| AdditionalItemImpressions[].Currency | AdditionalItemImpressions[].Currency | 
| Cart.Id | Cart.Id | 
| Cart.Value | Cart.Value | 
| Cart.Currency | Cart.Currency | 
| Form.Id | Form.Id | 
| Form.Name | Form.Name | 
| Form.Length | Form.Length | 
| Form.ValidationErrors | Form.ValidationErrors | 
| Form.FieldsCompleted | Form.FieldsCompleted | 
| Form.FieldsRequired | Form.FieldsRequired | 
| Scroll.DepthPercentage | Scroll.DepthPercentage | 
| Scroll.PositionX | Scroll.PositionX | 
| Scroll.PositionY | Scroll.PositionY | 
| Error.Description | Error.Description | 
| Error.Type | Error.Type | 
| Location.Country | Location.Country | 
| Location.State | Location.State | 
| Location.Province | Location.Province | 
| Location.City | Location.City | 
| Location.County | Location.County | 
| Location.Latitude | Location.Latitude | 
| Location.Longitude | Location.Longitude | 
| Application.Name | Application.Name | 
| Application.Version | Application.Version | 
| Application.Environment | Application.Environment | 

**Mapping to the standard order object**

The following table lists which fields are mapped from the WebAnalytics-Clickstream source to the standard order object.


| WebAnalytics-Clickstream source field | Standard order target field | 
| --- | --- | 
| OrderId | Attributes.WebAnalyticsOrderId | 
| Session.Id | Attributes.WebSessionId | 
| Order.Value | TotalPrice | 
| Order.Currency | Currency | 
| Order.Discounts | TotalDiscounts | 
| Order.ShippingMethod | Attributes.ShippingMethod | 
| Order.ShipmentTrackingId | Attributes.ShipmentTrackingId | 
| Order.ShippingAddress | ShippingAddress.Address1 | 
| Order.PaymentMethod | Gateway | 
| ItemsList[].Title | OrderItems[].Title | 
| ItemsList[].Price | OrderItems[].Price | 
| ItemsList[].Quantity | OrderItems[].Quantity | 

**Mapping to the standard device object**

The following table lists which fields are mapped from the WebAnalytics-Clickstream source to the standard device object.


| WebAnalytics-Clickstream source field | Standard device target field | 
| --- | --- | 
| DeviceId | Attributes.WebAnalyticsDeviceId | 
| Session.Id | Attributes.WebSessionId | 
| Device.Type | Type | 
| Device.OperatingSystem | OperatingSystem | 
| Device.OSVersion | OperatingSystemVersion | 
| Device.ScreenWidth | ScreenWidth | 
| Device.ScreenHeight | ScreenHeight | 
| Device.Browser | Browser | 
| Device.BrowserVersion | BrowserVersion | 
| Device.Locale | Locale | 
| Device.Model | Model | 
| Device.Manufacturer | Manufacturer | 

**WebAnalytics-Clickstream keys**

The WebAnalytics-Clickstream data is associated with profiles using the following indexes.


| Standard index name | WebAnalytics-Clickstream source field | Standard identifiers | 
| --- | --- | --- | 
| \_webAnalyticsClickstreamEventId | EventId | WEB\_ANALYTICS, UNIQUE | 
| \_webAnalyticsUserId | User.Id | PROFILE | 
| \_webAnalyticsAnonymousUserId | User.AnonymousId | PROFILE | 
| \_webAnalyticsOrderId | OrderId | ORDER | 
| \_webAnalyticsDeviceId | DeviceId | DEVICE | 

For example, you can use `_webAnalyticsUserId` or `_webAnalyticsAnonymousUserId` as a key name with the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API to find a profile associated with web analytics clickstream events. You can find the WebAnalytics-Clickstream objects associated with a specific profile by using the [ListProfileObjects](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjects.html) API with the `ProfileId` and `ObjectTypeName` set to `WebAnalytics-Clickstream`.