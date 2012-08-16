Name: x11-driver-input-vmmouse
Version: 12.9.0
Release: 1
Summary: Xorg input driver for mice in VMware
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-vmmouse-%{version}.tar.bz2
License: MIT
ExclusiveArch: %{ix86} x86_64

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

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
%setup -qn xf86-input-vmmouse-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_datadir}/hal/fdi/policy/20thirdparty/11-x11-vmmouse.fdi
%{_libdir}/hal/hal-probe-vmmouse
%{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_bindir}/vmmouse_detect
%{_mandir}/man1/vmmouse_detect.*
%{_mandir}/man4/vmmouse.*
/lib/udev/rules.d/69-xorg-vmmouse.rules
%{_datadir}/X11/xorg.conf.d/50-vmmouse.conf


%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 12.8.0-6
+ Revision: 787189
- Rebuild for x11-server 1.12

* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 12.8.0-5
+ Revision: 783806
- version update 12.8.0

* Fri Dec 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 12.7.0-5
+ Revision: 748295
- rebuild
- cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 12.7.0-4
+ Revision: 703627
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 12.7.0-3
+ Revision: 683570
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 12.7.0-2
+ Revision: 671132
- mass rebuild

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - New version: 12.7.0

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 12.6.10-3mdv2011.0
+ Revision: 595748
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 12.6.10-2mdv2011.0
+ Revision: 584641
- adjus file list for xserver 1.9
- bump release before rebuilding for xserver 1.9

* Mon Aug 16 2010 Thierry Vignaud <tv@mandriva.org> 12.6.10-1mdv2011.0
+ Revision: 570277
- new release

* Fri Apr 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 12.6.9-1mdv2010.1
+ Revision: 533521
- New version: 12.6.9

* Thu Apr 08 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 12.6.8-1mdv2010.1
+ Revision: 533102
- New version: 12.6.8

* Wed Mar 24 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 12.6.7-1mdv2010.1
+ Revision: 527186
- New versioni: 12.6.7

* Wed Feb 10 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 12.6.6-1mdv2010.1
+ Revision: 503787
- New version: 12.6.6
  abi2.patch applied upstream (in a different way)

* Sat Jan 23 2010 Luca Berra <bluca@mandriva.org> 12.6.5-2mdv2010.1
+ Revision: 495243
- fix unresolved symbol (from archlinux)

* Fri Aug 07 2009 Thierry Vignaud <tv@mandriva.org> 12.6.5-1mdv2010.0
+ Revision: 411042
- new release

* Tue May 12 2009 Thierry Vignaud <tv@mandriva.org> 12.6.4-1mdv2010.0
+ Revision: 374900
- new version

* Mon Jan 05 2009 Thierry Vignaud <tv@mandriva.org> 12.6.3-1mdv2009.1
+ Revision: 325164
- new release

  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild for new xserver

* Sun Nov 30 2008 Thierry Vignaud <tv@mandriva.org> 12.6.2-2mdv2009.1
+ Revision: 308625
- rebuild for new xserver

* Mon Nov 17 2008 Thierry Vignaud <tv@mandriva.org> 12.6.2-1mdv2009.1
+ Revision: 303999
- adjust filelist
- new release

* Mon Oct 20 2008 Thierry Vignaud <tv@mandriva.org> 12.5.2-1mdv2009.1
+ Revision: 295707
- new release

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 12.5.1-2mdv2009.0
+ Revision: 265896
- rebuild early 2009.0 package (before pixel changes)
- add missing dot at end of description

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 12.5.1-1mdv2009.0
+ Revision: 211785
- New version

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 12.5.0-1mdv2009.0
+ Revision: 194253
- Update to version 12.5.0.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 12.4.3-4mdv2008.1
+ Revision: 160498
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 12.4.3-3mdv2008.1
+ Revision: 156593
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 12.4.3-2mdv2008.1
+ Revision: 154933
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-input-vmmouse-12.4.3@mandriva suggested on upstream
  Tag at git checkout vmmouse-12_4_3
  This tag is redundant, and only added to match pattern used in other
  repositories. Also redundant as this is a repository with a few tags, and
  all in the format ``vmmouse-12_4_[0-3]''
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 12.4.3-1mdv2008.1
+ Revision: 97067
- new upstream version: 12.4.3
- minor spec cleanup

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed Feb 28 2007 Thierry Vignaud <tvignaud@mandriva.com> 12.4.1-1mdv2007.0
+ Revision: 127113
- new release
- fix group
- fix summary & description

  + Christiaan Welvaart <cjw@daneel.dyndns.org>
    - ExclusiveArch: x86 and x86-64

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - New driver (part of X11R7.1)

