Name: x11-driver-input-vmmouse
Version: 12.4.3
Release: %mkrel 2
Summary: Xorg input driver for mice in VMware
Group: System/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-input-vmmouse-12.4.3@mandriva suggested on upstream
# Tag at git checkout vmmouse-12_4_3
########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-vmmouse  xorg/drivers/xf86-input-vmmouse
# cd xorg/drivers/xf86-input/vmmouse
# git-archive --format=tar --prefix=xf86-input-vmmouse-12.4.3/ xf86-input-vmmouse-12.4.3@mandriva | bzip2 -9 > xf86-input-vmmouse-12.4.3.tar.bz2
########################################################################
Source0: xf86-input-vmmouse-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-vmmouse-12.4.3@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
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

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/vmmouse_drv.la
%{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_mandir}/man4/vmmouse.*

