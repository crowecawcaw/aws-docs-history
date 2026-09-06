

# Viewing data repository association details
<a name="view-dra-details"></a>

You can view the details of a data repository association using the FSx for Lustre console, the AWS CLI, and the API. The details include the DRA's association ID, file system path, data repository path, import settings, export settings, status, and the ID of its associated file system.

## To view DRA details (console)
<a name="view-dra-details-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the dashboard, choose **File systems** and then select the file system that you want to view a data repository association's details for.

1. Choose the **Data repository** tab.

1. In the **Data repository associations** pane, choose the data repository association that you want to view. The **Summary** page appears, showing the DRA details.  
![Amazon FSx Details page of a data repository association.](http://docs.aws.amazon.com/fsx/latest/LustreGuide/images/dra-describe.png)

## To view DRA details (CLI)
<a name="view-dra-details-cli"></a>
+ To view the details of a specific data repository association, use the Amazon FSx CLI command `describe-data-repository-associations`, as shown following.

  ```
  $ aws fsx describe-data-repository-associations \
        --association-ids dra-872abab4b4503bfc2
  ```

  Amazon FSx returns the description of the data repository association as JSON.