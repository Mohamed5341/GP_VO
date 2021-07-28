# Installing PX4 Development Environment

## 1. Git
Before installing PX4 development environment, you need to install [git](https://git-scm.com/). Open terminal and write

        sudo apt install git

![git install command](../Images/PX4/Install/install_git_command.png)


Terminal asks for user confirmation to install required packages. Write "y" and hit **enter**.

![git installation promote message](../Images/PX4/Install/install_git_promot.png)

When installation is completed you can check using:

        git --version

This will show version of installed git.

![git version](../Images/PX4/Install/git_check_version.png)

## 2. Download source code

First, you need to have an account on [GitHub](https://github.com/) then fork [PX4 repository](https://github.com/PX4/PX4-Autopilot) to your account, so you can have your own version of code to save your changes. After login with your GitHub account you can fork repository using fork button.

![GitHub Fork](../Images/PX4/Install/github_fork_button.png)

It will take seconds to fork repository.

![GitHub Forking](../Images/PX4/Install/github_forking.png)

Next, you can find a version of code to your account.

![GitHub Fork Completed](../Images/PX4/Install/github_fork_finished.png)

Before downloading source code, we need to edit something to be used later, we need to fork [PX4-SITL_gazebo repository](https://github.com/PX4/PX4-SITL_gazebo). But PX4 requires certain version of this repository. which can be found inside `PX4-Autopilot/Tools/` 

![SITL Gazebo Version](../Images/PX4/Install/sitl_gazebo_submodule_version.png)

After forking this repository, open commits

![SITL Gazebo commits](../Images/PX4/Install/open_sitl_gazebo_commits.png)

and find required commit from PX4 repository.

![SITL Gazebo required commit](../Images/PX4/Install/find_required_px4_commit.png)

open this commit and select browse files.

![Select browse file](../Images/PX4/Install/select_browse_file.png)

Then your forked repository is opened at this commit.

![Repository at certain commit](../Images/PX4/Install/repo_at_certain_commit.png)

From commit name, write branch name, then create this branch from selected commit.

![create branch from commit](../Images/PX4/Install/create_branch_from_commit.png)

Now, we have our branch of PX4-SITL_Gazebo repository. We need PX4 repository to use our gazebo repository instead of original one.Git specify modules of a repository by a `.gitmodules` file. First we need to create a branch in our forked PX4 repository.

![create PX4 branch](../Images/PX4/Install/px4_create_branch.png)

In this branch, modify `.gitmodules` file by removing URL of gazebo repository with your forked one and specify branch to your branch.

![.gitmodule file](../Images/PX4/Install/gitmodules_file.png)

![modify modules file](../Images/PX4/Install/edit_submodules_file.png)

![add your date to modules file](../Images/PX4/Install/edit_submodules_with_your_data.png)

don't forget to commit changes.

![commit changes](../Images/PX4/Install/commit_submodule_changes.png)

Now, you are ready to download your forked PX4 repository.

        git clone https://github.com/<username>/PX4-Autopilot.git

![clone px4 repo](../Images/PX4/Install/git_clone_px4.png)

It will take some time to download (depending on your internet connection).

![clone is finished](../Images/PX4/Install/git_clone_finish.png)

Next, you need to download submodules. But first you need to change branch to created one.

        cd PX4-Autopilot
        git checkout <branch_name>

![change branch](../Images/PX4/Install/px4_change_branch.png)

Next, download submodules

        git submodule update --init --recursive

![install submodules](../Images/PX4/Install/download_submodules.png)

Now source code is download.

## 3. Installing ROS Melodic and Gazebo
PX4 provides a script to download required tools using.

        bash Tools/setup/ubuntu.sh

![PX4 install requirements](../Images/PX4/Install/install_px4_requirements.png)

it also provides another script to download ROS Melodic and Gazebo.

        wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_ros_melodic.sh
        bash ubuntu_sim_ros_melodic.sh

![install ROS and Gazebo](../Images/PX4/Install/install_ros_gazebo.png)

It will take time to download (depending on your internet connection). It can give error while compiling ROS packages

![ROS install Error](../Images/PX4/Install/ROS_error_compile.png)

This happens because some ROS packages are missing. To solve this solution use this command to downlaod required packages:

        cd ~/catkin_ws
        sudo rosdep init
        rosdep update

![ROS dependencies install](../Images/PX4/Install/rosdep_init_install.png)

Now, try to build ROS packages again using (**be careful** when building mavros package it takes a lot of processing so try when you run next command to close every opened window and leave terminal only).

        catkin build

If error appears again (because missing package is not listed in dependencies list). Look in error message and find missing package and try to install it manually, or even some python packages are missing.

![ROS missing package](../Images/PX4/Install/ros_package_is_missing.png)

![python missing package](../Images/PX4/Install/ros_package_is_missing2.png)

Install ROS package by using

        sudo apt-get install ros-melodic-<package_name>

Or installing python package by using

        pip install <package_name>

![ROS install package](../Images/PX4/Install/ros_install_package_manually.png)

Another possible problem is:

![ROS compile problem](../Images/PX4/Install/missing_library.png)

you need to download `Geographic_Lib` using

        sudo apt-get install libgeographic-dev

Build ROS workspace again until it builds successfully.

![ROS compile sucess](../Images/PX4/Install/ros_build_success.png)

Now everything is installed and ready to run.