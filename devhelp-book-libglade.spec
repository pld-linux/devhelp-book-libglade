Summary:	DevHelp book: libglade
Summary(pl):	Ksi±¿ka do DevHelp'a o libglade
Name:		devhelp-book-libglade
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libglade.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about libglade

%description -l pl
Ksi±¿ka do DevHelp o libglade

%prep
%setup -q -c libglade -n libglade

%build
mv -f book libglade
mv -f book.devhelp libglade.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/libglade
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install libglade.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install libglade/* $RPM_BUILD_ROOT%{_prefix}/books/libglade

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
