%define major 6
%define libname %mklibname unity %{major}
%define develname %mklibname unity -d

Name:           libunity
Version:        4.0.6
Release:        1
License:        LGPLv3
Summary:        Unity instrumenting and integration library
Url:            http://launchpad.net/libunity
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dee-1.0)
BuildRequires:  pkgconfig(gee-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala-devel

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

This package provides the shared libraries to be used by applications.

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
%py_requires

%description -n python-%{name}
Unity instrumenting and integration library - python bindings
Libunity is a shared library to be able to interact with the launcher and
add places in Unity environment.

%prep
%setup -q

%build
%configure2_5x \
  --disable-static \
  --enable-gtk-doc
%make

%install
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libunity.so.%{major}*
%{_libdir}/girepository-1.0/*.typelib

%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/gi/overrides/Unity.*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/unity
%dir %{_datadir}/gir-1.0
%{_includedir}/unity/unity/
%{_libdir}/libunity.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/
%{_datadir}/gir-1.0/*.gir

