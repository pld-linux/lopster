Summary:	A Napster clone for linux written in gtk
Summary(pl):	Klon klienta napstera napisany w gtk
Name:		lopster
Version:	1.2.2
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ae857116eddd01f1f7d2769908a142c0
Source1:	%{name}.desktop
Patch0:		%{name}-protocol.patch
URL:		http://lopster.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libogg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Napster clone for linux written in gtk.

%description -l pl
Klon klienta napstera napisany w gtk.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README README.pings TODO
%lang(es) %doc README.ES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/lopster
%{_desktopdir}/*.desktop
