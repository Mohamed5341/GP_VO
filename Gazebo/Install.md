# Install Gazebo

We are using Gazebo 9 which is used with ROS melodic and PX4. For detailed steps see [Gazebo](http://gazebosim.org/tutorials?cat=install&tut=install_ubuntu&ver=9.0)

1. Setup computer to accept software

    sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

to check if process is done correctly

    cat /etc/apt/sources.list.d/gazebo-stable.list

![Gazebo Accept software](../Images/Gazebo/Install/gazebo_accept_software.png)

2. Setup Key

    wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -

![Setup Key](../Images/Gazebo/Install/setup_key.png)

3. Check if there is required updates

    sudo apt-get update

4. Install Gazebo

    sudo apt-get install gazebo9 libgazebo9-dev

![Gazebo Install](../Images/Gazebo/Install/gazebo_install_command.png)

5. To make sure it is installed correctly write

    gazebo

if this error appears

![Gazebo Install Error](../Images/Gazebo/Install/gazebo_install_error.png)

Use this command to update package

    sudo apt upgrade libignition-math2

![Gazebo Error Fix](../Images/Gazebo/Install/gazebo_error_fix.png)

Then run `gazebo` command again and it will open gazebo simulator.

![Gazebo Error Fix](../Images/Gazebo/Install/gazebo_simulator.png)