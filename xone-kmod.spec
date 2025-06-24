%if 0%{?fedora}
%global buildforkernels akmod
%endif
%global debug_package %{nil}

%global commit 474bace4dde2cac5784828e7504735d909b291a0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20250622
%global tag 0.3.1

%global prjname xone

Name:           %{prjname}-kmod
Summary:        Kernel module (kmod) for %{prjname}
Version:        %{tag}
Release:        1.%{git_date}git%{shortcommit}%{?dist}
Epoch:          1
License:        GPLv2+
#URL:            https://github.com/medusalix/xone
URL:            https://github.com/dlundqvist/xone
#Source0:       %%{url}/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  elfutils-libelf-devel
BuildRequires:  kmodtool

Requires:       lpf-xone-firmware

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{prjname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
xone is a Linux kernel driver for Xbox One and Xbox Series X|S accessories.
It serves as a modern replacement for xpad, aiming to be compatible with
Microsoft's Game Input Protocol (GIP).

This package contains the kmod module for %{prjname}.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu} --kmodname %{prjname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -c %{name}-%{commit} -N

for kernel_version  in %{?kernel_versions} ; do
  cp -a xone-%{version} _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -D -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}


%changelog
* Thu May 22 2025 Jan200101 <sentrycraft123@gmail.com> - 1:0.3.1-1
- Updatae to 0.3.1

* Sat Apr 19 2025 Jan200101 <sentrycraft123@gmail.com> - 1:0.3.0-8
- switch package to a maintained fork

* Wed Nov 27 2024 Jan200101 <sentrycraft123@gmail.com> - 1:0.3.0-7
- split kernel module into separate package

