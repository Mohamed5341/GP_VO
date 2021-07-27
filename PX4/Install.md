# Installing PX4 Development Environment
---

## 1. Git
Before installing PX4 development environment, you need to install [git](https://git-scm.com/). Open terminal and write

        sudo apt install git

<div style="text-align:center"><img alt="git install command" src="../Images/PX4/Install/install_git_command.png"/></div>


Terminal asks for user confirmation to install required packages. Write "y" and hit **enter**.

<div style="text-align:center"><img alt="git installation promote message" src="../Images/PX4/Install/install_git_promot.png"/></div>

When installation is completed you can check using:

        git --version

This will show version of installed git.

<div style="text-align:center"><img alt="git version" src="../Images/PX4/Install/git_check_version.png"/></div>

***

## 2. Download source code

First, you need to have an account on [GitHub](https://github.com/) then fork [PX4 repository](https://github.com/PX4/PX4-Autopilot) to your account, so you can have your own version of code to save your changes. After login with your GitHub account you can fork repository using fork button.

<div style="text-align:center"><img alt="GitHub Fork" src="../Images/PX4/Install/github_fork_button.png"/></div>

It will take seconds to fork repository.

<div style="text-align:center"><img alt="GitHub Forking" src="../Images/PX4/Install/github_forking.png"/></div>

Next, you can find a version of code to your account.

<div style="text-align:center"><img alt="GitHub Fork Completed" src="../Images/PX4/Install/github_fork_finished.png"/></div>

Before downloading source code, we need to edit something to be used later, we need to fork [PX4-SITL_gazebo repository](https://github.com/PX4/PX4-SITL_gazebo). But PX4 requires certain version of this repository. which can be found inside `PX4-Autopilot/Tools/` 

<div style="text-align:center"><img alt="SITL Gazebo Version" src="../Images/PX4/Install/sitl_gazebo_submodule_version.png"/></div>

After forking this repository, open commits

<div style="text-align:center"><img alt="SITL Gazebo commits" src="../Images/PX4/Install/open_sitl_gazebo_commits.png"/></div>

and find required commit from PX4 repository.

<div style="text-align:center"><img alt="SITL Gazebo required commit" src="../Images/PX4/Install/find_required_px4_commit.png"/></div>

open this commit and select browse files.

<div style="text-align:center"><img alt="Select browse file" src="../Images/PX4/Install/select_browse_file.png"/></div>

Then your forked repository is opened at this commit.

<div style="text-align:center"><img alt="Repository at certain commit" src="../Images/PX4/Install/repo_at_certain_commit.png"/></div>

From commit name, write branch name, then create this branch from selected commit.

<div style="text-align:center"><img alt="create branch from commit" src="../Images/PX4/Install/create_branch_from_commit.png"/></div>

Now, we have our branch of PX4-SITL_Gazebo repository. We need PX4 repository to use our gazebo repository instead of original one.Git specify modules of a repository by a `.gitmodules` file. First we need to create a branch in our forked PX4 repository.

<div style="text-align:center"><img alt="create PX4 branch" src="../Images/PX4/Install/px4_create_branch.png"/></div>

In this branch, modify `.gitmodules` file by removing URL of gazebo repository with your forked one and specify branch to your branch.

<div style="text-align:center"><img alt=".gitmodule file" src="../Images/PX4/Install/gitmodules_file.png"/></div>

<div style="text-align:center"><img alt="modify modules file" src="../Images/PX4/Install/edit_submodules_file.png"/></div>

<div style="text-align:center"><img alt="add your date to modules file" src="../Images/PX4/Install/edit_submodules_with_your_data.png"/></div>

don't forget to commit changes.

<div style="text-align:center"><img alt="commit changes" src="../Images/PX4/Install/commit_submodule_changes.png"/></div>

Now, you are ready to download your forked PX4 repository.

        git clone https://github.com/<username>/PX4-Autopilot.git

<div style="text-align:center"><img alt="clone px4 repo" src="../Images/PX4/Install/git_clone_px4.png"/></div>

It will take some time to download (depending on your internet connection).

<div style="text-align:center"><img alt="clone is finished" src="../Images/PX4/Install/git_clone_finish.png"/></div>

Next, you need to download submodules. But first you need to change branch to created one.

        cd PX4-Autopilot
        git checkout <branch_name>

<div style="text-align:center"><img alt="change branch" src="../Images/PX4/Install/px4_change_branch.png"/></div>

Next, download submodules

        git submodule update --init --recursive

<div style="text-align:center"><img alt="install submodules" src="../Images/PX4/Install/download_submodules.png"/></div>

Now source code is download.

***

## 3. Installing ROS Melodic and Gazebo
PX4 provides a script to download ROS Melodic and Gazebo.

        wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_ros_melodic.sh
        bash ubuntu_sim_ros_melodic.sh

<div style="text-align:center"><img alt="install ROS and Gazebo" src="../Images/PX4/Install/install_ros_gazebo.png"/></div>

It will take time to download (depending on your internet connection). It can give error while compiling ROS packages

<div style="text-align:center"><img alt="ROS install Error" src="../Images/PX4/Install/ROS_error_compile.png"/></div>

This happens because some ROS packages are missing. To solve this solution use this command to downlaod required packages:

        cd ~/catkin_ws
        sudo rosdep init
        rosdep update

<div style="text-align:center"><img alt="ROS dependencies install" src="../Images/PX4/Install/rosdep_init_install.png"/></div>

Now, try to build ROS packages again using (**be careful** when building mavros package it takes a lot of processing so try when you run next command to close every opened window and leave terminal only).

        catkin build

If error appears again (because missing package is not listed in dependencies list). Look in error message and find missing package and try to install it manually, or even some python packages are missing.

<div style="text-align:center"><img alt="ROS missing package" src="../Images/PX4/Install/ros_package_is_missing.png"/></div>

<div style="text-align:center"><img alt="python missing package" src="../Images/PX4/Install/ros_package_is_missing2.png"/></div>

Install ROS package by using

        sudo apt-get install ros-melodic-<package_name>

Or installing python package by using

        pip install <package_name>

<div style="text-align:center"><img alt="ROS install package" src="../Images/PX4/Install/ros_install_package_manually.png"/></div>

Another possible problem is:

<div style="text-align:center"><img alt="ROS compile problem" src="../Images/PX4/Install/missing_library.png"/></div>

you need to download `Geographic_Lib` using

        sudo apt-get install libgeographic-dev

Build ROS workspace again until it builds successfully.

<div style="text-align:center"><img alt="ROS compile sucess" src="../Images/PX4/Install/ros_build_success.png"/></div>

Now everything is installed and ready to run.