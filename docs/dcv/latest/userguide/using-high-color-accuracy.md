

# Using high color accuracy
<a name="using-high-color-accuracy"></a>

By default, Amazon DCV uses YUV 4:2:0 chroma subsampling when compressing the display output and then updates the parts of the screen that are not changing over time to a full lossless RGB implementation. This default behavior aims to strike a balance between performance and image fidelity, though it may introduce chroma artifacts. By enabling the High color accuracy setting, the YUV chroma subsampling will be set to 4:4:4, thus increasing color fidelity. However this will increase network bandwidth and could affect performance of clients, especially at high resolution, because most client machines do not support HW accelerated decoding when using YUV 4:4:4.

**Important**  
High color accuracy requires a Amazon DCV Server and a Amazon DCV Client both having version 2022.0 or later.

**Note**  
The web browser client also requires a browser supporting the [VideoDecoder](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder) interface of the Web Codecs API.

The steps depend on the client used.

------
#### [ Windows ]

1. Choose the **Settings** icon.

1. Select **Streaming Mode** from the drop-down menu.  
![Settings button located in the top-left corner of the interface.](https://docs.aws.amazon.com/dcv/latest/userguide/images/windows-yuv444.png)

1. Check the High color accuracy (YUV 4:4:4) checkbox in the **Streaming Mode** window.

1. Close the **Streaming Mode** window.

------
#### [ macOS ]

1. Choose the **Display** toolbar button.

1. Toggle **High Color Accuracy** on or off.  
![Display toolbar showing the High Color Accuracy toggle.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-high-color-accuracy.png)

**Tip**  
You can also toggle this setting from the menu bar. Choose the **Connection** menu, then select **Display**, **High Color Accuracy**.

------
#### [ Linux ]

1. Click on the **Display Settings** menu icon from the toolbar at the top.

1. Turn on the **High color accuracy** option.  
![Display Settings menu showing the High color accuracy toggle.](https://docs.aws.amazon.com/dcv/latest/userguide/images/linux-pref-display-high-accu.png)

------
#### [ Web browser ]

1. In the client, choose **Session**, **Preferences**.  
![Session is located inside the menu in the top-right of the interface.](https://docs.aws.amazon.com/dcv/latest/userguide/images/web-preferences-menu.png)

1. Under the **Display** tab, if the high color accuracy feature is available, the corresponding toggle will be visible and allows to specify whether to enable or disable the YUV chroma subsampling set to 4:4:4:  
![Display is the second tab from the left inside the Preferences modal.](https://docs.aws.amazon.com/dcv/latest/userguide/images/web-preferences-yuv444.png)

1. Save and close the **Preferences** modal.

------