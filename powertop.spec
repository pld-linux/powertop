Summary:	PowerTOP - tool that finds the software component(s) that make your laptop use more power
Summary(pl.UTF-8):	PowerTOP - narzędzie wykrywające programy zwiększające pobór energii laptopa
Name:		powertop
Version:	2.15
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/fenrus75/powertop/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a8008e2b16fb648c03faeec3c1047521
URL:		https://01.org/powertop/
BuildRequires:	autoconf >= 2.69
BuildRequires:	autoconf-archive
BuildRequires:	automake >= 1:1.12.2
BuildRequires:	bash-completion >= 1:2.0
BuildRequires:	gettext-tools >= 0.20.2
BuildRequires:	libnl-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
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

%package -n bash-completion-powertop
Summary:	Bash completion for powertop command line
Summary(pl.UTF-8):	Bashowe dopełnianie linii poleceń programu powertop
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-powertop
Bash completion for powertop command line.

%description -n bash-completion-powertop -l pl.UTF-8
Bashowe dopełnianie linii poleceń programu powertop.

%prep
%setup -q

echo "v%{version}" > version-long
echo '"v%{version}"' > version-short

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
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
%{__mv} $RPM_BUILD_ROOT%{_localedir}/cs{_CZ,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/de{_DE,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/es{_ES,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/hu{_HU,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/id{_ID,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/nl{_NL,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md TODO
%attr(755,root,root) %{_sbindir}/powertop
%{_mandir}/man8/powertop.8*
%dir /var/cache/powertop
%ghost /var/cache/powertop/saved_parameters.powertop

%files -n bash-completion-powertop
%defattr(644,root,root,755)
%{bash_compdir}/powertop
