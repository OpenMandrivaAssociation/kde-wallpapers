Name:		kde-wallpapers
Summary:	Additional official wallpapers for KDE 4
Version: 4.9.3
Release: 1
Epoch:		2
Group:		Graphical desktop/KDE
License:	LGPLv3
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	automoc4
Conflicts:	kdebase4-workspace < 2:4.6.90

%description
This package contains additional official wallpapers for KDE 4.

%files
%doc LICENSE
%{_kde_datadir}/wallpapers/*

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

