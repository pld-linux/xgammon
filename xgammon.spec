Summary:	An X Window System based backgammon game
Summary(pl.UTF-8):   Gra backgammon pod X Window System
Name:		xgammon
Version:	0.98
Release:	15
License:	GPL
Group:		X11/Applications/Games
#Source0:	ftp://sunsite.unc.edu/pub/Linux/X11/games/strategy/%{name}-%{version}.tar.gz
#Source0-md5:	29d7b0299e046d4e534b974eb202253e
Source0:	%{name}_%{version}a.orig.tar.gz
# fetched from debian, and stored in distfiles
Patch0:		%{name}-0.98-config.patch
Patch1:		%{name}-0.98-dirent.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xgammon is an X Window System based backgammon game. Xgammon allows
you to play against the computer, or you can play against another
person. Xgammon also supports playing a game against another person on
a remote X terminal, and will display a second board there for their
use.

%description -l pl.UTF-8
Xgammon to gra backgammon dla X Window System. Można grać przeciwko
komputerowi lub drugiej osobie. Xgammon obsługuje grę przeciwko
drugiej osobie na zdalnym X terminalu - w takim przypadku wyświetla
dla niej drugą planszę.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_mandir}/man6}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install xgammon.6 $RPM_BUILD_ROOT%{_mandir}/man6/xgammon.6x

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xgammon.desktop <<EOF
Name=xgammon
Comment=Backgammon
Exec=xgammon
Terminal=0
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xgammon
%config %{_libdir}/X11/app-defaults/XGammon
%{_datadir}/xgammon
%{_mandir}/man6/xgammon.6x*
%{_applnkdir}/Games/xgammon.desktop
