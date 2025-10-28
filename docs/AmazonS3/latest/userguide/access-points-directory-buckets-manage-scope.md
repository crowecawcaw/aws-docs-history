# Manage the scope of your access points for directory buckets

This section explains how to view and modify the scope of your access points for directory buckets using the AWS Command Line Interface, REST API, or AWS SDKs. You can use the access point scope to restrict access to specific prefixes or API operations.

###### Topics

- [View the scope of your access points for directory buckets](#access-points-directory-buckets-view-scope "#access-points-directory-buckets-view-scope")
- [Modify the scope of your access point for directory buckets](#access-points-directory-buckets-modify-scope "#access-points-directory-buckets-modify-scope")
- [Delete the scope of your access points for directory buckets](#access-points-directory-buckets-delete-scope "#access-points-directory-buckets-delete-scope")

## View the scope of your access points for directory buckets

You can use the AWS Management Console, AWS Command Line Interface, REST API, or AWS SDKs to view the scope of your access point for directory buckets.

###### To view the scope of your access point for directory buckets

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access points for directory buckets**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage.
6. Choose the **Permissions** tab.
7. In the **Access point scope**, you can see the prefixes and permissions applied to the access point.
   The following `get-access-point-scope` example command shows how you can use
   the AWS CLI to view the scope of your access point.

The following command shows the scope of the access point `my-access-point`--`zoneID`--xa-s3 for AWS account `111122223333`.

```
aws s3control get-access-point-scope --name ``my-access-point``--`zoneID`--xa-s3 --account-id `111122223333`
```

For more information and examples, see [get-access-point-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-scope.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-scope.html") in the AWS CLI Command Reference.

###### Example result of `get-access-point-scope`

```

{
    "Scope": {
        "Permissions": [
            "ListBucket",
            "PutObject"
        ]
  "Prefixes": [
            "Prefix": "MyPrefix1*",
            "Prefix": "MyObjectName.csv"
        ]
    }
}

```

The following `GetAccessPointScope` example request shows how you can use
the REST API to view the scope of your access point.

The following request shows the scope of the access point `my-access-point`--`region`-`zoneID`--xa-s3 for AWS account `111122223333`.

```

GET /v20180820/accesspoint/``my-access-point``--`zoneID`--xa-s3/scope HTTP/1.1
Host: s3express-control.`region`.amazonaws.com
x-amz-account-id: `111122223333`

```

###### Example result of `GetAccessPointScope`

```

      HTTP/1.1 200
      <?xml version="1.0" encoding="UTF-8"?>
      <GetAccessPointScopeResult>
          <Scope>
              <Prefixes>
                  <Prefix>MyPrefix1*</Prefix>
                  <Prefix>MyObjectName.csv</Prefix>
              </Prefixes>
              <Permissions>
                  <Permission>ListBucket</Permission>
                  <Permission>PutObject</Permission>
              </Permissions>
              <Scope>
      </GetAccessPointScopeResult>

```

You can use the AWS SDKs to view the scope of your access point. For more information, see [list of supported SDKs](../API/API_control_GetAccessPointScope.md#API_control_GetAccessPointScope_SeeAlso "../API/API_control_GetAccessPointScope.md#API_control_GetAccessPointScope_SeeAlso") in the Amazon Simple Storage Service API Reference.

## Modify the scope of your access point for directory buckets

You can use the AWS Management Console, AWS Command Line Interface, REST API, or AWS SDKs to modify the scope of your access points for directory buckets. Access point scope is used to restrict access to specific prefixes, API operations, or a combination of both.

You can include one or more of the following API operations as permissions:

- `PutObject`
- `GetObject`
- `DeleteObject`
- `ListBucket` (required for `ListObjectsV2`)
- `GetObjectAttributes`
- `AbortMultipartUploads`
- `ListBucketMultipartUploads`
- `ListMultipartUploadParts`

###### Note

You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.

###### To modify access point scope

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access points for directory buckets**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage.
6. Choose the **Permissions** tab.
7. In the **Access point scope** section, choose **Edit**.
8. To add or remove prefixes:
   1. To add a prefix, choose **Add prefix**. In the **Prefix** field, enter a prefix of the directory bucket. Repeat to add more prefixes.
   2. To remove a prefix, choose **Remove**.

9. To add or remove permissions:
   1. To add a permission, in the **Choose data operations** field, choose the permission.
   2. To remove a permission, choose the **X** next to the permission.

10. Choose **Save changes**.
    The following `put-access-point-scope` example command shows how you can use
    the AWS CLI to modify the scope of your access point.

The following command modifies the access point scope of `my-access-point`--`zoneID`--xa-s3 for AWS account `111122223333`.

###### Note

You can use wildcards in prefixes by using the asterisk (\*) character. If you want to use the asterisk character as a literal, add a backslash character (\) before it to escape it.

All prefixes have an implicit '\*' ending, meaning all paths withing the prefix will be included.

When you modify the scope of an access point with the AWS CLI, you replace the existing scope.

```
aws s3control put-access-point-scope --name ``my-access-point``--`zoneID`--xa-s3 --account-id `111122223333` --scope Prefixes=`string`,Permissions=`string`
```

For more information and examples, see [put-access-point-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-access-point-scope.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-access-point-scope.html") in the AWS CLI Command Reference.

The following `PutAccessPointScope` example request shows how you can use
the REST API to modify the scope of your access point.

The following request modifies the access point scope of `my-access-point`--`zoneID`--xa-s3 for AWS account `111122223333`.

###### Note

You can use wildcards in prefixes by using the asterisk (\*) character. If you want to use the asterisk character as a literal, add a backslash character (\) before it to escape it.

All prefixes have an implicit '\*' ending, meaning all paths withing the prefix will be included.

When you modify the scope of an access point with the API, you replace the existing scope.

```

PUT /v20180820/accesspoint/``my-access-point``--`zoneID`--xa-s3/scope HTTP/1.1
Host: s3express-control.`region`.amazonaws.com
x-amz-account-id: `111122223333`
<?xml version="1.0" encoding="UTF-8"?>
<PutAccessPointScopeRequest>
        <Scope>
            <Prefixes>
                <Prefix>Jane/*</Prefix>
            </Prefixes>
            <Permissions>
                <Permission>PutObject</Permission>
                <Permission>GetObject</Permission>
            </Permissions>
            <Scope>
    </PutAccessPointScopeRequest>

```

You can use the AWS CLI, AWS SDKs, or REST API to modify the scope of your access point. For more information, see [list of supported SDKs](../API/API_control_PutAccessPointScope.md#API_control_PutAccessPointScope_SeeAlso "../API/API_control_PutAccessPointScope.md#API_control_PutAccessPointScope_SeeAlso") in the Amazon Simple Storage Service API Reference.

## Delete the scope of your access points for directory buckets

You can use the AWS Management Console, AWS Command Line Interface, REST API, or AWS SDKs to delete the scope of your access points for directory buckets.

###### Note

When you delete the scope of an access point, all prefixes and permissions are deleted.

###### To delete access point scope

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access points for directory buckets**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage.
6. Choose the **Permissions** tab.
7. In **Access point scope**, choose **Delete**.
8. In the **to confirm this deletion, type "confirm".** field, enter `confirm`.
9. Choose **Delete**.
   The following `delete-access-point-scope` example command shows how you can use
   the AWS CLI to delete the scope of your access point.

The following command deletes the scope of the access point `my-access-point`--`zoneID`--xa-s3 for AWS account `111122223333`.

```
aws s3control delete-access-point-scope --name ``my-access-point``--`region`-`zoneID`--xa-s3 --account-id `111122223333`
```

For more information and examples, see [delete-access-point-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point-scope.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point-scope.html") in the AWS CLI Command Reference.

The following request deletes the scope of the access point `my-access-point`--`zoneID`--xa-s3 for AWS account `111122223333`.

```

DELETE /v20180820/accesspoint/``my-access-point``--`zoneID`--xa-s3/scope HTTP/1.1
Host: s3express-control.`region`.amazonaws.com
x-amz-account-id: `111122223333`

```

You can use the AWS SDKs to delete the scope of your access point. For more information, see [list of supported SDKs](../API/API_control_DeleteAccessPointScope.md#API_control_DeleteAccessPointScope_SeeAlso "../API/API_control_DeleteAccessPointScope.md#API_control_DeleteAccessPointScope_SeeAlso") in the Amazon Simple Storage Service API Reference.
