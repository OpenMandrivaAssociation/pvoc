Summary:	LADSPA plugins for time compression/expansion of sound data
Name:		pvoc
Version:	0.1.12
Release:	%{mkrel 2}
License:	GPLv2+
Group:		Sound
URL:		http://quitte.de/dsp/pvoc.html
Source0:	http://quitte.de/dsp/%{name}_%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	libsndfile-devel

%description
pvoc is a collection of LADSPA units and a command line tool for time
compression/expansion of sound data making use of the phase-vocoding
technique

%prep
%setup -q 

%build
make PREFIX=%{_prefix} MAN1DEST=%{_mandir}/man1 PLUGDEST=%{_libdir}/ladspa

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot}%{_prefix} MAN1DEST=%{buildroot}%{_mandir}/man1 PLUGDEST=%{buildroot}%{_libdir}/ladspa install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_libdir}/ladspa/*.so
%{_mandir}/man1/*

