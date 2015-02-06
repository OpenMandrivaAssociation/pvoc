%define debug_package          %{nil}

Summary:	LADSPA plugins for time compression/expansion of sound data
Name:		pvoc
Version:	0.1.12
Release:	6
License:	GPLv2+
Group:		Sound
URL:		http://quitte.de/dsp/pvoc.html
Source0:	http://quitte.de/dsp/%{name}_%{version}.tar.gz
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(sndfile)

%description
pvoc is a collection of LADSPA units and a command line tool for time
compression/expansion of sound data making use of the phase-vocoding
technique

%prep
%setup -q 

%build
make PREFIX=%{_prefix} MAN1DEST=%{_mandir}/man1 PLUGDEST=%{_libdir}/ladspa

%install
make PREFIX=%{buildroot}%{_prefix} MAN1DEST=%{buildroot}%{_mandir}/man1 PLUGDEST=%{buildroot}%{_libdir}/ladspa install

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_libdir}/ladspa/*.so
%{_mandir}/man1/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.12-3mdv2010.0
+ Revision: 430815
- rebuild

* Fri Sep 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.12-2mdv2009.0
+ Revision: 284029
- bump release for stupid bs
- fix install location for x86-64
- s,$RPM_BUILD_ROOT,%%{buildroot}
- trim buildrequires
- new license policy
- new reelase 0.1.12
- tabs not spaces
- drop unnecessary defines

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - fix fftw3-devel BR
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import pvoc

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.9-2mdk
- rebuild with new g++

* Sat May 8 2004 Austin Acton <austin@mandrake.org> 0.1.9-1mdk
- mandrakize

* Fri Apr  2 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.9
- initial build
