Summary: An X Window System based backgammon game.
Name: xgammon
Version: 0.98
Release: 14
Copyright: GPL
Group: Amusements/Games
Source: ftp://sunsite.unc.edu:/pub/Linux/X11/games/strategy/xgammon-0.98.tar.gz
Patch0: xgammon-0.98-config.patch
Patch1: xgammon-0.98-dirent.patch
BuildRoot: /var/tmp/xgammon-root

%description
Xgammon is an X Window System based backgammon game.  Xgammon allows you
to play against the computer, or you can play against another person.
Xgammon also supports playing a game against another person on a remote
X terminal, and will display a second board there for their use.

%prep
%setup -q -c
%patch0 -p1 -b .rhconfig
%patch1 -p1

%build
export PATH=$PATH:.
xmkmf
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man6
install -m 644 xgammon.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xgammon.6

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xgammon <<EOF
xgammon name "xgammon"
xgammon description "Backgamoon"
xgammon group Games/Strategy
xgammon exec "xgammon &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xgammon
%config /usr/X11R6/lib/X11/app-defaults/XGammon
/usr/X11R6/lib/X11/xgammon
/usr/X11R6/man/man6/xgammon.6
%config /etc/X11/wmconfig/xgammon
