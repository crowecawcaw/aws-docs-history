# Re-eliciting slots

You can configure your bot to re-elicit a slot that has already been filled by
setting that slot value to `null` and setting the next step in the
conversation to loop back to eliciting that slot. For example, you may want to re-elicit a slot after your customer declines a
confirmation of the slot elicitation based on extra information, as in the following
conversation:

![A conversation eliciting a customer's meat preference for a food order.](images/slots/order-food.png)
You can configure a loop from the confirmation response back to re-elicit the
slot with either the intent editor or the [Using Visual conversation builder](visual-conversation-builder.md "visual-conversation-builder.md").

###### Note

You can loop back to re-elicit a slot at any point in the conversation
provided that you set that slot value to `null` beforehand.

###### Reproducing the above example with the intent editor

1.  In the **Confirmation** section of
    the intent editor, select the right arrow next to
    **Prompts to confirm the intent** to
    expand the section.
2.  Select **Advanced options** at the bottom.
3.  In the **Decline response** section,
    select the right arrow next to **Set values** to
    expand the section. Fill in this section with the following steps,
    as in the image below:

        1. Set the slot value you want to re-elicit to `null`.
         In this example, we want to re-elicit the `Meat` slot,
         so we input `{Meat} = null` in the **Slot values**
         section.
        2. In the dropdown menu under **Next step in conversation**,
         choose **Elicit a slot**.
        3. A **Slot** section will appear. In the dropdown menu under
         it, choose the slot you want to re-elicit.
        4. Select **Update options** to confirm your changes.

    ![A conversation eliciting a customer's meat preference for a food order.](images/slots/decline-food.png)

###### Reproducing the above example with the Visual conversation builder

1. Create a connection from the **No** port of the **Confirmation** block to the incoming port of the **Get slot value: Meat** block.

![A connection from the declination of the confirmation prompt to the Meat slot elicitation block.](images/slots/vcb-reelicit-slot-loop.png) 2. Select the **Edit** icon in the top right corner of the **Confirmation** block.

![Edit icon in the top right corner of the confirmation block.](images/slots/vcb-reelicit-slot-confirmation-edit.png) 3. Select the gear icon next to the bot response in the **Decilne response** section.

![Gear icon next to bot response in decline response section](images/slots/vcb-reelicit-slot-confirmation.png) 4. In the **Set values** section, add "{Meat} = null" in the **Slot values** box.

![Set the slot value to be re-elicited to null in the slot values box of the set values section.](images/slots/vcb-reelicit-slot-set-slot-null.png) 5. Select **Save Intent.**
