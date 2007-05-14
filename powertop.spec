Summary:	PowerTOP - tool that finds the software component(s) that make your laptop use more power
Name:		powertop
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.linuxpowertop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	4420482fff4c3f0c63a4a3cec56f2931
Patch0:		%{name}-make.patch
URL:		http://www.linuxpowertop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PowerTOP is a Linux tool that finds the software component(s) that make your laptop use more power than necessary while it is idle. As of Linux kernel version 2.6.21, the kernel no longer has a fixed 1000Hz timer tick. This will (in theory) give a huge power savings because the CPU stays in low power mode for longer periods of time during system idle.

However... there are many things that can ruin the party, both inside the kernel and in userspace. PowerTOP combines various sources of information from the kernel into one convenient screen so that you can see how well your system is doing, and which components are the biggest problem. 

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README 
%attr(755,root,root) %{_bindir}/*
