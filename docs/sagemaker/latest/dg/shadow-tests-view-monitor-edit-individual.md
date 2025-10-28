# Edit a shadow test

You can modify both scheduled and in-progress tests. Before your test starts, you can change the
description, the shadow variant configuration, the start date, and the end date of the test. You can also
turn on or turn off data capture.

After your test starts, you can only change the description, the traffic sampling percentage for the
shadow variant, and the end date.

To edit the details of your test through the console, do the following:

1. Select the test you want to edit from the **Shadow test** section on the
   **Shadow tests** page.
2. From the **Actions** dropdown list, choose **Edit**. The
   **Enter shadow test details** page appears.
3. (Optional) Under **Description**, enter a description of your test.
4. Choose **Next**. The **Enter shadow test settings** page
   appears.
5. (Optional) To edit your shadow variant, do the following:
   1. Select the shadow variant and choose **Edit**. The **Edit shadow
      variant** dialog box appears. If your test has already started, then you can
      only change the traffic sampling percentage.
   2. (Optional) Under **Name**, enter the new name to replace the old name.
   3. (Optional) Under **Traffic sample**, enter the new traffic sampling
      percentage to replace the old traffic sampling percentage.
   4. (Optional) Under **Instance type**, select the new instance type from the
      dropdown list.
   5. (Optional) Under **Instance count**, enter the new instance count to
      replace the old instance count.
   6. Choose **Apply**.
      You cannot change the model in your shadow variant using the above procedure. If you want to change
      the model, first remove the shadow variant by selecting it and choosing
      **Remove**. Then add a new shadow variant.

6. (Optional) To edit the duration of the test, do the following:
   1. Choose the box under **Duration** in the **Schedule**
      section. A popup calender appears.
   2. If your test is yet to start, you can change both the start and end dates. Select the new
      start and end dates from the calender, or enter the new start and end dates under
      **Start date** and **End date**, respectively.

   If your test has already started, you can only change the end date. Enter the new end date
   under **End date**. 3. (Optional) If your test is yet to start, you can change both the start and end times. Enter
   the new start and end times under **Start time**, and **End
   time**, respectively, in the 24 hour format.

   If your test has already started, you can only change the end time. Enter the new end time
   under **End time**, in the 24 hour format. 4. Choose **Apply**.

7. (Optional) Turn on or turn off **Enable data capture**.
8. Choose **Update shadow test**.
