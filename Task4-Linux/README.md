# Task 4: Installing Linux and Running ROS

## Objective

The objective of this task is to install the Ubuntu Linux operating system and set up the Robot Operating System (ROS).

---

## Installation Steps

### 1. Install VirtualBox
- Downloaded and installed Oracle VirtualBox.
- Created a new virtual machine.

### 2. Install Ubuntu
- Downloaded the Ubuntu LTS ISO file.
- Attached the ISO file to the virtual machine.
- Allocated RAM and disk space.
- Installed Ubuntu by following the installation wizard.
- Restarted the virtual machine after the installation was completed.

### 3. Update the System
Opened the Terminal and updated the operating system using the following commands:
sudo apt update
sudo apt upgrade -y

### 4. Install ROS
- Added the required ROS repository.
- Installed ROS by following the official installation instructions.
- Configured the environment.

### 5. Verify the Installation

To make sure ROS was installed successfully, I ran:
roscore

The command started successfully, confirming that ROS was installed correctly.

---

## Problems I Faced

- Downloading the Ubuntu ISO file took a long time because of its large size.
- The Ubuntu installation process was slower than expected.
- I had to update the system before installing ROS to avoid package errors.
- I experienced a temporary internet connection issue inside the virtual machine, which was fixed by restarting VirtualBox.
- Some warning messages appeared during installation, but they did not affect the final result.

---

## Result

Ubuntu Linux was installed successfully, and ROS was installed and tested successfully by running the roscore command.

The system is now ready for future ROS projects and robotics development.
