#

Delete accelerator

If you created an accelerator as a test or if you're no longer using an accelerator, you can
delete it. On the console, disable the accelerator, and then you can delete it. You don't
have to remove listeners and endpoint groups from the accelerator.

To delete an accelerator by using an API operation instead of the console, you must first
remove all listeners and endpoint groups that are associated with the accelerator, and then
disable it. For more information, see the [DeleteAccelerator](../api/API_DeleteAccelerator.md "../api/API_DeleteAccelerator.md") operation in
the _AWS Global Accelerator API Reference_.

###### Warning

When you delete an accelerator, you lose the static IP addresses that are assigned
to the accelerator and you can no longer route traffic by using them.

# To disable an accelerator

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. In the list, choose an accelerator that you want to disable.
3. Choose **Edit**.
4. Choose **Disable accelerator**, and then choose
   **Save**.

# To delete an accelerator

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. In the list, choose an accelerator that you want to delete.
3. Choose **Delete**.

###### Note

If you haven't disabled the accelerator, **Delete** is unavailable. 4. In the confirmation dialog box, choose **Delete**.
