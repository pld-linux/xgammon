Summary:	An X Window System based backgammon game.
Name:		xgammon
Version:	0.98
Release:	14
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://sunsite.unc.edu:/pub/Linux/X11/games/strategy/%{name}-%{version}.tar.gz
Patch0:		xgammon-0.98-config.patch
Patch1:		xgammon-0.98-dirent.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xgammon is an X Window System based backgammon game. Xgammon allows
you to play against the computer, or you can play against another
person. Xgammon also supports playing a game against another person on
a remote X terminal, and will display a second board there for their
use.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/X11/wmconfig,%{_mandir}/man6}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install xgammon.6 $RPM_BUILD_ROOT%{_mandir}/man6/xgammon.6x

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/*

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xgammon <<EOF
xgammon name "xgammon"
xgammon description "Backgamoon"
xgammon group Games/Strategy
xgammon exec "xgammon &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xgammon
%config %{_libdir}/X11/app-defaults/XGammon
%{_datadir}/xgammon
%{_mandir}/man6/xgammon.6x.gz
%config %{_sysconfdir}/X11/wmconfig/xgammon
