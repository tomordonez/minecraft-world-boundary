# Minecraft World Boundary

This project is inspired by this <a href="https://minecraft.gamepedia.com/World_boundary" target="_blank">page</a> about Minecraft world boundaries.

To use this project you need to install a Minecraft server. Here is a tutorial about <a href="https://www.tomordonez.com/installing-minecraft-server-mac.html">installing a Minecraft server on Mac</a>.

## Setup a Python3 environment

Git clone the project. Then setup a virtualenv with Python3.

## Running the project

* Start the Minecraft server.
* Launch Minecraft in multiplayer mode.
* Select the local server created.

Then in another terminal run:

    (env)$ python main.py

## Discovering Minecraft world boundaries

After loading the program. A menu shows the `XYZ` limits of a Minecraft world.

Choose an option to teleport to world boundary coordinates.

Interesting things happen at these world boundaries.

## Log file

I added an example of an output log file.

## Pending todo

The program is missing unit tests.

It's missing a time delay between Teleports. I commented sequential Teleports. You can uncomment them to test.
