# Profiling Unreal Engine performance

In this section, learn how to analyze your Unreal Engine game or application performance. This can help you identify area's to optimize,
leading to smoother streaming in Amazon GameLift Streams.

You can use Unreal Engine's console and its built-in stat commands to get a detailed look at your game's performance. You can access the
console in a non-shippable build or the **Editor**. A non-shippable build refers to a project that was built
using a debug or development configuration.

**To access the console**

In non-shippable builds and the [Play In
Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine#pieconsole "https://dev.epicgames.com/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine#pieconsole") mode, press the tilde (**~**) key to open the console. Double-press the tilde key to expand
the console.

Here are some tips for using the console:

- Type a keyword to list all possible commands containing that keyword. Scroll through the list using the arrow keys.
- Scroll through the history by using the arrow keys or Page up and Page down keys.
- Logs are saved in a `.txt` file in your project's `Saved/Logs` directory

###### To profile your game's performance

1. Start by running the `stat fps` and `stat unit` commands. This will give you an overview of where your game
   struggles with performance.
   - `stat fps`: Shows the current frames per second.
   - `stat unit`: Breaks down the frame into several subsections.
     - **Frame**: Total wall-clock time starting from when the simulation of the frame starts to
       when the presentation of the frame is on the screen.
     - **Game**: Total CPU time taken by the game simulation thread per frame.
     - **Draw**: Total CPU time for the rendering threads to translate the scene to commands for
       the GPU and submit them to the GPU.
     - **GPU**: Total time for the GPU to process all commands.
     - **Draws**: Total number of draws submitted for the frame.
     - **Prims**: Total number of triangles drawn.

2. Play through the game and identify areas with low performance, indicated by decreased FPS and increased time in **Game**, **Draw**, or **GPU**.
3. Run `stat game` to see how time is spent for the various gameplay groups.
4. Refine the stats for specific gameplay factors like AI, animation, physics, gameplay, scripting, and so on. Here are a few
   examples:
   - `stat ai`: Time to compute AI behavior.
   - `stat anim`: Time to compute skinned meshes.
   - `stat physics`: Time to compute physics simulations.

5. Run `stat drawcount` to see which render areas generate the most draws. The list shows the render passes that emit
   draws, and the number of draws emitted each frame. You can get more information by analyzing the GPU stats in the next step.
6. Run `stat gpu` to see which render types consume the most GPU time.
7. Refine the rendering types into broad groups, such as lights, shadows, lumen (lighting), hair, post processing, and so on. Here are
   a few common examples:
   - `stat lightrendering`: GPU time to render lights and shadows.
   - `stat shadowrendering`: GPU time to update the various shadows.
   - `stat scenerendering`: GPU time to render the scene.
     This section covers only a subset of available commands. Depending on your game's features, look into stats for areas such as asset
     streaming, virtual texturing, CPU task workload distribution, threading, sound, particles, and so on. For more information, refer to [Stat commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine "https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine").
