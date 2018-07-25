Summary:	Xorg input driver for mice in VMware
Name:		x11-driver-input-vmmouse
Version:	13.1.0
Release:	4
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-vmmouse-%{version}.tar.bz2
ExclusiveArch:	%{ix86} x86_64
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.18
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

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
%setup -qn xf86-input-vmmouse-%{version}
%apply_patches
autoreconf -fiv

%build
%configure  --with-udev-rules-dir=%{_udevrulesdir}
%make

%install
%makeinstall_std

# HAL is dead for long time
rm -rf %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty/11-x11-vmmouse.fdi

%files
%{_libdir}/hal/hal-probe-vmmouse
%{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_bindir}/vmmouse_detect
%{_mandir}/man1/vmmouse_detect.*
%{_mandir}/man4/vmmouse.*
%{_udevrulesdir}/69-xorg-vmmouse.rules
%{_datadir}/X11/xorg.conf.d/50-vmmouse.conf
