Summary:	Super-flat Mozilla theme
Summary(pl):	Super p³aski motyw dla Mozilli
Name:		mozilla-theme-LopburiFlat
Version:	3.0
%define		_realname	lopburi
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}12.xpi
# Source0-md5:	2b6ee74c67f25b0c71318c96e232b327
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/lopburi.html
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Super-flat Mozilla theme.

%description -l pl
Super p³aski motyw dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} 19410-%{_realname}.jar -d $RPM_BUILD_ROOT%{_chromedir}
mv $RPM_BUILD_ROOT%{_chromedir}/19410-%{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
