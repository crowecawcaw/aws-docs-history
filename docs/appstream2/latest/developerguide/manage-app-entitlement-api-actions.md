# API Actions for Managing

App Entitlement for AppStream 2.0

You can use the following API operations to manage application entitlement for
AppStream 2.0.

## `AddApplicationsRequest` operation

Adds applications to the application catalog for AppStream 2.0 users. The
application catalog displayed by AppStream 2.0 includes the applications that you
add by using this API operation and the applications that you add in the
image. After you add applications by using one or both of these methods,
your users can launch the applications.

**Request syntax**

`string userSid;`

`list<Application> applications;`

**Request parameters**

**`userSid`**

The SID of the user who the request applies to.

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 208 characters.

**`applications`**

The list of applications that the request applies to.

**Type:** String

**Required**: Yes

## `Application` object

Describes the application metadata required to display and launch the
application. The application identifier must be unique and not in conflict
with other applications specified through the API operation or the
image.

**`id`**

The identifier of the application being specified. This value,
which corresponds to the `application_name` value in
an AppStream 2.0 applications report, is provided when a user launches
the application. When you enable [usage reports](enable-usage-reports.md "enable-usage-reports.md"), for
each day that users launch at least one application during their
streaming sessions, AppStream 2.0 exports an applications report to
your Amazon S3 bucket. For more information about applications
reports, see [Applications Report Fields](usage-reports-fields-applications-reports.md "usage-reports-fields-applications-reports.md").

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 512 characters.

**`displayName`**

The display name of the application being specified. This name
is displayed to the user in the application catalog.

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 512 characters.

**`launchPath`**

The Windows file system path to the executable of the
application to be launched.

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 32,767 characters.

**`iconData`**

The base-64 encoded image to display in the application
catalog. The image must be in one of the following formats:
.png, .jpeg, or .jpg.

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 1,000,000 characters.

**`launchParams`**

The parameters used to launch the application.

**Type**: String

**Required**: No

**Length constraints:** Maximum
length of 32,000 characters.

**`workingDirectory`**

The Windows file system path to the working directory the
application should be launched in.

**Type**: String

**Required**: No

**Length constraints:** Maximum
length of 32,767 characters.

## `RemoveApplicationsRequest` operation

Removes applications that were added by using the
`AddApplicationsRequest` operation. The applications are
removed from the application catalog for the user. After applications are
removed, they can't be launched. If an application is still running, AppStream 2.0
does not close it. Applications that are specified directly in the AppStream 2.0
image can't be removed.

**Request syntax**

`string userSid;`

`list<Application> applications;`

**Request parameters**

**`userSid`**

The SID of the user the request applies to.

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 208 characters.

**`applications`**

The list of applications that the request applies to.

**Type:** String

**Required**: Yes

## `ClearApplicationsRequest` operation

Removes all applications that were added to the application catalog by
using the `AddApplicationsRequest` operation. After applications
are removed, they can't be launched. If the applications are running when
the `ClearApplicationsRequest` operation is used, AppStream 2.0 does not
close them. Applications that are specified directly in the AppStream 2.0 image
can't be removed.

**Request syntax**

`string userSid;`

**Request parameters**

**`userSid`**

The SID of the user the request applies to.

**Type**: String

**Required**: Yes

**Length constraints:** Minimum
length of 1, maximum length of 208 characters.
