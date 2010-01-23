Name: x11-driver-input-vmmouse
Version: 12.6.5
Release: %mkrel 2
Summary: Xorg input driver for mice in VMware
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-vmmouse-%{version}.tar.bz2
Patch0: abi2.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
ExclusiveArch: %{ix86} x86_64

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
The VMMouse driver enables support for the special VMMouse protocol
that is provided by VMware virtual machines to give absolute pointer
positioning.

Installing the driver will improve the user experience when using the
mouse to interact with the guest operating system. In particular, use of
the driver improves mouse "lag", provides mouse speed and acceleration
consistent with the user's host operating system, and enables the
auto-grab/ungrab feature in VMware products without requiring the VMware
toolbox application.


%prep
%setup -q -n xf86-input-vmmouse-%{version}
%patch0 -p1 -b .abi2

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/hal/fdi/policy/20thirdparty/11-x11-vmmouse.fdi
%{_libdir}/hal/hal-probe-vmmouse
%{_libdir}/xorg/modules/input/vmmouse_drv.la
%{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_bindir}/vmmouse_detect
%{_mandir}/man1/vmmouse_detect.*
%{_mandir}/man4/vmmouse.*
