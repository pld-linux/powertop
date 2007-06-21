Summary:	PowerTOP - tool that finds the software component(s) that make your laptop use more power
Summary(pl.UTF-8):	PowerTOP - narzędzie wykrywające programy zwiększające pobór energii laptopa
Name:		powertop
Version:	1.7
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://www.linuxpowertop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	84c012fe5e866b5deb588606a6b9822b
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
URL:		http://www.linuxpowertop.org/
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
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# FIXME
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/zh

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
