# Approve previously rejected assignments

You can approve previously rejected assignments to reverse any rejections you
might make by mistake. It is important to make sure that all acceptable work is
approved to ensure a good reputation with Workers.

You can only approve previously rejected assignments that were submitted within the previous 30 days
and only if the assignment's related Human Intelligence Task (HIT) has not been disposed.

###### To approve previously rejected assignments

1. On the Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/ "https://requester.mturk.com/"),
   choose the **Manage** tab and then choose
   **Results**.
2. Under **Manage Batches**, choose the arrow next to **Batches already
   reviewed**.
3. Choose **Results** on the batch that contains the
   previously rejected assignments that you want to approve.
4. On the **Review Results** page for the batch that
   contains the rejected assignments you want to approve, choose
   **Download CSV**. If you have not downloaded a results
   .csv file before, you can follow the detailed steps described in [Download and review assignments](ReviewingResultsOutsideoftheRUI.md#DownloadtheResults "ReviewingResultsOutsideoftheRUI.md#DownloadtheResults").
5. In the downloaded .csv file, mark an assignment as approved by putting
   an **x** in the **Approve** column and
   remove the text from the **Reject** column.
6. After you mark the rejected assignments for approval, save the file,
   and then upload the modified .csv file by choosing **Upload
   CSV** on the **Review Results** page for the
   batch. If you have not uploaded a modified results .csv file before, you can
   follow the steps in [Upload reviewed results](ReviewingResultsOutsideoftheRUI.md#ReviewingandUploadingtheResults "ReviewingResultsOutsideoftheRUI.md#ReviewingandUploadingtheResults").
7. When you're asked to confirm your approval choices, choose
   **Yes** to confirm the approval of the assignments,
   which approves the assignments, pays the Workers, and updates the Workers'
   HITs submitted statistics.
   Approving a rejected assignment initiates two payments from your
   Requester Amazon.com account: one payment to the Worker who submitted the
   results for the reward amount specified in the HIT and one payment for
   Mechanical Turk fees. For the operation to succeed, you must have
   sufficient funds in your account to pay the Worker and the fees.

If your HITs were created using the Mechanical Turk API, you can approve a previously rejected assignment using the
[ApproveRejectedAssignment](../AWSMturkAPI/ApiReference_ApproveRejectedAssignmentOperation.md "../AWSMturkAPI/ApiReference_ApproveRejectedAssignmentOperation.md") operation.
