Summary:	A Napster clone for linux written in gtk
Summary(pl):	Klon klienta napstera napisany w gtk
Name:		lopster
Version:	0.9.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://lopster.sourceforge.net/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-protocol.patch
URL:		http://lopster.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
A Napster clone for linux written in gtk.

%description -l pl
Klon klienta napstera napisany w gtk.

%prep
%setup -q
%patch0 -p1

%build
rm missing acinclude.m4
gettextize --copy --force
aclocal
autoconf
automake -a -c -f
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README BUGS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/lopster
%{_applnkdir}/Network/Misc/*.desktop
