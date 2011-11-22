Name: kde-wallpapers
Summary: KDE 4 application workspace components
Version: 4.7.80
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: LGPLv3
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: automoc4

Conflicts:   kdebase4-workspace < 2:4.6.90
 
%description
This package contains the KDE 4 application workspace components.

%files
%doc LICENSE
%_kde_datadir/wallpapers/


#-----------------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
