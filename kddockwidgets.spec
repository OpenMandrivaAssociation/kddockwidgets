%define major 3
%define libname %mklibname kddockwidgets-qt6
%define devname %mklibname kddockwidgets-qt6 -d

Name:		kddockwidgets
Version:	2.4.1
Release:	1
Source0:	https://github.com/KDAB/KDDockWidgets/releases/download/v%{version}/kddockwidgets-%{version}.tar.gz
Summary:	Dock Widget Framework for Qt
URL:		https://github.com/KDAB/KDDockWidgets
License:	GPL-2.0/GPL-3.0
Group:		System/Libraries
BuildRequires:	cmake
BuildSystem:	cmake
BuildOption:	-DKDE_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickTools)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6WidgetsPrivate)
BuildRequires:	cmake(Qt6QuickPrivate)
BuildRequires:	cmake(spdlog)
BuildRequires:	cmake(fmt)
BuildRequires:	cmake(nlohmann_json)

%description
Dock Widget Framework for Qt

%package -n %{libname}
Summary:	Dock Widget Framework for Qt
Group:		System/Libraries

%description -n %{libname}
Dock Widget Framework for Qt

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name},
the Dock Widget Framework for Qt

%install -a
rm -rf %{buildroot}%{_docdir} %{buildroot}%{_prefix}/mkspecs

%files -n %{libname}
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
