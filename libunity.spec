%define major 9
%define libname %mklibname unity %{major}
%define develname %mklibname unity -d
%define git 20210128

Name:           libunity
Version:        7.1.4
Release:        1.%{git}.1
License:        LGPLv3
Summary:        Unity instrumenting and integration library

Url:            http://launchpad.net/libunity
Group:          System/Libraries
# Switch to git, as it contains some fixes
Source0:        %{name}-%{git}.tar.xz
#Source0:        https://launchpad.net/ubuntu/+archive/primary/+files/libunity_%{version}+19.04.20190319.orig.tar.gz
#Source0:        https://launchpad.net/libunity/6.0/%{version}/+download/libunity-%{version}.tar.gz
Patch0:         libunity-7.1.4-vala-053.patch

BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dee-1.0)
BuildRequires:  pkgconfig(gee-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala-devel
BuildRequires:  vala
BuildRequires:	intltool
BuildRequires:  gnome-common
BuildRequires:	gtk+3-devel

%description
Libunity is a shared library to be able to interact with the launcher and
add places in Unity environment.

%package -n %{libname}
Summary:        Unity instrumenting and integration library - shared libraries

Group:          System/Libraries

%description -n %{libname}
Unity instrumenting and integration library - shared libraries
Libunity is a shared library to be able to interact with the launcher and
add places in Unity environment.

%package -n %{develname}
Summary:        Unity instrumenting and integration library - development files

Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
Unity instrumenting and integration library - development files
Libunity is a shared library to be able to interact with the launcher and
add places in Unity environment.

This package provides the development files required to build applications.

%package -n python-%{name}
Summary:        Python bindings for libunity

Group:          Development/Python
BuildRequires:	python-devel

%description -n python-%{name}
Unity instrumenting and integration library - python bindings
Libunity is a shared library to be able to interact with the launcher and
add places in Unity environment.

%prep
%autosetup -p1 -n libunity-%{git}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static \
  --enable-gtk-doc
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print


%files -n %{libname}
%{_bindir}/libunity-tool
%{_bindir}/unity-scope-loader
%{_libdir}/libunity.so.%{major}*
%{_libdir}/libunity-extras.so.%{major}*
%{_libdir}/libunity/libunity-protocol-private.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/unity-scopes/__pycache__/scope-runner-dbus.cpython-38.opt-1.pyc
%{_datadir}/unity-scopes/__pycache__/scope-runner-dbus.cpython-38.pyc
%{_datadir}/unity-scopes/scope-runner-dbus.py
%{_datadir}/unity/client-scopes-phone.json
%{_datadir}/unity/client-scopes.json

%files -n python-%{name}
%{py_platsitedir}/gi/overrides/Unity.*
%{py_platsitedir}/gi/overrides/__pycache__/Unity.cpython-38.opt-1.pyc
%{py_platsitedir}/gi/overrides/__pycache__/Unity.cpython-38.pyc

%files -n %{develname}
%dir %{_includedir}/unity
%dir %{_datadir}/gir-1.0
%{_includedir}/unity/unity/
%{_libdir}/libunity.so
%{_libdir}/libunity-extras.so
%{_libdir}/libunity/libunity-protocol-private.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/
%{_datadir}/gir-1.0/*.gir
%{_datadir}/glib-2.0/schemas/com.canonical.Unity.Lenses.gschema.xml
