Summary:	PowerTOP - tool that finds the software component(s) that make your laptop use more power
Summary(pl.UTF-8):	PowerTOP - narzędzie wykrywające programy zwiększające pobór energii laptopa
Name:		powertop
Version:	2.6.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://01.org/sites/default/files/downloads/powertop/%{name}-%{version}.tar.gz
# Source0-md5:	705e091fa9e79a12d16bc3cb0c688280
URL:		https://01.org/powertop/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	libnl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pciutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PowerTOP is a Linux tool that finds the software component(s) that
make your laptop use more power than necessary while it is idle. As of
Linux kernel version 2.6.21, the kernel no longer has a fixed 1000Hz
timer tick. This will (in theory) give a huge power savings because
the CPU stays in low power mode for longer periods of time during
system idle.

However... there are many things that can ruin the party, both inside
the kernel and in userspace. PowerTOP combines various sources of
information from the kernel into one convenient screen so that you can
see how well your system is doing, and which components are the
biggest problem.

%description -l pl.UTF-8
PowerTOP to narzędzie linuksowe znajdujące programy zwiększające pobór
energii laptopa w czasie bezczynności. Od wersji 2.6.21 jądro Linuksa
już nie ma stałej częstotliwości zegara 1000Hz. Daje to (w teorii)
dużą oszczędność energii, ponieważ procesor pozostaje w trybie małego
poboru energii na dłuższe okresy czasu podczas bezczynności systemu.

Jednak jest wiele elementów, które mogą zrujnować tę właściwość,
zarówno w jądrze, jak i przestrzeni użytkownika. PowerTOP łączy różne
źródła informacji z jądra w jeden wygodny ekran pozwalający obejrzeć,
jak dobrze system się sprawuje i które komponenty stanowią największy
problem.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/cache/powertop
touch $RPM_BUILD_ROOT/var/cache/powertop/saved_parameters.powertop

# fix locales names
mv $RPM_BUILD_ROOT%{_localedir}/cs{_CZ,}
mv $RPM_BUILD_ROOT%{_localedir}/de{_DE,}
mv $RPM_BUILD_ROOT%{_localedir}/es{_ES,}
mv $RPM_BUILD_ROOT%{_localedir}/hu{_HU,}
mv $RPM_BUILD_ROOT%{_localedir}/id{_ID,}
mv $RPM_BUILD_ROOT%{_localedir}/nl{_NL,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_sbindir}/powertop
%{_mandir}/man8/powertop.8*
%dir /var/cache/powertop
%ghost /var/cache/powertop/saved_parameters.powertop
