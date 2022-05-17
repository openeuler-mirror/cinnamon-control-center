%global _artwork_version 5.7
%global cinnamon_desktop_version 5.2.0
%global csd_version 5.2.0
%global cinnamon_menus_version 5.2.0

Name:    cinnamon-control-center
Version: 5.2.1
Release: 1
Summary: Utilities to configure the Cinnamon desktop
# The following files contain code from
# ISC for panels/network/rfkill.h
# And MIT for wacom/calibrator/calibrator.c
# wacom/calibrator/calibrator.h
# wacom/calibrator/gui_gtk.c
# wacom/calibrator/gui_gtk.h
# wacom/calibrator/main.c
License: GPLv2+ and LGPLv2+ and MIT and ISC
URL:     https://github.com/linuxmint/%{name}
Source0: https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: http://packages.linuxmint.com/pool/main/m/mint-artwork-cinnamon/mint-artwork-cinnamon_%{_artwork_version}.tar.gz
Patch0:  https://github.com/linuxmint/%{name}/commit/0f4d212874c4fbee18b860963d0a5c7bd54dcfd1.patch

ExcludeArch: %{ix86}

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: meson
BuildRequires: intltool
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pkgconfig(libcinnamon-menu-3.0) >= %{cinnamon_menus_version}
BuildRequires: pkgconfig(cinnamon-settings-daemon) >= %{csd_version}
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(goa-backend-1.0) >= 3.21.5
BuildRequires: pkgconfig(libgnomekbd)
BuildRequires: pkgconfig(libnm) >= 1.2
BuildRequires: pkgconfig(libnma) >= 1.2
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(mm-glib) >= 0.7
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(xkbfile)

Requires: cinnamon-settings-daemon >= %{csd_version}
Requires: openEuler-menus
Requires: hicolor-icon-theme
Requires: cinnamon-translations
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
# For the network panel
Requires: nm-connection-editor
# For the colour panel
Requires: gnome-color-manager

%description
This package contains configuration utilities for the Cinnamon desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

%package filesystem
Summary: Cinnamon Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The Cinnamon control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.

%prep
%autosetup -a 1 -p 1

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install                                  \
  --delete-original                                   \
  --dir %{buildroot}/%{_datadir}/applications         \
  %{buildroot}/%{_datadir}/applications/*.desktop

# install sound files
mkdir -p %{buildroot}/%{_datadir}/cinnamon-control-center/sounds/
install -pm 0644 mint-artwork-cinnamon-%{_artwork_version}/%{_datadir}/mint-artwork-cinnamon/sounds/* %{buildroot}/%{_datadir}/cinnamon-control-center/sounds/

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/cinnamon-control-center
%{_datadir}/cinnamon-control-center/ui/
%{_datadir}/cinnamon-control-center/sounds/*.og*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/org.cinnamon.control-center.display.gschema.xml
# list all binaries explicitly, so we notice if one goes missing
%{_libdir}/libcinnamon-control-center.so.1*
%dir %{_libdir}/cinnamon-control-center-1/
%{_libdir}/cinnamon-control-center-1/panels/libcolor.so
%{_libdir}/cinnamon-control-center-1/panels/libdisplay.so
%{_libdir}/cinnamon-control-center-1/panels/libnetwork.so
%{_libdir}/cinnamon-control-center-1/panels/libonline-accounts.so
%{_libdir}/cinnamon-control-center-1/panels/libregion.so
%{_libdir}/cinnamon-control-center-1/panels/libwacom-properties.so

%files filesystem
%dir %{_datadir}/cinnamon-control-center/
%dir %{_datadir}/cinnamon-control-center/sounds/

%files devel
%{_includedir}/cinnamon-control-center-1/
%{_libdir}/libcinnamon-control-center.so
%{_libdir}/pkgconfig/libcinnamon-control-center.pc

%changelog
* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.1-1
- Inital Packaging
