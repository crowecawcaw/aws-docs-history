

# Troubleshooting Android and iOS applications in AWS Device Farm

The following topics describe common problems with Android and iOS applications in Device Farm and how to resolve them.

## Certain windows in my Android application show a blank or black screen
<a name="flag-secure-screen-issue"></a>

If you are testing an Android application and notice that certain windows in the application appear with a black screen in Device Farm's video recording of your test, your application may be using Android's `FLAG_SECURE` feature. This flag (as described in [Android's official documentation](https://developer.android.com/reference/android/view/WindowManager.LayoutParams.html#FLAG_SECURE)) is used to prevent certain windows of an application from being recorded by screen recording tools. As a result, Device Farm's screen recording feature (for both automation and remote access testing) may show a black screen in place of your application's window if the window uses this flag. 

This flag is often used by developers for pages in their application that contain sensitive information such as login pages. If you are seeing a black screen in place of your application's screen for certain pages like its login page, work with your developer(s) to obtain a build of the application that doesn't use this flag for testing.

Additionally, note that Device Farm can still interact with application windows that have this flag. So, if your application's login page appears as a black screen, you may still be able to enter your credentials in order to log in to the application (and thus view pages not blocked by the `FLAG_SECURE` flag).