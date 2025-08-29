> ⚠️ **Notice:**  
> This project has migrated to **[Codeberg](https://codeberg.org/Synchro/copr-xone-git)**. 

Copr repository for git builds of xone, commits are fetched every hour.

The packages in this repo should work on Fedora 41+.



## Installation 
* Activate the COPR repo with: `sudo dnf copr enable jackgreiner/xone-git`
* Build the firmware package with: `sudo dnf install xone lpf-xone-firmware`
  * Approve the package build: `lpf approve xone-firmware`
  * Build the Firmware package: `lpf build xone-firmware`
  * Install the built firmware package: `lpf install xone-firmware`
* Reboot your system (this is needed to load the modules)

## Removal
* Remove the xone packages with `sudo dnf remove xone lpf-xone-firmware xone-firmware`
* Remove the repository with `sudo dnf copr remove jackgreiner/xone-git`


## Issues

Feel free to open issues when there are build issues I haven't fixed for a few days: https://github.com/ProjectSynchro/copr-xone-git/issues

If you'd like me to attempt to package this for other RPM based distros like SUSE, open an issue and I'll see what I can do :)


## Building Locally Using fedpkg

To build this package locally using `fedpkg`, follow these steps:

1. **Clone the Repository**:
    ```sh
    fedpkg clone -a https://github.com/ProjectSynchro/copr-xone-git.git
    cd copr-xone-git
    ```

2. **Install Dependencies**:
    ```sh
    sudo dnf install fedpkg
    sudo dnf builddep xone.spec
    ```

3. **Build the Package**:
    ```sh
    fedpkg local
    ```

This will create the RPM packages in the `~/rpmbuild/RPMS/` directory.

For more information on using `fedpkg`, refer to the [Fedora Packaging Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/).
