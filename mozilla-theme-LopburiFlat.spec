Summary:	Super-flat Mozilla theme
Summary(pl):	Super p³aski motyw dla Mozilli
Name:		mozilla-theme-LopburiFlat
%define		_realname	lopburi
Version:	3.5
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}.jar
# Source0-md5:	4849975a644e299e9a82dd2ea4a84c34
# Source0-size:	294759
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/lopburi.html
Requires(post,postun):	textutils
Requires:	mozilla >= 4:1.5b
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Super-flat Mozilla theme.

%description -l pl
Super p³aski motyw dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}/

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
