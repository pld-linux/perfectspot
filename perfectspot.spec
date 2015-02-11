Summary:	Perfectspot - graphical viewer for WordPerfect Graphics (WPG) files
Summary(pl.UTF-8):	Perfectspot - graficzna przeglądarka plików WordPerfect Graphics (WPG)
Name:		perfectspot
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/libwpg/%{name}-%{version}.tar.xz
# Source0-md5:	2b352c5d12f742cb0ea0285b047adeeb
URL:		http://libwpg.sourceforge.net/
BuildRequires:	QtCore-devel >= 4.1
BuildRequires:	QtGui-devel >= 4.1
BuildRequires:	QtSvg-devel >= 4.1
BuildRequires:	cmake >= 2.4.2
BuildRequires:	libodfgen-devel >= 0.1
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libwpg-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.1
Requires:	QtCore >= 4.1
Requires:	QtGui >= 4.1
Requires:	QtSvg >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perfectspot is a graphical viewer for WordPerfect Graphics (WPG)
files.

%description -l pl.UTF-8
Perfectspot to graficzna przeglądarka plików WordPerfect Graphics
(WPG).

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/perfectspot
%{_desktopdir}/perfectspot.desktop
%{_pixmapsdir}/perfectspot.png
