Summary:	Additional official wallpapers for KDE4
Name:		kde-wallpapers
Version:	4.12.1
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	LGPLv3
Url:		http://www.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	automoc4
Conflicts:	kdebase4-workspace < 2:4.6.90
BuildArch:	noarch

%description
This package contains additional official wallpapers for KDE4.

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

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-2
- New version 4.9.2
- Make it noarch package

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97
- Change summary and description

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762456
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758049
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744531
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739359
- New upstream tarball

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 732345
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New upstream tarball 4.7.80

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 697221
- New version 4.7.41

* Mon Jul 11 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.90-1
+ Revision: 689476
- import kde-wallpapers

