Summary:	Super-flat Mozilla theme
Summary(pl):	Super p³aski temat dla Mozilli
Name:		mozilla-theme-LopburiFlat
Version:	2.1
%define		_realname	lopburi
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/%{_realname}-1.jar
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/lopburi.html
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Super-flat Mozilla theme.

%description -l pl
Super p³aski temat dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean 
rm -rf $RPM_BUILD_ROOT

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
