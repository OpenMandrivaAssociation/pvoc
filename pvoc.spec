%define name    pvoc
%define version 0.1.9
%define release %mkrel 2

Summary:      	LADSPA plugins for time compression/expansion of sound data
Name:         	%{name}
Version:      	%{version}
Release:      	%{release}
License:    	GPL
Group:        	Sound
URL:          	http://quitte.de/dsp/pvoc.html
Source0:      	pvoc_%{version}.tar.bz2
BuildRoot:    	%{_tmppath}/%{name}-buildroot

BuildRequires:	pkgconfig libfftw3-devel ladspa-devel libsndfile-devel

%description
pvoc is a collection of LADSPA units and a command line tool for time
compression/expansion of sound data making use of the phase-vocoding
technique

%prep
%setup -q 

%build
make PREFIX=%{_prefix} MAN1DEST=%{_mandir}/man1

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} MAN1DEST=$RPM_BUILD_ROOT%{_mandir}/man1 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_libdir}/ladspa/*.so
%{_mandir}/man1/*

