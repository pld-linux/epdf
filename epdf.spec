%define	_snap	20060223
Summary:	pdf viewer using Enlightenment libraries
Summary(pl):	Przegl±darka pdfów u¿ywaj±ca bibliotek Enlightenmenta
Name:		epdf
Version:	0.1
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://sparky.homelinux.org/snaps/enli/e17/proto/%{name}-%{_snap}.tar.bz2
# Source0-md5:	764ddf9621a7d810872b8283ec0d2ced
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	etk-devel
BuildRequires:	ewl-devel
BuildRequires:	libtool
BuildRequires:	poppler-devel >= 0.5.0-3
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
epdf is an image pdf using Enlightenment libraries.

%description -l pl
epdf to przegl±darka pdfów u¿ywaj±ca bibliotek Enlightenmenta.

%package libs
Summary:	epdf library
Summary(pl):	Biblioteka epdf
Group:		Libraries

%description libs
epdf library.

%description libs -l pl
Biblioteka epdf.

%package devel
Summary:	Header files for epdf library
Summary(pl):	Pliki nag³ówkowe biblioteki epdf
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for epdf library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki epdf.

%package static
Summary:	Static epdf library
Summary(pl):	Statyczna biblioteka epdf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static epdf library.

%description static -l pl
Statyczna biblioteka epdf

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}_*_test

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepdf.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/libepdf.so
%{_libdir}/libepdf.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libepdf.a
